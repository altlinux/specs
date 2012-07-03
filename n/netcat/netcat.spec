Name: netcat
%define datestamp 20100725
Version: 4.0.%datestamp
Release: alt1

Summary: Reads and writes data across network connections using TCP or UDP
License: BSD
Group: Networking/Other
Url: http://www.openbsd.org/cgi-bin/cvsweb/src/usr.bin/nc/
Packager: Dmitry V. Levin <ldv@altlinux.org>

#  Sources are taken and packaged by following command:
#     CVSROOT=anoncvs@anoncvs2.de.openbsd.org:/cvs cvs get src/usr.bin/nc                                      
#     tar czf netcat-$(date +%%Y%%m%%d).tar.gz src/
#  Note: replace double percents in date arguments above by single percent sign.
Source: %name-%datestamp.tar
Patch1: netcat-4.0.20100725-owl-alt-linux.patch
Patch2: netcat-4.0.20100725-owl-ipv4-default.patch
Patch3: netcat-4.0.20100725-owl-alt-fixes.patch
Patch4: netcat-4.0.20100725-alt-usage.patch
Patch5: netcat-4.0.20100725-alt-bsdsockopts.patch
Patch6: netcat-4.0.20100725-alt-rpp.patch
Patch7: netcat-4.0.20100725-alt-strtonum.patch
Patch8: netcat-4.0.20100725-alt-execcmd.patch
Patch9: netcat-4.0.20100725-alt-proxy_pass.patch
Patch10: netcat-4.0.20100725-alt-warnings.patch
Patch11: netcat-4.0.20100725-jzeleny-pollhup.patch

Obsoletes: nc
Provides: nc
Conflicts: nedit < 5.5-alt3

%description
This package contains netcat, a simple utility for reading and writing
data across network connections, using the TCP or UDP protocols.
netcat is intended to be a reliable back-end tool which can be used
directly or easily driven by other programs and scripts.  netcat is
also a feature-rich network debugging and exploration tool, since
it can create many different connections and has many built-in
capabilities.

There are three well-known netcat implementations, see here for
details: http://pintday.org/downloads/netcat/. This package contains
OpenBSD utility with improvements from Openwall project.

%define srcdir src/usr.bin/nc

%prep
%setup -q -c
cd src
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
sed -i 's,\mnc\M,netcat,' usr.bin/nc/nc.1

%build
%make_build -C %srcdir CFLAGS='-c %optflags'

%install
install -pD -m755 %srcdir/nc   %buildroot%_bindir/netcat
install -pD -m644 %srcdir/nc.1 %buildroot%_man1dir/netcat.1
ln -s netcat %buildroot%_bindir/nc
ln -s netcat.1 %buildroot%_man1dir/nc.1

%files
%_bindir/*
%_mandir/man?/*

%changelog
* Thu Dec 09 2010 Dmitry V. Levin <ldv@altlinux.org> 4.0.20100725-alt1
- Updated to 20100725 snapshot.
- Imported a POLLHUP detection patch by Jan Zeleny (closes: #24657).

* Fri Jul 02 2010 Dmitry V. Levin <ldv@altlinux.org> 4.0.20100420-alt1
- Updated to 20100420 snapshot (closes: #23214).
- Added %_bindir/nc symlink.

* Wed Jul 09 2008 Dmitry V. Levin <ldv@altlinux.org> 4.0.20061122-alt2
- Added proxy password support (Closes: ALT#16312).
- Fixed compilation warnings (Closes: ALT#16312).

* Wed Nov 22 2006 Ilya Evseev <evseev@altlinux.ru> 4.0.20061122-alt1
- updated to 20061122 snapshot

* Tue Aug  8 2006 Ilya Evseev <evseev@altlinux.ru> 3.9.20060725-alt1
- updated to 20060725 snapshot: 
   + reapply patches #3, #5, #6, #7
   + added patches #8 and #9 for replacing readpassphrase() and strtonum()
   + modify patch #1 for adding libresolv to linked libs
- bugfix #9822: providing 'nc' feature

* Mon Nov  7 2005 Ilya Evseev <evseev@altlinux.ru> 3.7.20051010-alt2
- added patch #7: support '-e cmd' for calling subprocess
  for talking with remote side via established connection.

* Wed Oct 12 2005 Ilya Evseev <evseev@altlinux.ru> 3.7.20051010-alt1
- update to current CVS snapshot (10 Oct 2005):
    + fix patches #1, #3, #5, #6
    + replace patch #4 by direct call of 'subst' utility
- new versions convention - add datestamp suffix

* Mon Apr 11 2005 Ilya Evseev <evseev@altlinux.ru> 3.6-alt3
- update to current CVS snapshot

* Sun Jan  9 2005 Ilya Evseev <evseev@altlinux.ru> 3.6-alt2
- specfile fixes: replace 'SolarDesigner' to 'Openwall/Owl'
- tcp_md5sig patch cleanup

* Fri Jan  7 2005 Ilya Evseev <evseev@altlinux.ru> 3.6-alt1
- update to current CVS snapshot: december 2004, post-OpenBSD-3.6
- apply latest Owl patch, disable TCP_MD5SIG using
- specfile: added russian summary/description, added URL

* Fri Jul 02 2004 Dmitry V. Levin <ldv@altlinux.org> 3.2-alt2
- Fixed usage text (#4345).

* Wed Feb 05 2003 Dmitry V. Levin <ldv@altlinux.org> 3.2-alt1
- Migrated to another implementation: from OpenBSD with Owl patches.

* Thu Oct 24 2002 Stanislav Ievlev <inger@altlinux.ru> 1.10-ipl3mdk
- rebuild with gcc3
- added some RH patches
  TODO: change perl into subst

* Mon Mar 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.10-ipl2mdk
- Rebuilt

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.10-ipl10mdk
- Renamed to netcat (avoid clash with program nc from nedit package).

* Wed Aug  8 2000 Dmitry V. Levin <ldv@fandra.org> 1.10-ipl10mdk
- RE and Fandra adaptions.

* Mon Apr 10 2000 Maurizio De Cecco  <maurizio@mandrakesoft.com>
- Fixed error in Group

* Thu Mar 16 2000 Maurizio De Cecco  <maurizio@mandrakesoft.com>
- Adapted to the new Group structure

* Wed Nov 10 1999 Jerome Martin <jerome@mandrakesoft.com>
- Build for new environment

* Wed May 05 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- make it build on the arm

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0
