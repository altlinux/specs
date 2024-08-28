Name: ddd
Version: 3.4.1
Release: alt1

Summary: Graphical debugger front-end for GDB, DBX, Ladebug, JDB, Perl, Python
License: GPLv2+
Group: Development/Other

Url: http://www.gnu.org/software/%name/
Packager: Ilya Mashkin <oddity@altlinux.ru>
# ftp://alpha.gnu.org/gnu/%name/
Source: ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz
Source3: http://www.cs.tu-bs.de/softech/ddd/ftp/doc/vse.ps.bz2

Patch1: ddd-3.3.8-alt-texinfo.patch
Patch2: ddd-texinfo-5.0.patch
Patch3: ddd-buildcompare.patch
Patch4: ddd-wrong-memcpy.patch
Patch5: ddd-3.3.12-alt-e2k-lcc.patch
Patch6: ddd-3.3.12-make_gcc_happy.patch
Patch7: ddd-3.3.12-debuginfo.patch

Requires: gdb
Obsoletes: ddd-static, ddd-semistatic, ddd-dynamic

# Added by buildreq2 on Чтв Окт 05 2006
BuildRequires: flex gcc-c++ libX11-devel libXext-devel libXi-devel libXaw-devel libXp-devel libreadline-devel libtinfo-devel openmotif-devel texinfo

BuildRequires: makeinfo

%package doc-html
Summary: HTML documentation for %name
Group: Development/Other
Requires: %name = %version-%release

%package doc-ps
Summary: PostScript documentation for %name
Group: Development/Other
Requires: %name = %version-%release

%description
DDD is a graphical front-end for command-line debuggers such as GDB,
DBX, WDB, Ladebug, JDB, XDB, the Perl debugger, or the Python debugger.
Besides "usual" front-end features such as viewing source texts, DDD has
become famous through its interactive graphical data display, where data
structures are displayed as graphs.

%description doc-html
DDD is a graphical front-end for command-line debuggers such as GDB,
DBX, WDB, Ladebug, JDB, XDB, the Perl debugger, or the Python debugger.
Besides "usual" front-end features such as viewing source texts, DDD has
become famous through its interactive graphical data display, where data
structures are displayed as graphs.

This packages contains HTML documentation for DDD.

%description doc-ps
DDD is a graphical front-end for command-line debuggers such as GDB,
DBX, WDB, Ladebug, JDB, XDB, the Perl debugger, or the Python debugger.
Besides "usual" front-end features such as viewing source texts, DDD has
become famous through its interactive graphical data display, where data
structures are displayed as graphs.

This packages contains PostScript documentation for DDD.

%prep
%setup
#patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p1
#patch5 -p1
#patch6 -p0
%patch7  -p1

install -pm644 %SOURCE3 doc/
#rm -f doc/html/%name.html ddd/*.info*
touch ddd/ddd.info.txt
find -type f -name \*.orig -print -delete

%build
#set_automake_version 1.10
##set_autoconf_version 2.5
autoreconf -fi
# Fix build via precaching configure variables.
#export \
#	ac_cv_func_alloca=yes \
#	ac_cv_lib_dnet=no \
#	ac_cv_lib_dnet_dnet_ntoa=no \
#	ac_cv_lib_dnet_stub_dnet_ntoa=no \
#	ac_cv_header_elf_h=no \
#	ac_cv_header_libelf_h=no \
#	ac_cv_header_sys_elf_h=no \
#	ac_cv_lib_elf_elf_version=no \
#	ice_cv_external_templates=no \
#	ice_cv_have_named_return_values=no \
#	ac_cv_path_RSH=ssh \
#	ac_cv_prog_DEBUGGER=gdb \
#	ac_cv_prog_LPR=lpr \
#	ac_cv_prog_XTERM=xvt \
#	#

# Fix tinfo support.
find -type f -name configure -print0 |
	xargs -r0 subst -p 's/mytinfo/tinfo/g' configure*

%add_optflags -DWITH_READLINE
%configure --with-readline

rm -rf readline libiberty

# Fix packager information.
cat >ddd/userinfo.C <<__EOF__
#include <stdio.h>
int main (void){ puts ("%packager"); return 0; }
__EOF__

%make_build LIBREADLINE=-lreadline
#bzip2 -9fk doc/*.ps

%install
mkdir -p $RPM_BUILD_ROOT%_libdir
%makeinstall

rm -fv $RPM_BUILD_ROOT%_datadir/%name-%version/[A-Z]*
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/X11/app-defaults
#mv $RPM_BUILD_ROOT%_datadir/%name-%version/%name/ddd $RPM_BUILD_ROOT%_sysconfdir/X11/app-defaults
#rmdir $RPM_BUILD_ROOT%_datadir/%name-%version/%name

