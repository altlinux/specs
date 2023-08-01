%define _unpackaged_files_terminate_build 1

%set_verify_elf_method skip
%set_debuginfo_skiplist /*
%set_fixup_skiplist /*

Summary: Rutoken PKCS#11 engine for OpenSSL
Name: openssl-engines-rutoken
Version: 3.1.1
Release: alt1
Epoch: 1
Vendor: Aktiv Co.
License: Distributable
URL: https://www.rutoken.ru/solutions/freeware/openssl/
#Download: https://download.rutoken.ru/Rutoken/Support_OpenSSL/3.1.1/rtengine-3.1.1.zip

Group: System/Libraries
Source0: %name-%version.tar

ExclusiveArch: %ix86 x86_64 e2k mipsel aarch64 armh

BuildRequires: libcrypto3

Requires: libcrypto3
Requires: openssl-engines
Requires: librtpkcs11ecp

%description
Allow users to work with Rutoken ECP through OpenSSL.

%prep
%setup

%install
mkdir -p -m755 %buildroot%_libdir
%ifarch %ix86
cp -aRf linux_glibc-x86/lib/* %buildroot%_libdir/
%else
cp -aRf linux_glibc-%_arch/lib/* %buildroot%_libdir/
%endif

%files
%doc license.ru.html version.txt
%_libdir/librtengine.so*

%changelog
* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 1:3.1.1-alt1
- New version compatible with OpenSSL 3.x.

* Mon Feb 14 2022 Andrey Cherepanov <cas@altlinux.org> 1:1.4.2-alt2
- FTBFS: add libcrypto1.1 to fix library autorequirements.

* Fri Dec 03 2021 Andrey Cherepanov <cas@altlinux.org> 1:1.4.2-alt1
- Use upstream version.

* Tue Nov 30 2021 Leonid Krivoshein <klark@altlinux.org> 210824-alt1.1
- Updated to version 1.4.2 from Aktiv Co. web site.
- Added support for e2k, e2kv4, mipsel, armh and aarch64.

* Mon Sep 16 2019 Andrey Cherepanov <cas@altlinux.org> 190628-alt1.88d4ce
- New version from sdk-280619-88d4ce.zip.

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
