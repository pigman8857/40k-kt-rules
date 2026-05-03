#!/usr/bin/env python3
"""Kill Team PDF Generator — grimdark parchment aesthetic."""

import re, os, textwrap
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Font registration ────────────────────────────────────────────────────────
FONT_DIR = '/usr/share/fonts/truetype/dejavu'
pdfmetrics.registerFont(TTFont('DV',       f'{FONT_DIR}/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DV-Bold',  f'{FONT_DIR}/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVMono',   f'{FONT_DIR}/DejaVuSansMono.ttf'))
pdfmetrics.registerFont(TTFont('DVMono-B', f'{FONT_DIR}/DejaVuSansMono-Bold.ttf'))

# ── Colour palette ───────────────────────────────────────────────────────────
PARCHMENT   = colors.HexColor('#F5F0E8')
PARCHMENT2  = colors.HexColor('#EDE8DC')
DARK_RED    = colors.HexColor('#7A0000')
DARK_RED2   = colors.HexColor('#4A0000')
GOLD        = colors.HexColor('#C9A84C')
GOLD2       = colors.HexColor('#8B6914')
NEAR_BLACK  = colors.HexColor('#111111')
CODE_BG     = colors.HexColor('#1A1A1A')
CODE_BG2    = colors.HexColor('#252525')
CODE_FG     = colors.HexColor('#DDDDDD')
BLOCKQ_BG   = colors.HexColor('#EDE5CE')
BLOCKQ_BAR  = colors.HexColor('#C9A84C')
TBL_HDR_BG  = colors.HexColor('#4A0000')
TBL_ALT     = colors.HexColor('#EDE8DC')
TBL_GRID    = colors.HexColor('#C9A84C')
CHECK_YES   = colors.HexColor('#145214')
CHECK_NO    = colors.HexColor('#7A0000')
MID_GRAY    = colors.HexColor('#888888')

PAGE_W, PAGE_H = A4
MARGIN = 1.6 * cm
CONTENT_W = PAGE_W - 2 * MARGIN

# ── Styles ───────────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

STYLES = {
    'h1': S('h1', fontName='DV-Bold', fontSize=22, leading=27,
            textColor=DARK_RED, alignment=TA_CENTER,
            spaceBefore=0, spaceAfter=4),
    'subtitle': S('subtitle', fontName='DV', fontSize=11, leading=14,
                  textColor=GOLD, alignment=TA_CENTER, spaceAfter=14),
    'h2': S('h2', fontName='DV-Bold', fontSize=13, leading=17,
            textColor=DARK_RED, spaceBefore=14, spaceAfter=5),
    'h3': S('h3', fontName='DV-Bold', fontSize=10.5, leading=14,
            textColor=DARK_RED2, spaceBefore=8, spaceAfter=3),
    'body': S('body', fontName='DV', fontSize=9, leading=13,
              textColor=NEAR_BLACK, spaceAfter=4),
    'bullet': S('bullet', fontName='DV', fontSize=9, leading=13,
                textColor=NEAR_BLACK, leftIndent=14, spaceAfter=2),
    'numbered': S('numbered', fontName='DV', fontSize=9, leading=13,
                  textColor=NEAR_BLACK, leftIndent=14, spaceAfter=2),
    'blockquote': S('blockquote', fontName='DV', fontSize=8.5, leading=12.5,
                    textColor=colors.HexColor('#333333'),
                    leftIndent=14, rightIndent=6,
                    spaceAfter=6, spaceBefore=4),
    'code': S('code', fontName='DVMono', fontSize=7.2, leading=10,
              textColor=CODE_FG, spaceAfter=0, spaceBefore=0,
              leftIndent=8, rightIndent=8),
    'tip': S('tip', fontName='DV', fontSize=8.5, leading=12,
             textColor=colors.HexColor('#1A3A1A'),
             leftIndent=14, spaceAfter=4, spaceBefore=4),
}

# ── Custom flowables ─────────────────────────────────────────────────────────
class GoldRule(Flowable):
    """Decorative gold horizontal rule with corner diamonds."""
    def __init__(self, width, thickness=1.2):
        super().__init__()
        self.width = width
        self.height = 8
        self.thickness = thickness

    def draw(self):
        c = self.canv
        y = self.height / 2
        c.setStrokeColor(GOLD)
        c.setLineWidth(self.thickness)
        c.line(8, y, self.width - 8, y)
        # Diamond ends
        c.setFillColor(GOLD)
        for x in [4, self.width - 4]:
            c.saveState()
            c.translate(x, y)
            c.rotate(45)
            c.rect(-3, -3, 6, 6, fill=1, stroke=0)
            c.restoreState()


