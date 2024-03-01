%define _unpackaged_files_terminate_build 1

%def_with check

Name: pkcs11-provider
Version: 0.3
Release: alt1
Summary: A PKCS#11 provider for OpenSSL 3.0+
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/latchset/pkcs11-provider
Source: %name-%version.tar

# BUILD.md
BuildRequires: openssl-devel >= 3.0.7
BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: gcc
BuildRequires: autoconf-archive

%if_with check
BuildRequires: /dev/pts
BuildRequires: libnss-devel
BuildRequires: nss-utils
BuildRequires: softhsm
BuildRequires: opensc
BuildRequires: gnutls-utils
BuildRequires: openssl
BuildRequires: expect
%endif

%description
This is an Openssl 3.x provider to access Hardware or Software Tokens using the
PKCS#11 Cryptographic Token Interface.

This code targets version 3.1 of the interface but should be backwards
compatible to previous versions as well.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# don't package libtool's .la files
rm %buildroot%_libdir/ossl-modules/*.la

cp -a HOWTO.md %buildroot%_docdir/%name/

%check
# per upstream comment: do not run them in parrallel
make check || { cat tests/*.log; exit 1; }

%files
%doc %_docdir/%name
%_man7dir/provider-pkcs11.*
%_libdir/ossl-modules/pkcs11.so

%changelog
* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 0.3-alt1
- Initial build for Sisyphus.
