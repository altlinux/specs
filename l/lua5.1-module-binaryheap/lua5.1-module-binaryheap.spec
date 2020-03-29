%define target_lua_version 5.1

# Original package name binaryheap
%define oname binaryheap
%define oversion 0.4-1
%define rockspec binaryheap-0.4-1.rockspec
Name: lua%target_lua_version-module-%oname
Version: 0.4
Release: alt1
Summary: Binary heap implementation in pure Lua
License: MIT/X11
Group: Development/Other
Url: https://github.com/Tieske/binaryheap.lua
Provides: luarocks%target_lua_version(%oname) = %EVR
BuildArch: noarch

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/Tieske/binaryheap.lua/archive/version_0v4.tar.gz
Source1: https://luarocks.org/manifests/luarocks/binaryheap-0.4-1.rockspec

BuildRequires(pre): rpm-macros-lua >= 1.4
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
Binary heaps are an efficient sorting algorithm. This module
implements a plain binary heap (without reverse lookup) and a
'unique' binary heap (with unique payloads and reverse lookup).

%prep
%setup -n binaryheap.lua-version_0v4

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%files
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc docs_from_rockstree/*
%exclude %luarocks_dbdir/manifest

%changelog
* Sun Mar 29 2020 Alexey Shabalin <shaba@altlinux.org> 0.4-alt1
- Initial build.


