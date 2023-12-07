%define _unpackaged_files_terminate_build 1

#%ifarch %ix86
%set_verify_elf_method relaxed
#%endif

%brp_strip_none

%define soversion 2.9.0

Name: libjcpkcs11
Version: 2.9.0.806
Release: alt3

Summary: Aladdin JaCarta PKCS#11 library
License: Proprietary
Group: System/Configuration/Hardware

Url: https://www.aladdin-rd.ru/support/downloads/c9b88e95-aaef-4448-9c86-745639439189
Source: %name-%version.tar
ExclusiveArch: aarch64 armh e2kv4 %ix86 mipsel x86_64

BuildRequires: libpcsclite-devel chrpath

Requires: pcsc-lite-ccid

Provides: pcsc-lite-jcpkcs11 = %version-%release
Obsoletes: pcsc-lite-jcpkcs11 < %version-%release
Conflicts: pcsc-lite-jcpkcs11 < %version-%release

# Provide "jcPKCS11-2" for Jacarta Client.
Provides: jcPKCS11-2 = %version
Conflicts: jcPKCS11-2
Provides: jcpkcs11-2 = %version
Conflicts: jcpkcs11-2

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
chrpath -d %buildroot%_libdir/*.so* \
	   %buildroot%_bindir/*

%files
%dir %_datadir/doc/%name-%soversion
%_datadir/doc/%name-%soversion/README.ALT
%_datadir/doc/%name-%soversion/EULA.pdf
%_libdir/*.so.%soversion
%_libdir/*.so
%_libdir/pkcs11/*.so
%_bindir/jcverify
%dir %_datadir/%name
%_datadir/%name/jcverify.txt
%_datadir/%name/jckt2.txt
%config(noreplace) %_sysconfdir/pkcs11/modules/jcpkcs11.module

%changelog
* Thu Dec 07 2023 Paul Wolneykien <manowar@altlinux.org> 2.9.0.806-alt3
- Added armh, i586 and mipsel arches.
- Fix: update.sh: Delete old binaries before update.
- Fix: Update with excess builds excluded.
- Use chrpath to fix the binaries.

* Wed Dec 06 2023 Paul Wolneykien <manowar@altlinux.org> 2.9.0.806-alt2
- Use chrpath to fix the libraries.

* Wed Dec 06 2023 Paul Wolneykien <manowar@altlinux.org> 2.9.0.806-alt1
- New version 2.9.0.806.

* Thu Nov 16 2023 Paul Wolneykien <manowar@altlinux.org> 2.8.0-alt4
- Add additional provides and conflicts of "jcPKCS11-2" and
  "jcpkcs11-2".

* Tue Oct 24 2023 Paul Wolneykien <manowar@altlinux.org> 2.8.0-alt3
- Provide "jcPKCS11-2" for Jacarta Client.

* Tue Apr 25 2023 Paul Wolneykien <manowar@altlinux.org> 2.8.0-alt2
- Restore support for i586, armh and mipsel architectures. E2K is
  replaced by e2kv4.

* Tue Apr 18 2023 Paul Wolneykien <manowar@altlinux.org> 2.8.0-alt1
- Update to v2.8.0.
- Drop support for i586, armh, e2k and mipsel architectures.

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
