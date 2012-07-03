%define ltversion 1.4
%define libtool libtool-%ltversion
%define libltdl libltdl
%define priority 140

Name: libtool_%ltversion
Version: 1.4.3
Release: alt11
Epoch: 3

Summary: The GNU libtool, which simplifies the use of shared libraries
License: GPLv2+
Group: Development/Other
Url: http://www.gnu.org/software/libtool/libtool.html

%add_findreq_skiplist %_datadir/%libtool/config.guess-%ltversion
%set_compress_method gzip
%set_libtool_version 1.5
%set_automake_version 1.4
%set_autoconf_version 2.13

Provides: libtool = %epoch:%version-%release
PreReq: libtool-common, alternatives >= 0.4
Requires: %libltdl >= %epoch:%version-%release
Requires: aclocal(libtool)
Obsoletes: libtool < %epoch:%version

Source: ftp://ftp.gnu.org/gnu/libtool/libtool-1.4.3.tar
Source1: %name-buildreq.ignore

# RedHat patches
Patch1: libtool-1.3.5-rh-tmp.patch
Patch2: libtool-1.4-rh-ltmain-nonneg.patch
Patch3: libtool-1.4.3-rh-ltmain-SED.patch
Patch6: libtool-1.4.2-rh-relink-58664.patch
Patch9: libtool-1.4.2-rh-multilib.patch
Patch10: libtool-1.4.2-rh-demo.patch
# Patch from James Henstridge making restricted symbol exports work on Linux
Patch11: libtool-1.5-jh-expsym-linux.patch
# http://mail.gnu.org/pipermail/bug-libtool/2002-October/004272.html
Patch12: libtool-1.4.3-rh-readonlysym.patch
# Fix automake related test failure
#Patch14: libtool-1.5-rh-testfailure.patch
Patch17: libtool-1.4.3-rh-nostdlib.patch

# ALT patches
Patch20: libtool-1.5-alt-sys_lib_dlsearch.patch
Patch21: libtool-1.4.2-alt-ltmain-cpp-linkage.patch
Patch22: libtool-1.5-alt-texinfo.patch
Patch23: libtool-1.5-alt-makefile.patch
Patch24: libtool-1.5-alt-libtoolize-libtool.m4.patch

# Automatically added by buildreq on Tue Aug 19 2003
BuildRequires: gcc-c++ gcc-g77 libstdc++-devel

%description
The libtool package contains the GNU libtool, a set of shell scripts
which automatically configure UNIX and UNIX-like architectures to
generically build shared libraries.  Libtool provides a consistent,
portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, you
should install libtool.

%prep
%setup -q -n libtool-%version

# RedHat patches
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch6 -p1
%patch9 -p1
%patch10 -p1
#patch11 -p1
%patch12 -p1
# backup suffix undesirable here
#patch14 -p1
#patch17 -p1

# ALT patches
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1

# Hack in the version-specific package data dir and aclocal dir variables.
perl -pi -e 's|^(pkgdatadir=.*?)\s*$|$1-%ltversion\n|;' configure.in

cp -p /usr/share/libtool/config/config.* .

rm doc/*.info*

bzip2 -9k ChangeLog*

find -type f -print0 |
	xargs -r0 grep -Zl '^# Libtool was configured' -- |
	xargs -r0 sed -i 's/^\(# Libtool was configured\).*/\1 as follows:/' --

%build
export CC=gcc
export CXX=g++
export F77=g77
export GCJ=gcj
for f in {,*/}acinclude.m4; do
	cp -p libtool.m4 "$f"
done
%undefine __libtoolize
%__aclocal
# new gettext introduce new m4 macros which depend on fresh autoconf
# and automake; hopefully libtool doesn't use gettext and its m4 macros.
%__subst -p 's,^AC_PREREQ(\[\?2\.5[0-9]\]\?),AC_PREREQ(2.13),' *.m4
%__autoheader
%__automake
%__autoconf
touch aclocal.m4
for f in */aclocal.m4; do
	cp aclocal.m4 "$f"
done

