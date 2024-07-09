# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%define sover 14

Name: libfm-qt6
Version: 2.0.2
Release: alt1

Summary: Core library of PCManFM-Qt file manager
License: LGPL-2.1
Group: System/Libraries

Url: https://github.com/lxqt/libfm-qt
Source: %name-%version.tar

BuildRequires: rpm-macros-cmake
BuildRequires: cmake
BuildRequires: rpm-build-xdg
BuildRequires: gcc-c++
BuildRequires: lxqt2-build-tools
BuildRequires: libexif-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libmenu-cache) >= 1.1.0
BuildRequires: lxqt-menu-data-devel

Requires: lxqt-menu-data >= 2.0.0

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
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -name '*.cpp' -o -name '*.hpp' -o -name '*.h' -print0 |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake
export NPROCS=1
%cmake_build

%install
%cmake_install

# We need to fix this upstream
find %buildroot -size 0 -delete

%files
%_libdir/%name.so.%sover
%_libdir/%name.so.%sover.*
%_datadir/%name/
%_xdgmimedir/packages/%name-mimetypes.xml

%files devel
%_libdir/%name.so
%_includedir/%name/
%_pkgconfigdir/%name.pc
%_datadir/cmake/fm-qt6
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Wed Jun 12 2024 Anton Midyukov <antohami@altlinux.org> 2.0.2-alt1
- New version 2.0.2
- rename libfm-qt -> libfm-qt6

* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Sat Nov 26 2022 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1.1
- fix

* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Apr 17 2022 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Fri Nov 05 2021 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Fri Apr 16 2021 Anton Midyukov <antohami@altlinux.org> 0.17.1-alt1
- new version 0.17.1

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Fri May 29 2020 Anton Midyukov <antohami@altlinux.org> 0.15.1-alt1
- new version 0.15.1

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Mon Jun 24 2019 Michael Shigorin <mike@altlinux.org> 0.14.1-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Sat Aug 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.1-alt1.1
- Rebuilt with qt 5.11

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

