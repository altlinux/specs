%global pkgname		dirsrv
%global groupname	%pkgname.target
%def_without selinux

Summary: 389 Directory Server (base)
Name: 	 389-ds-base
Version: 1.3.7.1
Release: alt2
License: GPLv3+ with exceptions
Url: 	 http://port389.org
Group: 	 System/Servers
Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version.tar
# VCS:   https://git@pagure.io/389-ds-base.git
Patch1:  alt-fix-initscripts.patch
Patch2:  alt-bash3-support.patch
Patch3:  alt-fix-sasl2.patch
Patch4:  alt-fix-const-declatations.patch
Patch5:  alt-link-libsds-with-pthread.patch
Patch6:  alt-link-ldaputil-with-libslapd.patch

BuildRequires: 389-adminutil-devel gcc-c++ libdb4-devel libicu-devel 
BuildRequires: libldap-devel libnet-snmp-devel libnl-devel libpam-devel 
BuildRequires: libpcre-devel libsasl2-devel libsensors3-devel libsvrcore-devel >= 4.1.2
BuildRequires: perl-devel
BuildRequires: perl-Mozilla-LDAP perl-libnet perl-bignum
BuildRequires: perl-DBM
BuildRequires: perl-NetAddr-IP
BuildRequires: perl-Archive-Tar
BuildRequires: perl-Socket6
BuildRequires: libsystemd-devel
BuildRequires: libevent-devel
BuildRequires: doxygen

Provides:  fedora-ds = %version-%release
Obsoletes: fedora-ds < %version-%release
Provides:  ldif2ldbm
Conflicts: lprng

