Name: libnss-mysql
Version: 1.6
Release: alt4

Summary: NSS API library
Summary(ru_RU.UTF-8): Библиотека NSS API

License: GPL
URL: http://libnss-mysql.sourceforge.net
Group: System/Libraries

#Source: http://dl.sf.net/%name/%name-%version.tar.bz2
Source: http://libnss-mysql.sourceforge.net/snapshot/libnss-mysql-20060915.tar

# Automatically added by buildreq on Tue Apr 18 2006
BuildRequires: gcc-c++ libMySQL-devel zlib-devel

BuildPreReq: rpm-build-intro

%description
NSS API library for store passwd/group info in MySQL.

%description -l ru_RU.UTF-8
Библиотека NSS API, позволяющая хранить passwd/group в MySQL.

%prep
%setup -n %name
%remove_repo_info

%build
%configure MYSQL_LIB_DIR=%_libdir
%make_build

%install
mkdir -p %buildroot/etc/
%makeinstall_std

mkdir -p %buildroot/etc/buildreqs/packages/ignore.d/
touch %buildroot/etc/buildreqs/packages/ignore.d/%name

%files
%_libdir/*.so*
%config(noreplace) /etc/libnss-mysql.cfg
%config(noreplace) /etc/libnss-mysql-root.cfg
/etc/buildreqs/packages/ignore.d/%name
%doc README ChangeLog AUTHORS THANKS NEWS FAQ DEBUGGING UPGRADING TODO
%doc sample/README sample/linux/

%changelog
* Mon Mar 28 2011 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt4
- add buildreqs ignore files (ALT bug #21886)

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt3
- cleanup spec
- rebuild with libmysqlclient16

* Thu May 14 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt2
- fix doc packing (remove CVS subdirs)

* Sat Mar 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- build CVS snapshot from Fri Sep 15 21:16:03 PDT 2006 (fix SegFault with alien)

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt2
- NMU: fix build on x86_64, enable SMP-build
- cleanup spec, remove COPYING
- add URL for Source

* Fri Mar 31 2006 Alexander V. Denisov <rupor@altlinux.ru> 1.5-alt1
- Bugfix Connect timeout broke ability to connect to MySQL server on some platforms.

* Wed Mar 09 2005 Alexander V. Denisov <rupor@altlinux.ru> 1.4-alt1
- Read [libnss-mysql] and [client] sections in /etc/my.cnf
- Removed these options from libnss-mysql.cfg: timeout, compress, initcmd

* Mon Nov 22 2004 Alexander V. Denisov <rupor@altlinux.ru> 1.3-alt1
- Configuration file line continuation is now supported.
- Removed extraneous UNLOCK that caused thread instability due to changes in version 1.2
- Added missing Makefile path to <OS>.sym
- Safely purge MySQL password at program exit
- Big changes in config parsing; [section]'s are meaningless and safely ignored, but should be removed
- Static allocation of configuration variables
- Moved sources to src/ and aux files to aux/
- Send a syslog if number of columns returned != expected #
- (Internal) code and support file cleanup; comments

* Wed May 19 2004 Alexander V. Denisov <rupor at altlinux dot ru> 1.2-alt2
- some spec changes 

* Wed Mar 31 2004 Alexander V. Denisov <rupor at altlinux dot ru> 1.2-alt1
- euid-change detection was broken, causing things like privsep-enabled SSH daemons to be unable to log in a MySQL user.
- Fixed broken 'initcmd' option
- supported MySQL version is 3.23.09
- Removed 'ssl' config option - it's not supposed to be used by client programs
						      

* Thu Mar 25 2004 Alexander V. Denisov <rupor at altlinux dot ru> 1.1-alt1
- Update to 1.1
- Some fixes 

* Tue Oct 28 2003 Alexander V. Denisov <rupor@altlinux.ru> 1.0-alt1
- Update to 1.0

* Tue Jul 01 2003 Alexander V. Denisov <rupor@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Team


