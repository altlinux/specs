Name: openssl-config
Version: 3.2.0
Release: alt1
Summary: OpenSSL configuration
License: OpenSSL
Group: System/Configuration/Other
BuildArch: noarch

Conflicts: libcrypto1.1 < 1.1.1w-alt3
Conflicts: libcrypto3 < 3.1.7-alt3

Source0: openssl.cnf

%description
This package contains openssl.cnf configuration file for OpenSSL.

%install
mkdir -p %buildroot/etc/openssl
install -m644 %SOURCE0 %buildroot/etc/openssl/

%files
%config(noreplace) /etc/openssl/openssl.cnf

%changelog
* Wed Jan 15 2025 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.2.0-alt1
- Update the base config from the upstream commit openssl-3.2.0-beta1~60.

* Thu Dec 26 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.1-alt1
- Initial build of ALT OpenSSL config based on openssl.cnf from the upstream
  commit openssl-3.1.1~21.
