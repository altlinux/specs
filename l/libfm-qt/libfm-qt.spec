Name: libfm-qt
Version: 0.13.1
Release: alt1

Summary: Core library of PCManFM-Qt file manager
License: LGPLv2+
Group: System/Libraries

Url: https://lxqt.org
Source: %name-%version.tar

BuildRequires: cmake rpm-macros-cmake
BuildRequires: rpm-build-xdg
BuildRequires: gcc-c++
BuildRequires: lxqt-build-tools >= 0.5.0
BuildRequires: libexif-devel
BuildRequires: qt5-base-devel 
BuildRequires: qt5-tools-devel
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(libfm) >= 1.2.0
BuildRequires: pkgconfig(libmenu-cache) >= 0.4.0

Conflicts: libfm-qt3
Obsoletes: libfm-qt3

%description
LibFM-Qt is a core library of PCManFM-Qt file manager.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: libexif-devel libmenu-cache-devel
Requires: %name = %EVR

%description devel
This package contains files needed to build applications using LibFM-Qt.

%prep
%setup

%build
%cmake -DPULL_TRANSLATIONS=OFF \
       -DUPDATE_TRANSLATIONS=OFF
%cmake_build

%install
%cmakeinstall_std

# We need to fix this upstream
find %buildroot -size 0 -delete

%files
%_libdir/*.so.*
%_datadir/%name/
%_xdgmimedir/*/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_datadir/cmake/fm-qt/*
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Tue Jun 05 2018 Anton Midyukov <antohami@altlinux.org> 0.13.1-alt1
- new version 0.13.1

* Mon May 28 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt2
- obsoletes libfm-qt3

* Thu May 24 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 0.11.1-alt1
- built for sisyphus (partially based on fedora spec)

