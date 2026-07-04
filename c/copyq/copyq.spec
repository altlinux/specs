Name: copyq
Version: 16.0.0
Release: alt1

Summary: CopyQ - Advanced clipboard manager

License: GPL-3.0-or-later
Group: Text tools
Url: https://github.com/hluk/CopyQ/

# Source-url: https://github.com/hluk/CopyQ/archive/refs/tags/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake, extra-cmake-modules, gcc-c++

BuildRequires: libXtst-devel, libXfixes-devel
BuildRequires: qt6-tools-devel qt6-svg-devel
BuildRequires: qt6-wayland-devel wayland-devel libwayland-cursor-devel qt6-declarative-devel
BuildRequires: kf6-knotifications-devel kf6-kstatusnotifieritem-devel kf6-kguiaddons-devel
BuildRequires: qca-qt6-devel libqtkeychain-qt6-devel
BuildRequires: miniaudio-devel

%description
CopyQ is advanced clipboard manager with searchable and editable history with
support for image formats, command line control and more.

%prep
%setup
%__subst '/DQT_RESTRICTED_CAST_FROM_ASCII/d' CMakeLists.txt

%build
%cmake \
  -Wno-dev \
  -DWITH_QT6:BOOL=ON \
  -DWITH_AUDIO:BOOL=ON \
  -DMINIAUDIO_INCLUDE_DIR=%_includedir/miniaudio \
  -DWITH_TESTS:BOOL=ON \
  -DPLUGIN_INSTALL_PREFIX=%_libdir/%name/plugins \
  -DTRANSLATION_INSTALL_PREFIX:PATH=%_datadir/%name/locale
%cmake_build

%install
%cmake_install
%find_lang %name --with-qt

%files -f %name.lang
%doc AUTHORS CHANGES.md HACKING README.md
%doc LICENSE
%_bindir/%name
%_libdir/%name/
%_datadir/metainfo/com.github.hluk.%name.metainfo.xml
%_desktopdir/com.github.hluk.%name.desktop
%_datadir/bash-completion/completions/copyq
%_iconsdir/hicolor/*/apps/%{name}*.png
%_iconsdir/hicolor/*/apps/%{name}*.svg
%dir %_datadir/%name/
%dir %_datadir/%name/locale/
%_datadir/%name/themes/
%_datadir/gnome-shell/extensions/copyq-clipboard@hluk.github.com/
%_man1dir/%name.1.*

%changelog
* Wed Jul 01 2026 Vitaly Lipatov <lav@altlinux.ru> 16.0.0-alt1
- new version 16.0.0

* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 15.0.0-alt1
- new version 15.0.0
- drop alt-qt6.10.patch (fixed in upstream)
- pack gnome-shell extension

* Mon Apr 06 2026 Vitaly Lipatov <lav@altlinux.ru> 14.0.0-alt1
- new version 14.0.0
- build with qca-qt6, qt6keychain, miniaudio support

* Thu Jan 22 2026 Sergey V Turchin <zerg@altlinux.org> 13.0.0-alt2
- fix compile with Qt-6.10

* Sat Dec 20 2025 Vitaly Lipatov <lav@altlinux.ru> 13.0.0-alt1
- new version 13.0.0 (with rpmrb script)
- build with Qt6 instead of Qt5 (ALT bug 45722)

* Thu May 22 2025 Vitaly Lipatov <lav@altlinux.ru> 10.0.0-alt1
- new version 10.0.0 (with rpmrb script)

* Mon Dec 02 2024 Vitaly Lipatov <lav@altlinux.ru> 9.1.0-alt1
- new version 9.1.0 (with rpmrb script)

* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 7.1.0-alt1
- new version 7.1.0 (with rpmrb script)

* Sat May 06 2023 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt1
- new version 7.0.0 (with rpmrb script)

* Fri Mar 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1.1
- NMU: build with Qt5 (closes: 45722)

* Wed Mar 22 2023 Vitaly Lipatov <lav@altlinux.ru> 6.4.0-alt1
- initial build for ALT Sisyphus
