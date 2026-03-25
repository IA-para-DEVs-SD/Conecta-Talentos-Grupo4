"""Extração de texto de arquivos PDF."""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
import pymupdf


@dataclass
class TextoExtraido:
    conteudo: str
    num_paginas: int
    tamanho_bytes: int
    sucesso: bool = True


class PDFError(Exception):
    pass

class PDFCorromidoError(PDFError):
    pass

class PDFMuitoGrandeError(PDFError):
    pass


class ExtratorPDF:
    """Converte PDFs em texto estruturado.

    Example:
        >>> extrator = ExtratorPDF(max_paginas=10)
        >>> resultado = extrator.extrair_texto(Path("curriculo.pdf"))
        >>> print(resultado.conteudo)
    """

    def __init__(self, max_paginas: int = 10):
        self.max_paginas = max_paginas

    def extrair_texto(self, pdf_path: Path) -> TextoExtraido:
        """Extrai texto de um PDF, validando tamanho e integridade."""
        if not pdf_path.exists():
            raise PDFCorromidoError(f"Arquivo não encontrado: {pdf_path}")

        try:
            doc = pymupdf.open(pdf_path)
        except Exception as e:
            raise PDFCorromidoError(f"Não foi possível abrir o PDF: {e}")

        with doc:
            if len(doc) > self.max_paginas:
                raise PDFMuitoGrandeError(
                    f"PDF tem {len(doc)} páginas, máximo permitido: {self.max_paginas}"
                )

            return TextoExtraido(
                conteudo=self._extrair_texto_estruturado(doc),
                num_paginas=len(doc),
                tamanho_bytes=pdf_path.stat().st_size,
            )

    def _extrair_texto_estruturado(self, doc: pymupdf.Document) -> str:
        partes = []
        for i, page in enumerate(doc, start=1):
            if i > 1:
                partes.append(f"\n--- Página {i} ---\n")
            partes.append(page.get_text())
        return "".join(partes)

    def validar_pdf(self, pdf_path: Path) -> tuple[bool, Optional[str]]:
        """Retorna (válido, mensagem_erro)."""
        try:
            self.extrair_texto(pdf_path)
            return True, None
        except PDFError as e:
            return False, str(e)
        except Exception as e:
            return False, f"Erro inesperado: {e}"


def pdf_to_text(pdf_path: str) -> str:
    """Função legada — prefira usar ExtratorPDF diretamente."""
    return ExtratorPDF().extrair_texto(Path(pdf_path)).conteudo


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python extrator_pdf.py <arquivo.pdf> [saida.txt]")
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    extrator = ExtratorPDF(max_paginas=10)

    try:
        resultado = extrator.extrair_texto(pdf_path)
        print(f"✓ {resultado.num_paginas} páginas | {resultado.tamanho_bytes} bytes | {len(resultado.conteudo)} chars")

        if len(sys.argv) >= 3:
            Path(sys.argv[2]).write_text(resultado.conteudo, encoding="utf-8")
            print(f"✓ Salvo em: {sys.argv[2]}")
        else:
            print(resultado.conteudo)

    except PDFError as e:
        print(f"✗ {e}")
        sys.exit(1)
