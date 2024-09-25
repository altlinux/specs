%define soversion 5

Name: json-c
Version: 0.18
Release: alt1

Summary: JSON implementation in C
License: MIT
Group: System/Libraries
Url: https://github.com/json-c/json-c/wiki

Source: %name-%version.tar
# git://github.com/json-c/json-c.git

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ctest

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

%package -n lib%name%soversion
Summary: JSON shared library
Group: System/Libraries
Conflicts: filesystem < 3

%description -n lib%name%soversion
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

This package contains shared JSON-C library

%package -n lib%name-devel
Summary: header files for libjson
Group: Development/C
Requires: lib%name%soversion = %version-%release

%description -n lib%name-devel
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

This package contains development part of JSON-C

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
  -DBUILD_STATIC_LIBS:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DCMAKE_C_FLAGS_RELEASE:STRING="" \
  -DDISABLE_BSYMBOLIC:BOOL=OFF \
  -DDISABLE_WERROR:BOOL=OFF \
  -DENABLE_RDRAND:BOOL=OFF \
  -DENABLE_THREADING:BOOL=ON

%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%ctest

%files -n lib%name%soversion
%_libdir/*.so.%{soversion}*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/cmake/%name

%changelog
* Wed Sep 25 2024 Alexey Shabalin <shaba@altlinux.org> 0.18-alt1
- Updated to 0.18
- Not relocate shared libraries to /lib.

* Thu Oct 19 2023 Alexey Shabalin <shaba@altlinux.org> 0.17-alt1
- Updated to 0.17 (Fixes: CVE-2021-32292).

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.15-alt1.1
- NMU: spec: adapted to new cmake macros.

* Wed Jan 20 2021 Alexey Shabalin <shaba@altlinux.org> 0.15-alt1
- Updated to 0.15.

* Sat Jul 04 2020 Alexey Shabalin <shaba@altlinux.org> 0.14-alt2
- Fixes: CVE-2020-12762

* Sat May 09 2020 Alexey Shabalin <shaba@altlinux.org> 0.14-alt1
- Updated to 0.14.

* Mon Dec 31 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.13.1-alt1
- Updated to 0.13.1.

* Fri Jan 26 2018 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt2
- move library /usr/lib -> /lib

* Fri May 05 2017 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Tue May 27 2014 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12
- rename to libjson-c

* Fri Dec 07 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10-alt1
- 0.10

* Tue Nov 30 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt2
- updated to svn rev.59

* Tue Aug  4 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- 0.9 released
