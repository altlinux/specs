%define _unpackaged_files_terminate_build 1

%global luaver 5.3
%global oname luaossl
%global oversion 20220711-0

Name: lua%luaver-module-%oname
Version: 20220711
Release: alt1

Summary: Most comprehensive OpenSSL module in the Lua universe.
License: MIT
Group: Development/Other
Url: http://25thandclement.com/~william/projects/luaossl.html
Vcs: https://github.com/wahern/luaossl

Source0: %name-%version.tar
Source1: %oname-%oversion.rockspec

BuildRequires(pre): lua%luaver-luarocks
BuildRequires(pre): rpm-macros-lua
BuildRequires: liblua%luaver-devel
BuildRequires: libssl-devel

# Remove self-requires
%filter_from_requires /lua%luaver(_openssl.*)/d

Provides: luarocks%luaver(%oname) = %EVR

%description
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later. I
dare say it's the most comprehensive OpenSSL binding in the Lua universe, and
one of the most comprehensive bindings of OpenSSL in any language, on par with
the best bindings in Python and Ruby.

It includes support for certificate and key management, key generation,
signature verification, and deep bindings to the distinguished name,
alternative name, and X.509v3 extension interfaces.

%prep
%setup

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%files
%doc LICENSE* examples
%lua_modulesdir/*
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%exclude %luarocks_dbdir/manifest

%changelog
* Sat Mar 18 2023 Alexandr Shashkin <dutyrok@altlinux.org> 20220711-alt1
- Initial build for Sisyphus


