Name: texmf-pgf
Version: 2.10
Release: alt0.1
Summary: A sophisticated graphical macro package for LaTeX, plain-TeX
Summary(ru_RU.UTF-8): Изощрённый макропакет TeX/LaTeX/ConTeXt для создания рисунков, диаграмм и графиков
License: LPPL (LaTeX Project Public License)
Group: Publishing
Url: http://sourceforge.net/projects/pgf/

BuildArchitectures: noarch
BuildRequires(pre): rpm-build-texmf
Conflicts: tetex-latex-pgf

Packager: Andrey Bergman <vkni@altlinux.org>

Source: %name-%version.tar

%description
pgf is a LaTeX, ConTeXt and plain-TeX macro package that allows to create graphics in
LaTeX documents using a special pgfpicture environment and special macros for
drawing lines, curves, rectangles, and many other kind of graphic objects.

%description -l ru_RU.UTF-8
pgf - это макропакет для LaTeX, plain-TeX и Context, позволяющий
создавать в теле LaTeX или TeX документа графические рисунки с
помощью окружения pgfpicture. В этом окружении можно использовать различные
макросы для рисования линий, кривых, прямоугольников и других графических
объектов.

Кроме макропакета pgf данный rpm файл содержит удобную макропакет-оболочку для
низкоуровнего pgf кода - TikZ. Его название расшифровывается как
Tikz ist kein Zeichenprogramm.

%prep
%setup -q -n %name-%version

%install
mkdir -p %buildroot%_texmfdoc/pgf
mkdir -p %buildroot%_texmfmain/tex/{generic,plain,latex,context}/pgf/{basiclayer,frontendlayer,math,systemlayer,utilities}
mkdir -p %buildroot%_texmfmain/tex/generic/pgf/frontendlayer/tikz/libraries/{circuits,datavisualization,graphs}
mkdir -p %buildroot%_texmfmain/tex/generic/pgf/{libraries,modules}
mkdir -p %buildroot%_texmfmain/tex/generic/pgf/libraries/{datavisualization,decorations,shapes}
mkdir -p %buildroot%_texmfmain/tex/generic/pgf/libraries/shapes/circuits
mkdir -p %buildroot%_texmfmain/tex/latex/pgf/compatibility
mkdir -p %buildroot%_texmfmain/tex/latex/pgf/frontendlayer/libraries

