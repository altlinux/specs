Name:     mbelib
Version:  1.3.0
Release:  alt1%ubt

Summary:  P25 Phase 1 and ProVoice vocoder
License:  ISC
Group:    Engineering
Url:      https://github.com/szechyjs/mbelib

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar
Patch:    cmakelibdir.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-ubt
BuildRequires: cmake gcc-c++

%description
mbelib supports the 7200x4400 bit/s codec used in P25 Phase 1,
the 7100x4400 bit/s codec used in ProVoice and the "Half Rate"
3600x2250 bit/s vocoder used in various radio systems.

%package devel
Summary:  Development files for mbelib
Group:    Development/Other
Requires: %name = %version-%release

%description devel
Development files for mbelib

%prep
%setup
%patch -p1 -b .cmakelibdir

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md COPYRIGHT CHANGELOG
%_libdir/libmbe.so.*
%exclude %_libdir/libmbe.a

%files devel
%_includedir/mbelib.h
%_libdir/libmbe.so

%changelog
* Thu Jan 25 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1%ubt
- Initial build for Sisyphus
