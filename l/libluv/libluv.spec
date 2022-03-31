%set_verify_elf_method unresolved=relaxed

Name: libluv
Version: 1.43.0
Release: alt1

Summary: libuv bindings for luajit

Group: Development/Tools
License: Apache-2.0
Url: https://github.com/luvit/luv

Source: %name-%version.tar

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

%build
%cmake \
    -DWITH_SHARED_LIBUV=ON \
    -DLUA_BUILD_TYPE=System \
    -DBUILD_MODULE=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DSHAREDLIBS_INSTALL_LIB_DIR=%_libdir

%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%name.pc


%changelog
* Thu Mar 31 2022 Vladimir Didenko <cow@altlinux.ru> 1.43.0-alt1
- new version

* Mon May 31 2021 Vladimir Didenko <cow@altlinux.ru> 1.41.0-alt2
- fix build with a new cmake macros

* Tue Apr 20 2021 Vladimir Didenko <cow@altlinux.ru> 1.41.0-alt1
- new version

* Mon Oct 19 2020 Vladimir Didenko <cow@altlinux.ru> 1.36.0-alt1
- new version

* Wed Sep 18 2019 Vladimir Didenko <cow@altlinux.ru> 1.30.1-alt1
- initial build for Sisyphus