%define docdir %_docdir/%name-%version
rm -rf $RPM_BUILD_ROOT%docdir
mkdir -p $RPM_BUILD_ROOT%docdir
cp -a  doc/*.ps.* doc/html \
	$RPM_BUILD_ROOT%docdir/

# The manpage installed contains a reference to a logo .eps file in the
# build directory which isn't even created; remove this reference to
# eliminate man warnings.
sed -i -e '/^\.PSPIC/d' %buildroot/%_man1dir/ddd.1

%files
#config %_sysconfdir/X11/app-defaults/*
%_bindir/*
%_datadir/%name-%version
%_mandir/man?/*
%_infodir/*.info*
%_desktopdir/%name.desktop
%dir %docdir
#docdir/*

%files doc-ps
%dir %docdir
%docdir/*.ps.*

%files doc-html
%dir %docdir
%docdir/html

%changelog
* Wed Aug 28 2024 Ilya Mashkin <oddity@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Sun Aug 06 2023 Ilya Mashkin <oddity@altlinux.ru> 3.4.0-alt1
- 3.4.0
- Update License tag to GPLv2+

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 3.3.12-alt4
- Fixed FTBFS.

* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 3.3.12-alt3
- fixed build on e2k with lcc

* Thu Feb 07 2019 Grigory Ustinov <grenka@altlinux.org> 3.3.12-alt2
- Rebuild with libreadline7 and new gcc-c++.
- Package desktop file.

* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 3.3.12-alt1.qa2
- NMU:
  + fixed FTBFS (BR: makeinfo and opensuse texinfo-5.0 patch)
  + added two more opensuse patches (reproducible, memcpy)
  + added debian fixup for ddd(1) manpage
  + minor spec cleanup

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.3.12-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Sep 03 2009 Ilya Mashkin <oddity@altlinux.ru> 3.3.12-alt1
- 3.3.12
- remove old macros

* Sun Aug 30 2009 Ilya Mashkin <oddity@altlinux.ru> 3.3.11-alt2.2
- Rebuild from orphaned

* Wed Dec 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.3.11-alt2.1
- NMU:
  * updated build dependencies

* Sat Mar 29 2008 Damir Shayhutdinov <damir@altlinux.ru> 3.3.11-alt2
- Added gdb to Requires (#10974)

* Thu Oct 05 2006 Damir Shayhutdinov <damir@altlinux.ru> 3.3.11-alt1
- New version.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.3.8-alt1.1.1
- Rebuilt with libreadline.so.5.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.3.8-alt1.1
- Rebuilt with libstdc++.so.6.

* Thu May 06 2004 Dmitry V. Levin <ldv@altlinux.org> 3.3.8-alt1
- Updated to 3.3.8.
- Updated patches.
- Repackaged documentation.
- Fixed readline support.

* Fri Sep 12 2003 Dmitry V. Levin <ldv@altlinux.org> 3.3.1-alt5
- Fixed python support (#2922).
- Updated build dependencies.

* Tue Nov 19 2002 Dmitry V. Levin <ldv@altlinux.org> 3.3.1-alt4
- Use xvt instead of xterm.
- Fix packager information.

* Mon Nov 18 2002 Dmitry V. Levin <ldv@altlinux.org> 3.3.1-alt3
- Merged RH patch for gcc-3.2 support.
- Fixed build via precaching configure variables.
- Linked with -ltinfo.
- Additional convention enforcement on patch file names.
- Packaged Python debugger.

* Fri Apr 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.3.1-alt2
- Rebuilt with openmotif-2.2.2.

* Mon Oct 15 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.3.1-alt1
- 3.3.1

* Mon Feb 05 2001 Dmitry V. Levin <ldv@fandra.org> 3.3-ipl1mdk
- 3.3

* Wed Jan 24 2001 Dmitry V. Levin <ldv@fandra.org> 3.2.98-ipl2mdk
- Create tmpfiles in more secure way.

* Thu Jan 18 2001 Dmitry V. Levin <ldv@fandra.org> 3.2.98-ipl1mdk
- 3.2.98

* Thu Jan 11 2001 Dmitry V. Levin <ldv@fandra.org> 3.2.95-ipl1mdk
- 3.2.95

* Sat Dec 30 2000 Dmitry V. Levin <ldv@fandra.org> 3.2.93-ipl2mdk
- Updated html documentation.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 3.2.93-ipl1mdk
- 3.2.93
- Added font patch (from AEN).
- Added menu entry.

* Mon Dec 04 2000 Dmitry V. Levin <ldv@fandra.org> 3.2.92-ipl1mdk
- 3.2.92
- FHSification.
- Fixed texinfo documentation.

* Thu Jun 22 2000 Dmitry V. Levin <ldv@fandra.org>
- 3.2.90
- Build with external readline libraries.
- Made separate doc-html and doc-ps packages.

* Mon May 22 2000 AEN <aen@logic.ru>
- build for RE with new spec

* Wed Nov 3  1999 Mirko Streckenbach <strecken@fmi.uni-passau.de>
- Initial skeleton, based on the .specs from gnome-libs-1.0.17 and
  redhat 6.1 tar-1.13.11
