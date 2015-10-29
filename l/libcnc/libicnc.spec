%define oname icnc
Name: libcnc
Version: 1.0.100git
Release: alt1

Summary: Intel(R) Concurrent Collections for C++

License: see LICENSE file
Group: Development/C++
Url: https://icnc.github.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/icnc/icnc
Source: %name-%version.tar

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
* Thu Oct 29 2015 Vitaly Lipatov <lav@altlinux.ru> 1.0.100git-alt1
- initial build for ALT Linux Sisyphus
