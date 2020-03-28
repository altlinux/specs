%define target_lua_version 5.1

# Original package name basexx
%define oname basexx
%define oversion 0.4.1-1
%define rockspec basexx-0.4.1-1.rockspec
Name: lua%target_lua_version-module-%oname
Version: 0.4.1
Release: alt2
Summary: A base2, base16, base32, base64 and base85 library for Lua
License: MIT
Group: Development/Other
Url: https://github.com/aiq/basexx
BuildArch: noarch
Provides: luarocks%target_lua_version(%oname) = %EVR

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/aiq/basexx/archive/v0.4.1.tar.gz
Source1: https://luarocks.org/manifests/luarocks/basexx-0.4.1-1.rockspec

BuildRequires(pre): rpm-macros-lua >= 1.4
# Automatically added by buildreq on ...
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
A Lua library which provides base2(bitfield), base16(hex), base32(crockford/rfc), base64(rfc/url), base85(z85) decoding and encoding.

%prep
%setup -n %oname-%version

%install
%luarocks_make %SOURCE1

%files
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc LICENSE* README*
%exclude %luarocks_dbdir/manifest

%changelog
* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 0.4.1-alt2
- fix path to rockspec

* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 0.4.1-alt1
- Initial build

