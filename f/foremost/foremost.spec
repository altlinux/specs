Name: foremost
Version: 1.5.7
Release: alt2

Summary: Recover files by "carving" them from a raw disk

License: Public Domain
Group: Text tools
Url: http://foremost.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://foremost.sourceforge.net/pkg/%name-%version.tar
Patch0: foremost-broken-jpeg.patch
Patch1: foremost-fix-permission-timestamp.patch
Patch2: foremost-1.5.7-format-security.patch
Patch3: foremost-1.5.7-gcc10.patch
Patch10: %name-sysconfdir.patch

%description
Foremost recovers files files based on their headers, footers, and
internal data structures. This process is commonly referred to as data
carving. Foremost can work on a raw disk drive or image file generated
by dd. The headers and footers can be specified by a configuration
file or you can use command line switches to specify built-in file
types. These built-in types look at the data structures of a given
file format allowing for a more reliable and faster recovery.

See use case in russian: http://mydebianblog.blogspot.com/2007/01/1-foremost.html

%prep
%setup
%patch10 -p2
%patch0
%patch1 -p2
%patch2 -p1
%patch3 -p1

%build
%make_build \
	RAW_CC="%__cc" \
	RAW_FLAGS="%optflags -DVERSION=\\\"%version\\\"" \
	BIN=%_bindir \
	MAN=%_man1dir \
	CONF=%_sysconfdir

%install
install -d %buildroot{%_bindir,%_man1dir,%_sysconfdir}

%make_install install \
	BIN=%buildroot%_bindir \
	MAN=%buildroot%_man1dir \
	CONF=%buildroot%_sysconfdir

%files
%doc README CHANGES
%_bindir/%name
%_man1dir/*
%config(noreplace) %_sysconfdir/%name.conf

%changelog
* Fri Feb 26 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5.7-alt2
- add fixes from Fedora

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 1.5.7-alt1
- new version 1.5.7 (with rpmrb script)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.5.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Jul 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- new version 1.5.4 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- new version 1.5.3 (with rpmrb script)

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (with rpmrb script)

* Sat Jan 20 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

