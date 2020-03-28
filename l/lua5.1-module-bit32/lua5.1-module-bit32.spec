%define target_lua_version 5.1

# Original package name bit32
%define oname bit32
%define oversion 5.3.0-1
%define rockspec bit32-5.3.0-1.rockspec
Name: lua%target_lua_version-module-%oname
Version: 5.3.0
Release: alt1
Summary: Lua 5.2 bit manipulation library
License: MIT/X11
Group: Development/Other
Url: http://www.lua.org/manual/5.2/manual.html#6.7
Provides: luarocks%target_lua_version(%oname) = %EVR

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/keplerproject/lua-compat-5.2/archive/bitlib-%version.tar.gz
Source1: https://luarocks.org/manifests/luarocks/bit32-%oversion.rockspec

BuildRequires(pre): rpm-macros-lua >= 1.4
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
bit32 is the native Lua 5.2 bit manipulation library, in the version
from Lua 5.3; it is compatible with Lua 5.1, 5.2 and 5.3.

%prep
%setup -n lua-compat-5.2-bitlib-%version

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc


%files
%lua_modulesdir/*
%luarocks_dbdir/%oname
%doc docs_from_rockstree/*
%exclude %luarocks_dbdir/manifest

%changelog
* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 5.3.0-alt1
- Initial build

