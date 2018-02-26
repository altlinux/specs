%def_with demos
%def_disable static
%define soname 4

Name: openmotif
Version: 2.3.3
Release: alt2.1

Summary: The Open Motif
License: Open Group Public License
Group: System/Libraries

Url: http://www.openmotif.org
Source: ftp://ftp.ics.com/openmotif/2.3/%version/%name-%version.tar.gz

### NB: most 2.2.x patches were either already applied upstream
### or failed to apply to 2.3.2, see setup section
# RH
Patch1: openMotif-2.2.3-rh-acinclude.patch
Patch2: openMotif-2.2.3-rh-char_not_supported.patch
Patch3: openMotif-2.2.3-rh-libdir.patch
Patch4: openMotif-2.2.3-rh-long64.patch
Patch5: openMotif-2.2.3-rh-multiscreen.patch
Patch6: openMotif-2.2.3-rh-pixel_length.patch
Patch7: openMotif-2.2.3-rh-popup_timeout.patch
Patch8: openMotif-2.2.3-rh-uil_lib.patch
Patch9: openmotif-2.2.3-rh-utf8.patch
Patch10: openMotif-2.2.3-rh-vizcount.patch
# CAN, CVE
Patch21: openMotif-2.2.3-CAN-2004-0687-0688.patch
Patch22: openMotif-2.2.3-CAN-2004-0914.patch
Patch23: openmotif-2.2.3-CAN-2004-0914_sec8.patch
Patch24: openmotif-CVE-2005-3964.patch
# misc
Patch31: openMotif-2.2.3-motifzone_1193.patch
Patch32: openMotif-2.2.3-motifzone_1202.patch
Patch33: openMotif-2.2.3-rgbtxt.patch
# ALT
Patch41: openmotif-2.2.2-alt-DefaultUserPath.patch
Patch42: openmotif-2.2.2-alt-VARDIR.patch
Patch43: openmotif-2.2.2-alt-bison.patch
Patch44: openmotif-2.2.3-alt-VERSION.patch
# PLD
Patch51: openmotif-makedepend.patch
Patch52: openmotif-mwmrc.patch
Patch53: openmotif-bison.patch
Patch54: openmotif-freetype.patch
Patch55: openmotif-parbuild.patch
Patch56: openmotif-libtool.patch
Patch57: openmotif-2.3.3-alt-DSO.patch

Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Feb 28 2011
BuildRequires: flex libXext-devel libXft-devel libXmu-devel libXp-devel libjpeg-devel libpng-devel xorg-bitmaps xorg-cf-files

%define libname lib%name
%define libnameso lib%name%soname
%define _x11sysconfdir %_sysconfdir/X11

%package -n %libnameso
Summary: The Open Motif shared libraries
Group: System/Libraries
Provides: %name = %version
Obsoletes: %name < %version

%package -n %libname-devel
Summary: Include files for OpenMotif development
Group: Development/C
Requires: %libnameso = %version-%release
Conflicts: lesstif-devel
Provides: motif-devel = %version
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%package -n %libname-devel-static
Summary: Static libraries for OpenMotif development
Group: Development/C
Requires: %libname-devel = %version-%release
Conflicts: lesstif-devel-static
Provides: motif-devel-static = %version
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static < %version

%package mwm
Summary: Motif window manager
Group: Graphical desktop/Motif
Requires: %libnameso = %version-%release
Conflicts: lesstif-mwm
Provides: motif-mwm = %version-%release

%package clients
Summary: Motif clients
Group: Graphical desktop/Motif
Requires: %libnameso = %version-%release
Conflicts: lesstif-clients
Provides: motif-clients = %version-%release

%package demos
Summary: OpenMotif demo applications
Group: Development/C
Requires: %libnameso = %version-%release

%description
This package intentionally left blank.

%description -n %libnameso
The industry standard user interface toolkit for the X Window System.
This package contains shared libraries to run Motif applications.

%description -n %libname-devel
The industry standard user interface toolkit for the X Window System.
This package contains header files to develop Motif applications.

%description -n %libname-devel-static
The industry standard user interface toolkit for the X Window System.
This package contains the Motif static libraries.

%description mwm
The industry standard user interface toolkit for the X Window System.
This package contains mwm, Motif window manager.

%description clients
The industry standard user interface toolkit for the X Window System.
This package contains uil and xmbind.

%description demos
The industry standard user interface toolkit for the X Window System.
This package contains the Motif demo applications.

%prep
%setup
# RH
%patch4 -p1
%patch7 -p1
%patch8 -p1
# ALT
%patch41 -p1
%patch42 -p1
%patch44 -p1
# PLD
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch57 -p2

find -type f -name \*.orig -print -delete

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
libtoolize --copy --force
%configure --enable-shared %{subst_enable static}

make clean
# SMP-incompatible build (still true for 2.3.2)
%make

%install
mkdir -p %buildroot%_x11sysconfdir/{app-defaults,mwm,xinit.d}
ln -s ../../..%_x11bindir/xmbind %buildroot%_x11sysconfdir/xinit.d/

