Name: groff
Version: 1.20.1
Release: alt0.20091013.1

Summary: A document formatting system
License: GPL
Group: Text tools
Url: ftp://ftp.gnu.org/gnu/%name
Packager: Alexey Gladkov <legion@altlinux.ru>

Source: %url/%name-%version.tar.gz
Source1: mandoc.local

Patch1: %name-1.19-alt-new_fonts.patch
Patch2: %name-1.19.1-alt-texinfo.patch
Patch3: %name-1.19.1-alt-use_system_getopt.patch
Patch6: %name-1.19.1-alt-tty-old_drawing_scheme.patch
Patch8: %name-1.19.1-rh-nohtml.patch
Patch9: %name-1.19.3-alt-nroff.patch
Patch10: %name-1.20.1-alt-perl.patch
Patch11: %name-1.19.3-fix-unicode-tmac.patch
Patch12: %name-1.19.3-add-T8bit.patch
Patch13: %name-1.20.1-replace-virmf.patch

PreReq: %name-base = %version-%release
Requires: %name-dvi = %version-%release
Requires: %name-lbp = %version-%release
Requires: %name-lj4 = %version-%release
Requires: %name-ps = %version-%release
Requires: %name-x11 = %version-%release
Requires: %name-extra = %version-%release

# Automatically added by buildreq on Mon Aug 21 2006
BuildRequires: fonts-type1-urw gcc-c++ ghostscript-module-X groff-base imake
BuildRequires: libXaw-devel netpbm psutils tcsh xorg-cf-files
BuildRequires: perl-Math-Complex

%package base
Summary: Parts of the %name formatting system that is required for viewing manpages
Group: Text tools
Provides: %name-tools, %name-for-man
Obsoletes: %name-tools, %name-for-man
Conflicts: %name < %version-%release
PreReq: coreutils

%package dvi
Summary: TeX dvi format driver for %name
Group: Text tools
Requires: %name-base = %version-%release

%package lbp
Summary: Canon CAPSL and VDM formats driver for %name
Group: Text tools
Requires: %name-base = %version-%release

%package lj4
Summary: HP Laserjet 4 family formats driver for %name
Group: Text tools
Requires: %name-base = %version-%release

%package ps
Summary: PostScript driver for %name
Group: Text tools
Requires: %name-base = %version-%release

%package x11
Summary: An X previewer for %name text processor output
Group: Text tools
Provides: %name-gxditview = %version-%release
Obsoletes: %name-gxditview, gxditview
Requires: %name-base = %version-%release

%package extra
Summary: Additional %name components
Group: Text tools
Requires: %name-base = %version-%release

%description
Groff is a document formatting system.  Groff takes standard text and
formatting commands as input and produces formatted output.  The
created documents can be shown on a display or printed on a printer.
Groff's formatting commands allow you to specify font type and size, bold
type, italic type, the number and size of columns on a page, and more.

%description base
A stripped-down %name package containing the components required
to view man pages in ASCII, Latin-1 and UTF-8.

For a full %name installation, install %name package.

%description dvi
This package contains grodvi - driver for %name that produces TeX dvi format,
and corresponding files.

%description lbp
This package contains grolbp - driver for %name that produces output in
CAPSL and VDM format suitable for Canon LBP-4 and LBP-8 printers,
and corresponding files.

%description lj4
This package contains grolj4 - driver for %name that produces PCL5 format output
suitable for HP Laserjet 4 family printers, and corresponding files.

%description ps
This package contains grops - driver for %name that produces PostScript format,
and corresponding files.

%description x11
This package contains gxditview - program that displays the %name text
processor's output on an X Window System display, and corresponding files.

%description extra
This package contains additional %name components.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p2
%patch11 -p1
%patch12 -p1
%patch13 -p1

# Purge self-contained getopt.
rm -f src/include/getopt.h src/libs/lib%name/getopt*

%build
# Force parser regeneration.
find -type f -name \*.y |while read f; do
	rm -fv ${f%%.y}.cc
done

# Precache parameters.
export YACC='bison -y' PAGE=A4

%configure

