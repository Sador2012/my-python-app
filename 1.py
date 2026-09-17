from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import docx.oxml.shared as shared


def add_bookmark(paragraph, bookmark_name: str, bookmark_id: int, text: str):
    """Вставляет закладку с текстом внутрь абзаца."""
    run = paragraph.add_run()

    # <w:bookmarkStart w:id="N" w:name="..."/>
    start = OxmlElement('w:bookmarkStart')
    start.set(qn('w:id'), str(bookmark_id))
    start.set(qn('w:name'), bookmark_name)
    run._r.append(start)

    # собственно текст закладки
    t = OxmlElement('w:t')
    t.text = text
    run._r.append(t)

    # <w:bookmarkEnd w:id="N"/>
    end = OxmlElement('w:bookmarkEnd')
    end.set(qn('w:id'), str(bookmark_id))
    run._r.append(end)


def add_ref_field(paragraph, bookmark_name: str, placeholder: str = "1"):
    """
    Вставляет поле REF <bookmark_name> — это и есть перекрёстная ссылка.
    Word покажет номер/текст закладки, если нажать F9 (обновить поле).
    """
    run = paragraph.add_run()

    # <w:fldChar w:fldCharType="begin"/>
    begin = OxmlElement('w:fldChar')
    begin.set(qn('w:fldCharType'), 'begin')
    run._r.append(begin)

    # <w:instrText xml:space="preserve"> REF name \h </w:instrText>
    instr = OxmlElement('w:instrText')
    instr.set(qn('xml:space'), 'preserve')
    instr.text = f' REF {bookmark_name} \\h '
    run._r.append(instr)

    # <w:fldChar w:fldCharType="separate"/>
    separate = OxmlElement('w:fldChar')
    separate.set(qn('w:fldCharType'), 'separate')
    run._r.append(separate)

    # текст-заглушка (виден до обновления поля)
    t = OxmlElement('w:t')
    t.text = placeholder
    run._r.append(t)

    # <w:fldChar w:fldCharType="end"/>
    end = OxmlElement('w:fldChar')
    end.set(qn('w:fldCharType'), 'end')
    run._r.append(end)


def main():
    doc = Document()

    # 1) Абзац-заголовок, на который будем ссылаться
    p1 = doc.add_paragraph("Раздел 1. Введение ")
    add_bookmark(p1, bookmark_name="_Section1", bookmark_id=1, text="Введение")

    doc.add_paragraph("Тут какой-то текст документа...")

    # 2) Абзац с перекрёстной ссылкой
    p2 = doc.add_paragraph("См. раздел ")
    add_ref_field(p2, bookmark_name="_Section1", placeholder="1")
    p2.add_run(" для подробностей.")

    doc.save("cross_ref_example.docx")
    print("Готово: cross_ref_example.docx")


if __name__ == "__main__":
    main()
