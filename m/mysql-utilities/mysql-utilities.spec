Name: mysql-utilities
Version: 1.4.4
Release: alt1

Summary: MySQL Utilities

License: GPLv2
Group: Databases
Url: https://launchpad.net/mysql-utilities

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Upstream has a mirror redirector for downloads, so the URL is hard to
# represent statically.  You can get the tarball by following a link from
# http://dev.mysql.com/downloads/tools/utilities/
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel

BuildRequires: python-module-mysql >= 1.2.1

Requires: python-module-mysql >= 1.2.1

# Is it correct method to disable python modules providing?
AutoProv: nopython

%description
A package of utilities that are used for maintenance and administration
of MySQL servers. These utilities encapsulate a set of primitive commands,
and bundles them so they can be used to perform macro operations with a
single command.

Documentation:
http://dev.mysql.com/doc/workbench/en/mysql-utilities.html

%prep
%setup

%build
%python_build

%install
install --directory %buildroot%_man1dir

%python_install --skip-profile

: Man pages
%__python setup.py install_man --root %buildroot

# Archive with doctrine files does not seem like something it should be
# part of RPM; it might un-packed into a separate package if necessary
rm -f %buildroot%_sysconfdir/mysql/mysql-fabric-doctrine-1.4.0.zip
# from python-module-mysql
rm -rf %buildroot%python_sitelibdir/mysql/connector/

%files
%doc CHANGES.txt LICENSE.txt README.txt
%_bindir/mysqlauditadmin
%_bindir/mysqlauditgrep
%_bindir/mysqldbcompare
%_bindir/mysqldbcopy
%_bindir/mysqldbexport
%_bindir/mysqldbimport
%_bindir/mysqldiff
%_bindir/mysqldiskusage
%_bindir/mysqlfailover
%_bindir/mysqlfrm
%_bindir/mysqlindexcheck
%_bindir/mysqlmetagrep
%_bindir/mysqlprocgrep
%_bindir/mysqlreplicate
%_bindir/mysqlrpladmin
%_bindir/mysqlrplcheck
%_bindir/mysqlrplshow
%_bindir/mysqlserverclone
%_bindir/mysqlserverinfo
%_bindir/mysqluc
%_bindir/mysqluserclone
%python_sitelibdir/mysql/utilities
%python_sitelibdir/mysql_utilities*
%_man1dir/mysql*
# empty file already provided by mysql-connector-python
%exclude %python_sitelibdir/mysql/__init*

# mysql fabric files
%dir %_sysconfdir/mysql/
%config(noreplace) %_sysconfdir/mysql/fabric.cfg
%_bindir/mysqlfabric
%_bindir/mysqlrplms
%_bindir/mysqlrplsync
%python_sitelibdir/mysql/fabric

%changelog
* Fri Sep 19 2014 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- initial build for ALT Linux Sisyphus

* Mon Aug 18 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 1.4.4-1
- Update to 1.4.4 - bz#1111839.

* Tue Jun 17 2014 Honza Horak <hhorak@redhat.com> - 1.4.3-1
- update to 1.4.3 GA, which adds mysql fabric

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 19 2013 Remi Collet <remi@fedoraproject.org> - 1.3.6-1
- update to 1.3.6 GA
- add mysqlauditadmin and mysqlauditgrep on EPEL-6

* Mon Sep  9 2013 Remi Collet <remi@fedoraproject.org> - 1.3.5-1
- update to 1.3.5 GA

* Mon Aug  5 2013 Remi Collet <remi@fedoraproject.org> - 1.3.4-1
- update to 1.3.4 GA

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Remi Collet <remi@fedoraproject.org> - 1.3.3-1
- update to 1.3.3 (beta)

* Sat Jun 15 2013 Remi Collet <remi@fedoraproject.org> - 1.3.2-1
- update to 1.3.2 (beta)

* Sat Apr  6 2013 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0 (alpha)
  http://dev.mysql.com/doc/relnotes/mysql-utilities/en/wb-utils-news-1-3-0.html
- move from launchpad to mysql.com
- new command mysqlfrm
- mysqluc is now usable
- man pages provided in upstream tarball

* Fri Mar  8 2013 Remi Collet <remi@fedoraproject.org> - 1.2.1-2
- generate minimal man pages using help2man
  http://bugs.mysql.com/68610 - Missing man pages
- drop mysqlauditadmin and mysqlauditgrep on EPEL-6
  http://bugs.mysql.com/68614 - Issue with python 2.6

* Fri Mar  8 2013 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1
- no man pages, http://bugs.mysql.com/68610

* Fri Feb  8 2013 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0
- new commands: mysqlauditadmin and mysqlauditgrep

* Wed Jan  9 2013 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Thu Oct  4 2012 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0
- new command mysqluc removed (broken)

* Fri Aug 10 2012 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- update to 1.0.6

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 27 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-3
- no man for EL-6 (missing recent python-sphinx)

* Sun Apr 15 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-2
- fix BR to python2-devel
- incorrect-fsf-address and non-executable-script referenced as
  Oracle BUG#13956819
- remove mut man page (command not installed)

* Wed Apr 11 2012 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- initial RPM

