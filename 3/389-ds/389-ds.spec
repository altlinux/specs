Summary: 389 Directory Server
Name: 389-ds
Version: 1.2.9.10
Release: alt1.1
License: GPLv2
Url: http://port389.org
Group: System/Servers
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Source: %name-%version-%release.tar
Source1: install.inf
Source3: setupssl2.sh

# Automatically added by buildreq on Thu May 05 2011
BuildRequires: 389-adminutil-devel gcc-c++ libdb4-devel libicu-devel libldap-devel libnet-snmp-devel libnl-devel libpam-devel libpcre-devel libsasl2-devel libsensors3-devel libsvrcore-devel perl-Mozilla-LDAP perl-libnet perl-bignum

Provides: fedora-ds = %version-%release
Obsoletes: fedora-ds < %version-%release

# AutoReq: yes, noperl
%add_perl_lib_path %_libdir/fedora-ds/perl
%add_findprov_skiplist %_datadir/fedora-ds/script-templates/*
%add_findreq_skiplist %_datadir/fedora-ds/script-templates/*

%description
389 Directory Server is an LDAPv3 compliant server. Use setup-ds.pl to setup instances.

%package devel
Summary: Development libraries for 389 Directory Server
Group: Development/C
Requires: %name = %version-%release

%description devel
Development Libraries and heades for 389 Directory Server.

%prep
%setup -n %name-%version
%autoreconf

cp %SOURCE1 install.inf

%build
./configure --prefix=/usr --exec-prefix=/usr --bindir=%_bindir --sbindir=%_sbindir --sysconfdir=%_sysconfdir \
 --datadir=%_datadir --includedir=%_includedir --libdir=%_libdir --libexecdir=%_libexecdir --localstatedir=/var \
 --sharedstatedir=/usr/com --mandir=/usr/share/man --infodir=/usr/share/info --with-openldap --with-selinux

export XCFLAGS=$RPM_OPT_FLAGS

#USE_ADMSERV to avoid strange get_mag_var unresolved symbol
echo "#define USE_ADMSERV 1" >>config.h

%ifarch x86_64 ppc64 ia64 s390x sparc64
export USE_64=1
%endif

%make_build

%install
%make DESTDIR="%buildroot" install

mkdir -p %buildroot%_logdir/fedora-ds
mkdir -p %buildroot%_localstatedir/fedora-ds
mkdir -p %buildroot%_lockdir/fedora-ds
mkdir -p %buildroot%_var/tmp/fedora-ds
mkdir -p %buildroot%_includedir/fedora-ds

install -p -m 644 ldap/servers/slapd/slapi-plugin.h %buildroot%_includedir/fedora-ds/
install -p -m 755 %SOURCE3 %buildroot%_datadir/fedora-ds/

# make sure perl scripts have a proper shebang
%__subst 's|#{{PERL-EXEC}}|#!%_bindir/perl|' %buildroot%_datadir/fedora-ds/script-templates/template-*.pl
%__subst 's|File::Spec->tmpdir|"/tmp"|' %buildroot%_libdir/fedora-ds/perl/DSCreate.pm

#move main libraries to common directory
mv %buildroot%_libdir/fedora-ds/*.so* %buildroot%_libdir/
find %buildroot%_libdir -name "*.la" -delete

%files
%doc README.ALT LICENSE EXCEPTION install.inf
%dir %_sysconfdir/fedora-ds
%dir %_sysconfdir/fedora-ds/schema
%config %_sysconfdir/fedora-ds/schema/*.ldif
%dir %_sysconfdir/fedora-ds/config
%config %_sysconfdir/fedora-ds/config/slapd-collations.conf
%config %_sysconfdir/fedora-ds/config/certmap.conf
%config %_sysconfdir/fedora-ds/config/ldap-agent.conf
%config %_sysconfdir/fedora-ds/config/template-initconfig
%config(noreplace) %_sysconfdir/sysconfig/fedora-ds
%_datadir/fedora-ds
%_bindir/*
%_sbindir/*
%dir	%_libdir/fedora-ds
%_libdir/*.so.*
%dir %_libdir/fedora-ds/perl
%_libdir/fedora-ds/perl/*.pm
%dir %_libdir/fedora-ds/plugins
%_libdir/fedora-ds/plugins/*.so*
%dir %_logdir/fedora-ds
%_initdir/*
%_man1dir/*.gz
%_man8dir/*.gz

%files devel
%doc LICENSE EXCEPTION
%_includedir/fedora-ds
%_libdir/*.so
%_pkgconfigdir/*.pc

%post
%post_service fedora-ds
%post_service fedora-ds-snmp

%preun
%preun_service fedora-ds
%preun_service fedora-ds-snmp

%changelog
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