class SectionBanner(Flowable):
    """Dark red banner for H2 headings."""
    def __init__(self, text, width):
        super().__init__()
        self.text = text
        self.width = width
        self.height = 22

    def draw(self):
        c = self.canv
        # Background bar
        c.setFillColor(DARK_RED2)
        c.rect(0, 0, self.width, self.height, fill=1, stroke=0)
        # Gold left accent bar
        c.setFillColor(GOLD)
        c.rect(0, 0, 4, self.height, fill=1, stroke=0)
        # Text
        c.setFillColor(PARCHMENT)
        c.setFont('DV-Bold', 11)
        c.drawString(12, 6, self.text)


class CodeBlock(Flowable):
    """Dark background code block with monospaced Unicode text."""
    def __init__(self, lines, width):
        super().__init__()
        self.lines = lines
        self.width = width
        self.line_h = 10.5
        self.pad = 8
        self.height = len(lines) * self.line_h + self.pad * 2

    def draw(self):
        c = self.canv
        h = self.height
        # Background
        c.setFillColor(CODE_BG)
        c.roundRect(0, 0, self.width, h, 4, fill=1, stroke=0)
        # Gold border
        c.setStrokeColor(GOLD2)
        c.setLineWidth(0.8)
        c.roundRect(0, 0, self.width, h, 4, fill=0, stroke=1)
        # Left accent
        c.setFillColor(DARK_RED)
        c.rect(0, 0, 3, h, fill=1, stroke=0)
        # Text lines (bottom-up in PDF coords)
        c.setFont('DVMono', 7.2)
        c.setFillColor(CODE_FG)
        for i, line in enumerate(self.lines):
            y = h - self.pad - (i + 1) * self.line_h + 2
            # Colour YES/NO/✅/❌ tokens
            self._draw_line(c, line, self.pad + 4, y)

    def _draw_line(self, c, line, x, y):
        # Simple coloured keyword highlighting
        highlights = {
            '✅': CHECK_YES, 'YES': CHECK_YES,
            '❌': CHECK_NO,  'NO': CHECK_NO,
            'CANNOT': CHECK_NO,
        }
        # Draw word by word with colour overrides
        c.setFont('DVMono', 7.2)
        for token in re.split(r'(\s+)', line):
            stripped = token.strip()
            col = None
            for kw, colour in highlights.items():
                if kw in stripped:
                    col = colour
                    break
            if col:
                c.setFillColor(col)
            else:
                c.setFillColor(CODE_FG)
            w = pdfmetrics.stringWidth(token, 'DVMono', 7.2)
            c.drawString(x, y, token)
            x += w
        c.setFillColor(CODE_FG)


class BlockQuote(Flowable):
    """Gold left-bar blockquote box."""
    def __init__(self, text, width):
        super().__init__()
        self.text = text
        self.width = width
        self.pad = 8
        # Estimate height
        chars_per_line = int((width - 24) / 5.2)
        wrapped = textwrap.wrap(text, chars_per_line) or ['']
        self.lines = wrapped
        self.height = len(self.lines) * 12 + self.pad * 2

    def draw(self):
        c = self.canv
        h = self.height
        c.setFillColor(BLOCKQ_BG)
        c.roundRect(0, 0, self.width, h, 3, fill=1, stroke=0)
        c.setFillColor(BLOCKQ_BAR)
        c.rect(0, 0, 4, h, fill=1, stroke=0)
        c.setFont('DV', 8.5)
        c.setFillColor(colors.HexColor('#222222'))
        for i, line in enumerate(self.lines):
            y = h - self.pad - (i + 1) * 12 + 2
            c.drawString(12, y, line)


# ── Inline markdown → ReportLab XML ─────────────────────────────────────────
def md_inline(text):
    """Convert **bold**, *italic*, `code` to reportlab XML."""
    # Escape XML special chars first (except ones we'll insert)
    text = text.replace('&', '&amp;')
    # Bold-italic ***text***
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic *text*
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Inline code `text`
    text = re.sub(r'`(.+?)`',
                  r'<font name="DVMono" size="8" color="#C9A84C">\1</font>', text)
    # Checkmarks / crosses colour
    text = text.replace('✅', '<font color="#145214">✅</font>')
    text = text.replace('❌', '<font color="#7A0000">❌</font>')
    return text


