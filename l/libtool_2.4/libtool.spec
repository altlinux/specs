%define ltversion 2.4
%define ltsoname 7
%define libtool libtool-%ltversion
%define libltdl libltdl%ltsoname
%define priority 242

Name: libtool_%ltversion
Version: 2.4.2
Release: alt2

Summary: The GNU libtool, which simplifies the use of shared libraries
License: GPLv2+
Group: Development/Other
Url: http://www.gnu.org/software/libtool/libtool.html

%add_findreq_skiplist %_datadir/%libtool/config.guess
%set_compress_method gzip

Provides: libtool = 3:%version-%release
Obsoletes: libtool
PreReq: libtool-common >= 0.2, alternatives >= 0:0.4
Requires: aclocal(libtool)
Requires: autoconf_2.60

# git://git.altlinux.org/gears/l/%name.git
Source: libtool-%version-%release.tar

BuildRequires: gcc-c++ gcc-g77
# for tests/search-path.at
BuildRequires: zlib-devel

%package -n %libltdl
Summary: dlopen wrapper for GNU libtool
License: LGPLv2+
Group: System/Libraries

%package -n %libltdl-devel
Summary: Development files for %libltdl
License: LGPLv2+
Group: Development/C
Requires: %name = %version-%release
Requires: %libltdl = %version-%release
Provides: libltdl-devel = 3:%version-%release
Conflicts: libltdl-devel < 3:%version

%package -n %libltdl-devel-static
Summary: Static %libltdl library
License: LGPLv2+
Group: Development/C
Requires: %libltdl-devel = %version-%release
Provides: libltdl-devel-static = 3:%version-%release
Conflicts: libltdl-devel-static < 3:%version

%package demos
Summary: Samples for Libtool
License: GPLv2+
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description
The libtool package contains the GNU libtool, a set of shell scripts
which automatically configure UNIX and UNIX-like architectures to
generically build shared libraries.  Libtool provides a consistent,
portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, you
should install libtool.

%description -n %libltdl
This package contains libltdl shared library,
a system independent dlopen wrapper for GNU libtool.

%description -n %libltdl-devel
Development files for libltdl, a system independent
dlopen wrapper for GNU libtool.

%description -n %libltdl-devel-static
Static libltdl library, a system independent dlopen wrapper for GNU libtool.

%description demos
Sample programs and libraries to build with libtool.

%prep
%setup -n libtool-%version

# Eliminate gnutar dependencies.
find -type f -name missing -print0|
	xargs -r0 sed -i 's/gnutar /gnutar=gnutar \&\& \$&/' --

# Rename due to alternatives.
sed -i '/@direntry/,/@end direntry/ s/^\(\*[[:space:]]\+[[:alnum:].]\+\)\(:[[:space:]]\+\)(libtool)/\1-%ltversion\2(%libtool)/' \
	doc/libtool.texi

%build
./bootstrap
%configure --program-suffix=-%ltversion

# SMP-incompatible build?
make MAKEINFOFLAGS=--no-split
# Do not hardcode gcc path information, and do not use -nostdlib.
sed -i -e 's/^\(predep_objects\|postdep_objects\|compiler_lib_search_path\)=.*/\1=""/' \
       -e 's/^\(archive\(_expsym\)\?_cmds=\".*\) -nostdlib /\1 /' libtool

%check
# Testsuite is SMP-compatible but the output is hard to read.
make -k check
find tests -maxdepth 1 -type d -name '*demo*' |
	xargs -rn1 make distclean -C

%install
%makeinstall_std
mv %buildroot%_infodir/libtool{,-%ltversion}.info

out="\$(\$CC -print-search-dirs |\$SED -e '/^libraries: *=/!d;s///;s!/:!:!g;s!/\$!!;s/:/ /g')"
sed -i 's#^\(compiler_lib_search_dirs="\)/.*#\1'"$out"'"#' %buildroot%_bindir/%libtool

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
echo '^/usr/share/libtool(-2\.2)?/aclocal/.+\.m4$' >%buildroot%_sysconfdir/buildreqs/files/ignore.d/%name

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
install -p -m644 AUTHORS NEWS README THANKS TODO %buildroot%ltdocdir/
rln %_licensedir/GPL-2 %ltdocdir/COPYING
mkdir -p %buildroot%ltdldocdir
install -p -m644 libltdl/README %buildroot%ltdldocdir/
rm %buildroot%_datadir/%libtool/libltdl/COPYING.LIB
rln %_licensedir/LGPL-2.1 %_datadir/%libtool/libltdl/COPYING.LIB
rln %_licensedir/LGPL-2.1 %ltdldocdir/COPYING.LIB

