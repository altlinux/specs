%brp_strip_none

Summary: Jacarta PKCS#11 Library
Name: libjcpkcs11
Version: 2.1.3.2043
Release: alt1
License: Proprietary
URL: https://www.aladdin-rd.ru/
Group: System/Configuration/Hardware
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64

Requires: pcsc-lite-ccid

%description
Jacarta PKCS#11 library.

%prep
%setup

%install
mkdir -p %buildroot%_libdir %buildroot%_libdir/pkcs11

%ifarch %ix86
cp %name-2-i386.so %buildroot%_libdir/pkcs11/%name-2.so
%else
cp %name-2-x86_64.so %buildroot%_libdir/pkcs11/%name-2.so
%endif
ln -s pkcs11/libjcpkcs11-2.so %buildroot%_libdir/

%files
%_libdir/*.so
%_libdir/pkcs11/*.so

%changelog
* Wed Nov 7 2018 Paul Wolneykien <manowar@altlinux.org> 2.1.3.2043-alt1
- Initial build.
