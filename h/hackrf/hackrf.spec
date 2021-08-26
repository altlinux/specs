Name: hackrf
Version: 2021.03.1
Release: alt2
Summary: HackRF Utilities

Group: Development/Other
License: GPLv2
Url: https://github.com/mossmann/%name
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch: disable_building_static_libraries.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libusb-devel
BuildRequires: udev-rules
BuildRequires: pkgconfig(fftw3f)

%description
Hardware designs and software for HackRF, a project to produce a low cost, open
source software radio platform.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release
Requires: libusb-devel

%description devel
Files needed to develop software against libhackrf.

%package doc
Summary: Supplemental documentation for HackRF
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description doc
Supplemental documentation for HackRF. For more information, visit the wiki at
https://github.com/mossmann/hackrf/wiki

%prep
%setup
%autopatch -p1

# Fix "plugdev" nonsense
%__subst 's/GROUP="@HACKRF_GROUP@"/ENV{ID_SOFTWARE_RADIO}="1"/g' host/libhackrf/53-hackrf.rules.in
%__subst 's/GROUP="plugdev"/ENV{ID_SOFTWARE_RADIO}="1"/g' host/libhackrf/53-hackrf.rules

%build
mkdir host/build
pushd host/build
%cmake_insource .. \
    -DINSTALL_UDEV_RULES=on \
    -DUDEV_RULES_PATH:PATH=%_udevrulesdir \
    -DUDEV_RULES_GROUP=plugdev

%make_build
popd

%install
pushd host/build
%makeinstall_std
popd

%files
%doc COPYING TRADEMARK Readme.md
%_bindir/hackrf_*
%_libdir/libhackrf.so.*
%_udevrulesdir/53-hackrf.rules

%files devel
%_includedir/libhackrf
%_pkgconfigdir/libhackrf.pc
%_libdir/libhackrf.so

%files doc
%doc doc/*

%changelog
* Thu Aug 26 2021 Anton Midyukov <antohami@altlinux.org> 2021.03.1-alt2
- disable building static libraries

* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 2021.03.1-alt1
- new version 2021.03.1

* Wed Apr 11 2018 Anton Midyukov <antohami@altlinux.org> 2018.01.1-alt1
- new version 2018.01.1

* Wed Oct 18 2017 Anton Midyukov <antohami@altlinux.org> 2015.07.2-alt1
- Initial build for ALT Sisyphus.
