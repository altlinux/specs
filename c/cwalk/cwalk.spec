%define _unpackaged_files_terminate_build 1
%define abiversion 1

Name: cwalk
Version: 1.2.9
Release: alt1
Summary: Path library for C/C++. Cross-Platform for Linux.
License: MIT
Group: Development/C
Url: https://github.com/likle/cwalk

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: /proc

%description
This is a lighweight C path manipulation library.
It is currently compiled and tested under Linux, FreeBSD,
Windows and MacOS.
It supports UNIX and Windows path styles on all platforms.

%package -n lib%{name}_%{abiversion}
Summary: hared library for %name
Group: Development/C

%description -n lib%{name}_%{abiversion}
libs files for %name

%package -n %name-devel
Summary: Development package for %name
Group: Development/C

%description -n %name-devel
Files for development with %name.

%prep
%setup
%autopatch -p1
sed -i 's/^\([[:space:]]*add_library[[:space:]]*(cwalk\)\([[:space:]]\)/\1 SHARED\2/' CMakeLists.txt
sed -i '/^[[:space:]]*if[[:space:]]*(BUILD_SHARED_LIBS)/i \
set_target_properties(cwalk PROPERTIES\
\n    VERSION %version\
\n    SOVERSION %abiversion\
\n)' CMakeLists.txt
sed -i 's|lib/pkgconfig/|%_pkgconfigdir|' CMakeLists.txt

%build
export CFLAGS="%optflags"
%cmake \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DLIB_INSTALL_DIR=%_libdir \
    -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmakeinstall_std

%files -n %name-devel
%doc *.md
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/*.h
%_libdir/cmake/%name/

%files -n lib%{name}_%{abiversion}
%_libdir/*.so.%abiversion
%_libdir/*.so.%abiversion.*

%changelog
* Tue Sep 30 2025 Pavel Shilov <zerospirit@altlinux.org> 1.2.9-alt1
- Initial build for Sisyphus.