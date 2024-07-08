%define git efa2712

Name: piper
Version: 0.7
Release: alt4.g%{git}
Summary: GTK+ application to configure gaming mice using ratbagd
Group: System/Configuration/Hardware
License: GPLv2
Url: https://github.com/libratbag/%name
Source0: https://github.com/libratbag/%name/archive/v%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: python3-module-pygobject3-devel python3-dev python3-module-flake8 gtk-update-icon-cache
BuildRequires: python3-module-pycairo python3-module-lxml python3-module-evdev ratbagd >= 0.17-alt2 appstream

BuildArch: noarch

# due API change
Requires: ratbagd >= 0.17-alt2

%description
Piper is a GTK+ application to configure gaming mice, using libratbag via
ratbagd.  In order to run Piper, ratbagd has to be running (without it, you'll
get to see a pretty mouse trap).

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README* COPYING
%_bindir/*
%dir %python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name
%dir %_datadir/%name
%_datadir/%name
%_datadir/metainfo/org.freedesktop.Piper.appdata.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_man1dir/*

%changelog
* Mon Jul 08 2024 L.A. Kostis <lakostis@altlinux.ru> 0.7-alt4.gefa2712
- Fix FTBFS: added gtk-update-icon-cache BR.

* Tue Jun 25 2024 L.A. Kostis <lakostis@altlinux.ru> 0.7-alt3.gefa2712
- Bump ratbag requires due API change.

* Tue Jun 25 2024 L.A. Kostis <lakostis@altlinux.ru> 0.7-alt2.gefa2712
- 0.7-123-gefa2712.

* Fri Sep 23 2022 L.A. Kostis <lakostis@altlinux.ru> 0.7-alt1
- 0.7.

* Mon Jul 19 2021 L.A. Kostis <lakostis@altlinux.ru> 0.5.1-alt20.ge117e87
- 0.5.1-20-ge117e87.
- Update BR (added flake8).

* Wed Nov 04 2020 L.A. Kostis <lakostis@altlinux.ru> 0.5.1-alt0.1
- 0.5.1.

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 0.4-alt0.1
- 0.4.

* Fri Sep 13 2019 L.A. Kostis <lakostis@altlinux.ru> 0.3-alt0.1.gitc7933aa
- 0.3-13-gc7933aa.

* Mon Apr 30 2018 L.A. Kostis <lakostis@altlinux.ru> 0.2.900-alt0.3.git5f6ed20
- GIT 5f6ed20.

* Thu Jan 04 2018 L.A. Kostis <lakostis@altlinux.ru> 0.2.900-alt0.2.gitd243325
- GIT d243325.

* Wed Oct 25 2017 L.A. Kostis <lakostis@altlinux.ru> 0.2.900-alt0.1.git39ddd05
- GIT 39ddd05.
- initial build for ALTLinux.
