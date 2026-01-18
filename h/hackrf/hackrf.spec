%define sover 0
%define sorel 9.1

Name: hackrf
Version: 2026.01.1
Release: alt1
Summary: HackRF Utilities

Group: Engineering
License: GPL-2.0-or-later AND BSD-3-Clause
URL: https://greatscottgadgets.com/hackrf/
VCS: https://github.com/mossmann/hackrf

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libusb-devel
BuildRequires: udev-rules
BuildRequires: pkgconfig(fftw3f)

%description
Hardware designs and software for HackRF, a project to produce a low cost, open
source software radio platform.

%package -n lib%name%sover
Summary: Library for HackRF
Group: System/Libraries
Conflicts: hackrf < 2026.01.1

%description -n lib%name%sover
Library for HackRF.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: lib%name%sover = %EVR
Requires: libusb-devel

%description devel
Files needed to develop software against libhackrf.

%package doc
Summary: Supplemental documentation for HackRF
Group: Development/Other
BuildArch: noarch

%description doc
Supplemental documentation for HackRF. For more information, visit the wiki at
https://github.com/mossmann/hackrf/wiki

%prep
%setup
%autopatch -p1

%build
pushd host
%cmake \
    -DENABLE_STATIC_LIB=OFF \
    -DENABLE_SHARED_LIB=ON \
    -DINSTALL_UDEV_RULES=ON \
    -DUDEV_RULES_PATH:PATH=%_udevrulesdir \
    -DUDEV_RULES_GROUP=uucp

%cmake_build
popd

%install
pushd host
%cmake_install
popd

# fix version
sed -i 's/^Version:*/Version: %sover.%sorel/' %buildroot%_pkgconfigdir/libhackrf.pc

%files
%doc COPYING TRADEMARK Readme.md
%_bindir/hackrf_*
%_udevrulesdir/53-hackrf.rules

%files -n libhackrf%sover
%_libdir/libhackrf.so.%sover
%_libdir/libhackrf.so.%sover.%sorel

%files devel
%_includedir/libhackrf
%_pkgconfigdir/libhackrf.pc
%_libdir/libhackrf.so
%_libdir/cmake/HackRF/

#files doc
#_docdir/%name

%changelog
* Sun Jan 18 2026 Anton Midyukov <antohami@altlinux.org> 2026.01.1-alt1
- New version 2026.01.1.

* Sun Jan 11 2026 Anton Midyukov <antohami@altlinux.org> 2024.02.1-alt2
- Improvement spec.

* Sat Feb 24 2024 Anton Midyukov <antohami@altlinux.org> 2024.02.1-alt1
- New version 2024.02.1.

* Sun Apr 23 2023 Anton Midyukov <antohami@altlinux.org> 2023.01.1-alt1
- New version 2023.01.1.

* Thu Aug 26 2021 Anton Midyukov <antohami@altlinux.org> 2021.03.1-alt2
- disable building static libraries

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 2021.03.1-alt1
- new version 2021.03.1

* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 2018.01.1-alt1
- new version 2018.01.1

* Wed Oct 18 2017 Anton Midyukov <antohami@altlinux.org> 2015.07.2-alt1
- Initial build for ALT Sisyphus.
