%define target_lua_version 5.1

# Original package name lpeg_patterns
%define oname lpeg_patterns
%define oversion 0.5-0
%define rockspec lpeg_patterns-0.5-0.rockspec
Name: lua%target_lua_version-module-%oname
Version: 0.5
Release: alt1
Summary: a collection of LPEG patterns
License: MIT
Group: Development/Other
Url: https://github.com/daurnimator/lpeg_patterns
Provides: luarocks%target_lua_version(%oname) = %EVR
BuildArch: noarch

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/daurnimator/lpeg_patterns/archive/v0.5.zip
Source1: https://luarocks.org/manifests/luarocks/lpeg_patterns-0.5-0.rockspec

Requires: luarocks%target_lua_version(lpeg)

BuildRequires(pre): rpm-macros-lua >= 1.4
BuildRequires: luarocks%target_lua_version(lpeg)
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
%summary.

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
* Sun Mar 29 2020 Alexey Shabalin <shaba@altlinux.org> 0.5-alt1
- Initial build.

