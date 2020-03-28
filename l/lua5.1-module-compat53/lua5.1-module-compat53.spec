%define target_lua_version 5.1

# Original package name compat53
%define oname compat53
%define oversion 0.7-1
%define rockspec /home/shaba/RPM/SOURCES/compat53-0.7-1.rockspec
Name: lua%target_lua_version-module-%oname
Version: 0.7
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

Source: https://github.com/keplerproject/lua-compat-5.3/archive/v0.7.zip
Source1: https://luarocks.org/manifests/luarocks//home/shaba/RPM/SOURCES/compat53-0.7-1.rockspec


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
%luarocks_make %SOURCE1

%files
%lua_modulesdir/*
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc LICENSE* README*
%exclude %luarocks_dbdir/manifest

%changelog
* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 0.7-alt1
- Initial build
