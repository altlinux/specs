#
# Copyright (c) 2004, 2005, 2006, 2007, 2008 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%def_with demos
%def_with examples

Name: Inventor
Version: 2.1.5
Release: alt3.4

Summary: SGI Open Inventor (TM)
License: LGPLv2+
Group: Development/C++

Url: http://oss.sgi.com/projects/inventor
Source: ftp://oss.sgi.com/projects/inventor/download/inventor-2.1.5-10.src.tar.gz
Patch: Inventor-2.1.5-30.diff.bz2
Patch1: Inventor-2.1.5-30-31.diff
# GCC44 compatibility hacks
Patch2: Inventor-2.1.5-31-32.diff
# Misc C++ modernization stuff
Patch3: Inventor-2.1.5-32-33.diff
Patch4: Inventor-2.1.5-alt-DSO.diff
Packager: Michael Shigorin <mike@altlinux.org>

%define hackcxxflags -O2 -fno-strict-aliasing

# Automatically added by buildreq on Mon Mar 23 2009
BuildRequires: gcc-c++ libGLw-devel libXext-devel libXi-devel libXt-devel libfreetype-devel libjpeg-devel

BuildRequires: gcc-c++
BuildRequires: libGLU-devel
BuildRequires: libGLw-devel
BuildRequires: libXi-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel

BuildRequires: libopenmotif-devel
BuildRequires: libfreetype-devel
BuildRequires: libjpeg-devel
BuildRequires: bison
BuildRequires: tcsh

BuildRequires: fonts-ttf-liberation rpm-macros-make

%description
SGI Open Inventor(TM) is an object-oriented 3D toolkit offering a
comprehensive solution to interactive graphics programming
problems. It presents a programming model based on a 3D scene database
that dramatically simplifies graphics programming. It includes a rich
set of objects such as cubes, polygons, text, materials, cameras,
lights, trackballs, handle boxes, 3D viewers, and editors that speed
up your programming time and extend your 3D programming capabilities.

%package -n lib%name
Summary: SGI Open Inventor (TM) shared libraries
Group: System/Libraries

%description -n lib%name
SGI Open Inventor (TM) shared libraries

%package -n lib%name-devel
Summary: SGI Open Inventor (TM) development files
Group: Development/C++
Requires: %name = %version-%release
Requires: pkgconfig
Requires: libGLU-devel
Requires: libfreetype-devel libjpeg-devel

%description -n lib%name-devel
SGI Open Inventor (TM) development files

%package -n libInventorXt
Summary: SGI Open Inventor (TM) Motif bindings
Group: System/Libraries
Requires: %name = %version-%release
Requires: %_bindir/xmessage

%description -n libInventorXt
SGI Open Inventor (TM) development files

%package -n libInventorXt-devel
Summary: SGI Open Inventor (TM) Motif bindings
Group: Development/C++
Requires: %name = %version-%release
Requires: libInventorXt = %version-%release
Requires: libInventor-devel = %version-%release
Requires: pkg-config
Requires: openmotif-devel

%description -n libInventorXt-devel
SGI Open Inventor (TM) development files

%if_with demos
%package demos
Summary: SGI Open Inventor (TM) Demos
Group: Development/Documentation
Requires: %name-data

%description demos
SGI Open Inventor (TM) demos
%endif

%package data
Summary: SGI Open Inventor (TM) data
Group: Development/C++
BuildArch: noarch

%description data
SGI Open Inventor data files

%if_with examples
%package examples
Summary: SGI Open Inventor (TM) source code examples
Group: Development/Documentation
# Should we once ship binary examples, this requirement can be dropped
Requires: libInventorXt-devel
BuildArch: noarch

%description examples
SGI Open Inventor (TM) Source Examples from the Inventor books
"The Inventor Mentor" and "The Inventor Toolmaker"
%endif

%prep
%setup -n inventor
find -name CVS | xargs rm -rf
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p2

