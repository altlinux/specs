%ifarch %ix86
%set_verify_elf_method relaxed
%endif
%brp_strip_none

Summary: Rutoken PKCS#11 Library
Name: librtpkcs11ecp
Version: 1.4.5.0
Release: alt1
License: Proprietary
Url: https://www.rutoken.ru/support/download/pkcs/
Group: System/Configuration/Hardware
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64

BuildRequires: libpcsclite-devel

Provides: pcsc-lite-rtpkcs11ecp = %version-%release
Obsoletes: pcsc-lite-rtpkcs11ecp < %version-%release
Conflicts: pcsc-lite-rtpkcs11ecp < %version-%release

%description
Allow users to work with Rutoken ECP through PKCS#11 standard.

%prep
%setup

%install
mkdir -p %buildroot%_libdir %buildroot%_libdir/pkcs11
%ifarch %ix86
cp %name-i586.so %buildroot%_libdir/pkcs11/librtpkcs11ecp.so
%else
cp %name-x86_64.so %buildroot%_libdir/pkcs11/librtpkcs11ecp.so
%endif
ln -s pkcs11/librtpkcs11ecp.so %buildroot%_libdir/

%files
%doc LICENSE_ru.txt
%_libdir/*.so
%_libdir/pkcs11/*.so

%changelog
* Wed Dec 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.4.5.0-alt1
- New version (ALT #32921)
- Fix homepage

* Wed Apr 02 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt3
- Merge with pcsc-lite-rtpkcs11ecp.

* Mon Mar 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- initial
