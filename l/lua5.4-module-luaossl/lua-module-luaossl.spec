%define _unpackaged_files_terminate_build 1

# Original package name luaossl
%define oname luaossl
%define rockspecrev 0
%define oversion %version-%rockspecrev
%global luaver 5.4

Name: lua%luaver-module-%oname
Version: 20250929
Release: alt2.%rockspecrev

Summary: Most comprehensive OpenSSL module in the Lua universe
License: MIT
Group: Development/Other
Url: http://25thandclement.com/~william/projects/luaossl.html
Vcs: https://github.com/wahern/luaossl

Provides: luarocks%luaver(%oname) = %EVR

Source0: %name-%version.tar
Source1: https://luarocks.org/manifests/daurnimator/luaossl-20250929-0.rockspec

BuildRequires(pre): rpm-macros-lua >= 1.4
# Automatically added by buildreq on ...
BuildRequires: liblua%luaver-devel
BuildRequires: lua%luaver-luarocks
BuildRequires: libssl-devel

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later.
It includes support for certificate and key management, key generation,
signature verification, and deep bindings to the distinguished name,
alternative name, and X.509v3 extension interfaces.

%prep
%setup

%build
luarocks-%luaver make --verbose --local --deps-mode all --pack-binary-rock \
	%SOURCE1

%install
luarocks-%luaver install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock
%luarocks_move_docs doc

%files
%luarocks_dbdir/%oname
%doc LICENSE* docs_from_rockstree/*
%lua_modulesdir/_openssl.so
%lua_modulesdir_noarch/openssl*

%changelog
* Sat Jun 13 2026 Alexandr Shashkin <dutyrok@altlinux.org> 20250929-alt2.0
- Fixed FTBFS: added patch to work around broken PEM_write_bio_OCSP_RESPONSE
  macro in OpenSSL 3.5.

* Thu Sep 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 20250929-alt1.0
- Updated to 20250929-0.

* Thu Aug 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 20220711-alt1.0
- 20190731-0 -> 20220711-0.

* Sun Mar 29 2020 Alexey Shabalin <shaba@altlinux.org> 20190731-alt1
- Initial build.