sed -i \
-e 's,^IVPREFIX =.*$,IVPREFIX = %prefix,' \
-e 's,^_BINDIR =.*$,_BINDIR = %_bindir,' \
-e 's,^_LIBDIR =.*$,_LIBDIR = %_libdir,' \
-e 's,^_HDRTOP =.*$,_HDRTOP = %_includedir/Inventor,' \
-e 's,^_MAN1DIR =.*$,_MAN1DIR = %_man1dir,' \
-e 's,^_MAN3DIR =.*$,_MAN3DIR = %_man3dir,' \
-e 's,^_FONTPATH =.*$,_FONTPATH = %_datadir/Inventor/fonts,' \
-e 's,^_HELPDIR =.*$,_HELPDIR = %_datadir/Inventor/help,' \
-e 's,^_DATADIR =.*$,_DATADIR = %_datadir/Inventor/data/models,' \
-e 's,^_MATERIALSDIR =.*$,_MATERIALSDIR = %_datadir/Inventor/data/materials,' \
-e 's,^_TEXTURESDIR =.*$,_TEXTURESDIR = %_datadir/Inventor/data/textures,' \
-e 's,^_DEMOBINDIR =.*$,_DEMOBINDIR = %_libdir/Inventor,' \
-e 's,^_DEMODATADIR =.*$,_DEMODATADIR = %_datadir/Inventor/data/demos,' \
-e 's,^OPTIMIZER = -O -DNDEBUG,OPTIMIZER = -DNDEBUG,' \
-e 's,(X11DIR)/lib,(X11DIR)/%_lib,g' \
make/ivcommondefs

for i in apps/demos/*/*.RUNME; do \
  # \/: otherwise rpmcs might break second pattern on x86_64
  # resulting in self-unmets in Inventor-demos
  sed -i \
    -e 's,/usr\/share/inventor/,%_datadir/Inventor/,g' \
    -e 's,/usr\/lib/inventor/,%_libdir/Inventor/,g' \
    $i
done

for i in *.pc.in; do
  sed \
    -e 's,@prefix@,%prefix,g' \
    -e 's,@exec_prefix@,%_exec_prefix,g' \
    -e 's,@includedir@,%_includedir,g' \
    -e 's,@libdir@,%_libdir,g' \
    -e 's,X11R6/lib,X11R6/%_lib,g' \
    < $i > $(basename $i .in)
done

rm -f data/models/scenes/chesschairs.iv

%build
# Inventor's build system wants us to install and build everything at once.

export LD_LIBRARY_PATH=%buildroot%_libdir
export VCOPTS="%optflags -D_REENTRANT"
export VCXXOPTS=$(echo "%optflags -D_REENTRANT -D__STDC_FORMAT_MACROS" | sed -e 's,-O2,%hackcxxflags,')
%make_ext all \
  FREETYPE=1 IVROOT=%buildroot \
  LSUBDIRS="libimage tools libFL"
%make_install install \
  FREETYPE=1 IVROOT=%buildroot
  LSUBDIRS="lib libSoXt"
%make_ext all \
  FREETYPE=1 IVROOT=%buildroot BUILDMAN=1 \
  LSUBDIRS="doc apps data"

# convert Mentor and Toolmaker examples into a standalone package
rm -rf devel-docs
cp -a apps/examples devel-docs
cp -a make devel-docs
pushd devel-docs > /dev/null
find -name 'GNUmakefile*' | while read a; do \
  b=`echo $a | sed 's,GNUmakefile.*$,,;s,^\./,,;s,[^/]*/,../,g;s,\/$,,;s,^$,.,'`
  sed -i -e "s,^IVDEPTH = .*$,IVDEPTH = $b," $a
done
find -name '*.c++' | while read a; do \
  sed -i -e "s,%_datadir/src/Inventor/examples/data,%_datadir/Inventor/examples/data,g" $a
done
subst '/^IVLIBHDRDIRS.*/,/libSoXt\/include/c\
IVLIBHDRS = `pkg-config --cflags libInventorXt`' \
make/ivcommondefs
make clean
popd > /dev/null

%install
export LD_LIBRARY_PATH=%buildroot%_libdir
export VCOPTS="%optflags -D_REENTRANT"
export VCXXOPTS="%optflags -D_REENTRANT"
%make_install install \
  FREETYPE=1 IVROOT=%buildroot BUILDMAN=1

install -d -m755 %buildroot%_pkgconfigdir
install -m644 libInventor.pc %buildroot%_pkgconfigdir
install -m644 libInventorXt.pc %buildroot%_pkgconfigdir

install -d -m755 %buildroot%_libdir/Inventor
mv devel-docs %buildroot%_datadir/Inventor/examples

install -d -m755 %buildroot%_datadir/Inventor/data/materials
install -d -m755 %buildroot%_datadir/Inventor/data/textures
install -d -m755 %buildroot%_datadir/Inventor/fonts

