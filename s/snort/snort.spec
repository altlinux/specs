Name: snort
Version: 3.12.4.0
Release: alt1
Summary: Network intrusion detection and prevention system

License: GPL-2.0-only
Group: Security/Networking
URL: https://www.snort.org
# Source0-url: https://github.com/snort3/snort3/archive/refs/tags/%version.tar.gz
Source0: snort-%{version}.tar
Source1: snort.service
Source2: snort.sysusers
Source3: snort.logrotate

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: bison
BuildRequires: libdaq-devel >= 3.0.28
BuildRequires: libdnet-devel
BuildRequires: libpcap-devel
BuildRequires: libpcre2-devel
BuildRequires: libhwloc-devel
BuildRequires: libluajit-devel
BuildRequires: libssl-devel
BuildRequires: zlib-devel
BuildRequires: liblzma-devel
%ifarch x86_64
BuildRequires: libhyperscan-devel
%endif

Obsoletes: snort-inline <= 2.9.7.0-alt2
Obsoletes: snort-inline+flexresp <= 2.9.7.0-alt2
Obsoletes: snort-plain+flexresp < 3.12.4.0

%description
Snort is a lightweight network intrusion detection and prevention system.
It performs real-time traffic analysis, packet logging, protocol analysis,
content searching and matching.

%prep
%setup -q -n snort-%{version}

%build
%cmake \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -DENABLE_STATIC_DAQ=OFF \
    -DMAKE_DOC=OFF
%cmake_build

%install
%cmake_install

rm -rv %{buildroot}%{_includedir}/snort
rm -v %{buildroot}%{_libdir}/pkgconfig/snort.pc

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/snort.service
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/snort.conf
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/snort

install -d -m 0755 %{buildroot}%{_sysconfdir}/snort/rules
install -d -m 0755 %{buildroot}%{_sysconfdir}/snort/lists
install -pm 0644 lua/snort.lua lua/snort_defaults.lua lua/balanced.lua \
    lua/connectivity.lua lua/inline.lua lua/max_detect.lua lua/security.lua \
    lua/talos.lua lua/file_magic.rules lua/sensitive_data.rules \
    %{buildroot}%{_sysconfdir}/snort/
touch %{buildroot}%{_sysconfdir}/snort/rules/local.rules
touch %{buildroot}%{_sysconfdir}/snort/lists/default.allowlist
touch %{buildroot}%{_sysconfdir}/snort/lists/default.blocklist

%post
%post_service snort

%preun
%preun_service snort

%pre
%sysusers_create_package snort %{SOURCE2}

%files
%doc README.md ChangeLog.md
%{_bindir}/snort
%{_bindir}/snort2lua
%{_bindir}/u2boat
%{_bindir}/appid_detector_builder.sh
%{_bindir}/show_flows
%{_bindir}/u2spewfoo
%{_libdir}/snort/daq/daq_file.so
%{_libdir}/snort/daq/daq_hext.so
%{_docdir}/snort/README.show_flows
%{_docdir}/snort/README.u2boat
%{_sysconfdir}/snort/
%config(noreplace) %{_sysconfdir}/logrotate.d/snort
%{_unitdir}/snort.service
%{_sysusersdir}/snort.conf

%changelog
* Fri Oct 30 2026 Vitaly Lipatov <lav@altlinux.ru> 3.12.4.0-alt1
- new version 3.12.4.0 (Snort 3): CMake build with libdaq 3
- replace the Snort 2 service and configuration with Snort 3 Lua and systemd
- build with Hyperscan on x86_64 only (not available elsewhere)
- added BuildRequires: rpm-macros-cmake, rpm-build-cmake, gcc-c++, bison,
  liblzma-devel, libhwloc-devel, libhyperscan-devel, libpcre2-devel (Snort 3)
- removed BuildRequires: libnghttp2-devel, libpcre-devel, libtirpc-devel,
  rpm-build-licenses, rpm-macros-alternatives (not used by Snort 3)

* Mon Apr 19 2021 Slava Aseev <ptrnine@altlinux.org> 2.9.17.1-alt1
- update to 2.9.17.1
- apply libtirpc patch from gentoo

* Thu Feb 21 2019 Mikhail Efremov <sem@altlinux.org> 2.9.7.0-alt3
- Drop remnants of bloat subpackage from spec.
- README-ALT.ru.m4: Drop inline from doc.
- Drop inline subpackages.
- Drop obsoleted configure options.
- Fix some compiler warnings.
- Use _unpackaged_files_terminate_build.
- Don't use deprecated PreReq for alternatives.
- Fix build: add rpm-macros-alternatives to BR.
- Fix BR: use BuildRequires(pre) for rpm-build-licenses.

* Mon Dec 14 2015 Mikhail Efremov <sem@altlinux.org> 2.9.7.0-alt2
- Drop libnet from BR.

* Fri Dec 12 2014 Anton Farygin <rider@altlinux.ru> 2.9.7.0-alt1
- new version

* Mon Jun 23 2014 Timur Aitov <timonbl4@altlinux.org> 2.9.6.1-alt4
- disable all rules by default

