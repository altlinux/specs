Name: rofi
Version: 1.7.5+wayland2
Release: alt1
Summary: A window switcher, run dialog and dmenu replacement
License: MIT
Group: Graphical desktop/Other
Url: https://davedavenport.github.io/rofi/
Vcs: https://github.com/lbonn/rofi

Source: https://github.com/lbonn/rofi/releases/download/1.7.5+wayland2/rofi-1.7.5+wayland2.tar.gz
#It tries to use x-terminal-emulator which is only available on debian systems, I replace it with xdg-terminal.
#Patch: 0001-Replace-x-terminal-emulator-with-xdg-terminal.patch
Patch: 0002-Workaround-for-ALT-flex-changes-ALT-35141.patch

BuildRequires(pre): rpm-macros-meson
# Automatically added by buildreq on Fri Nov 24 2023
# optimized out: glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libcairo-devel libgdk-pixbuf libgio-devel libgpg-error libharfbuzz-devel libstartup-notification libwayland-client libwayland-client-devel libwayland-cursor libxcb-devel libxcb-render-util libxcbutil-cursor libxcbutil-icccm libxcbutil-image libxkbcommon-devel libxkbcommon-x11 ninja-build pkg-config python3 python3-base python3-dev python3-module-setuptools sh5 wayland-devel xml-utils xorg-proto-devel xz
BuildRequires: flex libcheck-devel libgdk-pixbuf-devel libpango-devel libstartup-notification-devel libwayland-cursor-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel meson wayland-protocols

Requires: xdg-utils

%description
https://github.com/lbonn/rofi fork with Wayland support

A popup window switcher roughly based on superswitcher, requiring only xlib and pango.
This version started off as a clone of simpleswitcher, the version from Sean Pringle.
All credit for this great tool should go to him. Rofi developed extra features,
like a run-dialog, ssh-launcher and can act as a drop-in dmenu replacement, making it a very versatile tool.

%package devel
Summary: headers file for rofi launcher
Group: Graphical desktop/Other
Requires: %name

%description devel
%summary

%prep
%setup
%patch0 -p1

%build
%meson \

%meson_build

%install
%meson_install

%files
%doc Changelog README.md COPYING
%_bindir/rofi
%_bindir/rofi-*
%_man1dir/%name.*
%_man1dir/%name-*
%_man5dir/%name-*
%_datadir/%name/themes/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/rofi.svg

%files devel
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Fri Nov 24 2023 Ildar Mulyukov <ildar@altlinux.ru> 1.7.5+wayland2-alt1
- switch to the wayland port

* Mon Aug 07 2023 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- new version 1.7.5 (with rpmrb script)
- add BR: libxcbutil-cursor-devel, cleanup spec

* Mon Jun 21 2021 Ivan A. Melnikov <iv@altlinux.org> 1.6.1-alt1
- 1.6.1

* Wed Aug 07 2019 Konstantin Artyushkin <akv@altlinux.org> 1.5.4-alt2
- New 1.5.4 version

* Tue Jul 03 2018 Konstantin Artyushkin <akv@altlinux.org> 1.5.1-alt2
- add workaround for segfault ALTBUG-35141

* Tue Jul 03 2018 Konstantin Artyushkin <akv@altlinux.org> 1.5.1-alt1
- update

* Mon Mar 13 2017 Konstantin Artyushkin <akv@altlinux.org> 1.3.1-alt1
- update

* Tue Oct 18 2016 Konstantin Artyushkin <akv@altlinux.org> 1.2.0-alt1
- new version

* Wed Jul 13 2016 Konstantin Artyushkin <akv@altlinux.org> 1.1.0-alt2
- new 1.1.0 version

* Thu May 12 2016 Konstantin Artyushkin <akv@altlinux.org> 1.0.1-alt2
- new version 1.0.1

* Tue Jan 26 2016 Konstantin Artyushkin <akv@altlinux.org> 0.15.7-alt3
- replace man file extension

* Mon Sep 21 2015 Konstantin Artyushkin <akv@altlinux.org> 0.15.7-alt2
- initial build for ALT Linux Sisyphus

