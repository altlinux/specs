%ifarch %ix86
%set_verify_elf_method relaxed
%endif

%brp_strip_none

Name: libjcpkcs11
Version: 2.7.2
Release: alt4

Summary: Aladdin JaCarta PKCS#11 library
License: Proprietary
Group: System/Configuration/Hardware

Url: https://www.aladdin-rd.ru/support/downloads/c9b88e95-aaef-4448-9c86-745639439189
Source: %name-%version.tar
ExclusiveArch: x86_64 aarch64 armh e2k e2kv4 mipsel

BuildRequires: libpcsclite-devel

Requires: pcsc-lite-ccid

Provides: pcsc-lite-jcpkcs11 = %version-%release
Obsoletes: pcsc-lite-jcpkcs11 < %version-%release
Conflicts: pcsc-lite-jcpkcs11 < %version-%release

Summary(ru_RU.UTF-8): Библиотека PKCS#11 для Аладдин JaCarta

%description
A PKCS#11 library for Aladdin JaCarta tokens and cards.
The library is distributed in accordance with L-02210004 agreement
(04.02.2021).

%description -l ru_RU.UTF-8
Модуль PKCS#11 для работы с картами и токенами Аладдин JaCarta.
Модуль распространяется в соответствии с лицензионным договором
L-02210004 от 04.02.2021.

%prep
%setup

%install
%define sobasename libjcPKCS11-2.so
install -pDm644 %_arch/%sobasename.%version \
                %buildroot%_libdir/%sobasename.%version
mkdir -p %buildroot%_libdir/pkcs11
ln -s ../%sobasename.%version \
      %buildroot%_libdir/pkcs11/%sobasename

install -pDm644 jcpkcs11.module \
        %buildroot%_sysconfdir/pkcs11/modules/jcpkcs11.module

%files
%doc README.ALT EULA.pdf
%_libdir/*.so.%version
%_libdir/pkcs11/*.so
%config(noreplace) %_sysconfdir/pkcs11/modules/jcpkcs11.module

%changelog
* Mon Jul 19 2021 Paul Wolneykien <manowar@altlinux.org> 2.7.2-alt4
- Package unversioned %_libdir/pkcs11/*.so.

* Mon Jul 12 2021 Paul Wolneykien <manowar@altlinux.org> 2.7.2-alt3
- Fix: Use 'armh' for 'armhf'.

* Mon Jul 12 2021 Paul Wolneykien <manowar@altlinux.org> 2.7.2-alt2
- Added libjcPKCS11-2.so.2.7.2 for aarch64, armhf, e2k, e2kv4,
  and mipsel arches.

* Fri Jul 09 2021 Paul Wolneykien <manowar@altlinux.org> 2.7.2-alt1
- Initial version for Sisyphus.
