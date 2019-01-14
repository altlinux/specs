%brp_strip_none

Summary: JaCarta PKCS #11 library
Name: jcPKCS11-2
Version: 2.4.0.2946
Release: alt1
License: Proprietary
URL: https://www.aladdin-rd.ru/
ExclusiveArch: %ix86 x86_64
Group: System/Configuration/Hardware
Source0: %name-%version.tar

BuildRequires: libpcsclite
Requires: pcsc-lite-ccid

%description
JaCarta PKCS#11 library

%prep
%setup -q

%install

mkdir -p %buildroot%_libdir/pkcs11

%ifarch %ix86
cp -t %buildroot%_libdir/pkcs11 i386/*
%else
cp -t %buildroot%_libdir/pkcs11 x86_64/*
%endif

%files
%_libdir/pkcs11/jcverify
%_libdir/pkcs11/*.so.*
%_libdir/pkcs11/*.so
%_libdir/pkcs11/*.txt

%changelog
* Mon Jan 14 2019 Leonid Krashenko <krash@altlinux.org> 2.4.0.2946-alt1
- Initial build.
