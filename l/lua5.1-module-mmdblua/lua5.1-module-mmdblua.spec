%define target_lua_version 5.1

# Original package name mmdblua
%define oname mmdblua
%define oversion 0.2-0
%define rockspec mmdblua-0.2-0.rockspec
Name: lua%target_lua_version-module-%oname
Version: 0.2
Release: alt1
Summary: Library for reading MaxMind's Geolocation database format.
License: MIT
Group: Development/Other
Url: https://github.com/daurnimator/mmdblua
Provides: luarocks%target_lua_version(%oname) = %EVR
Provides: luarocks%target_lua_version(mmdb) = %EVR
BuildArch: noarch

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/daurnimator/mmdblua/archive/v0.2.zip
Source1: https://luarocks.org/manifests/luarocks/mmdblua-0.2-0.rockspec

Requires: luarocks%target_lua_version(compat53) >= 0.3

BuildRequires(pre): rpm-macros-lua >= 1.4
BuildRequires: luarocks%target_lua_version(compat53) >= 0.3
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
A Lua library for reading MaxMind's Geolocation database format.

%prep
%setup -n %oname-%version

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%files
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc docs_from_rockstree/*
%exclude %luarocks_dbdir/manifest

%changelog
* Sun Mar 29 2020 Alexey Shabalin <shaba@altlinux.org> 0.2-alt1
- Initial build.

