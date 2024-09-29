# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: picom
Version: 12.1
Release: alt1
Summary: A lightweight compositor for X11
License: MPL-2.0 or MIT
Group: System/X11
Url: https://github.com/yshui/picom
Source: %name-%version.tar
Source44: %name.watch

ExcludeArch: %ix86

Obsoletes: compton < %EVR
Provides: compton = %version

BuildRequires: asciidoc-a2x
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libconfig-devel
BuildRequires: libGL-devel
BuildRequires: libEGL-devel
BuildRequires: libepoxy-devel
BuildRequires: libdbus-devel
BuildRequires: libev-devel
BuildRequires: libuthash-devel
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libxdg-basedir)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: asciidoctor

%description
This is forked from the original Compton because it seems to have become
unmaintained.

The current battle plan of this fork is to refactor it to make the code
possible to maintain, so potential contributors won't be scared away when they
take a look at the code.

We also try to fix bugs.

You can leave your feedbacks or thoughts in the discussion tab.

%prep
%setup
%ifarch %e2k
sed -i "s/const auto/auto/" src/{render,win,picom}.c src/backend/xrender/xrender.c
sed -i "s/__attribute__((optimize(".*")))//" src/utils.h
sed -i "/#warning Use of -ffast-math/s/#warning/#error/" src/utils.h
%endif

%build
%meson -D with_docs=True
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc CONTRIBUTORS LICENSE.* README* dbus-examples man/%{name}* picom.sample.conf
%_bindir/*
%_sysconfdir/xdg/autostart/picom.desktop
%exclude %_datadir/applications/*.desktop
%_iconsdir/hicolor/*/*/*
%_man1dir/*
%_pkgconfigdir/picom-api.pc

%changelog
* Sun Sep 29 2024 Anton Midyukov <antohami@altlinux.org> 12.1-alt1
- New version 12.1.
- ExcludeArch: %%ix86

* Thu Feb 15 2024 Anton Midyukov <antohami@altlinux.org> 11.2-alt1
- New version 11.2.

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 11.1-alt1
- New version 11.1.

* Mon Jan 22 2024 Anton Midyukov <antohami@altlinux.org> 11-alt1
- new version 11

* Thu Jan 11 2024 Fr. Br. George <george@altlinux.ru> 10.2-alt2
- Add manpages build

* Sat Jan 21 2023 Anton Midyukov <antohami@altlinux.org> 10.2-alt1
- new version 10.2
- add %_sysconfdir/xdg/autostart/picom.desktop
- exclude %_datadir/applications/*.desktop

* Wed Mar 23 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 9.1-alt2
- fixed build for Elbrus

* Sun Mar 06 2022 Anton Midyukov <antohami@altlinux.org> 9.1-alt1
- new version 9.1

* Sat Oct 30 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 8.2-alt2
- fixed build for Elbrus

* Fri Aug 13 2021 Ildar Mulyukov <ildar@altlinux.ru> 8.2-alt1
- upstream renamed compton to picom

* Sun Jun 20 2021 Anton Midyukov <antohami@altlinux.org> 5.1-alt2
- Add missing buildrequires rpm-build-python3

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 5.1-alt1
- new version 5.1

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 5-alt1
- new version 5
- fix license
- fix URL

* Fri Aug 01 2014 Konstantin Artyushkin <akv@altlinux.org> 0.1_beta2_1-alt3
- change Group

* Fri Aug 01 2014 Konstantin Artyushkin <akv@altlinux.org> 0.1_beta2_1-alt2
- update compton 

* Thu Aug 23 2012 bla-bla <bla-bla@gmail.com> - alt1
- This packeg was create with --no-sisyphus-chek parameter and can contains some mistakes
- Данный пакет был собран с параметрами --no-sisyphus-check и может содежать ошибки
