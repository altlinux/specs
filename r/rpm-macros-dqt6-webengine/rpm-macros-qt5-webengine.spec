Name: rpm-macros-dqt6-webengine
Version: 0.2
Release: alt1.dde.1

BuildArch: noarch

Group: Development/KDE and QT
Summary: Arch macro to build dqt6-webengine clients
License: MIT

Source0: macros

%description
qt-webengine supports only some architectures.

This package provides macro with a list of architectures supported
by qt6-webengine.

%install
mkdir -p %buildroot%_rpmmacrosdir
cp %SOURCE0 %buildroot%_rpmmacrosdir/dqt6-webengine

%files
%_rpmmacrosdir/dqt6-webengine

%changelog
* Thu Aug 07 2025 Leontiy Volodin <lvol@altlinux.org> 0.2-alt1.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Apr 09 2024 Sergey V Turchin <zerg@altlinux.org> 0.2-alt2
- bump release

* Tue Apr 09 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.2-alt1
- Added LoongArch to list of supported architectures

* Fri Jun 03 2022 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