# Map Inventor's standard fonts
# Utopia, Helvetica and Courier to liberation-TTF fonts
# Times-Roman is being used by some examples
pushd %buildroot%_datadir/Inventor/fonts > /dev/null
ln -s Utopia-Regular Times-Roman
ln -s %_datadir/fonts/ttf/liberation/LiberationSerif-Regular.ttf Utopia-Regular
ln -s %_datadir/fonts/ttf/liberation/LiberationSerif-Bold.ttf Utopia-Bold
ln -s %_datadir/fonts/ttf/liberation/LiberationSerif-Italic.ttf Utopia-Italic
ln -s %_datadir/fonts/ttf/liberation/LiberationSerif-BoldItalic.ttf Utopia-BoldItalic
ln -s %_datadir/fonts/ttf/liberation/LiberationSans-Regular.ttf Helvetica
ln -s %_datadir/fonts/ttf/liberation/LiberationSans-Bold.ttf Helvetica-Bold
ln -s %_datadir/fonts/ttf/liberation/LiberationSans-Italic.ttf Helvetica-Oblique
ln -s %_datadir/fonts/ttf/liberation/LiberationSans-BoldItalic.ttf Helvetica-BoldOblique
ln -s %_datadir/fonts/ttf/liberation/LiberationMono-Regular.ttf Courier
ln -s %_datadir/fonts/ttf/liberation/LiberationMono-Bold.ttf Courier-Bold
ln -s %_datadir/fonts/ttf/liberation/LiberationMono-Italic.ttf Courier-Oblique
ln -s %_datadir/fonts/ttf/liberation/LiberationMono-BoldItalic.ttf Courier-BoldOblique
popd > /dev/null

%files
%doc COPYING BUGS FAQ README
%_bindir/iv2toiv1
%_bindir/ivcat
%_bindir/ivdowngrade
%_bindir/ivfix
%_bindir/ivinfo
%_bindir/ivnorm
%_bindir/ivAddVP
%dir %_datadir/Inventor
%_datadir/Inventor/fonts
%_man1dir/inventor.*
%_man1dir/iv2toiv1.*
%_man1dir/ivcat.*
%_man1dir/ivdowngrade.*
%_man1dir/ivfix.*
%_man1dir/ivinfo.*

%files -n lib%name
%_libdir/libInventor.so.*

%files -n lib%name-devel
%dir %_includedir/Inventor
%_includedir/Inventor/[^X]*
%_libdir/libInventor.so
%_pkgconfigdir/libInventor.pc
%_man3dir/Sb*
%_man3dir/So[^X]*

%files -n libInventorXt
%_bindir/SceneViewer
%_bindir/ivview
%_bindir/ivperf
%_man1dir/SceneViewer.*
%_man1dir/ivview.*
%_libdir/libInventorXt.so.*
%dir %_datadir/Inventor
# Used by libInventorXt
%_datadir/Inventor/help
# Used by SceneViewer
%dir %_datadir/Inventor/data
%dir %_datadir/Inventor/data/materials
%dir %_datadir/Inventor/data/textures

%files -n libInventorXt-devel
%dir %_includedir/Inventor
%_includedir/Inventor/Xt
%_libdir/libInventorXt.so
%_pkgconfigdir/libInventorXt*.pc
%_man3dir/SoXt*

%files data
%dir %_datadir/Inventor
%dir %_datadir/Inventor/data
%_datadir/Inventor/data/models
%_datadir/Inventor/data/materials
%_datadir/Inventor/data/textures

%if_with demos
%files demos
# requires data, so dirs already owned
%_datadir/Inventor/data/demos
%_libdir/Inventor/[^e]*
%endif

%if_with examples
%files examples
%dir %_datadir/Inventor
%_datadir/Inventor/examples
%endif

%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt3.4
- Fixed build

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt3.3
- Fixed build

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt3.2
- Rebuilt for soname set-versions

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt3.1
- Built from CVS
- Changed using glwMDrawingAreaWidgetClass -> SoglwMDrawingAreaWidgetClass

* Sat Mar 28 2009 Michael Shigorin <mike@altlinux.org> 2.1.5-alt3
- fixed subtle spec breakage resulting in wrong path fixup
  on x86_64; cheated rpmcs with escaping a slash in a path

* Tue Mar 24 2009 Michael Shigorin <mike@altlinux.org> 2.1.5-alt2
- *libification*
- introduced noarch subpackages

* Sun Mar 22 2009 Michael Shigorin <mike@altlinux.org> 2.1.5-alt1
- built for ALT Linux
  + based on Fedora spec
  + heavy spec cleanup
- libification
- examples moved from %%_libdir to %%_datadir
- buildreq 

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.5-34
- Add Inventor-2.1.5-31-32.diff.
- Add Inventor-2.1.5-32-33.diff.

* Tue Jun 03 2008 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-33
- Add -fnostrict-aliasing to VCXXOPTS to work around GCC-4.3 breakage.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.5-32
- Autorebuild for GCC 4.3

