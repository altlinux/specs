%define _unpackaged_files_terminate_build 1
%def_with check

%global luaver 5.3

Name: lua%luaver-module-zlib
Version: 1.2
Release: alt2.git15d4bc8

Summary: Simple streaming interface to zlib for Lua
License: MIT
Group: Development/Other
Url: https://luarocks.org/modules/brimworks/lua-zlib
Vcs: https://github.com/brimworks/lua-zlib

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-lua
BuildRequires: cmake
BuildRequires: lua%luaver
BuildRequires: liblua%luaver-devel
BuildRequires: zlib-devel

%description
Simple streaming interface to zlib for Lua.
Consists of two functions: inflate and deflate.
Both functions return "stream functions" (takes a buffer of input and
returns a buffer of output).

%prep
%setup

%build
%cmake \
  -DUSE_LUA=ON \
  -DUSE_LUA_VERSION=%luaver \
  -DLUA_INCLUDE_DIR=%_includedir \
  -DINSTALL_CMOD=%lua_modulesdir
%cmake_build

%install
%cmake_install

%check
%lua_path_add_buildroot
%lua test.lua

%files
%doc README
%lua_modulesdir/*

%changelog
* Fri Aug 04 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.2-alt2.git15d4bc8
- fixed adding lua-zlib files to dependent packages' buildroot

* Thu May 11 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.2-alt1.git15d4bc8
- Initial build for Sisyphus

