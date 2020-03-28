%define target_lua_version 5.1

# Original package name http
%define oname http
%define oversion 0.3-0
%define rockspec http-0.3-0.rockspec
Name: lua%target_lua_version-module-%oname
Version: 0.3
Release: alt1
Summary: HTTP library for Lua
License: MIT
Group: Development/Other
Url: https://github.com/daurnimator/lua-http
Provides: luarocks%target_lua_version(%oname) = %EVR
BuildArch: noarch

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/daurnimator/lua-http/archive/v0.3.zip
Source1: https://luarocks.org/manifests/luarocks/http-0.3-0.rockspec

Requires: luarocks%target_lua_version(compat53) >= 0.3 luarocks%target_lua_version(bit32) luarocks%target_lua_version(cqueues) >= 20161214 luarocks%target_lua_version(luaossl) >= 20161208 luarocks%target_lua_version(basexx) >= 0.2.0 luarocks%target_lua_version(lpeg) luarocks%target_lua_version(lpeg_patterns) >= 0.5 luarocks%target_lua_version(binaryheap) >= 0.3 luarocks%target_lua_version(fifo)

BuildRequires(pre): rpm-macros-lua >= 1.4
BuildRequires: luarocks%target_lua_version(compat53) >= 0.3 luarocks%target_lua_version(bit32) luarocks%target_lua_version(cqueues) >= 20161214 luarocks%target_lua_version(luaossl) >= 20161208 luarocks%target_lua_version(basexx) >= 0.2.0 luarocks%target_lua_version(lpeg) luarocks%target_lua_version(lpeg_patterns) >= 0.5 luarocks%target_lua_version(binaryheap) >= 0.3 luarocks%target_lua_version(fifo) 
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
lua-http is an performant, capable HTTP and WebSocket library for Lua.

%prep
%setup -n lua-%oname-%version

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%files
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc LICENSE* docs_from_rockstree/*
%exclude %luarocks_dbdir/manifest

%changelog
* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 0.3-alt1
- Initial build
