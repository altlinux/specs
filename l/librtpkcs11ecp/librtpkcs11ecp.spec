%set_verify_elf_method relaxed
%brp_strip_none /*

Summary: Rutoken PKCS11 library
Name: librtpkcs11ecp
Version: 0.1
Release: alt1
License: Proprietary
Url: http://www.rutoken.ru/hotline/download/nix/
Group: Development/Other
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%_libdir/
%ifarch %ix86
cp %name-i586.so %buildroot%_libdir/%name.so
%else
cp %name-x86_64.so %buildroot%_libdir/%name.so
%endif

%files
%doc LICENSE_ru.txt
%_libdir/*.so

%changelog
* Mon Mar 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- initial