def make_table(header_row, data_rows, col_widths=None):
    """Build a styled ReportLab Table from parsed markdown table data."""
    all_rows = [header_row] + data_rows
    if not col_widths:
        n = len(header_row)
        col_widths = [CONTENT_W / n] * n

    tbl_data = []
    # Header
    hdr = []
    for cell in header_row:
        p = Paragraph(md_inline(cell.strip()), ParagraphStyle(
            'th', fontName='DV-Bold', fontSize=8.5, leading=11,
            textColor=PARCHMENT, alignment=TA_CENTER))
        hdr.append(p)
    tbl_data.append(hdr)
    # Rows
    for ri, row in enumerate(data_rows):
        rd = []
        for cell in row:
            bg = TBL_ALT if ri % 2 else PARCHMENT
            p = Paragraph(md_inline(cell.strip()), ParagraphStyle(
                'td', fontName='DV', fontSize=8.5, leading=12,
                textColor=NEAR_BLACK))
            rd.append(p)
        tbl_data.append(rd)

    style = TableStyle([
        ('BACKGROUND',  (0, 0), (-1, 0),  TBL_HDR_BG),
        ('GRID',        (0, 0), (-1, -1), 0.6, TBL_GRID),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [PARCHMENT, TBL_ALT]),
        ('TOPPADDING',  (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING',(0,0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING',(0, 0), (-1, -1), 7),
        ('VALIGN',      (0, 0), (-1, -1), 'MIDDLE'),
        ('LINEBELOW',   (0, 0), (-1, 0),  1.5, GOLD),
    ])

    t = Table(tbl_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(style)
    return t


# ── Column width heuristics ──────────────────────────────────────────────────
COL_CONFIGS = {
    # Keyword-based overrides for known tables
    'order': [CONTENT_W * 0.18, CONTENT_W * 0.28, CONTENT_W * 0.54],
    'action': [CONTENT_W * 0.22, CONTENT_W * 0.10, CONTENT_W * 0.68],
    'keyword': [CONTENT_W * 0.22, CONTENT_W * 0.78],
    'stat': [CONTENT_W * 0.22, CONTENT_W * 0.78],
    'state': [CONTENT_W * 0.20, CONTENT_W * 0.35, CONTENT_W * 0.45],
    'terrain': [CONTENT_W * 0.18, CONTENT_W * 0.17, CONTENT_W * 0.15, CONTENT_W * 0.17, CONTENT_W * 0.33],
    'cover': [CONTENT_W * 0.38, CONTENT_W * 0.18, CONTENT_W * 0.18, CONTENT_W * 0.26],
    'window': [CONTENT_W * 0.30, CONTENT_W * 0.32, CONTENT_W * 0.38],
    'door': [CONTENT_W * 0.17, CONTENT_W * 0.22, CONTENT_W * 0.15, CONTENT_W * 0.17, CONTENT_W * 0.29],
    'default': None,
}

def guess_col_widths(header):
    h = [c.lower().strip() for c in header]
    n = len(header)
    # Use exact matches + length guards to avoid substring collisions
    # e.g. 'stat' is a substring of 'state', 'state' is in 'door state'
    if h[0] == 'order' and n == 3:
        return COL_CONFIGS['order']
    if 'action' in h[0] and n == 3 and 'ap' in str(h):
        return COL_CONFIGS['action']
    if h[0] == 'keyword' and n == 2:
        return COL_CONFIGS['keyword']
    if h[0] == 'stat' and n == 2:                    # exact — must not match 'state'
        return COL_CONFIGS['stat']
    if h[0] == 'door state' and n == 5:              # exact — must come before 'state'
        return COL_CONFIGS['door']
    if h[0] == 'state' and n == 3:                   # exact — Wounds table
        return COL_CONFIGS['state']
    if 'terrain type' in h[0] and n == 5:
        return COL_CONFIGS['terrain']
    if 'cover?' in str(h) and 'obscured?' in str(h) and n == 4:
        return COL_CONFIGS['cover']
    if 'window' in str(h) and n == 3:
        return COL_CONFIGS['window']
    # Generic fallbacks — mid column was 16% which is way too narrow
    if n == 2:
        return [CONTENT_W * 0.32, CONTENT_W * 0.68]
    if n == 3:
        return [CONTENT_W * 0.25, CONTENT_W * 0.30, CONTENT_W * 0.45]
    if n == 4:
        return [CONTENT_W * 0.22, CONTENT_W * 0.20, CONTENT_W * 0.20, CONTENT_W * 0.38]
    if n == 5:
        return [CONTENT_W * 0.18, CONTENT_W * 0.18, CONTENT_W * 0.16, CONTENT_W * 0.16, CONTENT_W * 0.32]
    return None


# ── Markdown parser → flowable list ─────────────────────────────────────────
def parse_md(text):
    lines = text.splitlines()
    story = []
    i = 0
    in_code = False
    code_lines = []
    in_table = False
    tbl_header = None
    tbl_rows = []
    bullet_group = []
    num_group = []

    def flush_bullets():
        if bullet_group:
            for b in bullet_group:
                story.append(Paragraph(
                    f'<font color="#C9A84C">▸</font>  {md_inline(b)}',
                    STYLES['bullet']))
            bullet_group.clear()

    def flush_numbered():
        if num_group:
            for idx, b in enumerate(num_group, 1):
                story.append(Paragraph(
                    f'<font color="#C9A84C"><b>{idx}.</b></font>  {md_inline(b)}',
                    STYLES['numbered']))
            num_group.clear()

    def flush_table():
        nonlocal in_table, tbl_header, tbl_rows
        if tbl_header and tbl_rows:
            cw = guess_col_widths(tbl_header)
            story.append(Spacer(1, 4))
            story.append(make_table(tbl_header, tbl_rows, cw))
            story.append(Spacer(1, 6))
        in_table = False
        tbl_header = None
        tbl_rows = []

    while i < len(lines):
        line = lines[i]

        # ── Code block toggle ────────────────────────────────────────────────
        if line.strip().startswith('```'):
            if in_code:
                # End code block
                flush_bullets(); flush_numbered(); flush_table()
                if code_lines:
                    story.append(Spacer(1, 4))
                    story.append(CodeBlock(code_lines, CONTENT_W))
                    story.append(Spacer(1, 8))
                code_lines = []
                in_code = False
            else:
                flush_bullets(); flush_numbered(); flush_table()
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        # ── Blank line ───────────────────────────────────────────────────────
        if line.strip() == '':
            flush_bullets(); flush_numbered(); flush_table()
            story.append(Spacer(1, 4))
            i += 1
            continue

        # ── Horizontal rule ──────────────────────────────────────────────────
        if re.match(r'^---+$', line.strip()):
            flush_bullets(); flush_numbered(); flush_table()
            story.append(Spacer(1, 4))
            story.append(GoldRule(CONTENT_W))
            story.append(Spacer(1, 4))
            i += 1
            continue

        # ── H1 ───────────────────────────────────────────────────────────────
        if line.startswith('# ') and not line.startswith('## '):
            flush_bullets(); flush_numbered(); flush_table()
            title_text = line[2:].strip()
            story.append(Paragraph(md_inline(title_text), STYLES['h1']))
            story.append(GoldRule(CONTENT_W, thickness=2))
            story.append(Spacer(1, 6))
            i += 1
            continue

        # ── H2 ───────────────────────────────────────────────────────────────
        if line.startswith('## '):
            flush_bullets(); flush_numbered(); flush_table()
            text = line[3:].strip()
            story.append(Spacer(1, 6))
            story.append(SectionBanner(text, CONTENT_W))
            story.append(Spacer(1, 5))
            i += 1
            continue

        # ── H3 ───────────────────────────────────────────────────────────────
        if line.startswith('### '):
            flush_bullets(); flush_numbered(); flush_table()
            text = line[4:].strip()
            story.append(Paragraph(md_inline(text), STYLES['h3']))
            i += 1
            continue

        # ── Blockquote ───────────────────────────────────────────────────────
        if line.startswith('> '):
            flush_bullets(); flush_numbered(); flush_table()
            # Collect multi-line blockquote
            bq_lines = []
            while i < len(lines) and lines[i].startswith('> '):
                bq_lines.append(lines[i][2:])
                i += 1
            bq_text = ' '.join(bq_lines)
            # Strip markdown inline
            plain = re.sub(r'\*\*(.+?)\*\*', r'\1', bq_text)
            plain = re.sub(r'\*(.+?)\*', r'\1', plain)
            plain = re.sub(r'`(.+?)`', r'\1', plain)
            story.append(BlockQuote(plain, CONTENT_W))
            continue

        # ── Table ────────────────────────────────────────────────────────────
        if line.startswith('|'):
            cells = [c for c in line.split('|') if c != '']
            # Separator row?
            if all(re.match(r'^[\s\-:]+$', c) for c in cells):
                i += 1
                continue
            if tbl_header is None:
                tbl_header = cells
            else:
                tbl_rows.append(cells)
            in_table = True
            i += 1
            continue
        elif in_table:
            flush_table()

        # ── Bullet list ──────────────────────────────────────────────────────
        if re.match(r'^[-*] ', line):
            flush_numbered(); flush_table()
            bullet_group.append(line[2:].strip())
            i += 1
            continue
        elif bullet_group and not line.startswith(' '):
            flush_bullets()

        # ── Numbered list ─────────────────────────────────────────────────────
        if re.match(r'^\d+\. ', line):
            flush_bullets(); flush_table()
            num_group.append(re.sub(r'^\d+\. ', '', line).strip())
            i += 1
            continue
        elif num_group and not line.startswith(' '):
            flush_numbered()

        # ── Indented continuation (sub-bullet) ───────────────────────────────
        if line.startswith('  - ') or line.startswith('  * '):
            text = line.strip()[2:].strip()
            story.append(Paragraph(
                f'<font color="#8B6914">◦</font>  {md_inline(text)}',
                ParagraphStyle('sub', fontName='DV', fontSize=8.5, leading=12,
                               textColor=NEAR_BLACK, leftIndent=26, spaceAfter=1)))
            i += 1
            continue

        # ── Italic-only source line ───────────────────────────────────────────
        if line.strip().startswith('*Source:'):
            flush_bullets(); flush_numbered(); flush_table()
            story.append(Spacer(1, 8))
            story.append(GoldRule(CONTENT_W))
            text = line.strip().strip('*')
            story.append(Paragraph(
                f'<i>{text}</i>',
                ParagraphStyle('src', fontName='DV', fontSize=8,
                               textColor=MID_GRAY, alignment=TA_CENTER,
                               spaceBefore=4)))
            i += 1
            continue

        # ── Regular paragraph ─────────────────────────────────────────────────
        flush_bullets(); flush_numbered(); flush_table()
        if line.strip():
            story.append(Paragraph(md_inline(line.strip()), STYLES['body']))
        i += 1

    flush_bullets(); flush_numbered(); flush_table()
    return story


# ── Page template (header + footer) ─────────────────────────────────────────
def make_page_template(doc, title):
    def on_page(canvas, doc):
        canvas.saveState()
        pw, ph = A4
        # Header bar
        canvas.setFillColor(DARK_RED2)
        canvas.rect(0, ph - 1.1 * cm, pw, 1.1 * cm, fill=1, stroke=0)
        canvas.setFillColor(GOLD)
        canvas.rect(0, ph - 1.1 * cm, pw, 2, fill=1, stroke=0)
        canvas.setFont('DV-Bold', 9)
        canvas.setFillColor(PARCHMENT)
        canvas.drawString(MARGIN, ph - 0.75 * cm, title)
        canvas.setFont('DV', 8)
        canvas.setFillColor(GOLD)
        canvas.drawRightString(pw - MARGIN, ph - 0.75 * cm,
                               'KILL TEAM 3rd Edition')
        # Footer
        canvas.setFillColor(DARK_RED2)
        canvas.rect(0, 0, pw, 0.9 * cm, fill=1, stroke=0)
        canvas.setFillColor(GOLD)
        canvas.rect(0, 0.9 * cm, pw, 1.5, fill=1, stroke=0)
        canvas.setFont('DV', 8)
        canvas.setFillColor(PARCHMENT)
        canvas.drawString(MARGIN, 0.32 * cm,
                          'Source: Wahapedia — Core Book Feb 2026')
        canvas.setFont('DV-Bold', 9)
        canvas.setFillColor(GOLD)
        canvas.drawCentredString(pw / 2, 0.32 * cm,
                                 f'— {doc.page} —')
        canvas.restoreState()

    return on_page


# ── Build one PDF ────────────────────────────────────────────────────────────
def build_pdf(md_path, pdf_path, doc_title):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    story = parse_md(md_text)

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=1.4 * cm, bottomMargin=1.2 * cm,
        title=doc_title,
        author='Kill Team Reference',
    )

    on_page = make_page_template(doc, doc_title)
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f'  ✅  {pdf_path}')


# ── Entry point ───────────────────────────────────────────────────────────────
BASE = '/home/somkamolv/Documents/killteams_rules'

build_pdf(
    f'{BASE}/kill_team_core_rules_guide.md',
    f'{BASE}/kill_team_core_rules_guide.pdf',
    'Kill Team Core Rules — How to Play Guide',
)

build_pdf(
    f'{BASE}/targeting_quick_reference.md',
    f'{BASE}/targeting_quick_reference.pdf',
    'Kill Team Targeting Quick Reference',
)

print('\nDone. Both PDFs written to:')
print(f'  {BASE}/')
