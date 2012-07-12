%define abiversion 26
%define _name net-snmp
%def_disable mibs
%def_with mysql
# XXX tests fail
%def_without test

Name: %_name%abiversion
Version: 5.6.1.1
Release: alt5.2

Summary: Tools and servers for the SNMP protocol
License: BSD-like
Group: System/Servers
Url: http://net-snmp.sourceforge.net
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source0: http://prdownloads.sourceforge.net/net-snmp/net-snmp-%version.tar

Patch: %name-%version-%release.patch
Patch1: %name-5.6.1.1-alt-DSO.patch

%define persistentdir %_localstatedir/%_name

%def_enable static
BuildPreReq: librpm-devel >= 4.0.4 libssl-devel
# Automatically added by buildreq on Wed Oct 13 2010
BuildRequires: libnl-devel librpm-devel libsensors3-devel libwrap-devel pdksh perl-devel python-module-setuptools perl-Tk perl-Term-ReadLine-Gnu perl-libnet perl-XML-Simple
%{?_enable_static:BuildPreReq: glibc-devel-static}
%{?_with_mysql:BuildRequires: libmysqlclient-devel}
BuildRequires: perl-podlators


%package -n lib%name
Summary: The shared libraries for the Net-SNMP project
Group: System/Libraries
Provides: lib%_name = %version-%release

%package -n lib%name-snmptrapd
Summary: The shared libraries for the Net-SNMP project
Group: System/Libraries
Provides: lib%_name-snmptrapd = %version-%release

%package -n libucd-snmp%abiversion
Summary: The shared libraries for the UCD-SNMP project
Group: System/Libraries
Provides: libucd-snmp = %version-%release

%description
SNMP (Simple Network Management Protocol) is a protocol used for network
management (hence the name).  The Net-SNMP project includes various SNMP
tools; an extensible agent, an SNMP library, tools for requesting or
setting information from SNMP agents, tools for generating and handling
SNMP traps, a version of the netstat command which uses SNMP, and a
Tk/Perl mib browser.  This package contains the snmpd and snmptrapd
daemons, documentation, etc.

Install the %_name package if you need network management tools.
You will probably also want to install the %_name-utils package, which
contains Net-SNMP utilities.

%description -n lib%name
The lib%_name package contains the shared libraries required for
Net-SNMP software.

%description -n lib%name-snmptrapd
The lib%name-snmptrapd package contains the shared libraries required for
Net-SNMP software.

%description -n libucd-snmp%abiversion
The libucd-snmp package contains the shared libraries required for
UCD-SNMP software.

%prep
%setup -q -n %_name-%version
%patch -p1
%patch1 -p0

%__subst "s|LIB_LD_LIBS)|LIB_LD_LIBS) \$\{ADD_HELPER\}|g" agent/Makefile.in
#Fix for compile with lmsensors_v3
%__subst "s|lmsensors_v2|lmsensors_v3|g" agent/mibgroup/hardware/sensors.h
#Fix flnk with mysql
sed -i '/LLIBTRAPD_OBJS/s/USELIBS)/USELIBS) \$(MYSQL_LIBS)/' apps/Makefile.in
#Fix install python
sed -i '/(PYMAKE) install/s/\$dir/\$dir --root \$(DESTDIR)/' Makefile.in
#Fix https://sourceforge.net/tracker/?func=detail&aid=3295407&group_id=12694&atid=112694
sed -i 's/PyInt_AsVoidPtr/PyLong_AsVoidPtr/' python/netsnmp/client_intf.c


%build

%autoreconf
#export NETSNMP_DONT_CHECK_VERSION=1
%configure %{subst_enable static} \
	--with-defaults \
	--enable-shared \
	--with-sys-location="Just west of Mars" \
	--with-sys-contact="root@localhost" \
	--with-logfile="/var/log/snmpd.log" \
	--with-mib-modules="mibII snmpv3mibs ucd_snmp agent_mibs notification target utilities disman/event disman/schedule host ucd-snmp/diskio ucd-snmp/lmsensorsMib tunnel misc/ipfwacc etherlike-mib" \
	--with-mibdirs="%_datadir/snmp/mibs:%_datadir/mibs/net-snmp:%_datadir/mibs/iana:%_datadir/mibs/ietf:%_datadir/mibs/tubs:%_datadir/mibs/cisco:%_datadir/pibs/ietf:%_datadir/pibs/tubs:" \
	--with-persistent-directory="%persistentdir" \
	--without-root-access \
	--without-rpm \
	--enable-ucd-snmp-compatibility \
	--enable-mfd-rewrites \
	--with-default-snmp-version="2" \
	--with-libwrap \
	--with-openssl \
	--with-zlib \
	--with-nl \
	--with-security-modules=tsm --with-transports="DTLSUDP TLSTCP" \
	--enable-as-needed \
	--with-perl-modules="INSTALLDIRS=vendor" \
	--enable-embedded-perl \
	--with-python-modules \
	%{subst_with mysql}

