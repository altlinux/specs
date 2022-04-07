%define _unpackaged_files_terminate_build 1

#%ifarch %ix86
%set_verify_elf_method relaxed
#%endif

%brp_strip_none

Name: libjcpkcs11
Version: 2.7.4
Release: alt6

Summary: Aladdin JaCarta PKCS#11 library
License: Proprietary
Group: System/Configuration/Hardware

Url: https://www.aladdin-rd.ru/support/downloads/c9b88e95-aaef-4448-9c86-745639439189
Source: %name-%version.tar
ExclusiveArch: i586 x86_64 aarch64 armh e2k e2kv4 mipsel

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
%makeinstall ARCH=%_arch

%files
%dir %_datadir/doc/%name-%version
%_datadir/doc/%name-%version/README.ALT
%_datadir/doc/%name-%version/EULA.pdf
%_libdir/*.so.%version
%_libdir/*.so
%_libdir/pkcs11/*.so
%_bindir/jcverify
%dir %_datadir/%name
%_datadir/%name/jcverify.txt
%_datadir/%name/jckt2.txt
%config(noreplace) %_sysconfdir/pkcs11/modules/jcpkcs11.module

%changelog
* Thu Apr 07 2022 Paul Wolneykien <manowar@altlinux.org> 2.7.4-alt6
- Make symlinks to all installed libraries from the pkcs11/ subdir
  (closes: 42342).

* Thu Feb 03 2022 Paul Wolneykien <manowar@altlinux.org> 2.7.4-alt5
- Set verify ELF method to 'relaxed' for all arches.

* Wed Jan 19 2022 Paul Wolneykien <manowar@altlinux.org> 2.7.4-alt4
- Fix: Package %_datadir/doc/%name-%version and %_datadir/%name.

* Wed Jan 19 2022 Paul Wolneykien <manowar@altlinux.org> 2.7.4-alt3
- Fix: Pass ARCH to make install.

* Wed Jan 19 2022 Paul Wolneykien <manowar@altlinux.org> 2.7.4-alt2
- Included other files, provided by the vendor.

* Thu Nov 18 2021 Paul Wolneykien <manowar@altlinux.org> 2.7.4-alt1
- Updated to v2.7.4.534 + i586.

* Mon Jul 19 2021 Paul Wolneykien <manowar@altlinux.org> 2.7.2-alt4
- Package unversioned %_libdir/pkcs11/*.so.

* Mon Jul 12 2021 Paul Wolneykien <manowar@altlinux.org> 2.7.2-alt3
- Fix: Use 'armh' for 'armhf'.

* Mon Jul 12 2021 Paul Wolneykien <manowar@altlinux.org> 2.7.2-alt2
- Added libjcPKCS11-2.so.2.7.2 for aarch64, armhf, e2k, e2kv4,
  and mipsel arches.

* Fri Jul 09 2021 Paul Wolneykien <manowar@altlinux.org> 2.7.2-alt1
- Initial version for Sisyphus.
