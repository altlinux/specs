Summary: Rutoken PKCS#11 engine for OpenSSL
Name: openssl-engines-rutoken
Version: 1.0
Release: alt1
License: Proprietary
URL: https://www.rutoken.ru/solutions/freeware/openssl/
#Download: https://download.rutoken.ru/Rutoken/Support_OpenSSL/
Group: System/Libraries
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64

Requires: openssl-engines

%description
Rutoken PKCS#11 engine for OpenSSL

%prep
%setup

%install
%ifarch %ix86
install -Dm 0644 pkcs11_gost-i586.so %buildroot%_libdir/openssl/engines/libpkcs11_gost.so
%else
install -Dm 0644 pkcs11_gost-x86_64.so %buildroot%_libdir/openssl/engines/libpkcs11_gost.so
%endif

%files
%doc license.ru.html
%_libdir/openssl/engines/libpkcs11_gost.so

%changelog
* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
