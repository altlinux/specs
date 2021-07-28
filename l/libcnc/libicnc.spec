%define oname icnc
Name: libcnc
Version: 1.0.100git
Release: alt2

Summary: Intel(R) Concurrent Collections for C++

License: see LICENSE file
Group: Development/C++
Url: https://icnc.github.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/icnc/icnc
Source: %name-%version.tar
Patch2000: %name-e2k.patch

BuildRequires: gcc-c++ cmake doxygen libtbb-devel

%description
CnC makes it easy to write C++ programs which take full advantage of the available parallelism.
Through its portabilty and composability (with itself and other tools) it provides future-proof scalability.

%package devel
Group: Development/C++
Summary: Development files for %name
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup
%ifarch %e2k
%patch2000 -p1
%endif

%build
%cmake -DLIB=%_libdir
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/cnc/
%_libdir/*.so
%_datadir/icnc/

%changelog
* Wed Jul 28 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.0.100git-alt2
- added patch for Elbrus

* Thu Oct 29 2015 Vitaly Lipatov <lav@altlinux.ru> 1.0.100git-alt1
- initial build for ALT Linux Sisyphus
