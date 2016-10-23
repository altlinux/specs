Name: xfce4-terminal-iterm2-themes
Version: 0.1
Release: alt1

Summary: This is a set of color schemes for iTerm (aka iTerm2))
License: GPL
Group: Graphical desktop/XFce

Url: https://github.com/gBopHuk/iTerm2-Color-Schemes/archive/xfce4terminal.zip
Source: %name-%version.tar
Packager:  Konstantin Artyushkin <akv@altlinux.org>

BuildArch: noarch

%description
%summary

%prep
%setup


%install
pushd xfce4terminal
mkdir -p %buildroot%_datadir/xfce4/terminal/colorschemes
cp colorschemes/*.theme %buildroot%_datadir/xfce4/terminal/colorschemes
popd

%files
%_datadir/xfce4/terminal/colorschemes/*.theme

%changelog
* Sun Oct 23 2016 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt1
- intial build for ALTLinux

