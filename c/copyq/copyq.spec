Name: copyq
Version: 6.4.0
Release: alt1.1

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
BuildRequires: qt5-tools-devel qt5-svg-devel qt5-x11extras-devel
BuildRequires: qt5-wayland-devel wayland-devel libwayland-cursor-devel qt5-declarative-devel
BuildRequires: kf5-knotifications-devel

%description
CopyQ is advanced clipboard manager with searchable and editable history with
support for image formats, command line control and more.

%prep
%setup
%__subst '/DQT_RESTRICTED_CAST_FROM_ASCII/d' CMakeLists.txt

%build
%cmake \
  -Wno-dev \
  -DWITH_QT6:BOOL=OFF \
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
%_datadir/metainfo/com.github.hluk.%name.appdata.xml
%_desktopdir/com.github.hluk.%name.desktop
%_datadir/bash-completion/completions/copyq
%_iconsdir/hicolor/*/apps/%{name}*.png
%_iconsdir/hicolor/*/apps/%{name}*.svg
%dir %_datadir/%name/
%dir %_datadir/%name/locale/
%_datadir/%name/themes/
%_man1dir/%name.1.*

%changelog
* Fri Mar 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1.1
- NMU: build with Qt5 (closes: 45722)

* Wed Mar 22 2023 Vitaly Lipatov <lav@altlinux.ru> 6.4.0-alt1
- initial build for ALT Sisyphus