# Ensure mkstemp is found.
grep -qs '^#define HAVE_MKSTEMP 1' src/include/config.h

%make_build

%install
mkdir -p -- $RPM_BUILD_ROOT%prefix
%makeinstall \
	manroot=$RPM_BUILD_ROOT%_mandir \
	indexdir=$RPM_BUILD_ROOT%_datadir/dict/papers \
	appresdir=$RPM_BUILD_ROOT%_x11appconfdir \
	#

# Add ALT specific (deb-based).
cat %SOURCE1 >>$RPM_BUILD_ROOT%_datadir/%name/site-tmac/man.local
cat %SOURCE1 >>$RPM_BUILD_ROOT%_datadir/%name/site-tmac/mdoc.local

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/buildreqs/files/ignore.d
cat >$RPM_BUILD_ROOT%_sysconfdir/buildreqs/files/ignore.d/%name <<EOF
^%_datadir/%name(/%version(/font)\?)\?\$
EOF

# Relocate config files.
mv $RPM_BUILD_ROOT%_datadir/%name/site-tmac $RPM_BUILD_ROOT%_sysconfdir/%name
ln -s -- %_sysconfdir/%name $RPM_BUILD_ROOT%_datadir/%name/site-tmac

# Required for PATCH12
ln -s -- devutf8 "$RPM_BUILD_ROOT%_datadir/%name/%version/font/dev8bit"

# <BEGIN BLACK MAGIC
for p in s m mse; do
	ln -s -- "$p.tmac" "$RPM_BUILD_ROOT%_datadir/%name/%version/tmac/g$p.tmac"
done

for f in $RPM_BUILD_ROOT{%_bindir,%_mandir/man*}/*; do
	n="${f##*/}"
	if [ -n "${n##*2*}" -a -n "${n##*-*}" -a -n "${n%%%%g*}" ]; then
		d="${f%%/*}/g$n"
		if [ ! -e "$d" ]; then
			ln -s -- "$n" "$d"
		fi
	fi
done
# END BLACK MAGIC>

# Prepare file lists.
find $RPM_BUILD_ROOT%_bindir $RPM_BUILD_ROOT%_mandir -type f -o -type l |
	sed -e "s|$RPM_BUILD_ROOT||g" |
	grep -E '/g?(eqn|groff|grog|grotty|neqn|nroff|pic|preconv|refer|soelim|tbl|troff)(\.|$)' |
	sed 's|\(/man/.*\.[0-9]\)\(.*\)|\1*|g' >%name-base.files

find $RPM_BUILD_ROOT%_bindir $RPM_BUILD_ROOT%_mandir -type f -o -type l |
	sed -e "s|$RPM_BUILD_ROOT||g" |
	grep -E '/g?(xditview|xtotroff)(\.|$)' |
	sed 's|\(/man/.*\.[0-9]\)\(.*\)|\1*|g'>%name-x11.files

find $RPM_BUILD_ROOT%_bindir $RPM_BUILD_ROOT%_mandir/ -type f -o -type l |
	sed -e "s|$RPM_BUILD_ROOT||g" |
	grep -Ev '/g?(eqn|groff|grog|grodvi|grolbp|grolj4|grotty|grops|neqn|nroff|pic|preconv|refer|soelim|tbl|troff|xditview|xtotroff)(\.|$)' |
	sed 's|\(/man/.*\.[0-9]\)\(.*\)|\1*|g' >%name-extra.files

# Prepare docs.
install -p -m644 BUG-REPORT ChangeLog MORE.STUFF NEWS PROBLEMS PROJECTS README TODO \
	$RPM_BUILD_ROOT%_docdir/%name-%version/
