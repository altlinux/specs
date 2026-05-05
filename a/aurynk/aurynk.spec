%define _unpackaged_files_terminate_build 1

Name: aurynk
Version: 1.3.1
Release: alt1

Summary: Wirelessly connect, manage and control your Android devices from Linux
License: GPL-3.0-or-later
Group: Networking/Remote access
URL: https://theishu.xyz/aurynk
Vcs: https://github.com/IshuSinghSE/aurynk

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-systemd

BuildRequires: meson
BuildRequires: cmake
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: pkgconfig(gio-2.0)

Requires: /usr/bin/adb
Requires: /usr/bin/scrcpy
Requires: /usr/bin/xdg-open
Requires: python3-module-qrcode
Requires: python3-module-zeroconf

%filter_from_requires /typelib(gi)/d

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Aurynk is a modern Android device manager for Linux that allows you to
wirelessly pair and manage your Android devices using ADB (Android Debug Bridge).

Features:

* Wireless pairing via QR code
* Device information and specifications
* Screenshot capture
* Modern GTK4/libadwaita interface
* Easy device management

%prep
%setup
%patch -p1
sed -i "s|Categories=.*|Categories=Network;RemoteAccess;|" data/io.github.IshuSinghSE.aurynk.desktop.in
sed -i "s|data/icons/io.github.IshuSinghSE.aurynk.png|%_iconsdir/hicolor/128x128/apps/io.github.IshuSinghSE.aurynk.png|" README.md
sed -i "s|data/screenshots/|screenshots/|g" README.md

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc CHANGELOG.md LICENSE README.md data/screenshots
%_bindir/aurynk
%_desktopdir/io.github.IshuSinghSE.aurynk.desktop
%_iconsdir/hicolor/*/apps/io.github.IshuSinghSE.aurynk.png
%_iconsdir/hicolor/*/apps/io.github.IshuSinghSE.aurynk.*.png
%_iconsdir/hicolor/scalable/apps/io.github.IshuSinghSE.aurynk.svg
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/metainfo/io.github.IshuSinghSE.aurynk.metainfo.xml
%python3_sitelibdir/%name/

%changelog
* Tue May 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.1-alt1
- New version 1.3.1.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Thu Jan 15 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.2-alt1
- New version 1.2.2.

* Mon Jan 12 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1
- New version 1.2.1 (closes: #57233).

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

* Thu Nov 27 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.0-alt2
- Put aurynk_tray.py into correct location, and enabled tray icon.

* Wed Nov 26 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