# AutoReq: yes, noperl
%add_perl_lib_path %_libdir/%pkgname/perl
%add_findprov_skiplist %_datadir/%pkgname/script-templates/*
%add_findreq_skiplist %_datadir/%pkgname/script-templates/* %_sbindir/*-%pkgname

%description
389 Directory Server is an LDAPv3 compliant server. Use setup-ds.pl to
setup instances.

%package -n 389-ds
Summary: 389 Directory, Administration, and Console Suite
Group: System/Servers
BuildArch: noarch
Requires: 389-ds-base
Requires: 389-admin
Requires: idm-console-framework
Requires: 389-console
Requires: 389-ds-console
Requires: 389-ds-console-doc
Requires: 389-admin-console
Requires: 389-admin-console-doc
Requires: 389-dsgw

%description -n 389-ds
The 389 Directory Server, Administration Server, and Console Suite
provide the LDAPv3 server, the httpd daemon used to administer the
server, and the console GUI application used for server and user/group
administration.

%package devel
Summary: Development libraries for 389 Directory Server
Group: Development/C
Requires: %name = %version-%release
Provides:  389-ds-devel = %version-%release
Obsoletes: 389-ds-devel < %version-%release

%description devel
Development Libraries and heades for 389 Directory Server.

%package libs
Summary: Core libraries for 389 Directory Server
Group: System/Libraries
Provides:  389-ds-libs = %version-%release
Obsoletes: 389-ds-libs < %version-%release

%description libs
Core libraries for the 389 Directory Server base package.  These
libraries are used by the main package and the -devel package.  This
allows the -devel package to be installed with just the -libs package
and without the main package.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%autoreconf
# Install SysVInit scripts anyway
subst 's/@\(INITDDIR_TRUE\|SYSTEMD_FALSE\)@//g' Makefile.in

# For starnge cleanup before documentation build
mkdir -p man/man3
touch man/man3/_file

%build
%configure  \
	--with-openldap \
%if_with selinux
	--with-selinux \
%endif
	--localstatedir=/var \
 	--enable-autobind \
	--with-systemd \
	--with-systemdsystemunitdir=%_unitdir \
	--with-systemdsystemconfdir=%_sysconfdir/systemd/system \
	--with-systemdgroupname=%groupname \
	--with-perldir=%_bindir \
	--with-svrcore-inc=%_includedir \
	--with-svrcore-lib=%_libdir \
	--with-nss-lib=%_libdir \
	--with-nss-inc=%_includedir/nss

export XCFLAGS=$RPM_OPT_FLAGS

#USE_ADMSERV to avoid strange get_mag_var unresolved symbol
echo "#define USE_ADMSERV 1" >>config.h

%make_build

%install
%makeinstall_std

mkdir -p %buildroot/{%_lockdir,%_localstatedir,%_logdir,%_var/tmp}/%pkgname

# for systemd
mkdir -p %buildroot%{_sysconfdir}/systemd/system/%{groupname}.wants

# remove libtool and static libs
rm -f %buildroot%_libdir/%pkgname/{,plugins/}*.{a,la}

# make sure perl scripts have a proper shebang 
subst 's|#{{PERL-EXEC}}|#!%_bindir/perl|' %buildroot%_datadir/%pkgname/script-templates/template-*.pl
subst 's|File::Spec->tmpdir|"/tmp"|' %buildroot%_libdir/%pkgname/perl/DSCreate.pm

# move main libraries to common directory
mv %buildroot%_libdir/%pkgname/*.so* %buildroot%_libdir/

# Copy in our docs from doxygen
mkdir -p %buildroot%_man3dir
cp man/man3/* %buildroot%_man3dir

# Fix path to systemctl in scripts
subst 's,%_bindir/systemctl,/bin/systemctl,' %buildroot%_sbindir/*-dirsrv


%files
%doc LICENSE LICENSE.GPLv3+ LICENSE.openssl README 
%dir %_sysconfdir/%pkgname
%dir %_sysconfdir/%pkgname/schema
%config(noreplace)%_sysconfdir/%pkgname/schema/*.ldif
%dir %_sysconfdir/%pkgname/config
%dir %_sysconfdir/systemd/system/%groupname.wants
%config(noreplace)%_sysconfdir/%pkgname/config/slapd-collations.conf
%config(noreplace)%_sysconfdir/%pkgname/config/certmap.conf
%config(noreplace)%_sysconfdir/%pkgname/config/ldap-agent.conf
%config(noreplace)%_sysconfdir/%pkgname/config/template-initconfig
%config(noreplace)%_sysconfdir/sysconfig/%pkgname
%config(noreplace)%_sysconfdir/sysconfig/%pkgname.systemd
%_datadir/%pkgname
%_unitdir/*
%_bindir/*
%_sbindir/*
%_libdir/%pkgname/perl
%_libdir/%pkgname/python
%_libdir/%pkgname/plugins/*.so
%_datadir/gdb/auto-load/*
%_libexecdir/sysctl.d/*
%dir %_libdir/%pkgname/plugins
%dir %_localstatedir/%pkgname
%dir %_logdir/%pkgname
%ghost %dir %_lockdir/%pkgname
%_initdir/*
%_man1dir/*
%_man8dir/*

%files -n 389-ds

%files devel
%_includedir/%pkgname
%_libdir/*.so
%exclude %_libdir/libns-dshttpd-*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%files libs
%dir %_libdir/%pkgname
%_libdir/libns-dshttpd-*.so
%_libdir/libnunc-stans.so.*
%_libdir/libsds.so.*
%_libdir/libslapd.so.*
%_libdir/libldaputil.so.*

%triggerpostun -- 389-ds < 1.2.10.0-alt1
echo "Upgrading 389-ds < 1.2.10.0, manual Offline upgrade is required!
Turn 389-ds off and make 'setup-ds -u' then"

%pre
%define _dirsrv_user dirsrv
%define _dirsrv_group dirsrv
%define _dirsrv_home %_localstatedir/dirsrv
/usr/sbin/groupadd -r -f %_dirsrv_group ||:
/usr/sbin/useradd -g %_dirsrv_group -c 'user for 389-ds-base' \
		  -d %_dirsrv_home -s /sbin/nologin -r %_dirsrv_user \
		  > /dev/null 2>&1 ||:

%post
%post_service %pkgname
%post_service %pkgname-snmp

%preun
%preun_service %pkgname
%preun_service %pkgname-snmp

%changelog
* Mon Nov 27 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.7.1-alt2
- Add dirsrv user during pre install step (thanks slev@) (ALT #34240)

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.7.1-alt1
- New version

* Wed Apr 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.7.0-alt1
- New version

* Mon Apr 24 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.6.4-alt1
- New version
- Fix path to systemctl in scripts (ALT #33392)

* Mon Mar 27 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.6.3-alt1
- New version
- Fix type conflict for snmptrap_oid and snmptrap_oid_len (ALT #33282)

* Sat Mar 18 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.6.2-alt1
- New version

* Wed Nov 02 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.6.1-alt1
- new version 1.3.6.1

* Sun Oct 16 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.14-alt1
- new version 1.3.5.14

* Thu Aug 11 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.13-alt1
- new version 1.3.5.13

* Thu Jul 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.11-alt1
- new version 1.3.5.11

* Mon Jul 04 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.10-alt1
- new version 1.3.5.10

* Sun Jun 19 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.6-alt1
- new version 1.3.5.6

* Fri Jun 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.4-alt2
- Fix 64-bit architecture check

* Tue Jun 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.4-alt1
- New version

* Thu May 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.3-alt1
- New version

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.5.1-alt1
- New version

* Thu Feb 18 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.4.8-alt1
- New version

* Thu Jan 28 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.4.7-alt1
- New version
- Conflicts: lprng

* Sun Jan 17 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.4.6-alt1
- New version

* Mon Nov 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.4.5-alt1
- New version

* Thu Oct 15 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.4.4-alt1
- New version
- Make 389-ds as metapackage for complete suite install
- Simplify spec
- SELinux support is disabled

* Wed Nov 05 2014 Michael Shigorin <mike@altlinux.org> 1.3.2.15-alt3.e9f86dab
- cherry-picked 9df31ed to fix https://fedorahosted.org/389/ticket/47589

* Mon May 19 2014 Timur Aitov <timonbl4@altlinux.org> 1.3.2.15-alt2.e9f86dab
- git e9f86dab

* Mon Apr 28 2014 Timur Aitov <timonbl4@altlinux.org> 1.3.2.15-alt1
- 1.3.2.15

* Tue Sep 17 2013 Sergey Y. Afonin <asy@altlinux.ru> 1.2.10.12-alt1.qa1.1
- NMU: rebuilt with cyrus-sasl 2.1.26

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.10.12-alt1.qa1
- NMU: rebuilt with libicuuc.so.50.

* Mon Jul 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.10.12-alt1
- 1.2.10.12

* Fri Jul 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.10.0-alt1
- 1.2.10.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.9.10-alt1.1
- Rebuild with Python-2.7

* Sat Sep 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.9.10-alt1
- 1.2.9.10

* Fri Aug 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.9.4-alt1
- 1.2.9.4

* Tue Jun 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8.3-alt2
- rebuild with openldap-2.4.25

* Fri May 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8.3-alt1
- 1.2.8.3

* Thu May 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8.1-alt2
- fix build

* Mon Apr 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8.1-alt1
- 1.2.8.1

* Wed Mar 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.5-alt4
- repair build

* Wed Feb 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.5-alt3
- CVE-2011-0019

* Thu Feb 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.5-alt2
- build with openldap instead of mozldap

* Thu Dec 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.5-alt1
- 1.2.7.5

* Mon Dec 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.4-alt1
- 1.2.7.4

* Wed Dec 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.3-alt1
- 1.2.7.3

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.2-alt1
- 1.2.7.2
- rebuild with icu-4.6

* Fri Nov 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.1-alt1
- 1.2.7.1

* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Tue Sep 28 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6.1-alt1
- 1.2.6.1

* Wed Sep 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue Jul 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6-alt0.rc3.1
- 1.2.6-rc3

* Thu Jun 17 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.5-alt2
- CVE-2010-2222

* Wed Jan 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Tue Nov 10 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Wed Oct 21 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt1
- 1.2.3
- remove /var/run/fedora-ds and /var/lock/fedora-ds from package
- post/preun_server fedora-ds-snmp

* Mon Oct 12 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt3
- fix build (add libicu-devel to buildreq)

* Wed Sep 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt2
- use autoreq (patched rpm-build-perl required)
- merge upstream de006310

* Mon Aug 24 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Aug 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt2
- merge upstream 1.2.1

* Thu May 21 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sat Apr 04 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt2
- disabled pam_passthru plugin

* Fri Apr 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Wed Nov 05 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt1
- 1.1.3, libdb4.7

* Sat Sep 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Fri Aug 01 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1
- 1.1.1
- set dependency to libdb4.4 (rebuild with 4.7 problems)
- fix #16370

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt3
- updated to fedora

* Sat Jan 26 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2
- Fix libcollation and libacl plugin packaging (Bug #14173)

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1
- Fedora-DS 1.1 Final release
- Resolves bug 193724: "nested" filtered roles result in deadlock
- Resolves bug 367671: verify-db.pl : can't find dbverify
- Resolves bug 339041: migration : encryption key entries missing when source is 6.21
- Resolves bug 345711: migration : ignore idl switch value in 6.21 and earlier
- Resolves bug 197997: PTA config parsing broken
- Resolves bug 383141: listenhost: hostname associated with multiple addresses
- Resolves bug 388021: MMR breaks from master that has been reinited
- Resolves bug 371771: '.' (dot) in the server ID
- Resolves bug 345671: clu test failures
- Resolves bug 371751: verify-db.pl : can't find dbverify
- Resolves bug 238649: Hide nsslapd-db-transaction
- Resolves bug 316281: db2bak fails if the archive path exists and ends with '/'
- Resolves bug 237040: Remove obsolete makefiles
- Resolves bug 229576: clean up template-scriptname which is derived from template-scriptname.in
- Resolves bug 403351: LongDuration: Error log Rotation test suite causes slapd hang
- Resolves bug 231093: db2bak: crash bug
- Resolves bug 174776: Multiple restores from a non-existant directory could wipe out database
- Resolves bug 403751: command line scripts fine tuning
- Resolves bug 400421: unable to restart configDS via console
- Resolves bug 424381: migrate-ds-admin.pl script - not working
- Resolves bug 425861: Instance creation through console is broken
- Resolves bug 425849: migrate-ds-admin.pl spins at 100 cpu
- Resolves bug 297221: rhds71 Malformed Dynamic Authorization Group makes Directory Server Crash

* Tue Oct 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071030
- CVS snapshot 20071030
- Resolves bug 305121: Server hangs when adding a group with two password entries
- Resolves bug 325281: Install SNMP subagent mibs.
- Resolves bug 244475: crash at startup with new ldap sdk on 64-bit platform
- migration starts instances now
- Clean up setup dialog text
- removed obsolete schema
- Resolves bug 288291: add an view object inside a view object that has an improper nsviewfilter crashes the server
- Resolves bug 238630: Remove changelog db file when replica config is removed.
- Resolves bug 193724: "nested" filtered roles result in deadlock
- Resolves bug 330121: uuid generator truncates clock_seq_hi_and_reserved field
- Resolves bug 328741: Ensure that we NULL terminate strings properly when processing config file settings.
- Resolves bug 327091: Migration/Upgrade fails when it's from 6.21 to 8.0 on the same OS/architecture
- Resolves bug 335081: Don't add mailGroup objectclass when sync'ing new group entries from AD.
- Resolves bug 185602: Netscape Console allows instance directory to be set as change log
- Resolves bug 219587: Fixed small non-recurring memory leak at startup.
- Resolves bug 333291: Do not allow direct migration if the source db index has old IDL format
- Resolves bug 250179: tmpwatch whacks stats
- Resolves bug 338611: Sleep longer when waiting for ldap-agent to start.
- Resolves bug 336871: Look for infadd data files in TEMPLATEDIR.
- Resolves bug 232910: ACI targetattr list parser is whitespace sensitive
- Resolves bug 297221: rhds71 Malformed Dynamic Authorization Group makes Directory Server Crash
- Resolves bug 336871: infadd tool won't start. Fails to load data file
- Resolves bug 338991: obsolete values migrated to target instance
- Resolves bug 339041: migration : encryption key entries missing when source is 6.21
- Resolves bug 336881: qualify warning message when cert8.db is missing

* Mon Oct 29 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071008.1
- Rebuild with new ICU

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071008
- CVS snapshot 20071008

* Mon May 28 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20070528
- Git clone, upstream update

* Thu Mar 22 2007 Stanislav Ievlev <inger@altlinux.org> 1.1.0-alt0.20070322
- Initial release

* Wed Mar  1 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.2-1
- Added admserv-conf-tmpl.patch and admserv-conf-admpw.patch to fix the use of admpw for basic auth

* Wed Feb 22 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.2-1
- Add patch to fix admin server httpd module load order; you
- must now run setup after an upgrade; copy in the new 00core.ldif
- schema file to the server instances

* Tue Dec  6 2005 Rich Megginson <rmeggins@redhat.com> - 1.0.1-1
- Use nosp version instead of gen version to get patch version numbers
- Patch the admin server in the post install section
- Remove the unnecessary log files after setup so they aren't packaged

* Wed Nov 09 2005 Nathan Kinder <nkinder@redhat.com> 7.1-2
- Changed cyrus-sasl dependency to >= 2.1.15 for RHEL3 compatibility

* Fri Nov 04 2005 Noriko Hosoi <nhosoi@redhat.com> 7.1-2
- Added a dependency: cyrus-sasl >= 2.1.19

* Wed Sep 14 2005 Nathan Kinder <nkinder@redhat.com> 7.1-2
- Added a dependency on the java-1.4.2-ibm package

* Tue May 10 2005 Richard Megginson <rmeggins@redhat.com> 7.1-2
- Change release to 2

* Fri Apr  8 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- check for last version removal in preun

* Tue Apr  5 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- make rpm name .flavor.rpm - flavor must be defined in rpmbuild

* Tue Apr  5 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- Removed all of the setup and build stuff - just use the regular DS build process for that

* Tue Apr  5 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- use platform specific packaging directory; add preun to do uninstall

* Fri Apr  1 2005 Rich Megginson <rmeggins@redhat.com> 7.1-1
- use setup -q to suppress tar output

* Tue Mar 29 2005 Richard Megginson <rmeggins@redhat.com> 7.1-1
- use INTERNAL_BUILD=1 for internal builds - change rev to 1

* Tue Mar  8 2005 Richard Megginson <rmeggins@redhat.com> 7.1-0
- use ${prefix} instead of /opt/ldapserver - prefix is defined as /opt/%{name}

* Thu Jan 20 2005 Richard Megginson <rmeggins@redhat.com>
- Initial build.
