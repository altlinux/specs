# spec by Konstantin Kogan <kostyalamer at yandex.ru> 

Name: wmaker-theme-cl_lumen_blue
Version: 0.60.0
Release: alt1

Summary: WindowMaker theme
Summary(ru_RU.UTF-8): тема для WindowMaker
License: GPL2
Group: Graphical desktop/Window Maker
Source: %name-%version.tar.bz2
Requires: WindowMaker >= 0.60.0
Url:  http://box-look.org/index.php?xsortmode=down&page=0&xcontentmode=7313

Provides: cl_lumen_blue-theme = %version-%release
Obsoletes: cl_lumen_blue-theme

BuildArch: noarch

%description
WindowMaker theme

%description -l ru_RU.UTF-8
тема для WindowMaker

%prep
%setup

%install
mkdir -p %buildroot%_datadir/WindowMaker/Themes/Cl_Lumen_Blue.themed/
install -m644 * %buildroot%_datadir/WindowMaker/Themes/Cl_Lumen_Blue.themed/

%files
%_datadir/WindowMaker/Themes/Cl_Lumen_Blue.themed/

%changelog
* Sun Jan 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.60.0-alt1
- Initial build for Sisyphus

