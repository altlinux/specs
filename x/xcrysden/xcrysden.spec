#
# spec file for package xcrysden (Version 1.5.21
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

Name: xcrysden
Version: 1.5.21
Release: alt4

Summary: X-window CRYstalline Structure and DENsities
License: GPLv2+
Group: Sciences/Chemistry

Url: http://www.xcrysden.org
Source: %url/download/%name-%version-src.tar.bz2
Patch1: xcrysden-1.5.21-opensuse-prototype.patch
Patch2: xcrysden-1.5.21-opensuse-getline.patch
Patch3: xcrysden-1.5.21-opensuse-readlink.patch
Patch4: xcrysden-1.5.21-opensuse-bwidget.patch
Patch5: xcrysden-1.5.21-opensuse-gdb.patch
Patch6: xcrysden-1.5.21-alt-autoreq.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: bwidget gawk ImageMagick netpbm
Requires: openbabel gifsicle

# Automatically added by buildreq on Sun Dec 19 2010++
BuildRequires: gcc-fortran libGL-devel libGLU-devel libXext-devel libXmu-devel tk-devel

# shell wrapped tcl scripts
%add_findreq_skiplist %_libdir/%name/util/*

%description
XCrySDen is a crystalline and molecular structure visualisation
program, which aims at display of isosurfaces and contours,
which can be superimposed on crystalline structures and
interactively rotated and manipulated.

%package examples
Summary: XCrySDen example data files
Group: Sciences/Chemistry
BuildArch: noarch

%description examples
This package contains various %name example data files.

%prep
%setup -n XCrySDen-%version-src
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6 -p1

%build
cp system/Make.linux Make.sys
make all CFLAGS="$CFLAGS -fPIC -DUSE_FONTS" FFLAGS="-O2 $FFLAGS" X_LIB="-L%_libdir -lXmu -lX11 -lXext"

%install
mkdir -p %buildroot%_libdir/%name/{images,bin,Awk,util,Tcl,Tcl/fs,scripts}
install -p version usage xcrysden %buildroot%_libdir/%name/
install -p bin/* %buildroot%_libdir/%name/bin/
install -p Awk/*.awk %buildroot%_libdir/%name/Awk/
install -p images/* %buildroot%_libdir/%name/images/
install -p scripts/* %buildroot%_libdir/%name/scripts/
install -p Tcl/{*.tcl,tclIndex} %buildroot%_libdir/%name/Tcl/
install -p Tcl/fs/{*.tcl,tclIndex} %buildroot%_libdir/%name/Tcl/fs/
install -p util/* %buildroot%_libdir/%name/util/
mkdir -p %buildroot%_bindir
ln -s %_libdir/%name/xcrysden %buildroot%_bindir/xcrysden
mkdir -p %buildroot%_sysconfdir/%name
install -p Tcl/{Xcrysden_defaults,custom-definitions} %buildroot%_sysconfdir/%name/
ln -s %_sysconfdir/%name/Xcrysden_defaults %buildroot%_libdir/%name/Tcl/Xcrysden_defaults
ln -s %_sysconfdir/%name/custom-definitions %buildroot%_libdir/%name/Tcl/custom-definitions

mkdir -p %buildroot%_datadir/%name/
cp -a examples %buildroot%_datadir/%name/
ln -s %_datadir/%name/examples %buildroot%_libdir/%name/examples

%files
%_bindir/%name
%_libdir/%name/
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/Xcrysden_defaults
%config(noreplace) %_sysconfdir/%name/custom-definitions
%doc AUTHORS COPYRIGHT ChangeLog NEWS README THANKS

%files examples
%_datadir/%name/examples

%changelog
* Sat Jun 25 2011 Michael Shigorin <mike@altlinux.org> 1.5.21-alt4
- BR += libXext-devel

* Sun Dec 19 2010 Michael Shigorin <mike@altlinux.org> 1.5.21-alt3
- BR += libGLU-devel

* Sat Sep 04 2010 Michael Shigorin <mike@altlinux.org> 1.5.21-alt2
- fixed Requires: to use gifsicle instead of (obsolete) ungifsicle

* Fri Sep 03 2010 Michael Shigorin <mike@altlinux.org> 1.5.21-alt1
- built for ALT Linux
  + based on openSUSE 1.5.21-27.9 package
  + heavy spec cleanup
- added patch to avoid autodependency on gdb and valgrind
- added examples subpackage

* Thu Mar  4 2010 tob@net-b.de
- Fix path globbing for bwidget
* Fri Jan 15 2010 tob@net-b.de
- Fix some patch to bwidget
* Thu Dec 10 2009 burnus@net-b.de
- Initial package version pre-1.6 (1.51.21)
