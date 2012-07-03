%define realname autoconf
%define dialect _2.13
%define suff -2.13

Name: %realname%dialect
Version: 2.13
Release: alt11
Serial: 2

%set_compress_method gzip

Summary: A GNU tool for automatically configuring source code
License: GPLv2+
Group: Development/Other
Url: http://www.gnu.org/software/%realname/
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

%define srcname %realname-%version
Source: ftp://ftp.gnu.org/gnu/%realname/%srcname.tar.bz2
Source1: %realname-2.13-manpages.tar

Patch1: %realname-2.13-alt-tmp.patch
Patch2: %realname-2.13-alt-c++exit.patch
Patch3: %realname-2.13-alt-headers.patch
Patch4: %realname-2.13-alt-autoscan.patch
Patch5: %realname-2.13-alt-exit.patch
Patch6: %realname-2.13-alt-noelf.patch
Patch7: %realname-2.13-alt-texinfo.patch
Patch8: %realname-2.13-alt-acdatadir.patch
Patch9: %realname-2.13-alt-dnet.patch
Patch10: %realname-2.13-alt-ac_extension.patch

Provides: %realname = %serial:%version-%release
Obsoletes: %realname

PreReq: autoconf-common, alternatives >= 0:0.4
Requires: m4 >= 1.4, mktemp >= 1:1.3.1

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to
specify various configuration options.

You should install Autoconf if you are developing software and you'd
like to use it to create shell scripts which will configure your
source code packages. If you are installing Autoconf, you will also
need to install the GNU m4 package.

Note that the Autoconf package is not required for the end user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not
their use.

%prep
%setup -q -n %srcname -a1
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

find -type f -print0 |
	xargs -r0 grep -FZl 'mawk gawk' |
	xargs -r0 sed -i 's/mawk gawk/gawk mawk/g'

# patch texinfo file
sed -i 's/(%realname)/(%realname%suff)/g;s/\(\* \([Aa]utoconf\|configure\)\):/\1%suff:/g' %realname.texi

%build
%configure --program-suffix=%suff
%make_build

%install
%makeinstall

# We don't want to include the standards.info stuff in the package,
# since it comes from binutils.
rm %buildroot%_infodir/standards*

# Install manpages.
for f in [a-z]*.1; do
	install -pD -m644 "$f" "%buildroot%_man1dir/${f%%.1}%suff.1"
done

# Some more helpful scripts.
install -pm755 *-sh %buildroot%_datadir/%realname%suff/
rm -f %buildroot%_datadir/%realname%suff/INSTALL

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo %realname >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name

mv %buildroot%_infodir/%realname.info %buildroot%_infodir/%realname%suff.info

%if 0
# rename binaries
for f in %buildroot%_bindir/*; do
	sed -e's@%_datadir/%realname@%_datadir/%realname%suff@' <"$f" >"${f}%suff"
	rm "$f"
	chmod a+x "${f}%suff"
done
# rename man files
for f in %buildroot%_man1dir/*; do
	mv $f ${f%%.1}%suff.1
done
%endif

for f in %buildroot%_bindir/*%suff; do
	ln -s "${f##*/}" "${f%%%suff}%dialect"
done

mkdir -p %buildroot%_altdir

cat >%buildroot%_altdir/%name <<EOF
%_bindir/%realname-default	%_bindir/%realname%suff	20
%_datadir/%realname	%_datadir/%realname%suff	%_bindir/%realname%suff
%_infodir/%realname.info.gz	%_infodir/%realname%suff.info.gz	%_bindir/%realname%suff
EOF

for i in autoheader autom4te autoreconf autoscan autoupdate ifnames; do
cat >>%buildroot%_altdir/%name <<EOF
%_bindir/$i-default	%_bindir/$i%suff	%_bindir/%realname%suff
EOF
done

for i in %realname autoheader autom4te autoreconf autoscan autoupdate config.guess config.sub ifnames; do
cat >>%buildroot%_altdir/%name <<EOF
%_man1dir/$i.1.gz	%_man1dir/$i%suff.1.gz	%_bindir/%realname%suff
EOF
done

%files
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%_altdir/*
%_bindir/*
%_datadir/%realname%suff
%_man1dir/*
%_infodir/*.info*
%doc AUTHORS NEWS README TODO

%changelog
* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 2:2.13-alt11
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sun Nov 23 2008 Dmitry V. Levin <ldv@altlinux.org> 2:2.13-alt10
- Switched to alternatives-0.4.

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 2:2.13-alt9
- Updated package dependencies.
- Corrected ac_extension order.

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 2:2.13-alt8.1
- move to new alternatives scheme

* Sun Oct 27 2002 Dmitry V. Levin <ldv@altlinux.org> 2:2.13-alt8
- Removed libdnet checks.
- Fixed %_datadir/%realname%suff relocation.
- Changed suffix, compatibility symlinks added (#0001192).
- Added autoconf-common support.

* Thu May 16 2002 Dmitry V. Levin <ldv@altlinux.org> 2:2.13-alt7
- Added few fake slave alternatives to avoid "slave update-alternatives bug".

* Wed Apr 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 2:2.13-alt6
- Set compress method to "gzip".
- Set dircategory to "Development/Other".

* Sat Apr 06 2002 Alexey Voinov <voins@voins.program.ru> 2.13-alt5
- URL corrected
- support for *.info and man-pages (update-)alternatives

* Tue Mar 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 2:2.13-alt4
- Renamed to autoconf_2.13
- Added update-alternatives support (voins).

* Wed Feb 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 2:2.13-alt3
- Fixed acspecific to avoid -lelf usage for getloadavg.

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.13-alt2
- Rebuilt.

* Thu Aug 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.13-alt1
- Revert back to stable version.
- Reworked tmp files handling.
- Merged RH patches:
  + acgeneral.m4: fixed exit status;
  + autoscan.pl: patched to get a better choice of init file (#42071),
    to test for CPP after CC (#42072) and to detect C++ source and g++ (#42073).
  + acspecific.m4: include various standard C headers as needed
    by various autoconf tests (#19114);
  + acgeneral.m4, acspecific.m4: back-ported _AC_PROG_CXX_EXIT_DECLARATION
    from version 2.50 to make detection of C++ exit() declaration prototype
    platform independent. The check is done in AC_PROG_CXX with the result
    stored in "confdefs.h". The exit() prototype in AC_TRY_RUN_NATIVE is no
    longer needed.

* Mon Aug 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.52b-alt1
- 2.52b

* Fri Aug 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.52-alt1
- 2.52
- Added manpages from debian.

* Sun Dec 24 2000 Dmitry V. Levin <ldv@fandra.org> 2.13-ipl5mdk
- Fixed exit function prototype for gcc >= 2.96.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 2.13-ipl4mdk
- RE adaptions.

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.13-4mdk
- macros for install-info

* Mon Jul 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.13-3mdk
- cleanup and macros

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.13-2mdk
- new groups

* Mon Mar  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.13-1mdk
- Back to last 2.13 and stable version, add a serial.

* Wed Oct 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge change of Jeff package.

* Thu May 13 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- 2.14.1

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add patch to help autoconf clean after itself and not leave /tmp clobbered
  with acin.* and acout.* files (can you say annoying?)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)
- use gawk, not mawk

* Thu Mar 18 1999 Preston Brown <pbrown@redhat.com>
- moved /usr/lib/autoconf to /usr/share/autoconf (with automake)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.13.

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- requires perl

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- patch for fixing /tmp race conditions

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- made a noarch package
- uses autoconf
- uses install-info

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built with glibc

