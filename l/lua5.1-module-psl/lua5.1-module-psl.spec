%define target_lua_version 5.1

# Original package name psl
%define oname psl
%define oversion 0.3-0
%define rockspec psl-0.3-0.rockspec
Name: lua%target_lua_version-module-%oname
Version: 0.3
Release: alt1
Summary: Bindings to libpsl, a C library that handles the Public Suffix List (PSL)
License: MIT
Group: Development/Other
Url: https://github.com/daurnimator/lua-psl
Provides: luarocks%target_lua_version(%oname) = %EVR

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/daurnimator/lua-psl/archive/v0.3.zip
Source1: https://luarocks.org/manifests/luarocks/psl-0.3-0.rockspec

BuildRequires(pre): rpm-macros-lua >= 1.4
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks
BuildRequires: libpsl-devel

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
Bindings to libpsl, a C library that handles the Public Suffix List (PSL).

The PSL is a list of domains where there may be sub-domains outside of the administrator's control.
e.g. the administrator of '.com' does not manage 'github.com'.

This list has found use in many internet technologies including:

  - preventing cross-domain cookie leakage
  - allowance of issuing wildcard TLS certificates

More information can be found at https://publicsuffix.org/

%prep
%setup -n lua-%oname-%version

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%files
%lua_modulesdir/*
%luarocks_dbdir/%oname
%doc LICENSE* docs_from_rockstree/*
%exclude %luarocks_dbdir/manifest

%changelog
* Sun Mar 29 2020 Alexey Shabalin <shaba@altlinux.org> 0.3-alt1
- Initial build.
