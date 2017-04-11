Name: iterm2-color-schemes
Version: 0.1
Release: alt2

Summary: This is a set of color schemes for iTerm (aka iTerm2))
License: GPL
Group: Graphics

Url: https://github.com/mbadolato/iTerm2-Color-Schemes
Source: %name-%version.tar
Packager:  Konstantin Artyushkin <akv@altlinux.org>

BuildArch: noarch

Requires: %name-xfce4-terminal
Requires: %name-kde4-konsole
Requires: %name-kde5-konsole

%description
%summary meta-package

%package xfce4-terminal
Summary: iterm2 colorschemes for xfce4-terminal
License: GPL
Group: Graphical desktop/XFce

%description xfce4-terminal
iterm2 colorschemes for xfce4-terminal

%package kde4-konsole
Summary: iterm2 colorschemes for kde4-konsole
License: GPL
Group: Graphical desktop/KDE

%description kde4-konsole
iterm2 colorschemes for kde4-konsole

%package kde5-konsole
Summary: iterm2 colorschemes for kde5-konsole
License: GPL
Group: Graphical desktop/KDE

%description kde5-konsole
iterm2 colorschemes for kde5-konsole

%prep
%setup


%install
pushd xfce4terminal
mkdir -p %buildroot%_datadir/xfce4/terminal/colorschemes
cp colorschemes/*.theme %buildroot%_datadir/xfce4/terminal/colorschemes
popd

pushd konsole
#kde4
mkdir -p %buildroot%_datadir/kde4/apps/konsole/
cp ./*.colorscheme %buildroot%_datadir/kde4/apps/konsole/
#kde5
mkdir -p %buildroot%_datadir/kf5/konsole/
cp ./*.colorscheme %buildroot%_datadir/kf5/konsole/
popd

%files

%files xfce4-terminal
%_datadir/xfce4/terminal/colorschemes/*.theme

%files kde4-konsole
%_datadir/kde4/apps/konsole/*.colorscheme

%files kde5-konsole
%_datadir/kf5/konsole/*.colorscheme

%changelog
* Tue Apr 11 2017 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt2
- split the kde-konsole packagae to packges for kde4 and kde5

* Sun Oct 23 2016 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt1
- intial build for ALTLinux

