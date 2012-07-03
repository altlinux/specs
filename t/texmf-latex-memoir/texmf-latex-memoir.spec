%define srcName memoir

Name: texmf-latex-%srcName
Version: 3.6
Release: alt1
Summary: Featured LaTeX class for typesetting fiction, non-fiction and mathematical books
Summary(ru_RU.UTF-8): Класс LaTeX для набора поэзии, прозы, технической и математической литературы
License: LPPL (LaTeX Project Public License)
Group: Publishing
Url: http://www.ctan.org/tex-archive/macros/latex/contrib/memoir/
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

Provides: tetex-latex-memoir <= 1.618033p5.1-alt1
Obsoletes: tetex-latex-memoir

Source0: %srcName-%version.tar

BuildRequires(pre): rpm-build-texmf rpm-build-licenses
BuildRequires: texlive-latex-recommended ctanify

%description
Memoir class is for typesetting poetry, fiction, non-fiction,
and mathematical works.

The normal font sizes range from 9 to 17pt.  There is a range of
page-styles and well over a dozen chapter-styles to choose from
and methods for specifying your own layouts and designs.  The
class encompasses over thirty of the more popular packages.

The class has an associated patch file
mempatch, which is automatically
loaded by the class itself, but which is updated from time to
time, between releases of the class itself.

Users who wish to use the hyperref
package, in a document written with the memoir class, should also
use the memhfixc package.

%description -l ru_RU.UTF-8
LaTeX-класс memoir предназначен для набора поэзии, прозы, 
технической и математической литературы.

Кегль основного шрифта может варьироваться от 9 до 17 пунктов.
Класс включает набор стилей оформления страницы и заголовков глав,
из которых можно выбрать, а также богатый инструментарий для
модификации и определения собственного оформления. 
Функциональность класса покрывает более тридцати популярных пакетов.

Вместе с классом распространяется файл модификаций mempatch, который
загружается автоматически при загрузке класса, однако время от веремени может
обновляться отдельно между обновлениями версий самого класса.

Тем пользователям, которые хотят использовать пакет hyperref в документах,
набранных в классе memoir, необходимо подключить пакет memfixc.

%prep
%setup -q -n %srcName-%version
rm -vf memoir.cls

%build
latex memoir.ins
pdflatex memoir.dtx
makeindex -s gind.ist memoir
pdflatex memoir.dtx
pdflatex memoir.dtx

latex mempatch.ins
pdflatex mempatch.dtx
makeindex -s gind.ist mempatch
pdflatex mempatch.dtx
pdflatex mempatch.dtx

%install
mkdir -p %buildroot%_texmfmain
ctanify --pkgname=%srcName --tdsdir=%buildroot/%_texmfmain "*" "doc-src/*=doc/latex/%srcName" "*.clo=tex/latex/%srcName"

%files
%_texmfmain/tex/latex/*
%_texmfmain/doc/latex/*
%_texmfmain/source/latex/*


%changelog
* Tue Apr 20 2010 Kirill Maslinsky <kirill@altlinux.org> 3.6-alt1
- 3.6

* Thu Nov 19 2009 Kirill Maslinsky <kirill@altlinux.org> 1.61803398c.p6.0f-alt1
- updated to 1.61803398c patch 6.0f
- packaged according to ALT TeX policy
  + renamed to texmf-latex-memoir
  + removed texhash calls from %%post(un)
  + require rpm-build-texmf
  + use ctanify to install files into TEXMF tree

* Fri Jul 04 2008 Kirill Maslinsky <kirill@altlinux.org> 1.618033p5.1-alt1
- new stable version for "considerable period of time" (Peter Wilson)
- added documented source (memoir.dvi, mempatch.dvi)

* Thu Jan 17 2008 Kirill Maslinsky <kirill@altlinux.org> 1.618p4.9a-alt1
- Updated to upstream patched version 4.9a

* Tue Sep 04 2007 Kirill Maslinsky <kirill@altlinux.ru> 1.618p4.8-alt1
- Initial build for Sisyphus
  (thanks Grigory Batalov for the initial draft of this package)