rm -f $RPM_BUILD_ROOT%_docdir/%name-%version/*.m?
bzip2 -9 $RPM_BUILD_ROOT%_docdir/%name-%version/*.ps 

mkdir -p $RPM_BUILD_ROOT%_docdir/%name-%version/X11
install -p -m644 src/devices/xditview/{ChangeLog,README,TODO} \
	$RPM_BUILD_ROOT%_docdir/%name-%version/X11/

%define r_dir %_sysconfdir/%name
%define r_link %_datadir/%name/site-tmac

%pre base
f=%r_link
if [ -d "$f" -a ! -L "$f" ]; then
	rm -rf "$f"
	/bin/touch "$f.RPMLOCK"
fi

%post base
d=%r_dir
f=%r_link
if [ -f "$f.RPMLOCK" -a -d "$d" -a ! -d "$d.RPMSAVE" ]; then
	mv "$d" "$d.RPMSAVE"
	rm -f "$f.RPMLOCK"
fi

%triggerpostun base -- %name-base < 0:1.18.1-alt2, %name < 0:0:1.18.1-alt1
d=%r_dir
if [ -d "$d.RPMSAVE" -a ! -d "$d" ]; then
	mv "$d.RPMSAVE" "$d"
fi

%files

%files base -f %name-base.files
%config %_sysconfdir/buildreqs/files/ignore.d/%name
%config %_sysconfdir/%name
%_libdir/%name
%dir %_datadir/%name
%_datadir/%name/site-tmac
%dir %_datadir/%name/%version
%_datadir/%name/%version/eign
%_datadir/%name/%version/tmac
%dir %_datadir/%name/%version/font
%_datadir/%name/%version/font/devascii
%_datadir/%name/%version/font/devlatin1
%_datadir/%name/%version/font/devutf8
%_datadir/%name/%version/font/dev8bit
%dir %_docdir/%name-%version
%_docdir/%name-%version/[ABD-WYZ]*
%exclude %_libdir/%name/groffer

%files dvi
%_bindir/grodvi
%_man1dir/grodvi.*
%dir %_datadir/%name
%dir %_datadir/%name/%version
%dir %_datadir/%name/%version/font
%_datadir/%name/%version/font/devdvi

%files lbp
%_bindir/grolbp
%_man1dir/grolbp.*
%dir %_datadir/%name
%dir %_datadir/%name/%version
%dir %_datadir/%name/%version/font
%_datadir/%name/%version/font/devlbp

%files lj4
%_bindir/grolj4
%_man1dir/grolj4.*
%dir %_datadir/%name
%dir %_datadir/%name/%version
%dir %_datadir/%name/%version/font
%_datadir/%name/%version/font/devlj4

%files ps
%_bindir/grops
%_man1dir/grops.*
%dir %_datadir/%name
%dir %_datadir/%name/%version
%dir %_datadir/%name/%version/font
%_datadir/%name/%version/font/devps

%files x11 -f %name-x11.files
%config %_x11appconfdir/GXditview*
%dir %_datadir/%name
%dir %_datadir/%name/%version
%dir %_datadir/%name/%version/font
%_datadir/%name/%version/font/devX*
%dir %_docdir/%name-%version
%_docdir/%name-%version/X11

%files extra -f %name-extra.files
%_infodir/*.info*
%_libdir/%name/groffer
%dir %_datadir/%name
%dir %_datadir/%name/%version
%dir %_datadir/%name/%version/font
%_datadir/%name/%version/font/devhtml
%_datadir/%name/%version/pic
%dir %_docdir/%name-%version
%_docdir/%name-%version/ChangeLog*
%_docdir/%name-%version/[a-z]*

%changelog
* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.20.1-alt0.20091013.1
- rebuilt with perl 5.12

* Tue Oct 13 2009 Alexey Gladkov <legion@altlinux.ru> 1.20.1-alt0.20091013
- New release (1.20.1 20091013).
- Remove obsolete rpm macros.
- Replace obsolete "virmf" with "mf --base=plain".

* Mon Dec 15 2008 Alexey Gladkov <legion@altlinux.ru> 1.19.3-alt3.20081215
- New cvs snapshot (1.19.3 cvs20081215).
- Fix special characters for 8-bit encodings.

* Mon Nov 17 2008 Alexey Gladkov <legion@altlinux.ru> 1.19.3-alt3.20081113
- New cvs snapshot (1.19.3 cvs20081113).

* Fri Sep 12 2008 Alexey Gladkov <legion@altlinux.ru> 1.19.3-alt3.20080912
- New cvs snapshot (1.19.3 cvs20080912).
- Fix unicode.tmac.

* Wed Aug 27 2008 Alexey Gladkov <legion@altlinux.ru> 1.19.3-alt2.20080822
- Fixed ALT#16878.

* Fri Aug 22 2008 Alexey Gladkov <legion@altlinux.ru> 1.19.3-alt1.20080822
- New cvs snapshot (1.19.3 cvs20080822).
- Update patches texinfo, nroff and nohtml.
- Fixed ALT#6988, ALT#13685.

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.19.2-alt2.0
- Automated rebuild.

* Mon Aug 21 2006 Alexey Gladkov <legion@altlinux.ru> 1.19.2-alt2
- Fix packages requires.

* Mon Aug 14 2006 Alexey Gladkov <legion@altlinux.ru> 1.19.2-alt1
- NMU.
- New version (1.19.2).
- Fixed rpm macro expantion.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.19.1-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Jan 11 2005 Alexey Voinov <voins@altlinux.ru> 1.19.1-alt1
- new version (1.19.1)
- texinfo patch updated
- use_system_getopt patch updated
- glibc patch updated
- tty-old_drawing_scheme patch updated
- pfbtops_cpp patch updated
- nohtml patch updated
- nroff patch updated
- dblfclose patch removed

* Wed Apr 28 2004 Alexey Voinov <voins@altlinux.ru> 1.19-alt3
- Fixed double call to fclose, that caused memory corruption
  [dblfclose patch]
- Fixed problem with info file installation [infoinst patch]

* Tue Apr 27 2004 Dmitry V. Levin <ldv@altlinux.org> 1.19-alt2
- Fixed build with fresh glibc headers:
  + do not override system getopt(3) prototype.

* Fri Feb 27 2004 Alexey Voinov <voins@altlinux.ru> 1.19-alt1
- new version (1.19)
- patches updated

* Thu Nov 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1.18.1-alt6
- Fixed groff upgrade problem (introduced in -alt5).

* Tue Nov 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1.18.1-alt5
- Fixed groff upgrade problem (introduced in -alt2).
- Patched nroff to use -Tlatin1 by default.

* Sun Nov 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1.18.1-alt4
- Relocated refer from -extra to -base.
- Patched nroff to use -Tlatin1 for KOI8-R/CP1251
  and -Tascii for ANSI_X3.4-1968.

* Thu Oct 24 2002 Dmitry V. Levin <ldv@altlinux.org> 1.18.1-alt3
- Fixed texinfo installation scripts (reported by Grigory Milev).

* Mon Oct 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1.18.1-alt2
- Moved all stuff from %name to -extra subpackage.
  We now use %name to install all %name components.
- Relocated %_datadir/%name/site-tmac -> %_sysconfdir/%name.

* Sat Oct 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1.18.1-alt1
- Updated to 1.18.1 (a lot of changes, see NEWS file for details).
- Removd README.A4
- Removed troff-to-ps.fpi
- Removed patches:
  + owl-latin1-shc-hack (better fix in upstream);
  + pre-html-mkdtemp (better fix in upstream);
  + zen-preproc-pic (merged upstream);
  + owl-grn-bound (merged upstream).
- Reviewed RH patches (groff-1.18-7):
  + 1.18-1: japanese support, unneeded;
  + 1.16-safer: unneeded;
  + 1.18-info: we have better patch;
  + 1.18-nohtml: applied as 1.18-rh-nohtml;
  + 1.18-patch: merged upstream;
  + 1.18-pfbtops_cpp: applied as 1.18-rh-pfbtops_cpp.
- Reviewed MDK patches (groff-1.18-4mdk):
  + 1.18-1: japanese support, unneeded;
  + 1.18-ia64-fix: merged upstream;
  + 1.18-unbrkble-spc-fix: merged upstream;
  + 1.18-warning-fixes: merged upstream;
  + 1.16.1-no-lbp-on-alpha: unneeded;
  + 1.17.2-libsupc++: unneeded;
  + 1.18-info: we have better patch;
  + 1.18-koi8-r: non-obvious;
  + 1.18-nohtml: applied as 1.18-rh-nohtml; 
- Fixed texinfo documentation (added in this version).
- Added man/mdoc ALT specific definitions (deb-based).
- Ensure parser gets regenerated during %%build.
- Fixed syntax error in pic2graph script.
- Don't build self-contained getopt, use system one.
- Added more documentation.
- Split %name subpackage into -dvi, -lbp, -lj4, -ps and -base
  subpackages.
- Renamed %name-gxditview subpackage to %name-x11.
- Merged %name-perl subpackage into %name subpackage.
- grotty: reverted to old drawing scheme by default.

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.17.2-alt4
- Added patch (owl-grn-bound) from Owl.

* Wed Sep 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.17.2-alt3
- Updated tmac black magic.

* Thu Aug 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.17.2-alt2
- Fixed format bug in preproc/pic.y (zen-parse).

* Mon Aug 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.17.2-alt1
- 1.17.2
- Patched pre-html.cc to use mkdtemp.
- Moved app-defaults/GXditview to %_sysconfdir/X11/app-defaults/.
+ Applied Owl patches:
  - README.A4 updates (mention grops -g and a4.tmac)
  - Patched the soft hyphen character out of the latin1 device such that
    latin1 may be used with non-Latin-1 8-bit character sets.  We might
    add an ascii8 device in the future.  Why this is needed is explained
    at http://www.ffii.org/archive/mails/groff/2000/Nov/0050.html
  - Enable mkstemp explicitly, not rely on configure.

* Thu Apr 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.16.1-ipl10mdk
- Rebuilt with new rpm-build to fix dependencies.

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.16.1-ipl9mdk
- Merged changes listed below.

* Fri Nov 17 2000 AEN <aen@logic.ru>
- KOI8-R, CP1251 and PT154 fonts added

* Tue Nov 16 2000 AEN <aen@logic.ru>
- Some i18n tricks.

* Thu Aug  3 2000 Dmitry V. Levin <ldv@fandra.org> 1.16.1-ipl1mdk
- 1.16.1

* Mon Jun 26 2000 Dmitry V. Levin <ldv@fandra.org> 1.16-ipl1mdk
- RE adaptions.

* Fri Jun  9 2000 Bill Nottingham <notting@redhat.com>
- move mmroff to -perl

* Wed Jun  7 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix build
- FHS
- 1.16

* Sun May 14 2000 Jeff Johnson <jbj@redhat.com>
- install tmac.mse (FWIW tmac.se looks broken) to fix dangling symlink (#10757).
- add README.A4, how to set up for A4 paper (#8276).
- add other documents to package.

* Thu Mar  2 2000 Jeff Johnson <jbj@redhat.com>
- permit sourcing on regular files within cwd tree (unless -U specified).

* Wed Feb  9 2000 Jeff Johnson <jbj@redhat.com>
- fix incorrectly installed tmac.m file (#8362).

* Mon Feb  7 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- check if build system is sane again

* Thu Feb 03 2000 Cristian Gafton <gafton@redhat.com>
- fix description and summary
- man pages are compressed. This is ugly.

* Mon Jan 31 2000 Bill Nottingham <notting@redhat.com>
- put the binaries actually in the package *oops*

* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- split perl components into separate subpackage

* Wed Jan  5 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Mon Jan  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.15-1mdk
- 1.15.

* Thu Oct 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix building as user.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- fix handling of RPM_OPT_FLAGS

* Tue Feb 16 1999 Cristian Gafton <gafton@redhat.com>
- glibc 2.1 patch for xditview (#992)

* Thu Oct 22 1998 Bill Nottingham <notting@redhat.com>
- build for Raw Hide

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- fix makefiles to work with bash2

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- use g++ for C++ code

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- manhattan and buildroot

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- made xdefaults file a config file

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- split perl components into separate subpackage

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated to 1.11a
- added safe troff-to-ps.fpi

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- removed troff-to-ps.fpi for security reasons.

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc
