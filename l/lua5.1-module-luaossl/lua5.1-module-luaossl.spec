%define target_lua_version 5.1

# Original package name luaossl
%define oname luaossl
%define oversion 20190731-0
%define rockspec luaossl-20190731-0.rockspec
Name: lua%target_lua_version-module-%oname
Version: 20190731
Release: alt1
Summary: Most comprehensive OpenSSL module in the Lua universe.
License: MIT
Group: Development/Other
Url: http://25thandclement.com/~william/projects/luaossl.html
Provides: luarocks%target_lua_version(%oname) = %EVR

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/wahern/luaossl/archive/rel-20190731.zip
Source1: https://luarocks.org/manifests/luarocks/luaossl-20190731-0.rockspec

BuildRequires(pre): rpm-macros-lua >= 1.4
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks
BuildRequires: libssl-devel

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later.
It includes support for certificate and key management, key generation,
signature verification, and deep bindings to the distinguished name,
alternative name, and X.509v3 extension interfaces.

%prep
%setup -n %oname-rel-%version

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
* Sun Mar 29 2020 Alexey Shabalin <shaba@altlinux.org> 20190731-alt1
- Initial build.
