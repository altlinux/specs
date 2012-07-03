Name: pkgsrc-mk-files
Version: 20100117
Release: alt1

Summary: PKGSRC mk-files for bmake, the NetBSD make(1) tool

License: BSD
Group: Development/Tools
Url: http://mova.org/~cheusov/pub/netbsd-tools/pkgsrc-mk-files/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://mova.org/~cheusov/pub/netbsd-tools/pkgsrc-mk-files/netbsd-%name-%version.tar

BuildArch: noarch

Conflicts: mk-files

%description
The mk-files package provides some bmake macros derived from the NetBSD
bsd.*.mk macros.  These macros allow the creation of simple Makefiles to
build all kinds of targets, including, for example, C/C++ programs and/or
shared libraries.
This package provides PKGSRC (http://pkgsrc.org) variants of mk-files.

%prep
%setup -n netbsd-%name-%version

%install
CP=/bin/cp
OPSYS=Linux
MK_DST=%buildroot%_datadir/mk
ROOT_GROUP=root
ROOT_USER=root
SED=/bin/sed
SYSCONFDIR=/etc
export CP OPSYS MK_DST ROOT_GROUP ROOT_USER SED SYSCONFDIR
mkdir -p ${MK_DST}
sh bootstrap.sh

%files
%_datadir/mk/

%changelog
* Sun Jun 27 2010 Vitaly Lipatov <lav@altlinux.ru> 20100117-alt1
- new version (20100117) import in git
- remove bmake requires (hold /usr/share/mk here)

* Wed Jul 29 2009 Vitaly Lipatov <lav@altlinux.ru> 20090329-alt2
- build for Sisyphus

* Thu Jul 23 2009 Aleksey Cheusov <vle@gmx.net> 20090329-alt1
- initial build of pkgsrc-mk-files for ALT Linux Sisyphus
