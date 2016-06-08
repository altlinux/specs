Name:		gamine
Version:	1.5
Release:	alt1
Summary:	An interactive game for young children
Source:		%name-%version.tar.gz
Source1:	%name.desktop.in
URL:		http://gamine-game.sourceforge.net/:q
Group:		Games/Educational
License:	GPLv3+

BuildRequires:  gstreamer1.0-devel libgtk+3-devel intltool

%description
Gamine is a game designed for 2 years old children who are not able to
use mouse and keyboard.

The child uses the mouse to draw coloured dots and lines on the screen
and keyboard to display letter.

Author:
--------
GARETTE Emmanuel (gnunux@gnunux.info)

%prep
%setup
cp %SOURCE1 .

%build
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%config(noreplace) %_sysconfdir/%name.conf
%_desktopdir/%name.desktop
%_datadir/doc/%name/*
%_datadir/%name/*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man6dir/%name.6*

%changelog
* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- New version

* Fri Feb 21 2014 Andrey Cherepanov <cas@altlinux.org> 1.1-alt4
- Fix build in Sisyphus (missing libm in linked libs)

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 1.1-alt3
- Adapt BuildRequires to new version of GConf

* Fri Jun 01 2012 Andrey Cherepanov <cas@altlinux.org> 1.1-alt2
- Add required X11 library to the linker command line

* Wed Aug 17 2011 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Initial build for Sisyphus (thanks kostyalamer) (closes: #26074)

