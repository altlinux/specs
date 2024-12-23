Name:    sakura
Version: 3.8.8
Release: alt1

Summary: Simple but powerful libvte based terminal emulator for X11
License: GPLv2 
Group:   Terminals
Url:     https://github.com/dabisu/sakura

Packager: Ulysses Apokin <ulysses@altlinux.org>

Source: %name-%version.tar
Patch0: 0001-Removed-image-installation-from-cmake.patch
Patch1: 0002-New-palette-added-monochrome.patch

Provides: xvt
Provides: x-terminal-emulator

BuildRequires(pre): cmake gcc-c++
BuildRequires: libvte3-devel libgtk+3-devel libpcre2-devel pkgconfig
BuildRequires: libffi-devel perl-podlators

# For desktop file
BuildRequires: desktop-file-utils

# For to convert SVG to PNG
BuildRequires: ImageMagick

%description
Sakura is a terminal emulator and it's only dependencies are GTK and VTE.
It uses a notebook to provide several terminals in one window and allows to
change configuration options via a contextual menu. No more no less.

%prep
%setup
%patch0 -p1
%patch1 -p1
mv terminal-tango.svg %name-terminal-emulator.svg
magick -background none %name-terminal-emulator.svg -strip %name-terminal-emulator.png

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
%find_lang %name

install -Dm 644 %name-terminal-emulator.png \
	%buildroot%_pixmapsdir/%name-terminal-emulator.png

desktop-file-install --dir %buildroot%_desktopdir \
	--set-icon=%name-terminal-emulator \
	--set-generic-name=%name \
	%buildroot%_desktopdir/%name.desktop

%files -f %name.lang
%_bindir/%name
%doc README.* LICENSE AUTHORS
%_desktopdir/%name.desktop
%_pixmapsdir/%name-terminal-emulator.*
%_man1dir/%name.1.xz

%changelog
* Tue Dec 03 2024 Ulysses Apokin <ulysses@altlinux.org> 3.8.8-alt1
- new version

* Tue Nov 06 2018 Konstantin Artyushkin <akv@altlinux.org> 3.6.0-alt2
- new version

* Mon Dec 04 2017 Konstantin Artyushkin <akv@altlinux.org> 3.5.0-alt2
- new version

* Fri Sep 08 2017 Konstantin Artyushkin <akv@altlinux.org> 3.4.0-alt2
- new version

* Sat Apr 30 2016 Konstantin Artyushkin <akv@altlinux.org> 3.3.4-alt2
- new version

* Sat Apr 30 2016 Konstantin Artyushkin <akv@altlinux.org> 3.2.0-alt5
- fix of unpacked INSTALL file

* Sat May 16 2015 Konstantin Artyushkin <akv@altlinux.org> 3.2.0-alt4
- Remove patches

* Sat Apr 11 2015 Konstantin Artyushkin <akv@altlinux.org> 3.2.0-alt3
-  3.2.0 build 

* Tue Feb 26 2013 Mykola Grechukh <gns@altlinux.ru> 2.4.2-alt3
- REALLY fixed (closes: #28607)

* Tue Feb 19 2013 Mykola Grechukh <gns@altlinux.ru> 2.4.2-alt2
- default font fixed

* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 2.4.2-alt1
- new version.

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.4.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for sakura

* Mon Feb 14 2011 Mykola Grechukh <gns@altlinux.ru> 2.4.0-alt1
- new version. Manpage fixed

* Wed Jun 09 2010 Mykola Grechukh <gns@altlinux.ru> 2.3.8-alt1
- new version. Default configfile added

* Tue Apr 13 2010 Mykola Grechukh <gns@altlinux.ru> 2.3.7-alt2
- build fixed

* Tue Apr 13 2010 Mykola Grechukh <gns@altlinux.ru> 2.3.7-alt1
- new version

* Tue May 26 2009 Nick S. Grechukh <gns@altlinux.org> 2.3.3-alt1
- new version

* Thu Oct 09 2008 Nick S. Grechukh <gns@altlinux.org> 2.3.0-alt2
- new version

* Mon Aug 04 2008 Nick S. Grechukh <gns@altlinux.org> 2.2.0-alt1
- first build