NPROCS=1
%make_build
rm -f `find ./ -name 'libnetsnmpagent*'`
%make ADD_HELPER="-L$PWD/agent/helpers/.libs -lnetsnmphelpers"


%install
%make DESTDIR=%buildroot install

rm -fR %buildroot%perl_vendor_autolib

%check
echo "===== start test ====="
%make test

%files -n lib%name
%_libdir/libnetsnmp.so.*
%_libdir/libnetsnmpagent.so.*
%_libdir/libnetsnmphelpers.so.*
%_libdir/libnetsnmpmibs.so.*

%files -n lib%name-snmptrapd
%_libdir/libnetsnmptrapd.so.*

%files -n libucd-snmp%abiversion
%_libdir/libsnmp.so.*

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1.1-alt5.2
- Fixed build

* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1.1-alt5.1
- Fixed build

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 5.6.1.1-alt5
- rebuilt for perl-5.14

* Sat Sep 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1.1-alt4
- Build compat libs

* Mon Jul 18 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1.1-alt3
- Remove noarch for net-snmp-config

* Sat Jul 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1.1-alt2
- Allocated libnetsnmptrapd.so.* to separate subpackage (ALT #25904)

* Sat Jul 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1.1-alt1
- 5.6.1.1 release
- Add new subpackage net-snmp-config for fix (ALT #25904)

* Thu Apr 28 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1-alt2
- Update patches from V5-6-patches branch

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.6.1-alt1.1
- Rebuilt for debuginfo

* Fri Jan 21 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6.1-alt1
- 5.6.1 release
- Update patches from V5-6-patches branch
- Add Requires: perl-SNMP in %_name-utils (ALT #24402)

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 5.6-alt5.1
- rebuilt with perl 5.12

* Tue Nov 09 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt5
- Add Requires: %_name-common in lib%_name-devel

* Tue Nov 09 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt4
- Set BuildArch: noarch for net-snmp net-snmp-bridge-mib net-snmp-cert net-snmp-utils

* Sat Nov 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt3
- Update patches from V5-6-patches branch. Fix (ALT #24493)
- Separate snmpd and snmptrapd in separate subpackage
- Add new subpackage net-snmp-clients and net-snmp-common net-snmp-bridge-mib net-snmp-cert
- Make net-snmp virtual package for quick install
- Disable smux (obsolete?)

* Sat Oct 30 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt2
- Update patches from V5-6-patches branch
- Add %_sysconfdir/sysconfig/snmpd (ALT #24402)
- Update spec: Relocation of often used utilities in net-snmp
- Add --with-security-modules=tsm and --with-transports="DTLSUDP TLSTCP"
  For configuration read http://www.net-snmp.org/wiki/index.php/TUT:Using_TLS
- snmpd is again single-threaded

* Tue Oct 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.6-alt1
- 5.6 release
- Update patches from V5-6-patches branch
- Enable MYSQL Trap Logging
- Enable tests
- Build python-module

* Sat Sep 18 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5-alt4
- Update patches from V5-5-patches branch
- Add mibs tunnel misc/ipfwacc etherlike-mib
- tar %_datadir/snmp/mibs/* for simple update snmp-mibs

* Thu Mar 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5-alt3
- Use svn upstream
- Apply patches from V5-5-patches branch
- Add to Requires snmp-mibs
- Set --with-mibdirs=...
- Fix preinstall section
- Delete .txt from name of mibs
- Disable build net-snmp-mibs

* Sat Feb 13 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5-alt2
- Fix repocop tests

* Wed Dec 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 5.5-alt1
- 5.5 release
- Update spec
- Apply net-snmp-proxy.patch and net-snmp-trunk-2.patch
- Enable ucd-snmp/diskio and ucd-snmp/lmsensorsMib
- Rename subpackage according to SharedLibsPolicy

* Sat Nov 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.2.1-alt4
- Fixed unsafe-tmp-usage-in-scripts, rpm-obsolete-self, big-changelog,
  big-changelog and repocop warnings

* Tue Jul 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.2.1-alt3
- Linked libnetsnmpagent with libnetsnmphelpers

* Fri May 22 2009 Pavlov Konstantin <thresh@altlinux.ru> 5.4.2.1-alt2
- Fix #19780: CVE-2008-6123.
- Dropped obsolete post_* macros.

* Mon Nov 10 2008 Pavlov Konstantin <thresh@altlinux.ru> 5.4.2.1-alt1
- 5.4.2.1 release (fixes CVE-2008-4309).

* Tue Sep 23 2008 Pavlov Konstantin <thresh@altlinux.ru> 5.4.2-alt1
- 5.4.2 release.
- Enable static library build.

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1.2-alt1
- 5.4.1.2 release.

* Mon Jun 16 2008 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1.1-alt1
- 5.4.1.1 security bugfix release.
- Fix CVE-2008-0960.
- Fix #13126.

* Fri Dec 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1-alt2
- Enable smux module build.
- Force autoconf version to 2.5.

* Wed Aug 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1-alt1
- 5.4.1 release.

* Tue Jul 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1-alt0.rc1
- 5.4.1 release candidate 1.

* Wed May 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4.1-alt0.pre1
- 5.4.1 prerelease 1.

* Tue Jan 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4-alt3
- Removed ipf-mod.pl from utils subpackage (as it isnt needed anyway).

* Tue Jan 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 5.4-alt2
- Added snmptrapd init-script (fixes #10672).
- Spec cleanup.
- Package tkmib into utils subpackage.

* Sun Dec 10 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.4-alt1
- 5.4 release.
- Really fixed 7664.
- Patches merged into source tree.
- Some minor spec cleanup.
- Funnier default sys location.

* Thu Sep 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.3.1-alt2
- Fixed #7664.
- Fixed #5757.

* Mon Jul 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.3.1-alt1
- 5.3.1 release.
- Added a patch to deal with perl bindings version problem (thx at@).

* Tue Jun 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.3.1-alt0.pre3
- 5.3.1.pre3.
- Reworked patch1, patch4, patch7 for current version.
- Synced with FC 5.3.1.pre3-1.
- Fix -ass-needed problem by damir@.

* Mon Mar 27 2006 Pavlov Konstantin <thresh@altlinux.ru> 5.2.2-alt2.EX
- Enabling mfd rewrites.

* Thu Feb 02 2006 Anton Farygin <rider@altlinux.ru> 5.2.2-alt1.1
- NMU: fix build for x86_64:
    - disabled patch2
    - fixed patch7 (snmptrapd.la added to libtool objects)

* Thu Dec 01 2005 Konstantin Timoshenko <kt@altlinux.ru> 5.2.2-alt1
- 5.2.2

* Mon May 30 2005 Konstantin Timoshenko <kt@altlinux.ru> 5.2.1-alt1
- 5.2.1

* Tue Dec 14 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.2-alt1
- 5.2
- Moved mib files to net-snmp-mibs subpackage.
- fix #5518, #5534, #5617

* Fri Nov 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 5.1.2-alt2.1
- Removed libelf-devel from build dependencies.

* Wed Oct 20 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1.2-alt2
- fixed bug #0005367

* Thu Aug 26 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1.2-alt1
- 5.1.2
- Move %_bindir/net-snmp-config to lib%name-devel (closes: #5068) Sir Raorn <raorn@altlinux.ru>

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 5.1.1-alt1.1
- Rebuilt with openssl-0.9.7d.

* Wed Apr 21 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1.1-alt1
- 5.1.1

* Wed Mar 03 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1-alt3
- rebuild with libdb4.2

* Wed Feb 18 2004 Konstantin Timoshenko <kt@altlinux.ru> 5.1-alt2
- fix init script
- add in group proc

* Tue Dec 30 2003 Konstantin Timoshenko <kt@altlinux.ru> 5.1-alt1
- 5.1

* Tue Dec 16 2003 Alexey Tourbin <at@altlinux.ru> 5.0.9-alt2
- perl-SNMP package built
- lib{net,ucd}-snmp-devel-static not packaged by default
- additional spec conventions enforcement

* Wed Oct 22 2003 Konstantin Timoshenko <kt@altlinux.ru> 5.0.9-alt1
- 5.0.9

* Mon Jan 20 2003 Rider <rider@altlinux.ru> 4.2.3-alt8
- fixed bug #0001668 (snmpd MUST HAVE rw access to /var/lib/ucd-snmp)

* Wed Dec 04 2002 AEN <aen@altlinux.ru> 4.2.3-alt7
- rebuilt with gcc-3.2

* Wed Aug 21 2002 Alexander Bokovoy <ab@altlinux.ru> 4.2.3-alt6
- Fix disk option problem again

* Tue Jul 30 2002 Alexander Bokovoy <ab@altlinux.ru> 4.2.3-alt5
- Fix disk option problem (see below)
- http://sourceforge.net/tracker/?group_id=12694&atid=112694&func=detail&aid=498809

* Thu Apr 18 2002 Alexander Bokovoy <ab@altlinux.ru> 4.2.3-alt4
- Fix includes

* Wed Mar 27 2002 Dmitry V. Levin <ldv@alt-linux.org> 4.2.3-alt3
- Added librpm-4.0.4 build support.
- Built with librpm-4.0.4, updated buildrequires.

* Thu Mar 14 2002 Rider <rider@altlinux.ru> 4.2.3-alt2
- requires fix

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 4.2.3-alt1
- 4.2.3
- add RH patches

* Fri Nov 09 2001 Dmitry V. Levin <ldv@alt-linux.org> 4.2.1-alt4
- Built without librpm support.

* Fri Aug 24 2001 Rider <rider@altlinux.ru> 4.2.1-alt3
- added security patches from Caldera

* Fri Aug 17 2001 Rider <rider@altlinux.ru> 4.2.1-alt2
- default config file changed
- ifdef path from SuSE
- snmpd new started over snmp user

* Mon Jun 04 2001 Alexander Bokovoy <ab@altlinux.ru> 4.2.1-alt1
- 4.2.1
- Installation fixed for broken libtool usage
- Null patch from RH applied
- BuildRequires cleaned

* Thu May 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.2-ipl2mdk
- Added patch so that only four bytes are returned for IP addresses on ia64 (rh #32244).
- Added patch to correcly handle a NULL value (rh #35016).
- Moved static libraries to devel-static subpackage.
- Fixed libraries, binaries and manpages packaging.

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 4.2-ipl1mdk
- 4.2
- Merged RH patches.
- Libification.
- RE adaptions.

* Wed Nov 22 2000 Vincent Saugey <vince@mandrakesoft.com> 4.1.2-5mdk
- Move include in correct dir

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.1.2-4mdk
- automatically added BuildRequires

* Wed Aug  2 2000 Vincent Saugey <vince@mandrakesoft.com> 4.1.2-3mdk
- Corrected a dependencie

* Fri Jul 28 2000 Vincent Saugey <vince@mandrakesoft.com> 4.1.2-2mdk
- Macro, BM

* Mon Jun 12 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 4.1.2-1mdk
- updated to 4.1.2
- removed ucd-snmp-man.patch, has been fixed with 4.1.2

* Tue Jun  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.1.1-6mdk
- Remove crappy perl-PDL dependences.

* Thu May 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.1.1-5mdk
- libtoolizifications.

* Wed Apr 12 2000 Vincent Saugey <vince@mandrakesoft.com> 4.1.1-4mdk
- Correct ldconfig in postun

* Sat Mar 25 2000 Vincent Saugey <vince@mandrakesoft.com> 4.1.1-3mdk
- many change in config snmpd file

* Thu Mar 23 2000 Vincent Saugey <vince@mandrakesoft.com> 4.1.1-2mdk
- Remove tkmib
- Patch for broken link in man page

* Thu Mar 21 2000 Vincent Saugey <vince@mandrakesoft.com> 4.1.1-1mdk
- Update to 4.1.1
- Modification in spec file
- corrected group

* Mon Jan 24 2000 Francis Galiegue <francis@mandrakesoft.com>
- Fixed spec file (%install tried to mkdir /var/ucd-snmp)

* Tue Nov 30 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- --with-libwrap, not --with-libwrap="-lwrap -lnsl" (rh on crack)
- bump spec to 3mdk to get above Chmouel

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- SMP check/build
- 4.0.1 + redhat patches

* Sat Jul 17 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 3.6.2

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Thu Apr  8 1999 Wes Hardaker <wjhardaker@ucdavis.edu>
- fix Source0 location.
- fix the snmpd.conf file to use real community names.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 3.6.1, fix configuration file stuff.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- restore host resources mib
- simplified config file
- rebuild for 6.0.

* Tue Dec 22 1998 Bill Nottingham <notting@redhat.com>
- remove backup file to fix perl dependencies

* Tue Dec  8 1998 Jeff Johnson <jbj@redhat.com>
- add all relevant rpm scalars to host resources mib.

* Sun Dec  6 1998 Jeff Johnson <jbj@redhat.com>
- enable libwrap (#253)
- enable host module (rpm queries over SNMP!).

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Fri Oct  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.5.3.
- don't include snmpcheck until perl-SNMP is packaged.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- ucd-snmpd.init: start daemon w/o -f.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- don't start snmpd unless requested
- start snmpd after pcmcia.

* Sun Jun 21 1998 Jeff Johnson <jbj@redhat.com>
- all but config (especially SNMPv2p) ready for prime time

* Sat Jun 20 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.5.

* Tue Dec 30 1997 Otto Hammersmith <otto@redhat.com>
- created the package... possibly replace cmu-snmp with this.

