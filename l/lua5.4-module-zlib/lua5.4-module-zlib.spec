Name: lua5.4-module-zlib
Version: 1.2
Release: alt1.git.15d4bc84b

Summary: Simple streaming interface to zlib for Lua
License: MIT
Url: https://github.com/brimworks/lua-zlib.git
Group: Development/Other

VCS: https://github.com/brimworks/lua-zlib.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: lua5.4
BuildRequires: liblua5.4-devel
BuildRequires: zlib-devel

%description
Simple streaming interface to zlib for Lua.
Consists of two functions: inflate and deflate.
Both functions return "stream functions" (takes a buffer of input and returns a buffer of output).

%prep
%setup

%build
%cmake \
  -DUSE_LUA=ON \
  -DUSE_LUA_VERSION=5.4 \
  -DLUA_INCLUDE_DIR=%_includedir \
  -DINSTALL_CMOD=%lua54_modulesdir
%cmake_build

%install
%cmake_install

%files
%doc README
%lua_modulesdir/*

%changelog
* Mon Apr 17 2023 Alexey Shabalin <shaba@altlinux.org> 1.2-alt1.git.15d4bc84b
- Initial build for ALT
