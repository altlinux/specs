%define _unpackaged_files_terminate_build 1
%def_with check

%global luaver 5.3
%global oname lua-zlib
%global oversion 1.2-2

Name: lua%luaver-module-zlib
Version: 1.2
Release: alt1.git15d4bc8

Summary: Simple streaming interface to zlib for Lua
License: MIT
Group: Development/Other
Url: https://luarocks.org/modules/brimworks/lua-zlib
Vcs: https://github.com/brimworks/lua-zlib

Source0: %name-%version.tar
Source1: %oname-%oversion.rockspec

BuildRequires(pre): lua%luaver-luarocks
BuildRequires(pre): rpm-macros-lua
BuildRequires: liblua%luaver-devel
BuildRequires: zlib-devel

# Remove requires on its doc dir
%filter_from_requires %_defaultdocdir/lua%luaver-module-%oname*/d

Provides: luarocks%luaver(%oname) = %EVR

%description
Simple streaming interface to zlib for Lua.
Consists of two functions: inflate and deflate.
Both functions return "stream functions" (takes a buffer of input and
returns a buffer of output).

%prep
%setup

%install
%luarocks_make %SOURCE1

%check
%lua_path_add_buildroot
%lua test.lua

%files
%doc README
%lua_modulesdir/*
%luarocks_dbdir/%oname
%exclude %luarocks_dbdir/manifest

%changelog
* Thu May 11 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.2-alt1.git15d4bc8
- Initial build for Sisyphus

