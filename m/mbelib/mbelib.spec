Name:     mbelib
Version:  1.3.0
Release:  alt4

Summary:  P25 Phase 1 and ProVoice vocoder
License:  ISC
Group:    Engineering
Url:      https://github.com/szechyjs/mbelib

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar
Patch:    cmakelibdir.patch

BuildRequires(pre): rpm-macros-cmake
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

# remove unpackaged static libraries
rm %buildroot%_libdir/*.a

%files
%doc README.md COPYRIGHT CHANGELOG
%_libdir/libmbe.so.*

%files devel
%_includedir/mbelib.h
%_libdir/libmbe.so

%changelog
* Thu Aug 26 2021 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt4
- remove unpackaged static libraries

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt3.1
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2.1
- NMU: remove %ubt from release

* Wed Jun 27 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1%ubt.1
- Rebuilt for aarch64

* Thu Jan 25 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1%ubt
- Initial build for Sisyphus
