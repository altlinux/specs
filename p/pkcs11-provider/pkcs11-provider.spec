%define _unpackaged_files_terminate_build 1
%define modulesdir %(pkg-config --variable=modulesdir --silence-errors libcrypto 2>/dev/null || echo unknown)

%def_with check

Name: pkcs11-provider
Version: 1.2.0
Release: alt3
Summary: A PKCS#11 provider for OpenSSL 3.0+
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/latchset/pkcs11-provider
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
# BUILD.md
BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: openssl-devel >= 3.0.7
BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: gcc

%if_with check
BuildRequires: /dev/pts
BuildRequires: libnss-devel
BuildRequires: nss-utils
BuildRequires: softhsm
BuildRequires: opensc
BuildRequires: openssl
BuildRequires: expect
BuildRequires: kryoptic
%endif

%description
This is an Openssl 3.x provider to access Hardware or Software Tokens using the
PKCS#11 Cryptographic Token Interface.

This code targets version 3.1 of the interface but should be backwards
compatible to previous versions as well.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_man7dir/provider-pkcs11.*
%modulesdir/pkcs11.so

%changelog
* Fri Jun 05 2026 Stanislav Levin <slev@altlinux.org> 1.2.0-alt3
- Fixed FTBFS (kryoptic 1.5.1).

* Wed May 13 2026 Stanislav Levin <slev@altlinux.org> 1.2.0-alt2
- Enabled testing against kryoptic.

* Fri Feb 20 2026 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Thu Oct 02 2025 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0 -> 1.1.0.

* Mon Feb 17 2025 Stanislav Levin <slev@altlinux.org> 1.0-alt1
- 0.6 -> 1.0.

* Mon Nov 25 2024 Stanislav Levin <slev@altlinux.org> 0.6-alt1
- 0.5 -> 0.6.

* Thu Jun 06 2024 Stanislav Levin <slev@altlinux.org> 0.5-alt1
- 0.4 -> 0.5.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.4-alt1
- 0.3 -> 0.4.

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 0.3-alt1
- Initial build for Sisyphus.
