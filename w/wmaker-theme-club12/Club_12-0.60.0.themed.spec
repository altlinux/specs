# spec by Konstantin Kogan <ALT Linux Active Users Club> 

Name: wmaker-theme-club12
Version: 0.60.0
Release: alt1

Summary: WindowMaker theme
Summary(ru_RU.UTF-8): тема для WindowMaker
License: GPL2
Group: Graphical desktop/Window Maker
Source:%name-%version.tar.bz2
Requires: WindowMaker >= 0.60.0

Provides: %name-theme = %version-%release
Obsoletes:  %name-theme

BuildArch: noarch

%description
WindowMaker theme

%description -l ru_RU.UTF-8
тема для WindowMaker

%prep
%setup

%install
mkdir -p %buildroot%_datadir/WindowMaker/Themes/%name.themed/
install -m644 * %buildroot%_datadir/WindowMaker/Themes/%name.themed/

%files
%_datadir/WindowMaker/Themes/%name.themed/

%changelog
* Sun Jan 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.60.0-alt1
- Initial build for Sisyphus

