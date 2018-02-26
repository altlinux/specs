Name: ccze
Version: 0.2.1
Release: alt6

Packager: Victor Forsyuk <force@altlinux.org>

Summary: A fast and robust log colorizer
License: GPLv2+
Group: File tools

# http://web.archive.org/web/20070331114414/http://bonehunter.rulez.org/software/ccze/
URL: http://packages.debian.org/search?keywords=ccze
Source0: ccze-%version.tar.gz
Patch0: ccze-0.2.1-alt-argp.patch
Patch1: ccze-configure.ac.patch
Patch2: ccze-man.patch
Patch3: mod_syslog.c.patch
Patch4: ccze-wordcolor.c.patch

# Automatically added by buildreq on Tue Aug 04 2009
BuildRequires: libncurses-devel libpcre-devel

%description
CCZE is a robust and modular log colorizer, with plugins for apm, exim,
fetchmail, httpd, postfix, procmail, squid, syslog, ulogd, vsftpd, xferlog
and more.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# Fix FTBFS with gcc4:
%__subst 's/ -Wmulticharacter//g' src/Makefile.in

autoconf
libtoolize --copy --force
%configure --with-builtins=all
%make_build

%install
%make_install install DESTDIR=%buildroot

install -d %buildroot%_sysconfdir
src/ccze-dump >%buildroot%_sysconfdir/cczerc

%files
%doc AUTHORS FAQ NEWS THANKS
%config %_sysconfdir/cczerc
%exclude %_includedir
%_bindir/*
%_man1dir/*
%_man7dir/*

%changelog
* Tue Aug 04 2009 Victor Forsyuk <force@altlinux.org> 0.2.1-alt6
- Upstream is dead. Point URL to Debian package page (better than nothing).

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.1-alt5.0
- Automated rebuild.

* Mon May 15 2006 Victor Forsyuk <force@altlinux.ru> 0.2.1-alt5
- Fix FTBFS with gcc4.
- Added Debian patches (BTS# 307036, 330974 and 345586).

* Mon Oct 10 2005 Victor Forsyuk <force@altlinux.ru> 0.2.1-alt4
- Just fix software URL.

* Thu May 20 2004 Victor Forsyuk <force@altlinux.ru> 0.2.1-alt3
- Patch from Dmitry Levin <ldv@> to eliminate segfaults in options
  parsing with recent releases of glibc 2.3.

* Mon Mar 01 2004 Victor Forsyuk <force@altlinux.ru> 0.2.1-alt2
- Rebuild to link with libpcre.so.3.

* Mon Jun 02 2003 Victor Forsyuk <force@altlinux.ru> 0.2.1-alt1
- New version.

* Tue Mar 25 2003 Victor Forsyuk <force@altlinux.ru> 0.1.228-alt1
- Initial build for Sisyphus.
