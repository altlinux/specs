%ifarch %ix86
%set_verify_elf_method relaxed
%endif
%brp_strip_none

Name: librtpkcs11ecp
Version: 2.7.1.0
Release: alt1

Summary: Rutoken PKCS#11 Library
License: Proprietary
Group: System/Configuration/Hardware

Url: https://www.rutoken.ru/support/download/pkcs/
Source: %name-%version.tar
ExclusiveArch: i586 x86_64 armh aarch64 mipsel mips64el e2k e2kv4 e2kv5 e2kv6

BuildRequires: libpcsclite-devel

Requires: pcsc-lite-ccid

Provides: pcsc-lite-rtpkcs11ecp = %version-%release
Obsoletes: pcsc-lite-rtpkcs11ecp < %version-%release
Conflicts: pcsc-lite-rtpkcs11ecp < %version-%release

Summary(ru_RU.UTF-8): Библиотека PKCS#11 для Рутокен ЭЦП

%description
Allow users to work with Rutoken ECP through PKCS#11 standard.

%description -l ru_RU.UTF-8
Позволяет пользоваться Рутокен ЭЦП посредством стандарта PKCS#11.

%prep
%setup
%ifarch e2kv5
# preparing for 8CB rollout (rather scarce yet);
# practical binary compatibility is good
[ -d e2kv5 ] || cp -a e2kv4 e2kv5
%endif
%ifarch e2kv6
# ditto for 16C
[ -d e2kv6 ] || cp -a e2kv4 e2kv6
%endif

%install
install -pDm644 %_arch/%name.so %buildroot%_libdir/pkcs11/%name.so
ln -s pkcs11/%name.so %buildroot%_libdir/%name.so

install -pDm644 rutokenecp.module \
        %buildroot%_sysconfdir/pkcs11/modules/rutokenecp.module

%files
%doc LICENSE NOTICE.txt
%_libdir/*.so
%_libdir/pkcs11/*.so
%config(noreplace) %_sysconfdir/pkcs11/modules/rutokenecp.module

%changelog
* Sun Dec 18 2022 Andrey Cherepanov <cas@altlinux.org> 2.7.1.0-alt1
- New version.
- Drop support of ppc64le by upstream.
- Use license files from upstream packages.

* Sun Oct 09 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.1.0-alt1
- New version.

* Sat Sep 17 2022 Michael Shigorin <mike@altlinux.org> 2.4.1.0-alt3
- No v5 binaries so far, fallback to v4.

* Thu Sep 15 2022 Michael Shigorin <mike@altlinux.org> 2.4.1.0-alt2
- Added e2kv6 target.

* Sat Sep 03 2022 Andrey Cherepanov <cas@altlinux.org> 2.4.1.0-alt1
- New version.

* Mon Jul 25 2022 Andrey Cherepanov <cas@altlinux.org> 2.4.0.0-alt1
- New version.

* Thu Mar 31 2022 Andrey Cherepanov <cas@altlinux.org> 2.3.3.0-alt1
- New version.

* Mon Jan 17 2022 Andrey Cherepanov <cas@altlinux.org> 2.3.2.0-alt1
- New version.

* Fri Dec 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.0.0-alt1
- New version.

* Thu Oct 07 2021 Andrey Cherepanov <cas@altlinux.org> 2.1.2.0-alt1
- New version.

* Thu Apr 29 2021 Anna Khrustova <khab@altlinux.org> 2.1.1.0-alt2
- Preparing for e2kv5, thanks @mike.

* Tue Apr 13 2021 Anna Khrustova <khab@altlinux.org> 2.1.1.0-alt1
- Update to 2.1.1.0 all library except ppc64le.

* Thu Jan 21 2021 Anna Khrustova <khab@altlinux.org> 2.0.11.0-alt1
- Update to 2.0.11.0 all library except ppc64le.

* Tue Nov 10 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.9.0-alt2
- Add library for ppc64le.

* Mon Oct 26 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.9.0-alt1
- Updated to 2.0.9.0.

* Sat Mar 14 2020 Andrey Cherepanov <cas@altlinux.org> 2.0.4.0-alt1
- Updated to 2.0.4.0.

* Wed Jun 26 2019 Michael Shigorin <mike@altlinux.org> 1.9.12.0-alt1
- Updated to 1.9.12.0; new arches: aarch64, e2k, e2kv4, mipsel.
- Added update.sh to automate the library extraction next time.
- Simplified spec, added Russian translation while at that.

* Thu Aug 30 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.2.0-alt2
- Install files with "install".

* Thu Aug 30 2018 Paul Wolneykien <manowar@altlinux.org> 1.8.2.0-alt1
- Updated to v1.8.2.0. New arches: armh, mips64el.

* Wed Sep 06 2017 Paul Wolneykien <manowar@altlinux.org> 1.5.3.0-alt4
- Add the module description for p11-kit.
- Require pcsc-lite-ccid.

* Thu Apr 06 2017 Andrey Cherepanov <cas@altlinux.org> 1.5.3.0-alt3
- Correct sources (separate .so files as vendor recommends)

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.5.3.0-alt2
- Update license

* Sat Apr 01 2017 Andrey Cherepanov <cas@altlinux.org> 1.5.3.0-alt1
- New version

* Wed Dec 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.4.5.0-alt1
- New version (ALT #32921)
- Fix homepage

* Wed Apr 02 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt3
- Merge with pcsc-lite-rtpkcs11ecp.

* Mon Mar 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- initial
