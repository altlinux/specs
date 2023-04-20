Name: libgflags
Summary: A commandline flags library that allows for distributed flags
Version: 2.2.2
Release: alt2
Group: System/Libraries
Url: http://gflags.github.io/gflags/
License: BSD

Source: v%version.tar
Patch1: gflags-fix_pkgconfig.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake ctest

%description
The %name package contains a library that implements commandline flags
processing.  As such it's a replacement for getopt().  It has increased
flexibility, including built-in support for C++ types like string, and
the ability to define flags in the source file in which they're used.

%package devel
Summary: A commandline flags library that allows for distributed flags
Group: Development/C++
Requires: %name = %EVR

%description devel
The %name-devel package contains static and debug libraries and header
files for developing applications that use the %name package.

%prep
%setup -n gflags-%version
%patch1 -p1

mv BUILD BUILD.txt

%build
%cmake \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DINSTALL_HEADERS:BOOL=ON \
  -DBUILD_TESTING:BOOL=ON \
  -DREGISTER_BUILD_DIR:BOOL=OFF \
  -DREGISTER_INSTALL_PREFIX:BOOL=OFF
%cmake_build

%install
%cmake_install

# remove cmake files
# they are broken, due to that can't build blender with this library on aarch64/ppc64le arches
#rm -rf %buildroot%_libdir/cmake

%check
%ctest

%files
%doc AUTHORS.txt COPYING.txt
%_libdir/*.so.*
%_bindir/gflags_completions.sh

%files devel
%doc README.md BUILD.txt ChangeLog.txt
%_includedir/gflags
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/*

%changelog
* Thu Apr 20 2023 Alexey Shabalin <shaba@altlinux.org> 2.2.2-alt2
- package cmake files.
- fix pkgconfig file.
- enable tests.
- build nothreads and threads libs.

* Thu Aug 01 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.2-alt1
- Updated to upstream version 2.2.2.

* Tue Sep 26 2017 Fr. Br. George <george@altlinux.ru> 2.2.1-alt1
- Autobuild version bump to 2.2.1

* Tue Apr 05 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1.2-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue Apr 21 2015 Fr. Br. George <george@altlinux.ru> 2.1.2-alt1
- Autobuild version bump to 2.1.2
- Upstream has provided soname, drop patch

* Fri Aug 22 2014 Fr. Br. George <george@altlinux.ru> 2.1.1-alt1
- Autobuild version bump to 2.1.1
- Provide CMake devel instead of pkgconfig (upstream switched to cmake)
- Switch nothread build off (temporary?)

* Thu Apr 19 2012 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Autobuild version bump to 2.0

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Autobuild version bump to 1.6

* Wed Mar 30 2011 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Initial build from native spec