* Thu Jan 10 2008 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-31
- Spec file cleanup.
- Introduce --with openmotif.
- Add Inventor-2.1.5-30-31.diff.

* Mon Nov 19 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-30.1
- Add hard-coded deps on font files (BZ 388761).
- Switch to using liberation-fonts instead of dejavu-fonts.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-30
- Apply major hacks (*-30.diff) to address BZ: 245192.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-29
- Update license tag.

* Thu Jun 21 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-28
- ExcludeArch: ppc64 (BZ: 245192).

* Thu Jun 21 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-27
- Add *-27.patch.
- Remove _ia64 grep (Incorporated into *-27.diff).
- Add powerpc64 hack.

* Wed Mar 14 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-26
- Use dejavu-fonts as fonts.
- Attempt to fix BZ 232017.

* Tue Feb 13 2007 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-25
- Specfile fixes.

* Tue Oct 03 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-24
- Specfile cosmetics.
- Use %%{_datadir}/Inventor instead of %%{_datadir}/%name
- Fix dep on xmessage for FC4.
- Add %%{_datadir}/Inventor/data/materials.
- Add %%{_datadir}/Inventor/fonts.

* Mon Oct 02 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-23
- Add make-var _PDFVIEWER.
- Backport to FC4.
- Fix path to chessboard.iv in chesschairs.iv.

* Thu Sep 25 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-22
- Misc minor fixes.
- Add dep to xmessage.
- Use unified patch.
- Rebuild against lesscrap.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-21
- Mass rebuild.

* Sun Feb 19 2006 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-20
- Rebuild.

* Fri Dec 30 2005 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-19
- Don't BR: libXau-devel (#176313 reported to be fixed).

* Wed Dec 28 2005 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-18
- Remove patch10 (#173879, #175251 are reported to be fixed).

* Thu Dec 22 2005 Ralf Corsépius <rc040203@freenet.de> - 2.1.5-17
- Remove BR: libX11-devel (#173712 reported to be fixed).
- Remove BR: libGL-devel (#175253 reported to be fixed).

* Wed Dec 14 2005 Ralf Corsepius <rc040203@freenet.de> - 2.1.5-16
- Remove BR: libXext-devel (Impl. R'd by openmotif-devel).
- Remove BR: xorg-x11-proto-devel (PR #175256).

* Thu Dec 8 2005 Ralf Corsepius <rc040203@freenet.de> - 2.1.5-15
- Further modular X fixes.
- Reflect modular X pkgconfigs.

* Thu Dec 8 2005 Ralf Corsepius <rc040203@freenet.de> - 2.1.5-14
- Attempt to build against modular X.
- Add Inventor-redhat-bugs patch.

* Tue Aug 03 2005 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-13
- Let PPC use standard RPM_OPT_FLAGS.

* Tue Aug 02 2005 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-12
- Add SoTempPath fix.

* Sun May 22 2005 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-9
- Increment release in an attempt to please build system.

* Sun May 22 2005 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-8
- Use BR: xorg-x11-* instead of *.so.1 to work around rpm's brain-dead
  SONAME handling.
- Add %%dist.
- Use sed -i to avoid temporary files.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Feb 16 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 2.1.5-7
- Add specfile-patch from Andy Loening to fix build on x86_64 (rhb#147267)

* Mon Feb 14 2005 David Woodhouse <dwmw2 infradead org> - 2.1.5-6
- Work around gcc bug by backing down to -O1 on ppc

* Mon Sep 6 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.5
- Add ivAddVP ivnorm ivperf to Inventor rsp. InventorXt.
- Remove BuildRequires: tcsh.

* Wed Aug 8 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.4
- Split out InventorXt, InventorXt-devel, Inventor-examples
- make/ivcommondefs: Remove -O from $OPTIMIZER.
- Various changes to libInventor.pc and libInventorXt.pc.

* Wed Jul 7 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.3
- Remove Mesa-Requires.
- Add pkgconfig support.
- Add various Requires: to *devel.
- Add Provides: InventorXt and InventorXt-devel.

* Thu Jul 1 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.2
- Adopt portions of Michael Schwendt's patch.
- Fix hard-coded paths in apps/demos/*.RUNMEs.
- Use %%{_prefix}/lib instead of %%{_libdir} to install the demos into.
- Add make/ to devel docs.
- Hack devel docs to be buildable.

* Wed Jun 30 2004 Ralf Corsepius <ralf[AT]links2linux.de> - 2.1.5-0.fdr.1
- Initial Fedora Extras RPM.
- Adopt Debian/Testing patches (Thanks to Steve M. Robbins for keeping
  Inventor alive).
