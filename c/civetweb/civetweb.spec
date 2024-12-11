%define soname 1
%def_enable ssl
%def_enable zlib
%def_disable lua
%def_disable duktape

Name: civetweb
Version: 1.16
Release: alt1

Summary: Embedded C/C++ web server
License: MIT
Group: Networking/WWW

Url: https://github.com/civetweb/civetweb
Source: %name-%version.tar

Patch0: %name-%version-%release.patch

BuildRequires(pre): cmake make gcc-c++
BuildRequires: /proc /dev/pts

%if_enabled zlib
BuildRequires: zlib-devel
%endif
%if_enabled duktape
BuildRequires: libduktape-devel
%endif
%if_enabled lua
BuildRequires: liblua5.3-devel
%endif

%description
Civetweb is an easy to use, powerful, C (C/C++) embeddable web server
with optional CGI, SSL and Lua support.

CivetWeb can be used by developers as a library, to add web server
functionality to an existing application. It can also be used by end
users as a stand-alone web server running on a Windows or Linux PC.
It is available as single executable, no installation is required.

%package devel
Summary: Civetweb C d C++ header files
Group: Development/Other
Requires: lib%name%soname = %EVR

%description devel
Civetweb associated header files

%package -n lib%name%soname
Summary: Civetweb shared library
Group: Development/Other

%description -n lib%name%soname
Civetweb is an easy to use, powerful, C (C/C++) embeddable web server
with optional CGI, SSL and Lua support.

CivetWeb can be used by developers as a library, to add web server
functionality to an existing application. It can also be used by end
users as a stand-alone web server running on a Windows or Linux PC.
It is available as single executable, no installation is required.

This package contains shared libs for Civetweb server.

%prep
%setup
%patch0 -p1

%build
%cmake . \
    -G "Unix Makefiles" \
    -DCMAKE_BUILD_TYPE=release \
    -DBUILD_CONFIG=rpmbuild \
    -DCIVETWEB_ENABLE_CXX:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCIVETWEB_BUILD_TESTING:BOOL=OFF \
%if_enabled lua
    -DCIVETWEB_ENABLE_LUA:BOOL=ON \
    -DCIVETWEB_ENABLE_LUA_SHARED:BOOL=ON \
%endif
%if_enabled ssl
    -DCIVETWEB_ENABLE_SSL:BOOL=ON \
%endif
%if_enabled zlib
    -DCIVETWEB_ENABLE_ZLIB:BOOL=ON \
%endif
%if_enabled duktape
    -DCIVETWEB_ENABLE_DUKTAPE:BOOL=ON \
%endif
%nil

%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_docdir/civetweb

%files
%_bindir/civetweb
%doc README.md RELEASE_NOTES.md SECURITY.md

%files -n lib%name%soname
%_libdir/libcivetweb.so.%soname.*
%_libdir/libcivetweb-cpp.so.%soname.*

%files -n %name-devel
%_includedir/*.h
%_libdir/cmake/civetweb
%_libdir/libcivetweb.so
%_libdir/libcivetweb-cpp.so
%_pkgconfigdir/*.pc

%changelog
* Sun Jul 02 2023 Andrey Kuznetcov <morgonf@altlinux.org> 1.16-alt1
- Initial build for Sisyphus (based on fedora spec)
  + patch CmakeLists.txt to add project version explicitly
