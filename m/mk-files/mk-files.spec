Name: mk-files
Version: 20220214
Release: alt1

Summary: Support files for bmake, the NetBSD make(1) tool

License: BSD
Group: Development/Tools
Url: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/mk-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3

#Requires: bmake

Conflicts: pkgsrc-mk-files

%description
The mk-files package provides some bmake macros derived from the NetBSD
bsd.*.mk macros.  These macros allow the creation of simple Makefiles to
build all kinds of targets, including, for example, C/C++ programs and/or
shared libraries.

%prep
%setup -n mk
sed -i 's|cp_f=-f|cp_f=-pf|' install-mk
sed -i "s|/usr/bin/env python\$|/usr/bin/env python3|" *.py

%install
install -m 755 -d %buildroot%_datadir/mk
env FORCE_BSD_MK=%buildroot/nonexistent \
    SYS_MK_DIR=%buildroot/nonexistent \
    sh install-mk -v -m 644 %buildroot%_datadir/mk

%files
%doc ChangeLog README
%_datadir/mk/*

%changelog
* Fri Jun 24 2022 Fr. Br. George <george@altlinux.org> 20220214-alt1
- Fresh version

* Sat May 15 2021 Vitaly Lipatov <lav@altlinux.ru> 20191111-alt2
- add BR: rpm-build-python3

* Tue Feb 11 2020 Vitaly Lipatov <lav@altlinux.ru> 20191111-alt1
- new version 20191111 (with rpmrb script)

* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 20180528-alt1
- new version (20180528) with rpmgs script

* Wed Jul 29 2009 Vitaly Lipatov <lav@altlinux.ru> 20081111-alt3
- cleanup spec, pack only files in mk dir

* Thu Jul 23 2009 Aleksey Cheusov <vle@gmx.net> 20081111-alt2
- improvements and clean-ups

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 20081111-alt1
- initial build for ALT Linux Sisyphus

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070430-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 2 2008 Julio M. Merino Vidal <jmmv@NetBSD.org> - 20070430-1
- Initial release for Fedora.
