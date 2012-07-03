Name: openais
Summary: The openais Standards-Based Cluster Framework executive and APIs
Version: 1.1.4
Release: alt1
License: BSD
Group: System/Base
Url: http://developer.osdl.org/dev/%name/
Source0: http://devresources.linuxfoundation.org/dev/%name/downloads/%name-%version/%name-%version.tar.gz
Patch0: openais-1.1.4-alt1-fix-lcrso-linking.patch

# Setup/build bits
BuildRequires: libcorosync-devel >= 1.0.0
BuildRequires: autoconf automake

%description
This package contains the openais service handlers, default configuration
files and init script.

%package -n libopenais
Summary: The openais Standards-Based Cluster Framework libraries
Group: System/Libraries
Requires: %name = %version-%release

%description -n libopenais
This package contains openais libraries.

%package -n libopenais-devel
Summary: The openais Standards-Based Cluster Framework libraries
Group: Development/C

%description -n libopenais-devel
This package contains the include files used to develop using openais APIs.

%prep
%setup -n %name-%version
%patch0 -p2

%build
./autogen.sh

%configure \
	--with-initddir=%_initddir

%make

%install
make install DESTDIR=%buildroot

## tree fixup
# drop static libs
rm -f %buildroot%_libdir/*.a
# drop docs and html docs for now
rm -rf %buildroot%_docdir/*

%post
%post_service openais

%preun
%preun_service openais

%files
%doc LICENSE README.amf
%dir %_sysconfdir/corosync
%config(noreplace) %_sysconfdir/corosync/amf.conf.example
%_initdir/openais
%dir %_libexecdir/lcrso
%_libexecdir/lcrso/openaisserviceenable.lcrso
%_libexecdir/lcrso/service_amf.lcrso
%_libexecdir/lcrso/service_ckpt.lcrso
%_libexecdir/lcrso/service_clm.lcrso
%_libexecdir/lcrso/service_evt.lcrso
%_libexecdir/lcrso/service_lck.lcrso
%_libexecdir/lcrso/service_msg.lcrso
%_libexecdir/lcrso/service_tmr.lcrso
%_mandir/man8/openais_overview.8*
%_mandir/man5/openais.conf.5*
%_mandir/man5/amf.conf.5*
%_sbindir/aisexec
%_sbindir/openais-instantiate

%files -n libopenais
%_libdir/libSaAmf.so.*
%_libdir/libSaCkpt.so.*
%_libdir/libSaClm.so.*
%_libdir/libSaEvt.so.*
%_libdir/libSaLck.so.*
%_libdir/libSaMsg.so.*
%_libdir/libSaTmr.so.*

%files -n libopenais-devel
%dir %_includedir/openais/
%_includedir/openais/saAis.h
%_includedir/openais/saAmf.h
%_includedir/openais/saCkpt.h
%_includedir/openais/saClm.h
%_includedir/openais/saEvt.h
%_includedir/openais/saLck.h
%_includedir/openais/saMsg.h
%_includedir/openais/saTmr.h
%_libdir/libSaAmf.so
%_libdir/libSaCkpt.so
%_libdir/libSaClm.so
%_libdir/libSaEvt.so
%_libdir/libSaLck.so
%_libdir/libSaMsg.so
%_libdir/libSaTmr.so
%_libdir/pkgconfig/*.pc

%changelog
* Thu Sep 22 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.4-alt1
- 1.1.4

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.80.5-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libopenais
  * postun_ldconfig for libopenais
  * postclean-05-filetriggers for spec file

* Tue Jun 02 2009 Michail Yakushin <silicium@altlinux.ru> 0.80.5-alt2
- fix build with new compiler 

* Tue Feb 17 2009 Michail Yakushin <silicium@altlinux.ru> 0.80.5-alt1
- update to 0.80.5 

* Sun Mar 23 2008 Nick S. Grechukh <gns@altlinux.org> 0.80.3-alt5
- initscript rewritten. lcrso path fixed

* Sun Mar 23 2008 Nick S. Grechukh <gns@altlinux.org> 0.80.3-alt2
- new version. spec reworked

* Thu Apr 26 2007 Michail Yakushin <silicium@altlinux.ru> 0.80.2-alt1
- build for alt 

* Mon Dec 18 2006 Steven Dake <sdake@redhat.com> - 0.80.2-1
- Resolves: rhbz#211357
- This is the rhel5 version of 0.80.2-0.

* Mon Dec 18 2006 Steven Dake <sdake@redhat.com> - 0.80.2-0
- Resolves: rhbz#211357
- New upstream version including all prevision revisions.
- Fixes cpg ordering problem.
- Fixes ia64 unaligned problem.
- This is the fc6 version.

* Tue Dec 5 2006 Steven Dake <sdake@redhat.com> - 0.80.1-22
- Resolves: rhbz#216492
- This is the rhel5 version of 0.80.1-21.

* Tue Dec 5 2006 Steven Dake <sdake@redhat.com> - 0.80.1-21
- Resolves: rhbz#216492
- Add upstream revision 1319 - Increase outbound buffer size to 5000 messages.
- Add upstream revision 1316 - Improvements on segfault logging.
- This is the fc6 version.

* Wed Nov 29 2006 Steven Dake <sdake@redhat.com> - 0.80.1-20
- Resolves: rhbz#216492
- Need new res line to commit.  This is the same as 0.80.1-18.

* Wed Nov 29 2006 Steven Dake <sdake@redhat.com> - 0.80.1-19
- This is the rhel5 version of 0.80.1-18.

* Wed Nov 29 2006 Steven Dake <sdake@redhat.com> - 0.80.1-18
- Add upstream revision 1315 - Fix compile error in libcpg.
- Add upstream revision 1314 - Change rundir to /var/openais.
- Add upstream revision 1313 - Flow control fixes for the CPG service.
- Add upstream revision 1312 - Correct usage of ERR_LIBRARY to SA_AIS_ERR_LIBRARY.
- Add upstream revision 1311 - handle case where POLLHUP and POLLERR are not uspported by OS.
- Add upstream revision 1309 - set default downcheck value to 1000ms.
- Add upstream revision 1308 - Remove invalid code and warnings detected by Intel compiler.
- This is the fc6 version.

* Tue Nov 14 2006 Steven Dake <sdake@redhat.com> - 0.80.1-17
- This is the rhel5 version of 0.80.1-16.

* Tue Nov 14 2006 Steven Dake <sdake@redhat.com> - 0.80.1-16
- Add upstream revision 1307 - Remove flow control compile warning.
- Add upstream revision 1306 - Make clean now really makes clean.
- Add upstream revision 1305 - Set scheduler SCHED_RR to max priority available
  in system.
- Add upstream revision 1300 - Improve behavior of flow control of CPG service
  during configuration changes.
- This is the fc6 version.

* Thu Nov 9 2006 Steven Dake <sdake@redhat.com> - 0.80.1-15
- This is the rhel5 version of 0.80.1-14

* Thu Nov 9 2006 Steven Dake <sdake@redhat.com> - 0.80.1-14
- Add upstream revision 1296 - Remove compile warnings.
- Add upstream revision 1295 - The totem membership protocol was changed to
- Add upstream revision 1294 - modify location of ringid file to
- Add upstream revision 1293 - flush output of debug messages on exit or segv.
  /var/run/openais and chdir here so cores are saved there.
  match specifications.
- This is the fc6 version.

* Fri Nov 3 2006 Steven Dake <sdake@redhat.com> - 0.80.1-13
- Add upstream revision 1286 - Fix checkpoint unlink operation under certain
  conditions.  This is the rhel5 version.

* Fri Nov 3 2006 Steven Dake <sdake@redhat.com> - 0.80.1-12
- Add upstream revision 1286 - Fix checkpoint unlink operation under certain
  conditions.  This is the fc6 version.

* Tue Oct 24 2006 Steven Dake <sdake@redhat.com> - 0.80.1-11
- Add upstream revision 1284 - Initialize variables for checkpoint sync.

* Tue Oct 24 2006 Steven Dake <sdake@redhat.com> - 0.80.1-10
- Add %{?dist} to release field.

* Tue Oct 24 2006 Steven Dake <sdake@redhat.com> - 0.80.1-9
- Add upstream revision 1270 - Resolve IPC segfault.
- Add upstream revision 1271 - Fix errors in ia64 alignment.
- Add upstream revision 1275 - pthread_mutex_destroy cleanup patch.
- Add upstream revision 1276 - Remove debug from makefile committed in revision 1275.
- Add upstream revision 1277 - Formatting changes.
- Add upstream revision 1278 - Patch testckpt to use proper seciton id size.
- Add upstream revision 1279 - Call abort in sync service when processing is interrupted.
- Add upstream revision 1282 - New generation checkpoint state machine.
- Add upstream revision 1283 - Fix memory leaks.

* Wed Oct 18 2006 Steven Dake <sdake@redhat.com> - 0.80.1-8
- Add upstream revision 1268 - Align data in totem delivery on 4 byte
  boundaries for ia64.
- Add upstream revision 1269 - Increase default stack size for IPC connections
  on ia64.

* Mon Oct 16 2006 Steven Dake <sdake@redhat.com> - 0.80.1-7
- Add upstream revision 1267 - rework of checkpoint synchronization.

* Thu Oct 12 2006 Steven Dake <sdake@redhat.com> - 0.80.1-6
- Add upstream revision 1260 - Allocate the retransmission token in
  instance initialize instead of totemsrp_initialize.
- Add upstream revision 1261 - cleanup the way the memb_index variable is
  handled in the commit token.
- Add upstream revision 1262 - Set the ring sequence number according to the
  totem specifications.
- Add upstream revision 1263 - Use the fullset variable instead of he local
  variable j to make easier code reading.
- Add upstream revision 1264 - If the failed_list has zero entries, don't
  add it as an iovector in the join messages.
- Add upstream revision 1265 - Only originate one regular token.

* Mon Oct 9 2006 Steven Dake <sdake@redhat.com> - 0.80.1-5
- Add upstream revision 1256 - remove extra totem debug logging output.
- Add upstream revision 1257 - fix subset operation to repair membership behavior.
- Add upstream revision 1258 - accept commit token in proper circumstances.

* Wed Oct 4 2006 Steven Dake <sdake@redhat.com> - 0.80.1-4
- Add upstream revision 1252 - display members that have left in system log properly.

* Thu Sep 28 2006 Steven Dake <sdake@redhat.com> - 0.80.1-3
- Add upstream revision 1248 - fix more intermittent failures with flow control
  system.

* Wed Sep 27 2006 Steven Dake <sdake@redhat.com> - 0.80.1-2
- Add upstream revision 1246 - fix intermittent failures with flow control
  system.

* Mon Sep 25 2006 Steven Dake <sdake@redhat.com> - 0.80.1-1.1
- Add upstream revision 1223 - Fix checkpoint write size of zero to
  return INVALID_PARAM error code.
- Add upstream revision 1230 - Add missing include for assert.h.
- Add upstream revision 1245 - Add cpgbench tool and better flow control system.
- Move /sbin/ldconfig into regular package from devel package.

* Tue Aug 15 2006 Steven Dake <sdake@redhat.com> - 0.80.1-1.0
- New stable upstream release

* Thu Aug 10 2006 Steven Dake <sdake@redhat.com> - 0.80-1.2
- Move libraries to openais package.
- Add cpg hash collision patch.
- Add makefile install clm patch.

* Tue Aug 8 2006 Steven Dake <sdake@redhat.com> - 0.80-1.1
- New process of tracking any revisions in the upstream stable branch.

* Sun Jul 23 2006 Steven Dake <sdake@redhat.com> - 0.80-1.0
- New upstream release.
- Added openais-cfgtool tool to install.
- Added openais/cfg.h header file.

* Mon Jul 17 2006 Steven Dake <sdake@redhat.com> - 0.79-1.0
- New upstream release.

* Mon Jul 10 2006 Steven Dake <sdake@redhat.com> - 0.78-1.2
- Allow build on s390 and s390x.

* Fri Jul 07 2006 Steven Dake <sdake@redhat.com> - 0.78-1.1
- Allow build on ia64.

* Thu Jul 06 2006 Steven Dake <sdake@redhat.com> - 0.78-1.0
- New upstream release.

* Wed Jun 21 2006 Steven Dake <sdake@redhat.com> - 0.77-1.0
- New upstream release.

* Tue Jun 13 2006 Steven Dake <sdake@redhat.com> - 0.76-1.8
- Readded ExlcusiveArch since build system builds s390 and ia64 which are
  untested.
- Add makefile override patch which fixes build with optflags on x86_64 arch.
- Remove -DOPENAIS_LINUX from passed CFLAGS since it now works properly with
  makefile override patch.

* Tue Jun 13 2006 Steven Dake <sdake@redhat.com> - 0.76-1.7
- Remove ExclusiveArch since all Fedora Core 6 arches have been tested.

* Fri Jun 9 2006 Steven Dake <sdake@redhat.com> - 0.76-1.6
- Move condrestart to %%postun instead of %%post.
- Call initscript directly as suggested by Jesse.

* Thu Jun 8 2006 Steven Dake <sdake@redhat.com> - 0.76-1.5
- Changed BuildRoot tag to match convention specified in Fedora Wiki.
- Removed /sbin/service dependency since it is pulled in from init packages.

* Mon Jun 5 2006 Steven Dake <sdake@redhat.com> - 0.76-1.4
- Moved uid 102 to 39 since uids over 99 are not suitable for core at Bill's
  suggestion.

* Mon Jun 5 2006 Steven Dake <sdake@redhat.com> - 0.76-1.3
- Allocated uid 102 from setup package for user add operation.
- Added || : to initscript stuff so initscript bugs dont cause RPM transaction
  failures as per Paul's suggestion.
- Added /sbin/services to post requires as per Paul's suggestion.
- Removed ldconfig from the requires post for the main package as per Paul's
  suggestion.
- Changed post devel scriptlet action as per Paul's suggestion.

* Thu May 31 2006 Steven Dake <sdake@redhat.com> - 0.76-1.2
- Add user account for AIS applications and authentication.
- Move /etc/ld.so.conf/openais-*.conf to devel package since it is
  only needed there.
- Move ldconfig to devel package.
- Execute condrestart on upgrade

* Fri May 25 2006 Steven Dake <sdake@redhat.com> - 0.76-1.1
- Fix unowned dirs problem.
- Correct make with optflags work properly.
- Move plugins from /usr/lib/openais/lcrso to /usr/libexec/lcrso.
- Remove static archives from RPM.
- Name shared objects in devel package as 1.0.0 instead of 1.0.

* Thu May 24 2006 Steven Dake <sdake@redhat.com> - 0.76-1.0
- New release of openais 0.76.

* Wed May 23 2006 Paul Howarth <paul@city-fan.org> - 0.75-1.1
- Address rpmlint issues during package review (#192889)
- Move docs to associated packages, don't bother with -docs subpackage
- Make -devel package require main package
- Fix Source: and URL: tags
- Fix up Makefile to handle DESTDIR properly
- Honoring %%{optflags} breaks build!

* Wed May 20 2006 Steven Dake <sdake@redhat.com> - 0.75-1.0
- Initial import.
