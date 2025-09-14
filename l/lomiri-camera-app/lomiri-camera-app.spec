%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-camera-app
Version: 4.1.1
Release: alt1

Summary: Camera application for Lomiri
License: GPL-3.0 and CC-BY-SA-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/apps/lomiri-camera-app

# sync with version 4.1.1+dfsg-1 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(QZXing)
BuildRequires: pkgconfig(exiv2)

%if_with check
BuildRequires: ctest
BuildRequires: /usr/bin/xvfb-run
BuildRequires: liblomiri-action-api-qt5
BuildRequires: libqt5-quick
BuildRequires: libusermetrics
BuildRequires: lomiri-thumbnailer
BuildRequires: qml(Lomiri.Components)
BuildRequires: qml(Lomiri.Components.Extras)
BuildRequires: qml(Lomiri.Content)
BuildRequires: qml(QtPositioning)
BuildRequires: qml(QtSensors)
BuildRequires: qt5-tools
%endif

Requires: liblomiri-action-api-qt5
Requires: libqt5-quick
Requires: libusermetrics
Requires: lomiri-thumbnailer
Requires: qml(Lomiri.Components)
Requires: qml(Lomiri.Components.Extras)
Requires: qml(Lomiri.Content)
Requires: qml(QtPositioning)
Requires: qml(QtSensors)
Requires: qt5-tools

%description
An application to take pictures, videos and scan barcodes with device
camera(s) for Lomiri.

%prep
%setup
%patch -p1

rm -vf lomiri-camera-app-migrate.py

%build
%cmake \
       -DCMAKE_INSTALL_PREFIX=%_prefix \
       -DCLICK_MODE=OFF \
%if_with check
       -DINSTALL_TESTS=ON
%else
       -DINSTALL_TESTS=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README-Developers.md README.md
%_bindir/lomiri-camera-app
%dir %_datadir/lomiri-camera-app
%_datadir/lomiri-camera-app/*
%_datadir/lomiri-content-hub/peers/lomiri-camera-app
%dir %_libdir/lomiri-camera-app
%dir %_libdir/lomiri-camera-app/CameraApp
%_libdir/lomiri-camera-app/CameraApp/libcamera-qml.so
%_libdir/lomiri-camera-app/CameraApp/qmldir
%_desktopdir/lomiri-barcode-reader-app.desktop
%_desktopdir/lomiri-camera-app.desktop
%_iconsdir/hicolor/128x128/apps/lomiri-barcode-reader-app.png
%_iconsdir/hicolor/128x128/apps/lomiri-camera-app.png
%_iconsdir/hicolor/256x256/apps/lomiri-barcode-reader-app.png
%_iconsdir/hicolor/256x256/apps/lomiri-camera-app.png
%_iconsdir/hicolor/64x64/apps/lomiri-barcode-reader-app.png
%_iconsdir/hicolor/64x64/apps/lomiri-camera-app.png
%_iconsdir/hicolor/scalable/apps/lomiri-barcode-reader-app.svg
%_iconsdir/hicolor/scalable/apps/lomiri-camera-app.svg

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-camera-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-camera-app.mo

%changelog
* Sun Sep 14 2025 Nikolay Strelkov <snk@altlinux.org> 4.1.1-alt1
- New version 4.1.1.

* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 4.0.8-alt1
- Initial build for Sisyphus