%makeinstall_std
mv %buildroot%_libdir/X11/system.mwmrc %buildroot%_x11sysconfdir/mwm
for f in %buildroot%_libexecdir/app-defaults/*; do
	[ -f "$f" ] || continue
	mv "$f" %buildroot%_x11sysconfdir/app-defaults/
done

%if_with demos
find %buildroot%_datadir/Xm -type f -perm +111
find %buildroot%_datadir/Xm -type f -perm +111 -exec mv '{}' %buildroot%_bindir/ \;
ls %buildroot%_bindir/* \
| sed -e "s,%buildroot,,g" \
| grep -Ev '/(mwm|uil|xmbind)$' >demos.list ||:
%endif

# Assist cpp.req by using fake pkgconfig file.
install -pD -m644 {,%buildroot}%_pkgconfigdir/xft.pc

%pre -n %libname-devel
rm -f %_x11includedir/{Mrm,Xm} >/dev/null 2>&1 ||:

%files -n %libnameso
%_libdir/*.so.*
%doc BUGREPORT COPYRIGHT.MOTIF RELNOTES TODO

%files -n %libname-devel
%_libdir/*.so
%_includedir/Mrm
%_includedir/Xm
%_includedir/uil
%_includedir/X11/bitmaps/*
%_man3dir/*

%if_enabled static
%files -n %libname-devel-static
%_libdir/*.a
%endif

%files clients
%_x11sysconfdir/xinit.d/xmbind
%_libdir/X11/bindings
%_bindir/xmbind
%_bindir/uil
%_man1dir/uil.1*
%_man1dir/xmbind.1*
%_man5dir/*

%files mwm
%dir %_x11sysconfdir/mwm
%config %_x11sysconfdir/mwm/*
%_bindir/mwm
%_man1dir/mwm.1*
%_man4dir/*

%if_with demos
%files demos -f demos.list
# conflicts with util-linux
%exclude %_bindir/column
%exclude %_bindir/tree
%_datadir/Xm
%_mandir/manm/*
%endif

# TODO:
# - skim over http://cvs.pld-linux.org/cgi-bin/cvsweb/packages/openmotif/
# - also in PLD spec: %package compat (libXm.so.[123])
# - actually test mwm?

%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt2.1
- Fixed build

* Mon Feb 28 2011 Alexey Tourbin <at@altlinux.ru> 2.3.3-alt2
- rebuilt for debuginfo
- enabled strict dependencies between subpackages
- enabled JPEG and PNG support

* Thu Nov 25 2010 Michael Shigorin <mike@altlinux.org> 2.3.3-alt1.1
- rebuilt for Sisyphus
- minor descriptions cleanup

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1
- Version 2.3.3 (ALT #24510)

* Wed May 27 2009 Michael Shigorin <mike@altlinux.org> 2.3.2-alt3
- excluded %_bindir/tree from openmotif-demos (closes: #9056)

* Sun May 24 2009 Michael Shigorin <mike@altlinux.org> 2.3.2-alt2
- renamed library packages according to shared library naming policy
  (if any); particularly, openmotif -> libopenmotif4 to work around
  apt misbehaviour during 2.2.3 to 2.3.2-alt1 upgrade (thanks vsu@)
- spec cleanup

* Thu May 21 2009 Michael Shigorin <mike@altlinux.org> 2.3.2-alt1
- 2.3.2 (#20114)
  + disabled most RH patches (see spec comments)
  + disabled openmotif-2.2.2-alt-bison.patch
  + disabled obsolete CVE-related patches
  + added most of PLD patches (as of 2.3.1-3)
- dropped autorecrap call
- updated an Url:
- me as a de facto Packager:
  + NB: I don't use mwm, users are welcome to help out

* Tue Mar 31 2009 Michael Shigorin <mike@altlinux.org> 2.2.3-alt3.3
- added libXt-devel, libXext-devel deps to devel subpackage (#17155)

* Mon Mar 23 2009 Michael Shigorin <mike@altlinux.org> 2.2.3-alt3.2
- added xorg-printproto-devel dependency to devel subpackage (#19285)
- removed obsolete macros

* Wed Jun 21 2006 Anton Farygin <rider@altlinux.ru> 2.2.3-alt3.1
- fixed build for x86_64

* Tue Feb 07 2006 Victor Forsyuk <force@altlinux.ru> 2.2.3-alt3
- Migration from /usr/X11R6 to /usr.
- Security fix for CVE-2005-3964 (buffer overflows in libUil).
- Patch for new rgb.txt location.
- Add buildreq'ed deps.

* Sat Mar 26 2005 Anton D. Kachalov <mouse@altlinux.org> 2.2.3-alt2
- Syncing with RH patches
- x86_64 support

* Wed May 05 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.3-alt1
- Updated to 2.2.3.
- Reviewed patches.

* Sun Nov 30 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt4
- Do not package .la files.
- Do not build static libraries by default.

* Wed Oct 01 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt3
- Merged RH patches:
  libdir, utf8 (rh #80271), Xmu (rh #80777).
- Fixed multiply build problems.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt2
- Merged two RH patches: rh-config, rh-maxlinelen.

* Fri Apr 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.2.2-alt1
- 2.2.2

* Sun Mar 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.30-ipl7mdk
- Moved static libraries to devel-static subpackage.

* Wed Mar 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.1.30-ipl6mdk
- Added bunch of provides.

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 2.1.30-ipl5mdk
- Relocated config files according to FHS.
- Use new group: Graphical desktop/Motif.

* Sun Dec 17 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.30-ipl4mdk
- Updated groups, summaries and descriptions.
- More compatibility with lesstif.

* Tue Jun 20 2000 Dmitry V. Levin <ldv@fandra.org>
- More RE adaptions.

* Wed May 17 2000 AEN <aen@logic.ru>
- build with -O2

* Wed May 17 2000 AEN <aen@logic.ru>
- first build for RE
