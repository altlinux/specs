%global optflags_lto %optflags_lto -ffat-lto-objects
%def_enable check

Name: uchardet
Version: 0.0.8
Release: alt1

Summary: Universal charset detection
License: GPL-2.0-or-later and LGPL-2.1-or-later or MPL-1.1
Group: Development/Tools
Url: https://www.freedesktop.org/wiki/Software/uchardet/

Vcs: https://gitlab.freedesktop.org/uchardet/uchardet.git

#Source: https://www.freedesktop.org/software/uchardet/releases/uchardet-0.0.7.tar.xz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: lib%name = %EVR

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ %{?_enable_check:ctest}

%description
uchardet is a C language binding of the original C++ implementation of the
universal charset detection library by Mozilla. uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text.

%package -n lib%name
Summary: %name shared library
Group: System/Libraries

%description -n lib%name
This package contains shared library required by %name.

%package -n lib%name-devel
Summary: Development files for uchardet
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Header files and Libraries for the package uchardet.

%package -n lib%name-devel-static
Summary: Static library for uchardet
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
Static library to build statically linked applications that lib%name.

%prep
%setup
#%%patch -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%_libdir
%nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc COPYING AUTHORS

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name/

%files -n lib%name-devel-static
%_libdir/lib%name.a

%changelog
* Wed Jul 22 2026 Yuri N. Sedunov <aris@altlinux.org> 0.0.8-alt1
- 0.0.8
- switched build from tarball to upstream git, added Vcs tag
- enabled %%check

* Sat Sep 04 2021 Motsyo Gennadi <drool@altlinux.ru> 0.0.7-alt1
- 0.0.7
- fix LTO
- change home URL

* Mon Mar 15 2021 Leontiy Volodin <lvol@altlinux.org> 0.0.5-alt1.1
- recompile with -fPIE

* Wed Feb 06 2019 Vitaly Lipatov <lav@altlinux.ru> 0.0.5-alt1
- new version 0.0.5 (with rpmrb script)

* Wed Feb 06 2019 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt3
- cleanup spec, fix cmake build

* Thu Apr 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.1-alt2
- fixed packaging on 64bit arches other than x86_64

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.0.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue Oct 15 2013 Motsyo Gennadi <drool@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux from Fedora package
