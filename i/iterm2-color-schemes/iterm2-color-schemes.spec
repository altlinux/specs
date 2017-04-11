Name: iterm2-color-schemes
Version: 0.1
Release: alt1

Summary: This is a set of color schemes for iTerm (aka iTerm2))
License: GPL
Group: Graphics

Url: https://github.com/mbadolato/iTerm2-Color-Schemes
Source: %name-%version.tar
Packager:  Konstantin Artyushkin <akv@altlinux.org>

BuildArch: noarch

Requires: %name-xfce4-terminal
Requires: %name-kde-konsole

%description
%summary meta-package

%package xfce4-terminal
Summary: iterm2 colorschemes for xfce4-terminal
License: GPL
Group: Graphical desktop/XFce

%description xfce4-terminal
iterm2 colorschemes for xfce4-terminal

%package kde-konsole
Summary: iterm2 colorschemes for kde4(5)-konsole
License: GPL
Group: Graphical desktop/KDE

%description kde-konsole
iterm2 colorschemes for kde4(5)-konsole

%prep
%setup


%install
pushd xfce4terminal
mkdir -p %buildroot%_datadir/xfce4/terminal/colorschemes
cp colorschemes/*.theme %buildroot%_datadir/xfce4/terminal/colorschemes
popd

pushd konsole
mkdir -p %buildroot%_datadir/kf5/konsole/
cp ./*.colorscheme %buildroot%_datadir/kf5/konsole/
popd

%files

%files xfce4-terminal
%_datadir/xfce4/terminal/colorschemes/*.theme

%files kde-konsole
%_datadir/kf5/konsole/*.colorscheme

%changelog
* Sun Oct 23 2016 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt1
- intial build for ALTLinux

