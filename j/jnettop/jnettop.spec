Name: jnettop
Version: 0.13.0
Release: alt3

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Network traffic tracker
License: GPLv2+
Group: Monitoring

URL: http://jnettop.kubs.info/
Source: http://jnettop.kubs.info/dist/jnettop-%version.tar.gz

# Automatically added by buildreq on Fri Jun 20 2008 (-bi)
BuildRequires: glib2-devel libdb4-devel libncurses-devel libpcap-devel samba-client

%description
Nettop is visualising active network traffic as top does with processes.
It displays active network streams sorted by bandwidth used. This is
often usable when you want to get a fast grip of what is going on on your
outbound router.

%package resolver-samba
Summary: External nmblookup resolver script for jnettop.
Group: Monitoring
Requires: %name = %version-%release

%description resolver-samba
External nmblookup resolver script for jnettop.

%prep
%setup

%__subst 's/AM_LDFLAGS/LDADD/' Makefile.am

%build
autoreconf -fisv
%configure
%make_build CFLAGS="%optflags"

%install
%make_install install DESTDIR=%buildroot

%files
%_bindir/*
%dir %_datadir/jnettop
%_man8dir/*
%doc AUTHORS NEWS README .jnettop

%files resolver-samba
%_datadir/jnettop/jnettop-lookup-nmb

%changelog
* Fri Jun 20 2008 Victor Forsyuk <force@altlinux.org> 0.13.0-alt3
- Split nmblookup resolver script to own package to avoid "heavy" main package
  dependency on samba-client (fix #15240).

* Sat Jun 14 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.13.0-alt2.1
- Automated rebuild with libdb-4.7.so.

* Mon Nov 12 2007 Victor Forsyuk <force@altlinux.org> 0.13.0-alt2
- Fix License tag.

* Tue Jul 17 2007 Victor Forsyuk <force@altlinux.org> 0.13.0-alt1
- 0.13.0

* Tue Mar 21 2006 Vladimir Lettiev <crux@altlinux.ru> 0.11.0-alt2
- Fix build with -Wl, --as-needed

* Sat Jul 02 2005 Vladimir Lettiev <crux@altlinux.ru> 0.11.0-alt1
- New upstream release

* Tue Feb 22 2005 Vladimir Lettiev <crux@altlinux.ru> 0.10.1-alt1
- Rebuilt for ALTLinux Sisyphus
- spec cleanup

* Sat Oct 2 2004 Jakub Skopal <j@kubs.cz> 0.10.1
- transition to release 0.10.1, see ChangeLog

* Wed Sep 29 2004 Jakub Skopal <j@kubs.cz> 0.10
- manual page is now part of RPM package
- transition to release 0.10, see ChangeLog

* Wed Jul 30 2003 Jakub Skopal <j@kubs.cz> 0.9
- transition to release 0.9, see ChangeLog

* Wed Apr 23 2003 Jakub Skopal <j@kubs.cz> 0.8.1-1
- transition to release 0.8.1, see ChangeLog

* Wed Apr 23 2003 Jakub Skopal <j@kubs.cz> 0.8-1
- transition to release 0.8, see ChangeLog

* Tue Oct 16 2002 Jakub Skopal <j@kubs.cz> 0.7-1
- transition to release 0.7, see ChangeLog

* Tue Oct 13 2002 Jakub Skopal <j@kubs.cz> 0.6-1
- transition to release 0.6, see ChangeLog

* Tue Sep 03 2002 Jakub Skopal <j@kubs.cz> 0.5-1
- transition to release 0.5, see ChangeLog

* Mon Sep 02 2002 Jakub Skopal <j@kubs.cz> 0.4-1
- transition to release 0.4, see ChangeLog

* Thu Aug 27 2002 Jakub Skopal <j@kubs.cz> 0.3-1
- transition to release 0.3, see ChangeLog

* Thu Aug 27 2002 Jakub Skopal <j@kubs.cz> 0.2-1
- transition to release 0.2, see ChangeLog

* Thu Aug 22 2002 Jakub Skopal <j@kubs.cz> 0.1-1
- initial release
