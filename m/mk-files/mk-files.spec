Name: mk-files
Version: 20081111
Release: alt3

Summary: Support files for bmake, the NetBSD make(1) tool

License: BSD
Group: Development/Tools
Url: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.NetBSD.org/pub/NetBSD/misc/sjg/mk-%version.tar.bz2

BuildArch: noarch

Requires: bmake

Conflicts: pkgsrc-mk-files

%description
The mk-files package provides some bmake macros derived from the NetBSD
bsd.*.mk macros.  These macros allow the creation of simple Makefiles to
build all kinds of targets, including, for example, C/C++ programs and/or
shared libraries.

%prep
%setup -n mk
%__subst 's|cp_f=-f|cp_f=-pf|' install-mk

%install
install -m 755 -d %buildroot%_datadir/mk
env FORCE_BSD_MK=%buildroot/nonexistent \
    SYS_MK_DIR=%buildroot/nonexistent \
    sh install-mk -v -m 644 %buildroot%_datadir/mk

%files
%doc ChangeLog README
%_datadir/mk/*

%changelog
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
