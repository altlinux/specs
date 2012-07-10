%define realname automake
%define dialect _1.11
%define dialect_regex _1\\.11
%define suff -1.11
%define altver 1115

Name: %realname%dialect
Version: 1.11.6
Release: alt1

%add_findreq_skiplist %_datadir/%realname%suff/config.guess
%set_compress_method gzip
%define _perl_lib_path %perl_vendor_privlib:%_datadir/%realname%suff
%{?filter_from_requires:%filter_from_requires /^perl(Automake/d}
%{?filter_from_provides:%filter_from_provides /^perl(Automake/d}

Summary: A GNU tool for automatically creating Makefiles
License: GPLv2+ and GFDLv1.3+
Group: Development/Other
Url: http://www.gnu.org/software/automake/
BuildArch: noarch

%define srcname %realname-%version-%release

# git://git.altlinux.org/gears/a/%name.git
Source: %srcname.tar

Provides: %realname = 1:%version-%release
Provides: aclocal(libtool)
Obsoletes: %realname
PreReq: automake-common, alternatives >= 0:0.4
Requires: autoconf >= 2:2.62

BuildPreReq: autoconf >= 2:2.58, texinfo >= 4.7, help2man, perl-threads
%{!?__buildreqs:%{!?_without_check:%{!?_disable_check:BuildRequires: dejagnu expect flex gcc-c++ gcc-fortran makedepend}}}

%description
Automake is a tool for automatically generating `Makefile.in'
files compliant with the GNU Coding Standards.

%prep
%setup -n %srcname
bzip2 -9fk NEWS TODO

# patch texinfo file
sed -i '/@direntry/,/@end direntry/ s/^\(\*[[:space:]]\+[[:alnum:].]\+\)\(:[[:space:]]\+\)(%realname)/\1%suff\2(%realname%suff)/' \
	doc/automake.texi

# fix tests
chmod a+x tests/*.test

%build
%define docdir %_docdir/%realname-%version
./bootstrap
%configure --docdir=%docdir
%make_build MAKEINFOFLAGS=--no-split

%install
%makeinstall_std MAKEINFOFLAGS=--no-split

mv %buildroot%_infodir/%realname.info %buildroot%_infodir/%realname%suff.info

mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat <<EOF >%buildroot%_sysconfdir/buildreqs/files/ignore.d/%name
^/usr/share/aclocal(%dialect_regex)?/.+\.m4$
EOF

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo %realname >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name

mkdir -p %buildroot%_altdir
cat <<EOF >%buildroot%_altdir/%name
%_bindir/%realname-default	%_bindir/%realname%suff	%altver
%_bindir/aclocal-default	%_bindir/aclocal%suff	%_bindir/%realname%suff
%_man1dir/%realname.1.gz	%_man1dir/%realname%suff.1.gz	%_bindir/%realname%suff
%_man1dir/aclocal.1.gz	%_man1dir/aclocal%suff.1.gz	%_bindir/%realname%suff
%_datadir/%realname	%_datadir/%realname%suff	%_bindir/%realname%suff
%_infodir/%realname.info.gz	%_infodir/%realname%suff.info.gz	%_bindir/%realname%suff
EOF

install -pm644 AUTHORS README THANKS NEWS.bz2 TODO.bz2 \
	%buildroot%docdir/

# reenable perl-threads dependencies
%define __spec_autodep_custom_pre export AUTOMAKE_JOBS=1

%check
%make_build -k check

%files
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%config %_sysconfdir/buildreqs/files/ignore.d/*
%_altdir/%name
%_bindir/*%suff
%_man1dir/*%suff.1.gz
%_datadir/aclocal%suff
%_datadir/%realname%suff
%_infodir/*.info*
%docdir

%changelog
* Mon Jul 09 2012 Dmitry V. Levin <ldv@altlinux.org> 1.11.6-alt1
- Updated to v1.11.6.

* Fri Apr 13 2012 Dmitry V. Levin <ldv@altlinux.org> 1.11.5-alt1
- Updated to v1.11.5.
- Reintroduced dependencies on perl-threads.

* Thu Apr 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.11.4-alt3
- Made shell quoting in generated commands more consistent.
  This fixes regression introduced by commit v1.11-759-g368f1c4.

* Tue Apr 10 2012 Dmitry V. Levin <ldv@altlinux.org> 1.11.4-alt2
- aclocal: fixed misapplied patch for /usr/share/libtool/aclocal support.

* Mon Apr 09 2012 Dmitry V. Levin <ldv@altlinux.org> 1.11.4-alt1
- Updated to v1.11.4.

* Sun Jan 23 2011 Alexey Tourbin <at@altlinux.ru> 1.11.1-alt3
- Automake/Config.pm: Disabled dependency on perl-threads.
- Filtered out perl(Automake*) provides using new rpm macros.

* Mon Jan 25 2010 Dmitry V. Levin <ldv@altlinux.org> 1.11.1-alt2
- Updated to branch-1.11 v1.11.1-16-g80c84dd.
- Merged upstream fix of silent-rules output for disabled
  dependency tracking.

* Wed Jan 06 2010 Dmitry V. Levin <ldv@altlinux.org> 1.11.1-alt1
- Updated to 1.11.1 stable release.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt2
- Moved "make check" to %%check section.

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt1
- Updated to 1.11 stable release.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Thu Apr 23 2009 Dmitry V. Levin <ldv@altlinux.org> 1.10b-alt1
- Updated to 1.10b unstable release.
- Disabled automake provides for unstable release.
- Packaged manual pages for automake and aclocal.
- Added buildrequires for testsuite.
- Made testsuite success result mandatory again.
- Fixed documentation packaging.

* Mon Feb 23 2009 Kirill A. Shutemov <kas@altlinux.ru> 1:1.10a-alt1
- Update to 1.10a snapshot
  + It's unstable version, so don't use it by default
- Ingore testsuite result for now.

* Sun Nov 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.10.2-alt1
- Updated to 1.10.2.

* Fri Nov 21 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.10.1-alt3
- Switched to alternatives-0.4.

* Sun Aug 03 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.10.1-alt2
- Updated to v1.10.1-26-g9f6dd90.
- Fixed alternatives version (reported by led@).

* Tue Jan 22 2008 Alex V. Myltsev <avm@altlinux.ru> 1:1.10.1-alt1
- Updated to 1.10.1.
- Beware: --add-missing now creates COPYING with GPLv3 inside.

* Tue Dec 25 2007 Dmitry V. Levin <ldv@altlinux.org> 1:1.10-alt2
- Disabled automatic requirements lookup in config.guess file.

* Tue Nov 27 2007 Alex V. Myltsev <avm@altlinux.ru> 1:1.10-alt1
- Updated to 1.10.

* Sun Dec 18 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.9.6-alt1
- Updated to 1.9.6.

* Wed Jun 22 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.9.5-alt3
- Fixed wording in documentation fix made in previous release.
- Rediffed patches.

* Mon May 23 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.9.5-alt2
- Adjusted test suite for upcoming GNU Make 3.81.
- Fixed temporary directory handling suggestions
  in texinfo documentation.

* Sun Feb 13 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.9.5-alt1
- Updated to 1.9.5.

* Sat Jan 08 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1:1.9.4-alt1
- Really install objc.m4 [Patch0]

* Mon Jan 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1:1.9.4-alt0.1
- Adapted for automake 1.9.x
- Switched to the new alternatives format
- Got rid of the separate buildreq ignore file

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.8.5-alt1
- Updated to 1.8.5.

* Wed Aug 04 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.8.3-alt3
- Provide objc.m4 to fix Objective-C support.

* Tue Mar 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.8.3-alt2
- Updated build dependencies for test suit.

* Mon Mar 08 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.8.3-alt1
- Updated to 1.8.3.

* Tue Feb 24 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.8.2-alt1
- Updated to 1.8.2, updated patches.

* Sun Nov 16 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.9-alt1
- Updated to 1.7.9.

* Tue Sep 23 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.7-alt1
- Updated to 1.7.7.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.6-alt3
- aclocal: enhanced $LIBTOOL_VERSION support.

* Tue Aug 19 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.6-alt2
- aclocal: added $LIBTOOL_VERSION support.

* Mon Jul 21 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.6-alt1
- Updated to 1.7.6, regenerated texinfo patch.

* Sat May 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.4-alt2
- Deal with info dir entries such that the menu looks pretty.

* Thu May 01 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.4-alt1
- Updated to 1.7.4

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.7.3-alt1.2
- Migrated to new alternatives config format.

* Thu Mar 20 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.7.3-alt1.1
- Migrated to new altenatives scheme.
- fixed strings spacing during install-info.

* Fri Mar 14 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.3-alt1
- Updated to 1.7.3

* Sat Dec 14 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.2-alt1
- Updated to 1.7.2

* Mon Dec 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.1-alt2
- Corrected provides.

* Sun Nov 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.1-alt1
- Updated to 1.7.1.

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt2
- Added automake-common support.
- Raised alternatives priority.

* Tue Oct 22 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.3-alt1
- Updated to 1.6.3.

* Wed May 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6.1-alt2
- Added buildreq substitution rules.

* Sat May 18 2002 Alexey Voinov <voins@voins.program.ru> 1:1.6.1-alt1
- Renamed to automake_1.6, based on automake-1.4-alt4.p5
- New version (1.6.1).
- Added update-alternatives support.

* Tue Jan 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.4-alt4.p5
- Added aclocal filter for buildreq.

* Wed Sep 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-alt3.p5
- Dont raise error when there is source in a subdirectory (hjl, rh #35156).
  This was preventing automake from working in binutuls/gas
  [patch from HJ Lu <hjl@gnu.org>]
- Format long lines of output properly with backslash + newlines as in 1.4
  (hjl, rh #35259)

* Mon Aug 20 2001 Sergey Vlasov <vsu@altlinux.ru> 1.4-alt2.p5
- Bugfix for Elisp file installation.
- Bugfix for lex file handling.

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-alt1.p5
- 1.4-p5

* Mon Jun 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-alt1.p4
- 1.4-p4

* Sat Jun 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-ipl16mdk
- 1.4-p3

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-ipl15mdk
- 1.4-p2

* Fri May 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-ipl14mdk
- 1.4-p1

* Sun May 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-ipl13mdk
- Updated vendor information.

* Thu Oct 05 2000 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl12mdk
- Merge RH patch.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl11mdk
- RE and Fandra adaptions.

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4-8mdk
- new groups

* Wed Oct 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with Jeff package.

* Tue Jun 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 1.4 version.
- Merging with RedHat patch.

* Thu May 13 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- 1.4a

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- arm netwinder patch

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb  8 1999 Jeff Johnson <jbj@redhat.com>
- add patches from CVS for 6.0beta1

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.4.

* Mon Nov 23 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.3b.
- add URL.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- updated to 1.3

* Tue Oct 28 1997 Cristian Gafton <gafton@redhat.com>
- added BuildRoot; added aclocal files

* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- made it a noarch package

* Thu Oct 16 1997 Michael Fulbright <msf@redhat.com>
- Fixed some tag lines to conform to 5.0 guidelines.

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- updated to 1.2

* Wed Mar 5 1997 msf@redhat.com <Michael Fulbright>
- first version (1.0)
