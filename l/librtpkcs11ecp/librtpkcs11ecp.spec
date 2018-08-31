%ifarch %ix86
%set_verify_elf_method relaxed
%endif
%brp_strip_none

Summary: Rutoken PKCS#11 Library
Name: librtpkcs11ecp
Version: 1.8.2.0
Release: alt2
License: Proprietary
Url: https://www.rutoken.ru/support/download/pkcs/
Group: System/Configuration/Hardware
Source0: %name-%version.tar
ExclusiveArch: %ix86 x86_64 armh mips64el

Requires: pcsc-lite-ccid

BuildRequires: libpcsclite-devel

Provides: pcsc-lite-rtpkcs11ecp = %version-%release
Obsoletes: pcsc-lite-rtpkcs11ecp < %version-%release
Conflicts: pcsc-lite-rtpkcs11ecp < %version-%release

%description
Allow users to work with Rutoken ECP through PKCS#11 standard.

%prep
%setup

%install
%ifarch %ix86
install -D -m0644 %name-i586.so %buildroot%_libdir/pkcs11/librtpkcs11ecp.so
%endif
%ifarch x86_64
install -D -m0644 %name-x86_64.so %buildroot%_libdir/pkcs11/librtpkcs11ecp.so
%endif
%ifarch armh
install -D -m0644 %name-armv7hf.so %buildroot%_libdir/pkcs11/librtpkcs11ecp.so
%endif
%ifarch mips64el
install -D -m0644 %name-mips64el.so %buildroot%_libdir/pkcs11/librtpkcs11ecp.so
%endif

ln -s pkcs11/librtpkcs11ecp.so %buildroot%_libdir/librtpkcs11ecp.so

install -D -m0644 rutokenecp.module \
        %buildroot%_sysconfdir/pkcs11/modules/rutokenecp.module

%files
%doc license.ru.html
%_libdir/*.so
%_libdir/pkcs11/*.so
%config(noreplace) %_sysconfdir/pkcs11/modules/rutokenecp.module

%changelog
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
