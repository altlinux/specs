%define appdir %webserver_htdocsdir/%name

Name: phpPgAdmin
Version: 5.0.4
Release: alt1

Summary: Handle the adminstration of PostgreSQL over the web
License: GPLv2+
Group: System/Servers

URL: http://phppgadmin.sourceforge.net/
Source0: http://downloads.sourceforge.net/phppgadmin/phpPgAdmin-%version.tar.bz2
Source1: phpPgAdmin.localhost.htaccess

# we need macros defining html files location:
BuildPrereq: rpm-macros-webserver-common

Requires: php5-pgsql
BuildArch: noarch

%description
phpPgAdmin is a fully functional PostgreSQL administration utility. You can use
it to create and maintain multiple databases and even multiple servers.

%prep
%setup

%build
mv -f conf/config.inc.php-dist conf/config.inc.php

%install
subst 's|error_reporting(E_ALL);|error_reporting(E_ALL \& ~E_NOTICE);|' libraries/lib.inc.php

install -m644 -pD %SOURCE1 %buildroot%appdir/.htaccess
cp -aRf [^A-Z]* %buildroot%appdir/

# cleanup
pushd %buildroot%appdir
rm -f conf/.cvsignore
rm -rf sql
rm -f lang/Makefile lang/convert.awk lang/php2po lang/po2php lang/synch lang/langcheck
popd

# may be move config.inc.php to /etc/... out of web docroot? see mdk-contrib package
%files
%doc CREDITS DEVELOPERS FAQ HISTORY INSTALL TODO TRANSLATORS sql/*
%config(noreplace) %attr(0640,apache,webmaster) %appdir/conf/config.inc.php
%config(noreplace) %attr(0640,apache,webmaster) %appdir/.htaccess
%appdir/

%changelog
* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 5.0.4-alt1
- 5.0.4

* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 5.0.3-alt1
- 5.0.3

* Tue Jan 04 2011 Victor Forsiuk <force@altlinux.org> 5.0.2-alt1
- 5.0.2

* Mon Dec 20 2010 Victor Forsiuk <force@altlinux.org> 5.0.1-alt1
- 5.0.1

* Mon Dec 13 2010 Victor Forsiuk <force@altlinux.org> 5.0-alt1
- 5.0

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 4.2.3-alt1
- 4.2.3

* Wed Dec 24 2008 Victor Forsyuk <force@altlinux.org> 4.2.2-alt1
- 4.2.2

* Tue Aug 19 2008 Victor Forsyuk <force@altlinux.org> 4.2.1-alt1
- 4.2.1

* Mon Apr 07 2008 Victor Forsyuk <force@altlinux.org> 4.2-alt1
- 4.2

* Mon Jul 23 2007 Victor Forsyuk <force@altlinux.org> 4.1.3-alt1
- 4.1.3

* Tue Jun 05 2007 Victor Forsyuk <force@altlinux.org> 4.1.2-alt1
- 4.1.2
- Contains security fix: http://www.securityfocus.com/bid/24115/

* Mon Apr 23 2007 Victor Forsyuk <force@altlinux.org> 4.1.1-alt1
- 4.1.1

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 4.1-alt1
- 4.1

* Tue Oct 03 2006 Victor Forsyuk <force@altlinux.ru> 4.0.1-alt1
- 4.0.1
- Change ownership of config files: "webmaster" should be group name, not user!
- Add directory that contains package files to %%files list.
- Use macros from apache-devel for html files location.

* Thu Oct 27 2005 Victor Forsyuk <force@altlinux.ru> 3.5.6-alt1
- 3.5.6

* Wed Jul 20 2005 Victor Forsyuk <force@altlinux.ru> 3.5.4-alt1
- 3.5.4

* Mon Apr 18 2005 Victor Forsyuk <force@altlinux.ru> 3.5.3-alt1
- 3.5.3
- Lowered error reporting level to eliminate notices from exported
  SQL files (PLD).

* Mon Feb 28 2005 Victor Forsyuk <force@altlinux.ru> 3.5.2-alt1
- 3.5.2

* Mon Aug 30 2004 Victor Forsyuk <force@altlinux.ru> 3.4.1-alt1
- 3.4.1.

* Wed Apr 28 2004 Victor Forsyuk <force@altlinux.ru> 3.3.1-alt1
- New version.

* Mon Aug 18 2003 Michael Shigorin <mike@altlinux.ru> 3.0.1-alt1
- 3.0.1
- removed postgresql dependency (already via php-pgsql)
- minor spec cleanup

* Thu Jul 03 2003 Michael Shigorin <mike@altlinux.ru> 3.0-alt1
- 3.0

* Tue Apr 22 2003 Michael Shigorin <mike@altlinux.ru> 2.4.2-alt3
- fixed Requires: (s/mysql/pgsql/)

* Tue Feb 11 2003 Michael Shigorin <mike@altlinux.ru> 2.4.2-alt2
- default access control implemented (from TODO) -- don't use 2.4.2-alt1
  (which was kind of internal packaging anyways)
- fixed config.inc.php owner (apache->webmaster)

* Tue Oct 08 2002 Michael Shigorin <mike@altlinux.ru> 2.4.2-alt1
- adapted from Cooker
- spec cleanup

* Thu Sep 19 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.4.2-2mdk
- misc spec file fixes
- install in common and relocatable %%{webadminroot}/ directory

* Tue Jul 09 2002 Christian Belisle <cbelisle@mandrakesoft.com> 2.4.2-1mdk
- Version 2.4.2.
- updated URL.
- no %%postun needed.

* Mon Apr 08 2002 Christian Belisle <cbelisle@mandrakesoft.com> 2.4.1-1mdk
- Version 2.4.1.

* Mon Mar 04 2002 Christian Belisle <cbelisle@mandrakesoft.com> 2.4a-1mdk
- official release 2.4a (major security fix and few bug fixes).
- Remove distribution tag.
- Updated URL.

* Thu Nov 15 2001 Christian Belisle <cbelisle@mandrakesoft.com> 2.3-4mdk
- Fix strange-permissions and no-url warning in rpmlint.

* Tue Oct 16 2001 Christian Belisle <cbelisle@mandrakesoft.com> 2.3-3mdk
- Make rpmlint happier.

* Thu Aug 09 2001 Christian Belisle <cbelisle@mandrakesoft.com> 2.3-2mdk
- s/PostgreSQL/postgresql in require.

* Thu Aug 09 2001 Christian Belisle <cbelisle@mandrakesoft.com> 2.3-1mdk
- first rpm distribution.
