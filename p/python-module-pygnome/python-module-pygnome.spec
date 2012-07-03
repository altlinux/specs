%define major 2.28

Name: python-module-pygnome
Version: %major.1
Release: alt2

Summary: Set of bindings for the GNOME2 platform library
License: LGPL
Group: Development/Python
Url: http://www.pygtk.org/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-python/%major/gnome-python-%version.tar.bz2

%setup_python_module pygnome

%define python_gnome_dir %python_sitelibdir/gtk-2.0/gnome

Obsoletes: gnome-python
Obsoletes: gnome-python2
Obsoletes: %name-zvt
Obsoletes: %name-nautilus
Provides: gnome-python2 = %version-%release

BuildPreReq: python-module-pygtk-devel >= 2.13.0
BuildPreReq: python-module-pygobject-devel >= 2.17.0
BuildRequires: python-module-pyorbit-devel
BuildRequires: gnome-vfs-devel libgnomeui-devel

%description
This package is a set of bindings for the Gnome platform libraries
called PyGNOME. It builds on top of the PyGTK bindings for GTK and the
PyORBit bindings for ORBit2.

PyGNOME is an extension module for Python that provides access to the
base GNOME libraries, so you have access to more widgets, a simple
configuration interface, and metadata support.

%package devel
Summary: files needed to build wrappers for GNOME libraries
Group: Development/Python
Requires: %name = %version-%release

%description devel
This package contains files required to build wrappers for GNOME
libraries so that they interoperate with pygnome.

%package canvas
Summary: Python bindings for the GNOME Canvas
Group: Development/Python
Requires: %name = %version-%release
Obsoletes: gnome-python2-canvas
Provides: gnome-python2-canvas

%description canvas
This module contains a wrapper that allows use of the GNOME Canvas
in Python.

%package bonobo
Summary: Python bindings for interacting with bonobo
Group: Development/Python
Obsoletes: gnome-python2-bonobo
Provides: gnome-python2-bonobo

%description bonobo
This module contains a wrapper that allows the creation of bonobo
components and the embedding of bonobo components in Python.

%package gconf
Summary: Python bindings for interacting with GConf
Group: Development/Python
Requires: %name = %version-%release
Obsoletes: gnome-python2-gconf
Provides: gnome-python2-gconf

%description gconf
This module contains a wrapper that allows the use of GConf via Python.

%package gnome-vfs
Summary: Python bindings for interacting with gnome-vfs
Group: Development/Python
Requires: %name = %version-%release

%description gnome-vfs
This module contains a wrapper that allows the use of gnome-vfs via Python.

%prep
%setup -q -n gnome-python-%version

%build
%configure
%make_build

%install
%makeinstall
find %buildroot -name '*.la' -exec rm {} \;

%files
%dir %python_gnome_dir
%python_gnome_dir/__init__.*
%python_gnome_dir/_gnome.so
%python_gnome_dir/ui.so
%doc AUTHORS ChangeLog README NEWS

