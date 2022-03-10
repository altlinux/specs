%define _unpackaged_files_terminate_build 1
%set_verify_elf_method relaxed
%brp_strip_none

Summary: ESMART PKCS#11 library
Name: isbc-pkcs11
Version: 4.9
Release: alt2
License: Proprietary
Url: https://esmart.ru/download/
Group: System/Configuration/Hardware
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64 armh aarch64 e2k

Requires: pcsc-lite-ccid

BuildRequires: libpcsclite-devel
BuildRequires: patchelf

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

%define arch_dir %_arch
%ifarch %ix86
%define arch_dir i586
%endif

%build
%ifarch aarch64
patchelf --set-interpreter /%_lib/ld-linux-aarch64.so.1 \
		 files/aarch64/utils/PKIClientCli
%endif

# Patching against "Inconsistency detected by ld.so:
# dl-version.c: 204: _dl_check_map_versions: Assertion
# `needed != NULL' failed!":
patchelf --add-needed libpthread.so.0 \
         files/%{arch_dir}/Release/libisbc_pkcs11_main.so
patchelf --add-needed libpthread.so.0 \
         files/%{arch_dir}/Release/libEsmartToken_Javalib.so

%install
for f in `find files/%{arch_dir}/Release/ -name '*.so'`; do \
	install -D -m0644 $f %buildroot%_libdir/pkcs11/${f##*/}; \
	ln -s pkcs11/${f##*/} %buildroot%_libdir/${f##*/}; \
done

install -D -m0644 isbc.module \
        %buildroot%_sysconfdir/pkcs11/modules/isbc.module

install -D -m0755 files/%{arch_dir}/utils/PKIClientCli \
		%buildroot%_bindir/PKIClientCli

%files
%doc files/%{arch_dir}/*.tmpl README.ALT
%_libdir/*.so
%_libdir/pkcs11/*.so
%config(noreplace) %_sysconfdir/pkcs11/modules/*.module

%files utils
%_bindir/*

%changelog
* Thu Mar 10 2022 Paul Wolneykien <manowar@altlinux.org> 4.9-alt2
- Fixed patchelf.
- Patching libraries against missing libpthread.so.0 as needed.

* Tue Feb 15 2022 Paul Wolneykien <manowar@altlinux.org> 4.9-alt1
- Updated to v4.9.

* Fri Aug 31 2018 Paul Wolneykien <manowar@altlinux.org> 4.4-alt2
- Patch esmart/armv8/utils/PKIClientCli: set interpreter path:
  /%_lib/ld-linux-aarch64.so.1.

* Fri Aug 31 2018 Paul Wolneykien <manowar@altlinux.org> 4.4-alt1
- ESMART Token 4.4 PKCS11 Linux 20180606.