* Wed Jun 04 2014 Timur Aitov <timonbl4@altlinux.org> 2.9.6.1-alt3
- change log directory

* Wed May 28 2014 Timur Aitov <timonbl4@altlinux.org> 2.9.6.1-alt2
- change attr /var/log/snort

* Tue May 27 2014 Timur Aitov <timonbl4@altlinux.org> 2.9.6.1-alt1
- 2.9.6.1
- use default memcap in snort.conf

* Mon Feb 18 2013 Timur Aitov <timonbl4@altlinux.org> 2.9.3.1-alt3
- set unified2 output by default

* Mon Jan 28 2013 Timur Aitov <timonbl4@altlinux.org> 2.9.3.1-alt2
- fix snort.conf

* Wed Jan 09 2013 Timur Aitov <timonbl4@altlinux.org> 2.9.3.1-alt1
- 2.9.3.1

* Tue Oct 05 2010 Mikhail Efremov <sem@altlinux.org> 2.8.6.1-alt3
- Really rebuild with libmysqlclient.so.16

* Sun Sep 19 2010 Mikhail Efremov <sem@altlinux.org> 2.8.6.1-alt2
- rebuild with libmysqlclient.so.16

* Tue Aug 03 2010 Mikhail Efremov <sem@altlinux.org> 2.8.6.1-alt1
- init script: fix service restart.
- 2.8.6.1
- package snort-dbhints and snort-doc as noarch.

* Mon May 31 2010 Mikhail Efremov <sem@altlinux.org> 2.8.6-alt1
- remove clamav support.
- 2.8.6

* Tue Mar 23 2010 Mikhail Efremov <sem@altlinux.org> 2.8.5.3-alt1
- 2.8.5.3

* Mon Jan 11 2010 Mikhail Efremov <sem@altlinux.org> 2.8.5.2-alt1
- 2.8.5.2

* Tue Nov 10 2009 Mikhail Efremov <sem@altlinux.org> 2.8.5.1-alt2
- drop obsolete configure option '--with-libpcap'.
- enable build with PostgreSQL support.
- disable build with libclamav.
- init script: always use '-D' option.
- fix alternatives files.

