%define realname automake
%define realver 1.4
%define dialect _1.4
%define suff -1.4

Name: %realname%dialect
%define patchlevel p6
Version: %realver%patchlevel
Release: alt5
Epoch: 1

%add_findreq_skiplist %_datadir/%realname%suff/config.guess
%set_compress_method gzip

Summary: A GNU tool for automatically creating Makefiles
License: GPLv2+
Group: Development/Other
Url: http://www.gnu.org/software/automake/
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

%define srcname %realname-%realver-%patchlevel

# ftp://ftp.gnu.org/gnu/%realname/%srcname.tar.bz2
Source: %srcname.tar
Source1: %name.buildreq

Patch1: automake-1.4-rh-libtoolize.patch
Patch2: automake-1.4-rh-subdir.patch
Patch3: automake-1.4-rh-backslash.patch
Patch4: automake-1.4-rh-subdirs-89656.patch
Patch5: automake-1.4-alt-texinfo.patch
Patch6: automake-1.4-alt-aclocal_libtool.patch

Provides: %realname = %epoch:%realver-%{release}0.%patchlevel
Provides: aclocal(libtool)
Obsoletes: %realname
PreReq: automake-common, alternatives >= 0.4

%description
Automake is a tool for automatically generating Makefiles compliant with the
GNU Coding Standards.

You should install Automake if you are developing software and would like to
use its capabilities of automatically generating GNU standard Makefiles.  If
you install Automake, you will also need to install GNU Autoconf package.

%prep
%setup -q -n %srcname
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%configure
%make_build MAKEINFO='makeinfo --no-split'

%install
%makeinstall MAKEINFO='makeinfo --no-split'

install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/buildreqs/files/ignore.d/%name
install -p -m644 %realname%suff.info %buildroot%_infodir/

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo %realname >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name

mkdir -p %buildroot%_altdir
cat <<EOF >%buildroot%_altdir/%name
%_bindir/%realname-default	%_bindir/%realname%suff	20
%_bindir/aclocal-default	%_bindir/aclocal%suff	%_bindir/%realname%suff
%_datadir/%realname	%_datadir/%realname%suff	%_bindir/%realname%suff
%_infodir/%realname.info.gz	%_infodir/%realname%suff.info.gz	%_bindir/%realname%suff
EOF

%files
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%config %_sysconfdir/buildreqs/files/ignore.d/*
%_altdir/%name
%_bindir/*%suff
%_datadir/aclocal%suff
%_datadir/%realname%suff
%_infodir/*.info*
%doc AUTHORS NEWS README THANKS TODO

%changelog
* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.4p6-alt5
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sun Nov 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.4p6-alt4
- Switched to alternatives-0.4.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.4p6-alt3
- aclocal: enhanced $LIBTOOL_VERSION support.

* Tue Aug 19 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.4p6-alt2
- aclocal: added $LIBTOOL_VERSION support.

* Sat May 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1:1.4p6-alt1
- Updated to 1.4p6.
- Deal with info dir entries such that the menu looks pretty.

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.4-alt9.p5
- new alternatives format

* Thu Mar 20 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.4-alt8.p5
- move to new altenatives scheme

* Mon Oct 28 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.4-alt7.p5
- Added automake-common support.

* Wed May 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.4-alt6.p5
- Added buildreq substitution rules.
- Fixed %%preun (added one more trigger to fix old package).

* Sat May 18 2002 Alexey Voinov <voins@altlinux.ru> 1:1.4-alt5.p5
- Renamed to automake_1.4
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