for d in `find tests -maxdepth 1 -type d -name '*demo*'`; do
	cp -a "$d" %buildroot%ltdocdir/
	rm -rf %buildroot%ltdocdir/"${d##*/}"/autom4te.cache
	find %buildroot%ltdocdir/"${d##*/}"/ -type f -print0 |
		xargs -r0 fgrep -lZ ../../libltdl/m4/ |
		xargs -r0 sed -i 's|libltdl/m4/|../libtool-%ltversion/aclocal/|' --
done

# This config.guess file usually emits tons of unwanted deps.
%add_findreq_skiplist %_datadir/%libtool/config/config.guess

%files
%_bindir/*
%_datadir/%libtool
%_infodir/%libtool.info*
%_altdir/%name
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%dir %ltdocdir
%ltdocdir/[A-Z]*

%files -n %libltdl
%_libdir/*.so.*
%dir %ltdldocdir
%ltdldocdir/README
%ltdldocdir/COPYING.LIB

%files -n %libltdl-devel
%_libdir/*.so
%_includedir/*

%files -n %libltdl-devel-static
%_libdir/*.a

%files demos
%dir %ltdocdir
%ltdocdir/*demo*

%changelog
* Fri Apr 13 2012 Dmitry V. Levin <ldv@altlinux.org> 2.4.2-alt2
- libltdl/config/ltmain.m4sh (func_mode_install): Changed to
  normalize destination directory name, for better cooperation
  with the change made in 2.2.6-alt4.

* Tue Apr 10 2012 Dmitry V. Levin <ldv@altlinux.org> 2.4.2-alt1
- Updated to 2.4.2.

* Mon Feb 14 2011 Alexey Tourbin <at@altlinux.ru> 2.2.10-alt3
- Rebuilt for debuginfo.

* Wed Oct 13 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.10-alt2
- Rebuilt for soname set-versions.

* Thu Jun 10 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.10-alt1
- Updated to 2.2.10.

* Mon Nov 30 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6b-alt1
- Updated to 2.2.6b (fixes CVE-2009-3736).

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt10
- Moved "make check" to %%check section.

* Mon Aug 24 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt9
- Fixed compiler_lib_search_dirs in %_bindir/%libtool file.

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt8
- Fixed build with fresh automake.

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt7
- Removed obsolete %%install_info/%%uninstall_info calls.

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt6
- libltdl/config/ltmain.m4sh (func_mode_install): Changed to
  tolerate trailing slash in destination directory name.

* Mon May 04 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt5
- libltdl/loaders/preopen.c (lt_dlpreload_open): Robustified.

* Sun May 03 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt4
- libltdl/config/ltmain.m4sh (func_mode_link):
  Changed to always canonicalize rpath and to skip finalize_rpath
  directories that are in the system default run-time search path.

* Tue Apr 28 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt3
- Moved ltdl.m4 from %_datadir/aclocal/ to %_datadir/%libtool/aclocal/
  and packaged it into the main subpackage.

* Wed Apr 22 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt2
- Backported remaining changes from 1.5.26-alt4 and Debian.

* Tue Apr 14 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.6-alt1
- 2.2.6 released

* Fri Nov 21 2008 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.26-alt4
- Switched to alternatives-0.4.
- Removed obsolete %%post_ldconfig/%%postun_ldconfig call.
- Packaged -demos subpackage as noarch.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.26-alt3
- aclocal.m4: Replaced deprecated macro AC_FOREACH with m4_foreach_w (closes: #15420).
- Updated license tags.

* Fri Mar 07 2008 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.26-alt2
- libtool.m4 (AC_LIBTOOL_PROG_LD_SHLIBS): Changed archive_expsym_cmds
  to support custom altlinux version scripts (#13577).

* Sat Feb 23 2008 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.26-alt1
- Updated to 1.5.26.

* Tue Dec 25 2007 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.24-alt3
- Disabled automatic requirements lookup in config.guess file.

* Tue Nov 27 2007 Alex V. Myltsev <avm@altlinux.ru> 3:1.5.24-alt2
- Updated to 1.5.24.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.22-alt2
- Uncompressed tarball, dropped ChangeLog* files.

* Mon Dec 19 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.22-alt1
- Updated to 1.5.22.

* Tue Sep 27 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.20-alt2
- Applied multilib hack from RH's libtool package.

* Mon Sep 19 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.20-alt1
- Updated to 1.5.20.

* Thu May 26 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.18-alt2
- Corrected License tags (#6704).
- Rediffed patches.

* Wed May 18 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.18-alt1
- Updated to 1.5.18.

* Tue Apr 26 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.16-alt1
- Updated to 1.5.16.
- Updated link_all_deplibs patch.

* Sun Feb 13 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.14-alt1
- Updated to 1.5.14.

* Sun Feb 06 2005 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.12-alt1
- Updated to 1.5.12.
- Rediffed few patches, dropped obsolete RH patches.
- Dropped custom ld.so.conf include syntax support,
  in favour of upstream solution for the same issue.
- Converted alternatives config file to new format (0.2.0).

* Sun Nov 28 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.10-alt1
- Updated to 1.5.10.
- Enhanced CXX fix introduced in this version.
- Backported ltmain.in func_mode_link fix from libtool cvs.
- Applied patch from Owl to prevent build host name leaks
  into the generated libtool script.
- Disabled alt-ltmain-cpp-linkage hack,
  hopefully no longer needed.
- Implemented ld.so.conf include syntax support.

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.8-alt1
- Updated to 1.5.8.

* Tue Apr 13 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.6-alt1
- Updated to 1.5.6.

* Thu Apr 08 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.4-alt2
- Updated legacy patch (added shrext_cmds initialization).
- Applied fix for LTDL_SHLIB_EXT initialization from upstream.

* Wed Apr 07 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.4-alt1
- Updated to 1.5.4, updated patches.
- Updated link_all_deplibs patch (Scott James Remnant).
- Applied ltdl fix (Scott James Remnant).

* Thu Feb 26 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.2-alt2
- libtool-demo: do not package obsolete mkinstalldirs.

* Wed Feb 04 2004 Dmitry V. Levin <ldv@altlinux.org> 3:1.5.2-alt1
- Updated to 1.5.2.
- Merged upstream patches:
  jh-expsym-linux
  rh-readonlysym
  rh-relink-libdir-order-91110
  rh-AC_PROG_LD_GNU-quote-v-97608
  rh-nostdlib
- Applied additional link_all_deplibs-runtime patch
  from Alexey Morozov.
- Disabled alt-tagconfig-deps patch for a while,
  it causes unwanted side effects.
- Added requires on fixed autoconf so #3414 will not arise
  again in its worst form.

* Mon Dec 29 2003 Dmitry V. Levin <ldv@altlinux.org> 3:1.5-alt11
- libtool.m4:_LT_AC_TAGCONFIG: fixed dependence loop problem
  (#3414).

* Tue Dec 02 2003 Dmitry V. Levin <ldv@altlinux.org> 3:1.5-alt10
- Rewritten ltmain tmp handling fix.
- Ensure that EGREP and max_cmd_len variables are defined
  in ltmain, to support legacy configure scripts.

* Sun Nov 30 2003 Dmitry V. Levin <ldv@altlinux.org> 3:1.5-alt9
- libltdl-devel: do not package .la files.

* Sun Nov 16 2003 Dmitry V. Levin <ldv@altlinux.org> 3:1.5-alt8
- Set link_all_deplibs=no for linux, to avoid linking a program
  against all its dependency lib tree.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 3:1.5-alt7
- Additional convention enforcement on patch file names.
- Raised serial number.

* Wed Aug 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2:1.5-alt6
- Reverted to libltdl
- Corrected libtoolize to expect ltdl.m4 in %_datadir/aclocal

* Tue Aug 19 2003 Dmitry V. Levin <ldv@altlinux.org> 2:1.5-alt5
- Renamed libltdl to libltdl3.
- Updated interpackage dependencies.
- Updated build dependencies.
- Deal with info dir entries such that the menu looks pretty.
- Do not create %_datadir/%libtool/aclocal/ltdl.m4 symlink
  (may reference to non-existing file).

* Tue Aug 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2:1.5-alt4
- Renamed to libtool_1.5 to install together with legacy libtool_1.4.
  Paths modified accordingly. libltdl is left unsplit though.
- Moved demos to a dedicated package named libtool-demos
- Corrected descriptions for libltdl

* Sat Aug 16 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2:1.5-alt3
- Define SED in ltmain.sh for legacy ltconfig's [Patch0]
- Disable distclean'ing of demo subdirs if check target has not been made

* Wed Aug 13 2003 Dmitry V. Levin <ldv@altlinux.org> 2:1.5-alt2
- Updated package dependencies.
- Updated build dependencies.
- Minor specfile cleanup.

* Sat Aug 09 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2:1.5-alt1
- New version
- Synchronized with RedHat package 1.5-5
- Override compiler tests in configure
- Bzip the changelogs
- Symlink the licenses to the shared license directory

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
- Re-splitted into libtool and libtool-libs.

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
