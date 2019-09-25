Name: libluv
Version: 1.30.1
Release: alt1

Summary: libuv bindings for luajit

Group: Development/Tools
License: Apache License 2.0
Url: https://github.com/luvit/luv

Source: %name-%version.tar
Patch: %name-1.30.1-alt-build-quickfix.patch

BuildRequires(pre): rpm-macros-cmake cmake

BuildRequires: libuv-devel
BuildRequires: libluajit-devel

%description
This library makes libuv available to lua scripts. It was made for the
luvit project but should usable from nearly any lua project.

%package devel
Summary: Devel package for libluv
Group: Development/Other
Requires: %name = %version-%release

%description devel
libluv header and build tools.

%prep
%setup
%patch -p2

%build
%cmake \
    -DWITH_SHARED_LIBUV=ON \
    -DLUA_BUILD_TYPE=System \
    -DBUILD_MODULE=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DINSTALL_LIB_DIR=%_libdir

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%name.pc


%changelog
* Wed Sep 18 2019 Vladimir Didenko <cow@altlinux.ru> 1.30.1-alt1
- initial build for Sisyphus
