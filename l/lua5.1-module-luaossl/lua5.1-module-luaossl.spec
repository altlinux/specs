%define _unpackaged_files_terminate_build 1

# Original package name luaossl
%define oname luaossl
%define rockspecrev 0
%define oversion %version-%rockspecrev
%define target_lua_version 5.1

Name: lua%target_lua_version-module-%oname
Version: 20220711
Release: alt1.%rockspecrev

Summary: Most comprehensive OpenSSL module in the Lua universe
License: MIT
Group: Development/Other
Url: http://25thandclement.com/~william/projects/luaossl.html
Vcs: https://github.com/wahern/luaossl

Provides: luarocks%target_lua_version(%oname) = %EVR

Source0: %name-%version.tar
Source1: https://luarocks.org/manifests/daurnimator/luaossl-20220711-0.rockspec

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

BuildRequires(pre): rpm-macros-lua >= 1.4
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel
BuildRequires: lua%target_lua_version-luarocks
BuildRequires: libssl-devel

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later.
It includes support for certificate and key management, key generation,
signature verification, and deep bindings to the distinguished name,
alternative name, and X.509v3 extension interfaces.

%prep
%setup

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%files
%lua_modulesdir/*
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc LICENSE* docs_from_rockstree/*
%exclude %luarocks_dbdir/manifest

%changelog
* Thu Aug 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 20220711-alt1.0
- 20190731-0 -> 20220711-0
- used sources from upstream branch instead of importing zip archive with ones
- reformatted spec file

* Sun Mar 29 2020 Alexey Shabalin <shaba@altlinux.org> 20190731-alt1
- Initial build.