install -pD -m644 doc/generic/pgf/{AUTHORS,ChangeLog,FILES,INSTALL,README,TODO,pgfmanual.pdf} %buildroot%_texmfdoc/pgf/
install -pD -m644 tex/context/third/pgf/basiclayer/* %buildroot%_texmfmain/tex/context/pgf/basiclayer/
install -pD -m644 tex/context/third/pgf/frontendlayer/* %buildroot%_texmfmain/tex/context/pgf/frontendlayer/
install -pD -m644 tex/context/third/pgf/math/* %buildroot%_texmfmain/tex/context/pgf/math/
install -pD -m644 tex/context/third/pgf/systemlayer/* %buildroot%_texmfmain/tex/context/pgf/systemlayer/
install -pD -m644 tex/context/third/pgf/utilities/* %buildroot%_texmfmain/tex/context/pgf/utilities/

install -pD -m644 tex/generic/pgf/basiclayer/* %buildroot%_texmfmain/tex/generic/pgf/basiclayer/
install -pD -m644 tex/generic/pgf/frontendlayer/tikz/*.tex %buildroot%_texmfmain/tex/generic/pgf/frontendlayer/tikz/
install -pD -m644 tex/generic/pgf/frontendlayer/tikz/libraries/*.tex %buildroot%_texmfmain/tex/generic/pgf/frontendlayer/tikz/libraries/
install -pD -m644 tex/generic/pgf/frontendlayer/tikz/libraries/circuits/*.tex %buildroot%_texmfmain/tex/generic/pgf/frontendlayer/tikz/libraries/circuits
install -pD -m644 tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/*.tex %buildroot%_texmfmain/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization
install -pD -m644 tex/generic/pgf/frontendlayer/tikz/libraries/graphs/*.tex %buildroot%_texmfmain/tex/generic/pgf/frontendlayer/tikz/libraries/graphs

install -pD -m644 tex/generic/pgf/libraries/*.tex %buildroot%_texmfmain/tex/generic/pgf/libraries/
install -pD -m644 tex/generic/pgf/libraries/datavisualization/*.tex %buildroot%_texmfmain/tex/generic/pgf/libraries/datavisualization/
install -pD -m644 tex/generic/pgf/libraries/decorations/*.tex %buildroot%_texmfmain/tex/generic/pgf/libraries/decorations/
install -pD -m644 tex/generic/pgf/libraries/shapes/*.tex %buildroot%_texmfmain/tex/generic/pgf/libraries/shapes/
install -pD -m644 tex/generic/pgf/libraries/shapes/circuits/*.tex %buildroot%_texmfmain/tex/generic/pgf/libraries/shapes/circuits/

install -pD -m644 tex/generic/pgf/math/* %buildroot%_texmfmain/tex/generic/pgf/math/
install -pD -m644 tex/generic/pgf/modules/* %buildroot%_texmfmain/tex/generic/pgf/modules/
install -pD -m644 tex/generic/pgf/systemlayer/* %buildroot%_texmfmain/tex/generic/pgf/systemlayer/
install -pD -m644 tex/generic/pgf/utilities/* %buildroot%_texmfmain/tex/generic/pgf/utilities/

install -pD -m644 tex/latex/pgf/basiclayer/* %buildroot%_texmfmain/tex/latex/pgf/basiclayer/
install -pD -m644 tex/latex/pgf/compatibility/* %buildroot%_texmfmain/tex/latex/pgf/compatibility/
install -pD -m644 tex/latex/pgf/frontendlayer/*.sty %buildroot%_texmfmain/tex/latex/pgf/frontendlayer/
install -pD -m644 tex/latex/pgf/frontendlayer/libraries/* %buildroot%_texmfmain/tex/latex/pgf/frontendlayer/libraries
install -pD -m644 tex/latex/pgf/math/* %buildroot%_texmfmain/tex/latex/pgf/math/
install -pD -m644 tex/latex/pgf/systemlayer/* %buildroot%_texmfmain/tex/latex/pgf/systemlayer/
install -pD -m644 tex/latex/pgf/utilities/* %buildroot%_texmfmain/tex/latex/pgf/utilities/

install -pD -m644 tex/plain/pgf/basiclayer/* %buildroot%_texmfmain/tex/plain/pgf/basiclayer/
install -pD -m644 tex/plain/pgf/frontendlayer/* %buildroot%_texmfmain/tex/plain/pgf/frontendlayer/
install -pD -m644 tex/plain/pgf/math/* %buildroot%_texmfmain/tex/plain/pgf/math/
install -pD -m644 tex/plain/pgf/systemlayer/* %buildroot%_texmfmain/tex/plain/pgf/systemlayer/
install -pD -m644 tex/plain/pgf/utilities/* %buildroot%_texmfmain/tex/plain/pgf/utilities/

%files
%dir %_texmfdoc/pgf/

%dir %_texmfmain/tex/

%dir %_texmfmain/tex/context/
%dir %_texmfmain/tex/context/pgf/
%dir %_texmfmain/tex/context/pgf/basiclayer/
%dir %_texmfmain/tex/context/pgf/frontendlayer/
%dir %_texmfmain/tex/context/pgf/math/
%dir %_texmfmain/tex/context/pgf/systemlayer/
%dir %_texmfmain/tex/context/pgf/utilities/

%dir %_texmfmain/tex/generic/
%dir %_texmfmain/tex/generic/pgf/
%dir %_texmfmain/tex/generic/pgf/basiclayer/
%dir %_texmfmain/tex/generic/pgf/frontendlayer/
%dir %_texmfmain/tex/generic/pgf/frontendlayer/tikz
%dir %_texmfmain/tex/generic/pgf/frontendlayer/tikz/libraries/
%dir %_texmfmain/tex/generic/pgf/frontendlayer/tikz/libraries/circuits
%dir %_texmfmain/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization
%dir %_texmfmain/tex/generic/pgf/frontendlayer/tikz/libraries/graphs
%dir %_texmfmain/tex/generic/pgf/libraries/
%dir %_texmfmain/tex/generic/pgf/libraries/datavisualization
%dir %_texmfmain/tex/generic/pgf/libraries/decorations
%dir %_texmfmain/tex/generic/pgf/libraries/shapes
%dir %_texmfmain/tex/generic/pgf/libraries/shapes/circuits
%dir %_texmfmain/tex/generic/pgf/modules/
%dir %_texmfmain/tex/generic/pgf/math/
%dir %_texmfmain/tex/generic/pgf/systemlayer/
%dir %_texmfmain/tex/generic/pgf/utilities/

%dir %_texmfmain/tex/latex/
%dir %_texmfmain/tex/latex/pgf/
%dir %_texmfmain/tex/latex/pgf/basiclayer/
%dir %_texmfmain/tex/latex/pgf/compatibility/
%dir %_texmfmain/tex/latex/pgf/frontendlayer/
%dir %_texmfmain/tex/latex/pgf/frontendlayer/libraries
%dir %_texmfmain/tex/latex/pgf/math/
%dir %_texmfmain/tex/latex/pgf/systemlayer/
%dir %_texmfmain/tex/latex/pgf/utilities/

%dir %_texmfmain/tex/plain/
%dir %_texmfmain/tex/plain/pgf/
%dir %_texmfmain/tex/plain/pgf/basiclayer/
%dir %_texmfmain/tex/plain/pgf/frontendlayer/
%dir %_texmfmain/tex/plain/pgf/math/
%dir %_texmfmain/tex/plain/pgf/systemlayer/
%dir %_texmfmain/tex/plain/pgf/utilities/

%_texmfdoc/pgf/*
%_texmfmain/tex/context/pgf/basiclayer/*
%_texmfmain/tex/context/pgf/frontendlayer/*
%_texmfmain/tex/context/pgf/math/*
%_texmfmain/tex/context/pgf/systemlayer/*
%_texmfmain/tex/context/pgf/utilities/*
%_texmfmain/tex/generic/pgf/basiclayer/*
%_texmfmain/tex/generic/pgf/frontendlayer/*
%_texmfmain/tex/generic/pgf/libraries/*
%_texmfmain/tex/generic/pgf/modules/*
%_texmfmain/tex/generic/pgf/math/*
%_texmfmain/tex/generic/pgf/systemlayer/*
%_texmfmain/tex/generic/pgf/utilities/*
%_texmfmain/tex/latex/pgf/basiclayer/*
%_texmfmain/tex/latex/pgf/compatibility/*
%_texmfmain/tex/latex/pgf/frontendlayer/*
%_texmfmain/tex/latex/pgf/math/*
%_texmfmain/tex/latex/pgf/systemlayer/*
%_texmfmain/tex/latex/pgf/utilities/*
%_texmfmain/tex/plain/pgf/basiclayer/*
%_texmfmain/tex/plain/pgf/frontendlayer/*
%_texmfmain/tex/plain/pgf/math/*
%_texmfmain/tex/plain/pgf/systemlayer/*
%_texmfmain/tex/plain/pgf/utilities/*

%changelog
* Thu Dec 09 2010 Andrey Bergman <vkni@altlinux.org> 2.10-alt0.1
- Update to version 2.10.

* Mon Jun 29 2009 Andrey Bergman <vkni@altlinux.org> 2.00-alt0.8
- Standartized directories. Changed short russian description.

* Thu Jun 25 2009 Andrey Bergman <vkni@altlinux.org> 2.00-alt0.7
- Included important documentation. Added explicit conflict with tetex-latex-pgf.

* Fri Jun 12 2009 Grigory Batalov <bga@altlinux.ru> 2.00-alt0.6
- Include more directories in the package.

* Thu Jun 04 2009 Grigory Batalov <bga@altlinux.ru> 2.00-alt0.5
- Rebuilt with rpm-build-texmf.

* Sun May 31 2009 Andrey Bergman <vkni@altlinux.org> 2.00-alt0.1
- initial version (inherited from tetex-latex-pgf) 

* Fri Mar 07 2008 Andrey Bergman <vkni@altlinux.org> 1.18-alt1
- pgf code update, added dependency on xkeyval (required for TikZ)

* Mon Oct 29 2005 Constantin (Const) Mikhaylenko <const at altlinux.ru> 1.00-alt1
- first stable version.
- Renamed from tetel-latex-pgf

* Mon Nov 11 2004 Constantin (Const) Mikhaylenko <const at altlinux.ru> 0.65-alt1
- Fixed bug in pgfshade.sty that arises in conjunction with calc.sty and latex+dvips.

* Mon Oct 27 2004 Constantin (Const) Mikhaylenko <const at altlinux.ru> 0.64-alt1
- initial release for Sisyphus
