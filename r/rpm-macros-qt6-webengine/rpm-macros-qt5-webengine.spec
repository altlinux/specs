Name: rpm-macros-qt6-webengine
Version: 0.1
Release: alt1

BuildArch: noarch

Group: Development/KDE and QT
Summary: Arch macro to build qt6-webengine clients
License: MIT

Source0: macros

%description
qt-webengine supports only some architectures.

This package provides macro with a list of architectures supported
by qt6-webengine.

%install
mkdir -p %buildroot%_rpmmacrosdir
cp %SOURCE0 %buildroot%_rpmmacrosdir/qt6-webengine

%files
%_rpmmacrosdir/qt6-webengine

%changelog
* Fri Jun 03 2022 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
