%define oname libfltk
%define major 1.3

Name: %{oname}13
Version: %major.3
Release: alt2

Summary: Multiplatform C++ GUI Fast Light ToolKit
License: LGPL
Group: System/Libraries
URL: http://www.fltk.org/

# http://seriss.com/public/fltk/fltk/branches/branch-1.3/
Source: %name-%version.tar
Source2: fltk-%version-docs-html.tar.gz

Patch1: fltk-1.3-L3156.patch
Patch2: fltk-1.3.2-fltk_config.patch

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: gcc-c++ groff-base libICE-devel libXext-devel
BuildRequires: libXft-devel libalsa-devel libjpeg-devel libGL-devel
BuildRequires: libpng-devel xprop libX11-devel fontconfig-devel
BuildPreReq: libfreetype-devel libGLU-devel libcairo-devel
BuildPreReq: libXtst-devel libXcomposite-devel
BuildPreReq: libXcursor-devel libXdamage-devel libXdmcp-devel
BuildPreReq: libXfixes-devel libXi-devel libXinerama-devel
BuildPreReq: libXpm-devel libXrandr-devel libXt-devel libXv-devel
BuildPreReq: libXxf86misc-devel libXScrnSaver-devel
BuildPreReq: cmake glib2-devel libpixman-devel
BuildPreReq: pkgconfig(glproto) pkgconfig(dri2proto)
BuildPreReq: libXxf86vm-devel libharfbuzz-devel libexpat-devel

%description
The Fast Light ToolKit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r),
and Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally
developed by Mr. Bill Spitzak and is currently maintained by a
small group of developers across the world with a central
repository in the US.

%package -n %oname-devel
Summary: Development environment for multiplatform C++ GUI Fast Light ToolKit
Group: Development/C
Requires: %name = %version-%release

%description -n %oname-devel
The Fast Light ToolKit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r),
and Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally
developed by Mr. Bill Spitzak and is currently maintained by a
small group of developers across the world with a central
repository in the US.

This package includes header files, static library, GUI builder fluid,
needed to develop FLTK applications.

%package doc
Summary: Documentation and test suit for multiplatform C++ GUI Fast Light ToolKit
Group: Development/C
Provides: %oname-doc = %version-%release
BuildArch: noarch

%description doc
The Fast Light ToolKit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r),
and Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally
developed by Mr. Bill Spitzak and is currently maintained by a
small group of developers across the world with a central
repository in the US.

This package includes test suit and documentation, needed to develop
FLTK applications.

%prep
%setup
tar xf %SOURCE2
%patch1 -p0
%patch2 -p1
perl -pi -e 's/\bcat([1-3])\b/man$1/g' documentation/Makefile

# change soname from so.1.3 to so.2 .
sed -r -e 's/FL_API_VERSION=.*/FL_API_VERSION=2/' -i configure configure.in
sed -r -e 's/(libfltk[^\.]*\.so)\.1\.3/\1.2/g' -i src/Makefile

%build
%configure --disable-static --enable-shared --enable-largefile --enable-xdbe --enable-xinerama --enable-xft --enable-threads
%make_build

%install
install -d %buildroot%_docdir/fltk-%version
install -d %buildroot%_mandir

%makeinstall_std docdir=%buildroot%_docdir/fltk-%version
cp -p ANNOUNCEMENT CHANGES CREDITS README %buildroot%_docdir/fltk-%version/
cp -fR fltk-%version/documentation/html %buildroot%_docdir/fltk-%version/