* Fri Oct 23 2009 Mikhail Efremov <sem@altlinux.org> 2.8.5.1-alt1
- start snort only for active interfaces.
- init script: display interface for snort.
- not start in chroot in any case.
- completely remove old alternatives.
- spec cleanup.
- removed SNMP support.
- 2.8.5.1 (closes: #11627)

* Sun Dec 14 2008 Ilya Mashkin <oddity@altlinux.ru> 2.4.5-alt4
- enable inline, fix #16686
- fix build with new glibc
- apply repocop patch (remove old alternatives), fix #17620
- remove "-Wl,--no-as-needed" from spec, fix #11147

* Mon Oct 13 2008 Ilya Mashkin <oddity@altlinux.ru> 2.4.5-alt3
- Rebuilt 
- Fixed x86_64 build, thanks to Sergey Y. Afonin
- Brand new version 2.8.3.1 will upload soon

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.5-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Fri Jun 23 2006 Ilya Evseev <evseev@altlinux.ru> 2.4.5-alt2
- fixup ia64 build: assign explicit path for OpenSSL libraries
- suppress warning on 'ghost' macro in comment

* Fri Jun 16 2006 Ilya Evseev <evseev@altlinux.ru> 2.4.5-alt1
- Updated to version 2.4.5 (of course, with SNMP patch renewed..)
- Prelude support is disabled by default because it's no more in Sisyphus
- Re-enable old libraries linking style,
  see http://wiki.sisyphus.ru/devel/UpStream/AsNeeded

* Thu Nov 10 2005 Ilya Evseev <evseev@altlinux.ru> 2.4.3-alt1
- Updated to version 2.4.3, revisite SNMP patch again..
- Replace manually created symlinks from %_sbindir/%name
  to actual snort binaries by modern alternatives
- Bugfix: create %name user/group before install stage, not after

* Tue Sep 20 2005 Ilya Evseev <evseev@altlinux.ru> 2.4.1-alt1
- Updated to version 2.4.1, revisited SNMP patch (#2)

* Mon Aug 15 2005 Ilya Evseev <evseev@altlinux.ru> 2.4.0-alt1
- Updated to version 2.4.0
- Rules and configuration directory skeleton are moved to separate package
  because they're distributed by upstream staff as independent tarball now,
  and updated more frequently than binary core.
- Patchset changes:
   + revisited patchset: SNMP(#2), ClamAV(#13), lib64(#14)
   + removed patch #1 for Prelude support because it is upstream part now!

* Mon Jun 02 2005 Ilya Evseev <evseev@altlinux.ru> 2.3.3-alt2
- changed PostgreSQL requirements: old = libpq3-devel, new = libpq-devel,
  added '--with libpq3' rpmbuild cmdline option for backward compatibility.
  Temporarily disabled because Sisyphus problems.
- small fixes taken from Mandrake Cooker 2.3.1-3mdk build: lib64, timestamp etc.
- use SNMP for sending alerts (mdk)
- use ClamAV for verifying traffic (mdk)
- use IPTables for verifying/managing traffic in addition to PCAP library (mdk)
- provide SQL script for describing flags/proto/services in snort database (mdk)

* Wed Apr 27 2005 Ilya Evseev <evseev@altlinux.ru> 2.3.3-alt1
- Updated to version 2.3.3
- Allow omit building selected targets via 'rpmbuild --without xxx'

* Sun Mar 13 2005 Ilya Evseev <evseev@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Thu Jan 27 2005 Ilya Evseev <evseev@altlinux.ru> 2.3.0-alt1
- 2.3.0
- revisioned prelude patch, use autoreconf instead of autogen.sh
- documentation is packaged separately (including 4MB of signatures descriptions)
- contrib package is obsoleted since upstream does not contain them anymore
- put rules to /etc/snort/rules instead of /etc/snort
- some generated configs are moved from specfile to separate m4-based templates
- specfile cleanups for better reading

* Fri Jan 14 2005 Ilya Evseev <evseev@altlinux.ru> 2.2.0-alt4
- prelude patch is updated to 0.3.6 for snort 2.2.0
- libltdl-devel is explicitly added to BuildPreReq for preventing rebuild failure

* Tue Sep  7 2004 Ilya Evseev <evseev@altlinux.ru> 2.2.0-alt3
- service script improvements:
   + global lockfile for correct shutdown
   + status routine checks per-process lockfiles using new service-0.5.6 feature
   + fixup is_loaded routine

* Sat Aug 28 2004 Ilya Evseev <evseev@altlinux.ru> 2.2.0-alt2
- fixed bug #1272: incorrect /var/log/snort ownership
- fixed bug #4771: snort daemon was not visible by snort service script
- service script is completely rewritten:
   + bugfix feature: when INTERFACES=any,
     all presented network interfaces are enumerated now
   + built-in default options for running daemon
     even sysconfig does not contain ADDPARAM_*
   + bugfix: condstop/condrestart was unusable
   + support virtual interfaces like eth0:1
- bugfix in logrotate: replace "restart" by "condreload"
- sysconfig description updated

* Wed Aug 25 2004 Ilya Evseev <evseev@altlinux.ru> 2.2.0-alt1
- New release
- added "Requires: service" for rejection install under pre-Master 2.4
- Prelude patch is upgraded to 0.3.5 for Snort 2.1.2
- removed separate Prelude README because Prelude patch already includes it.

* Fri Aug  6 2004 Ilya Evseev <evseev@altlinux.ru> 2.1.3-alt1
- New release
- separate Snort version and Prelude patch version because patch may be outdated.
- Prelude patch is upgraded to 0.3.0

* Fri May 14 2004 Serge A. Volkov <vserge@altlinux.ru> 2.1.0-alt2.2
- Add Buildreq: libunixODBC-devel
- Add Requires: libunixODBC for all snort-odbc* packages

* Thu May 13 2004 Serge A. Volkov <vserge@altlinux.ru> 2.1.0-alt2.1
- Rebuild with openssl-0.9.7d

* Fri Feb  6 2004 Serhii Hlodin <hlodin@altlinux.ru> 2.1.0-alt1
- New release
- Enable statistics reporting through proc by default
- Add unixODBC support to bloat package

* Tue Nov 25 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.5-alt1
- New release

* Thu Nov  6 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.4-alt1
- New release
- Add script for logrotate
- Create new package %name-contrib for all contrib files

* Thu Oct 09 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.2-alt1
- New release

* Sat Sep 06 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.1-alt3
- Add official Prelude IDS patch from Krzysztof Zaraska
  <kzaraska@student.uci.agh.edu.pl>
- Modify description (russian, ukrainian). Thanks to Michael Shigorin
  <mike@osdn.org.ua>
- Add README-ALT.ru README-ALT.uk files to documentation

* Sat Aug 30 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.1-alt2
- Add Prelude IDS patch

* Wed Aug 27 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.1-alt1
- fix host endianess problem in udp decoder
- vlan decoding fixes from Michael Pomraning
- add tcp state checking to httpflow
- ignoring bad checksums throughout snort if checksumming is turned on
- config disable_ttcp_alerts is now also config disable_tcpopt_ttcp_alerts
- better initialization handling of low memory conditions pointing to the low memory search engine
- byte_jump / byte_test 2 byte cases handled and unified
- correctly assign port numbers on tcpoption events
- pass rule logic changed to "win" in specific multiple event cases
- named interface support for win32 from the winpcap folks
- spp_bo now also will work with log-only output plugins
- added window detection plugin documentation to manual
- lots of new rules and tons of rule documentation 
- init-script rewrited according to new policy
- remove patch for Prelude IDS

* Wed May 28 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.0-alt3
- Fixed spec-file
- Fixed snord startup file

* Tue May 23 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.0-alt2
- Update source URL
- Update initscript
- Removed command for delete fakeuser "snort" in %postun section
- Fixed %post section
- Add patch for Prelude IDS

* Sun May 11 2003 Serhii Hlodin <hlodin@altlinux.ru> 2.0.0-alt1
- Initial build based on original SNORT spec-file