%configure --program-suffix=-%ltversion

perl -pi -e '/^\@direntry/../^\@end direntry/ and s/^\*\s*(libtool(ize)?):\s*\(libtool\)/* $1-%ltversion: (%libtool)/i' doc/libtool.texi

# SMP-incompatible build.
%make MAKEINFOFLAGS=--no-split

%check
make -k check ||:

%install
%makeinstall

mv %buildroot%_datadir/libtool/* \
      %buildroot%_datadir/%libtool/

mkdir %buildroot%_datadir/%libtool/aclocal
mv %buildroot%_datadir/aclocal/libtool.m4 \
    %buildroot%_datadir/%libtool/aclocal/

for f in ltmain.sh config.{guess,sub}; do
    rm -f %buildroot%_datadir/%libtool/$f
    ln -s $f-%ltversion %buildroot%_datadir/%libtool/$f
done
#for f in install-sh missing mkinstalldirs; do
#    mv %buildroot%_datadir/%libtool/$f{,-%ltversion}
#    ln -s $f-%ltversion %buildroot%_datadir/%libtool/$f
#done
#rm -f %buildroot%_datadir/libtool/libltdl/stamp-h.in

mv %buildroot%_infodir/libtool{,-%ltversion}.info

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/libtool-default	%_bindir/%libtool	%priority
%_bindir/libtoolize-default	%_bindir/libtoolize-%ltversion	%_bindir/%libtool
%_datadir/libtool	%_datadir/%libtool	%_bindir/%libtool
%_infodir/libtool.info.gz	%_infodir/%libtool.info.gz	%_bindir/%libtool
EOF

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo libtool >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name

mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
install -p -m644 %SOURCE1 \
    %buildroot%_sysconfdir/buildreqs/files/ignore.d/%name

%define ltdocdir %_docdir/libtool-%version
%define ltdldocdir %_docdir/libltdl-%version

rln()
{
	local target=$1 && shift
	local source=$1 && shift
	target=`relative "$target" "$source"`
	ln -snf "$target" "%buildroot$source"
}

mkdir -p %buildroot%ltdocdir
install -p -m644 AUTHORS NEWS README THANKS TODO ChangeLog*.bz2 \
    %buildroot%ltdocdir/
rln %_licensedir/GPL-2 %ltdocdir/COPYING
mkdir -p %buildroot%ltdldocdir
install -p -m644 libltdl/README %buildroot%ltdldocdir/
rm -f %buildroot%_datadir/%libtool/libltdl/COPYING.LIB
rln %_licensedir/LGPL-2.1 %_datadir/%libtool/libltdl/COPYING.LIB
rln %_licensedir/LGPL-2.1 %ltdldocdir/COPYING.LIB

%files
%_bindir/*
%_datadir/%libtool
%_infodir/%libtool.info*
%_altdir/%name
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%dir %ltdocdir
%ltdocdir/[A-Z]*

%changelog
* Sat Jun 05 2010 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.3-alt11
- Prevented build host name leaks into generated libtool scripts.
- Fixed build with gettext >= 0.18.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.3-alt10
- Moved "make check" to %%check section.

* Wed Jun 03 2009 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.3-alt9
- Removed obsolete %%install_info/%%uninstall_info calls.
- Fixed build in updated build environment.

* Sun Nov 23 2008 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.3-alt8
- Switched to alternatives-0.4.

* Tue Jan 15 2008 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.3-alt7
- Fixed build in new build environment.

* Sat Sep 16 2006 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.3-alt6
- Fixed build in new build environment.

* Tue May 24 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.3-alt5
- Fixed build in new build environment.

* Mon Dec 15 2003 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.3-alt4
- Updated to 1.4.3 (1.922.2.110 2002/10/23 01:39:54).
- Explicitly use old autotools for build.
- Do not package autoconf scripts (install-sh,missing,mkinstalldirs).

* Thu Oct 02 2003 Mikhail Zabaluev <mhz@altlinux.ru> 3:1.4.3-alt3
- Fixed installation of scripts
- Removed the rudimentary demo stuff

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 3:1.4.3-alt1
- Additional convention enforcement on patch file names.
- Do not apply jh-expsym-linux and rh-nostdlib patches in this branch.
- Raised serial number.

* Wed Aug 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2:1.4.3-alt1
- Packed libtool_1.4 as an alternative to libtool_1.5
- Dropped libltdl and demos as it's all provided by libtool_1.5

* Sun Sep 22 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2:1.4.2-alt0.2
- Replaced/appended patches with the RedHat patches from 1.4.2-12,
  save the X11R6 patch. RedHat should be the proper reference for patches,
  they do it cleaner, plus they have aoliva among them.
- Reversed the order in -L directories for the relink patch
  so that the inst-prefixed directory comes first
  (this is not apparent from the code, because the order of linking items
  is reversed afterwards)
- The tag patch is moot, as it changes two independent things and introduces
  an option yet unused. Let it dangle unapplied for now.
- Replaced the ugly c++ link patch from Mandrake
  with something more elegant

* Thu Jun 13 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2:1.4.2-alt0.1
- 1.4.2
- Patches from Mandrake, including the relink patch

* Mon Sep 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-alt2
- Do not infer tagged configuration yet.

* Thu Aug 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-alt1
- Revert back again to more stable(?) version.
- Readded k6/athlon arches support.

* Fri Aug 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4b-alt1
- 1.4b
- libtool_1.4b-3 patch from debian.
- Added more demos to libltdl-devel subpackage

* Tue May 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.5-alt2
- More architectures support (debian).

* Fri May 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.5-alt1
- Back to 1.3.5 (1.4 seems to be broken).

* Sat May 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.4-alt1
- 1.4
- Libificated into libtool, libltdl, libltdl-devel-static and libltdl-devel-static subpackages.
- Do not libtoolize during build.

* Wed Nov 15 2000 Dmitry V. Levin <ldv@fandra.org> 1.3.5-ipl3mdk
- Fixed texinfo documentation.
- Added fake "--build" option.

* Fri Sep 29 2000 Dmitry V. Levin <ldv@fandra.org> 1.3.5-ipl2mdk
- Merged with RH.
- Re-splitted into %name and %name-libs.

* Mon Jun 26 2000 Dmitry V. Levin <ldv@fandra.org> 1.3.5-ipl1mdk
- RE and Fandra adaptions.

* Wed Jun 21 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 1.3.5-1mdk
- picks up $arch-mandrake-linux-gnu not $arch-pc-linux-gnu (patch)
  well, for x86 and alpha anyway, maybe ultrasparc too ??
- new version
- fix bad source url
- add libtool url
- add devel package
- Chmouel Boudjnah <chmouel@mandrakesoft.com> - Spec Cleanup
  (makeinstall etc..).

* Wed Apr  5 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 1.3.4-2mdk
- updated BuildRoot
- group new Development/Other

* Thu Jan 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.4-1mdk
- 1.3.4.

* Wed Dec  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build Release.

* Sun Nov 07 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Mon Oct 25 1999  Jeff Garzik  <jgarzik@pobox.com>
- Import RedHat 6.1 spec
- s/gzip/bzip2/ for info documentation

* Thu Jul 15 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.3.3.

* Mon Jun 14 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.3.2.

* Tue May 11 1999 Jeff Johnson <jbj@redhat.com>
- explicitly disable per-arch libraries (#2210)
- undo hard links and remove zero length file (#2689)

* Sat May  1 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.3.

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- disable the --cache-file passing to ltconfig; this breaks the older
  ltconfig scripts found around.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.2f

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- completed arm patch
- added patch to make it more arm-friendly
- upgrade to version 1.2d

* Thu May 07 1998 Donnie Barnes <djb@redhat.com>
- fixed busted group

* Sat Jan 24 1998 Marc Ewing <marc@redhat.com>
- Update to 1.0h
- added install-info support

* Tue Nov 25 1997 Elliot Lee <sopwith@redhat.com>
- Update to 1.0f
- BuildRoot it
- Make it a noarch package
