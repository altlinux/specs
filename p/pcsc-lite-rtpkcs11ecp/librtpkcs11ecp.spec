%set_verify_elf_method relaxed
%brp_strip_none /*

Summary: Rutoken PKCS11 library
Name: pcsc-lite-rtpkcs11ecp
Version: 0.1
Release: alt2
License: Proprietary
Url: http://www.rutoken.ru/hotline/download/nix/
Group: Development/Other
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64

BuildRequires: libpcsclite-devel

Provides: librtpkcs11ecp = %version-%release
Obsoletes: librtpkcs11ecp < %version-%release

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%_libdir/pkcs11/
%ifarch %ix86
cp librtpkcs11ecp-i586.so %buildroot%_libdir/pkcs11/librtpkcs11ecp.so
%else
cp librtpkcs11ecp-x86_64.so %buildroot%_libdir/pkcs11/librtpkcs11ecp.so
%endif

%files
%doc LICENSE_ru.txt
%_libdir/pkcs11/*.so

%changelog
* Tue Mar 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2
- move lib to %%_libdir/pkcs11/

* Mon Mar 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- initial
