%define target_lua_version 5.1

# Original package name compat53
%define oname compat53
%define oversion 0.8-1
%define rockspec compat53-0.8-1.rockspec
%define lua_incdir %_includedir/lua-%target_lua_version

Name: lua%target_lua_version-module-%oname
Version: 0.8
Release: alt1
Summary: Compatibility module providing Lua-5.3-style APIs for Lua 5.2 and 5.1
License: MIT
Group: Development/Other
Url: https://github.com/keplerproject/lua-compat-5.3
Provides: luarocks%target_lua_version(%oname) = %EVR

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/keplerproject/lua-compat-5.3/archive/v%{version}/lua-compat-5.3-%version.tar.gz

BuildRequires(pre): rpm-macros-lua >= 1.4
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
This is a small module that aims to make it easier to write Lua
code in a Lua-5.3-style that runs on Lua 5.3, 5.2, and 5.1.
It does *not* make Lua 5.2 (or even 5.1) entirely compatible
with Lua 5.3, but it brings the API closer to that of Lua 5.3.

%prep
%setup -n lua-compat-5.3-%version

%install
%luarocks_make rockspecs/%rockspec

install -d -m 0755 %buildroot%lua_incdir/c-api
install -m 0644 -p -t %buildroot%lua_incdir/c-api c-api/*
install -m 0644 lprefix.h %buildroot%lua_incdir/lprefix.h

%files
%lua_modulesdir/*
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc LICENSE* README*
%exclude %luarocks_dbdir/manifest
%lua_incdir

%changelog
* Wed Dec 08 2021 Alexey Shabalin <shaba@altlinux.org> 0.8-alt1
- 0.8
- Package c-api (ALT #39056)

* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 0.7-alt2
- fix path to rockspec

* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 0.7-alt1
- Initial build
