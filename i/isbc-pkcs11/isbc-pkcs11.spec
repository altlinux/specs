%ifarch %ix86
%set_verify_elf_method relaxed
%endif
%brp_strip_none

Summary: ESMART PKCS#11 library
Name: isbc-pkcs11
Version: 4.4
Release: alt2
License: Proprietary
Url: https://esmart.ru/download/
Group: System/Configuration/Hardware
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64 armh aarch64 e2k

Requires: pcsc-lite-ccid

BuildRequires: libpcsclite-devel

%ifarch aarch64
BuildRequires: patchelf
%endif

%description
Allow users to work with ESMART through PKCS#11 standard.

%package utils
Summary: ESMART PKCS#11 utils
License: Proprietary
Url: https://esmart.ru/download/
Group: System/Configuration/Hardware
Requires: %name = %version-%release

%description utils
Command-line utility for ESMART PKCS#11 interface.

%prep
%setup
%ifarch aarch64
patchelf --set-interpreter /%_lib/ld-linux-aarch64.so.1 \
		 esmart/armv8/utils/PKIClientCli
%endif

%install
%ifarch %ix86
%define arch_dir x86
%endif
%ifarch x86_64
%define arch_dir x64
%endif
%ifarch armh
%define arch_dir armv7
%endif
%ifarch aarch64
%define arch_dir armv8
%endif
%ifarch e2k
%define arch_dir e2k
%endif

for f in `find esmart/%arch_dir/Release/ -name '*.so'`; do \
	install -D -m0644 $f %buildroot%_libdir/pkcs11/${f##*/}; \
	ln -s pkcs11/${f##*/} %buildroot%_libdir/${f##*/}; \
done

install -D -m0644 isbc.module \
        %buildroot%_sysconfdir/pkcs11/modules/isbc.module

install -D -m0755 esmart/%arch_dir/utils/PKIClientCli \
		%buildroot%_bindir/PKIClientCli

%files
%doc esmart/%arch_dir/*.tmpl
%_libdir/*.so
%_libdir/pkcs11/*.so
%config(noreplace) %_sysconfdir/pkcs11/modules/*.module

%files utils
%_bindir/*

%changelog
* Fri Aug 31 2018 Paul Wolneykien <manowar@altlinux.org> 4.4-alt2
- Patch esmart/armv8/utils/PKIClientCli: set interpreter path:
  /%_lib/ld-linux-aarch64.so.1.

* Fri Aug 31 2018 Paul Wolneykien <manowar@altlinux.org> 4.4-alt1
- ESMART Token 4.4 PKCS11 Linux 20180606.
