%define srcName pgf

Name: tetex-latex-pgf
Version: 1.18
Release: alt2
Summary: A sophisticated graphical macro package for LaTeX, plain-TeX
Summary(ru_RU.UTF-8): LaTeX макропакет для рисования
License: LPPL (LaTeX Project Public License)
Group: Publishing
Url: http://sourceforge.net/projects/pgf/

BuildArchitectures: noarch

BuildRequires(pre): rpm-build-texmf
Requires: tetex-core tetex-latex tetex-latex-xcolor tetex-latex-xkeyval

Packager: Andrey Bergman <vkni@altlinux.org>

Source: %srcName-%version.tar.bz2

%description
pgf is a LaTeX and plain-TeX macro package that allows to create graphics in
LaTeX documents using a special pgfpicture environment and special macros for
drawing lines, curves, rectangles, and many other kind of graphic objects.

%description -l ru_RU.UTF-8
pgf - это макропакет для LaTeX, plain-TeX и Context, позволяющий
создавать в теле LaTeX или TeX документа графические рисунки с
помощью окружения pgfpicture. В этом окружении можно использовать различные
макросы для рисования линий, кривых, прямоугольников и других графических
объектов.

Кроме макропакета pgf данный rpm файл содержит макропакет-оболочку для
низкоуровнего pgf кода - TikZ. Его название расшифровывается как
Tikz ist kein Zeichenprogramm.

%prep
%setup -q -n %srcName-%version

#%build

%install
mkdir -p %buildroot{%_datadir/texmf/tex/{generic,plain,latex,context}/pgf/{basiclayer,frontendlayer,math,systemlayer,utilities},%_datadir/texmf/tex/generic/pgf/libraries,%_datadir/texmf/tex/latex/pgf/compatibility,%_docdir}
install -pD -m644 context/pgf/basiclayer/* %buildroot%_datadir/texmf/tex/context/pgf/basiclayer/
install -pD -m644 context/pgf/frontendlayer/* %buildroot%_datadir/texmf/tex/context/pgf/frontendlayer/
install -pD -m644 context/pgf/math/* %buildroot%_datadir/texmf/tex/context/pgf/math/
install -pD -m644 context/pgf/systemlayer/* %buildroot%_datadir/texmf/tex/context/pgf/systemlayer/
install -pD -m644 context/pgf/utilities/* %buildroot%_datadir/texmf/tex/context/pgf/utilities/
install -pD -m644 generic/pgf/basiclayer/* %buildroot%_datadir/texmf/tex/generic/pgf/basiclayer/
install -pD -m644 generic/pgf/frontendlayer/* %buildroot%_datadir/texmf/tex/generic/pgf/frontendlayer/
install -pD -m644 generic/pgf/libraries/* %buildroot%_datadir/texmf/tex/generic/pgf/libraries/
install -pD -m644 generic/pgf/math/* %buildroot%_datadir/texmf/tex/generic/pgf/math/
install -pD -m644 generic/pgf/systemlayer/* %buildroot%_datadir/texmf/tex/generic/pgf/systemlayer/
install -pD -m644 generic/pgf/utilities/* %buildroot%_datadir/texmf/tex/generic/pgf/utilities/
install -pD -m644 latex/pgf/basiclayer/* %buildroot%_datadir/texmf/tex/latex/pgf/basiclayer/
install -pD -m644 latex/pgf/compatibility/* %buildroot%_datadir/texmf/tex/latex/pgf/compatibility/
install -pD -m644 latex/pgf/frontendlayer/* %buildroot%_datadir/texmf/tex/latex/pgf/frontendlayer/
install -pD -m644 latex/pgf/math/* %buildroot%_datadir/texmf/tex/latex/pgf/math/
install -pD -m644 latex/pgf/systemlayer/* %buildroot%_datadir/texmf/tex/latex/pgf/systemlayer/
install -pD -m644 latex/pgf/utilities/* %buildroot%_datadir/texmf/tex/latex/pgf/utilities/
install -pD -m644 plain/pgf/basiclayer/* %buildroot%_datadir/texmf/tex/plain/pgf/basiclayer/
install -pD -m644 plain/pgf/frontendlayer/* %buildroot%_datadir/texmf/tex/plain/pgf/frontendlayer/
install -pD -m644 plain/pgf/math/* %buildroot%_datadir/texmf/tex/plain/pgf/math/
install -pD -m644 plain/pgf/systemlayer/* %buildroot%_datadir/texmf/tex/plain/pgf/systemlayer/
install -pD -m644 plain/pgf/utilities/* %buildroot%_datadir/texmf/tex/plain/pgf/utilities/

%files
%_datadir/texmf/tex/context/pgf/basiclayer/*
%_datadir/texmf/tex/context/pgf/frontendlayer/*
%_datadir/texmf/tex/context/pgf/math/*
%_datadir/texmf/tex/context/pgf/systemlayer/*
%_datadir/texmf/tex/context/pgf/utilities/*
%_datadir/texmf/tex/generic/pgf/basiclayer/*
%_datadir/texmf/tex/generic/pgf/frontendlayer/*
%_datadir/texmf/tex/generic/pgf/libraries/*
%_datadir/texmf/tex/generic/pgf/math/*
%_datadir/texmf/tex/generic/pgf/systemlayer/*
%_datadir/texmf/tex/generic/pgf/utilities/*
%_datadir/texmf/tex/latex/pgf/basiclayer/*
%_datadir/texmf/tex/latex/pgf/compatibility/*
%_datadir/texmf/tex/latex/pgf/frontendlayer/*
%_datadir/texmf/tex/latex/pgf/math/*
%_datadir/texmf/tex/latex/pgf/systemlayer/*
%_datadir/texmf/tex/latex/pgf/utilities/*
%_datadir/texmf/tex/plain/pgf/basiclayer/*
%_datadir/texmf/tex/plain/pgf/frontendlayer/*
%_datadir/texmf/tex/plain/pgf/math/*
%_datadir/texmf/tex/plain/pgf/systemlayer/*
%_datadir/texmf/tex/plain/pgf/utilities/*
%doc doc/generic/pgf/*

%changelog
* Fri Nov 13 2009 Andrey Bergman <vkni@altlinux.org> 1.18-alt2
- Removed post and pre sections. Added dependence on rpm-build-texmf.

* Fri Mar 07 2008 Andrey Bergman <vkni@altlinux.org> 1.18-alt1
- pgf code update, added dependency on xkeyval (required for TikZ)

* Mon Oct 29 2005 Constantin (Const) Mikhaylenko <const at altlinux.ru> 1.00-alt1
- first stable version.
- Renamed from tetel-latex-pgf
* Mon Nov 11 2004 Constantin (Const) Mikhaylenko <const at altlinux.ru> 0.65-alt1
- Fixed bug in pgfshade.sty that arises in conjunction with calc.sty and latex+dvips.
* Mon Oct 27 2004 Constantin (Const) Mikhaylenko <const at altlinux.ru> 0.64-alt1
- initial release for Sisyphus