%files
%_bindir/fluid
%_libdir/*.so.*
%dir %_docdir/fltk-%version
%_docdir/fltk-%version/ANNOUNCEMENT
%_docdir/fltk-%version/CREDITS
%_docdir/fltk-%version/README
%_mandir/man1/fluid.1*

%files -n %oname-devel
%_bindir/*
%exclude %_bindir/fluid
%_libdir/*.so
%_includedir/*
%_mandir/man?/*
%exclude %_mandir/man1/fluid.1*

%files doc
%_docdir/fltk-%version
%exclude %_docdir/fltk-%version/ANNOUNCEMENT
%exclude %_docdir/fltk-%version/CREDITS
%exclude %_docdir/fltk-%version/README

%changelog
* Thu Feb 23 2017 Michael Shigorin <mike@altlinux.org> 1.3.3-alt2
- Dropped BR: libopensm-devel (what was it doing here?!)

* Tue Apr 26 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.3-alt1
- cas@:
 + New version
 + Apply patches from Fedora
 + Extract generated documentation from upstream tarball
- Changed sonames to libfltk*.so.2 .

* Fri Jul 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2.r10217-alt1
- New snapshot

* Sat Jun 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2.r10181-alt2
- Avoid conflict with libfltk0 (ALT #30107)

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2.r10181-alt1
- New snapshot

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2.r10018-alt1
- Version 1.3.2

* Tue Jun 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r9945-alt1
- New snapshot

* Tue Feb 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r9812-alt1
- New snapshot

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r9678-alt2
- Rebuilt with libpng15

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r9678-alt1
- New snapshot

* Sun Jun 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r9251-alt3
- Added glib2-devel, libpixman-devel, pkgconfig(glproto),
  pkgconfig(dri2proto), libXxf86vm-devel into BuildRequires (ALT #27429)

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r9251-alt2
- Fixed build

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r9251-alt1
- New snapshot

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r9208-alt1
- New snapshot

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r8575-alt1
- New snapshot
- Disabled devel-static package

* Mon Feb 07 2011 Alexey Tourbin <at@altlinux.ru> 1.3.0.r8323-alt1.1
- Rebuilt to enable debuginfo provides

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0.r8323-alt1
- Version 1.3.0-r8323

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.10-alt2
- Rebuilt for soname set-versions

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.10-alt1
- Version 1.1.10
- Fixed underlinked of libraries

* Mon Dec 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt3
- Built doc package as noarch

* Mon Jun 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt2
- Rebuild with gcc4.4

* Wed Dec 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.9-alt1.1
- NMU: updated build dependencies

* Mon May 12 2008 Alexey Tourbin <at@altlinux.ru> 1.1.9-alt1
- fltk-1.1.x-r5917 -> 1.1.9 release

* Mon Jul 30 2007 Alexey Tourbin <at@altlinux.ru> 1.1.8-alt0.1
- updated to fltk-1.1.x-r5917 shapshot
- fixed lib64 installation issue on x86_64
- introduced FLTK_1.1.8 symbol versioning for shared libraries

* Tue Jul 11 2006 Alexey Tourbin <at@altlinux.ru> 1.1.7-alt2
- fixed linkage
- specfile cleanup
- test suite not packaged
- configure --enable-shared (#8186)

* Mon Feb 27 2006 Stanislav Ievlev <inger@altlinux.org> 1.1.7-alt1
- 1.1.7, fixed buildreq

* Thu Nov 18 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.5-alt1
- 1.1.5

* Tue Apr 06 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.4-alt1
- 1.1.4

* Wed Mar 26 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Tue Aug  6 2002 Grigory Milev <week@altlinux.ru> 1.1.0rc7-alt1
- BUG!!!! PLEASE ADD CHANGELOGS

* Tue Aug  6 2002 Grigory Milev <week@altlinux.ru> 1.1.0rc5-alt1
- new version released

* Thu Oct 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.11-alt2
- Fixed linking with libGL (added patch3).

* Fri Jul 06 2001 Stanislav Ievlev <inger@altlinux.ru> 1.0.11-alt1
- 1.0.11, Librification, Statification.

* Sun Dec 17 2000 Dmitry V. Levin <ldv@fandra.org> 1.0.10-ipl1mdk
- 1.0.10
- FHSification.
- Moved documentation and test suit to doc subpackage.

* Tue Jun 27 2000 Dmitry V. Levin <ldv@fandra.org>
- 1.0.9

* Wed May 31 2000 AEN <aen@logic.ru>
- 1.0.8
- bugs in spec fixed

* Tue Dec 21 1999 AEN <aen@logic.ru>
- 1.0.7
* Fri Nov 12 1999 AEN <aen@logic.ru>
- two packages

* Wed Nov 10 1999 AEN <aen@logic.ru>
- build for RE

