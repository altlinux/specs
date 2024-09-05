Name: rpm-macros-dqt5-webengine
Version: 0.4
Release: alt0.dde.1
BuildArch: noarch

Summary: Arch macro to build qt5-webengine clients
License: MIT
Group: Development/KDE and QT

Source0: macros

%description
qt-webengine supports only some architectures.

This package provides macro with a list of architectures supported
by qt5-webengine.

%install
mkdir -p %buildroot%_rpmmacrosdir
cp %SOURCE0 %buildroot%_rpmmacrosdir/dqt5-webengine

%files
%_rpmmacrosdir/dqt5-webengine

%changelog
* Thu May 30 2024 Leontiy Volodin <lvol@altlinux.org> 0.4-alt0.dde.1
- fork qt5 for separate deepin buildings (ALT #48138)

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 0.4-alt1
- %%qt5_qtwebengine_arches: remove ppc64le architecture.

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- add %%not_qt5_qtwebengine_arches macro

* Thu Jun 27 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2-alt1
- %%qt5_qtwebengine_arches: add ppc64le architecture.

* Tue Feb 12 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Initial build.