%files devel
%doc examples/*
%_includedir/gnome-python-2.0/
%_pkgconfigdir/gnome-python-2.0.pc
%_datadir/pygtk/2.0/argtypes/
%_datadir/pygtk/2.0/defs/*

%files canvas
%python_gnome_dir/canvas.*
%python_sitelibdir/gtk-2.0/gnomecanvas.so

%files bonobo
%python_sitelibdir/gtk-2.0/bonobo/

%files gconf
%python_sitelibdir/gtk-2.0/gconf*

%files gnome-vfs
%_libdir/gnome-vfs-2.0/modules/libpythonmethod.so
%python_sitelibdir/gtk-2.0/gnomevfs/
%python_gnome_dir/vfs.*

%changelog
* Sat Apr 07 2012 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt2
- removed manual dependencies
- separate gnomevfs from main package
- updated buildreqs

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.28.1-alt1.1
- Rebuild with Python-2.7

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28.0-alt1.1
- Rebuilt with python 2.6

* Thu Sep 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sun Apr 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Feb 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.90-alt1
- 2.25.90

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.1-alt1
- 2.25.1

* Sun Jul 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.1-alt1
- new version 2.22.1 (with rpmrb script)

* Wed Apr 30 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.0-alt1
- new version 2.22.0 (with rpmrb script)

* Fri Nov 30 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.1-alt1
- new version 2.20.1 (with rpmrb script)

* Thu Nov 01 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt2
- add Requires python-module-pygnome-bonobo

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- new version 2.20.0 (with rpmrb script)

* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.19.2-alt1
- new version 2.19.2 (with rpmrb script)

* Thu May 17 2007 Vitaly Lipatov <lav@altlinux.ru> 2.18.2-alt1
- new version 2.18.2 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.18.0-alt1
- new version 2.18.0 (with rpmrb script)

* Thu Nov 16 2006 Vitaly Lipatov <lav@altlinux.ru> 2.16.2-alt0.1
- new version 2.16.2 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.15.91-alt0.1
- new version 2.15.91

* Tue Mar 28 2006 Vitaly Lipatov <lav@altlinux.ru> 2.12.3-alt0.2
- update buildreqs

* Sat Mar 04 2006 Vitaly Lipatov <lav@altlinux.ru> 2.12.3-alt0.1
- new version
- fix argtypes packing
- fix files section (thanks to php_coder@)

* Fri Oct 14 2005 Vitaly Lipatov <lav@altlinux.ru> 2.12.1-alt0.1
- new version

* Sun Sep 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt0.1
- new version
- add -gnome-vfs

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.10.0-alt1
- new version
- build with python 2.4

* Mon Jan 24 2005 Vitaly Lipatov <lav@altlinux.ru> 2.9.4-alt0.1
- new version
- remove client-command patch 
- add require for pyorbit

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt1.1
- remove version setting from subpackages
- add python-module-pygnome-nautilus in obsoletes

* Sat Dec 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt1
- new version
- some modules moved to python-pygnome-extras package

* Sat Dec 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1
- new version
- cleanup spec
- remove zvt subpackage

* Tue Jul 13 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version
- cleanup spec
- change group to Development/Python
- renamed
- adopted to python policy

* Thu Jan 29 2004 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt8
- libgtkhtml2 build

* Mon Dec 01 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt7
- fixed intersection with pygtk2-devel
- python23 build

* Wed Nov 12 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt6
- added obsoletes to gnome-python

* Tue Nov 11 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt5
- fixed file intersections with pkgconfig
- added gnomeprint package
- fixed intersections

* Wed Oct 29 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt4
- Added requires to subpackages

* Fri Oct 24 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt3
- to %name-bonobo added dependency for %name-canvas

* Thu Oct 23 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt2
- hasher rebuild
- fixed buildrequires acording to package spec
- build w/o libgtkhtml2

* Mon Sep 29 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt1
- New version

* Tue Nov 12 2002 AEN <aen@altlinux.ru> 1.99.11-alt1
- first build for Sisyphus

* Thu Oct 31 2002 Matt Wilson <msw@redhat.com>
- use %%configure

* Wed Oct 30 2002 Matt Wilson <msw@redhat.com>
- add gnome-python-2.0.pc to file list

* Wed Aug 28 2002 Matt Wilson <msw@redhat.com>
- bind gnome_client_set_*_command

* Wed Aug 28 2002 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Aug 20 2002 Matt Wilson <msw@redhat.com>
- obsolete pygtk-applet (#69830)

* Thu Aug  1 2002 Jonathan Blandford <jrb@redhat.com>
- make the GnomeDruid's fields accessible from python

* Tue Jul 30 2002 Matt Wilson <msw@redhat.com>
- official 1.99.11 release

* Thu May 30 2002 Matt Wilson <msw@redhat.com>
- s/Gconf/GConf/

* Thu May 30 2002 Jeremy Katz <katzj@redhat.com>
- add gtkhtml2 and gconf subpackages

* Wed May 29 2002 Bill Nottingham <notting@redhat.com>
- add some defattrs

* Fri May 24 2002 Matt Wilson <msw@redhat.com>
- added bonobo, nautilus subpackages.  re-enabled applet subpackage

* Mon Nov 26 2001 Matt Wilson <msw@redhat.com>
- subpackages will need __init__ included in them

* Thu Oct 18 2001 Matt Wilson <msw@redhat.com>
- doesn't obsolete pygnome - it can be installed side-by-side
- added _gnomemodule.so to base package filelist

* Mon Oct 15 2001 Matt Wilson <msw@redhat.com>
- added __init__ files to gnome-python main package

* Mon Oct  8 2001 Matt Wilson <msw@redhat.com>
- new gnome-python package based on old pygtk package.
