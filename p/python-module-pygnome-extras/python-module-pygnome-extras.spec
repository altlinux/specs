%define major 2.25
%def_enable docs

Name: python-module-pygnome-extras
Version: %major.3
Release: alt3.2.1

Summary: Set of extra bindings for the GNOME2 platform library

License: LGPL
Group: Development/Python
Url: http://www.pygtk.org/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-python-extras/%major/gnome-python-extras-%version.tar.bz2
# GNOME bug #584126
Patch1: gnome-python-extras-2.25.3-update-for-gdl-2.27.2.part1.patch
Patch2: gnome-python-extras-2.25.3-update-for-gdl-2.27.2.part2.patch

%setup_python_module pygnome

%define bname python-module-pygnome

%define python_gnome_dir %python_sitelibdir/gtk-2.0/gnome

%{?_enable_docs:BuildRequires: gtk-doc}
BuildPreReq: libgda4-devel >= 3.99.9
BuildRequires: gcc-c++ glibc-devel libgdl-devel libgksu-devel libgtkhtml2-devel
BuildRequires: libgtk+2-devel libbonoboui-devel libgnomeui-devel gnome-vfs-devel libgtkspell-devel
BuildRequires: python-module-pygnome-devel xulrunner-devel
# style.css from this package required to build documentation
BuildRequires: python-module-pygobject-devel-doc
BuildPreReq: python-module-pygtk-devel

%description
This package is a set of extra bindings for the Gnome platform
libraries called PyGNOME. It builds on top of the PyGTK bindings for GTK and
the PyORBit bindings for ORBit2.

PyGNOME is an extension module for Python that provides access to the
base GNOME libraries, so you have access to more widgets, a simple
configuration interface, and metadata support.

%package devel
Summary: files needed to build extra wrappers for GNOME libraries
Group: Development/Python
Requires: %name = %version-%release
Requires: python-module-pygnome-devel

%description devel
This package contains files required to build wrappers for GNOME
libraries so that they interoperate with pygnome.

%package devel-doc
Summary: Development documentation for extra wrappers for GNOME libraries
Group: Development/Python
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains development documentation for set of extra
bindings for GNOME libraries.

%package -n %bname-gtkhtml2
Summary: Python bindings for interacting with gtkhtml2
Group: Development/Python
Requires: %name = %version-%release
Obsoletes: gnome-python2-gtkhtml2
Provides: gnome-python2-gtkhtml2

%description -n %bname-gtkhtml2
This module contains a wrapper that allows the use of gtkhtml2 via Python.

%package -n %bname-gda
Summary: Python bindings for interacting with libgda-4
Group: Development/Python
Requires: %name = %version-%release

%description -n %bname-gda
This module contains a wrapper that allows the use of libgda-4 via Python.

%prep
%setup -q -n gnome-python-extras-%version
%patch1 -p1 -b .update-for-gdl-2.27.2.part1
%patch2 -p1 -b .update-for-gdl-2.27.2.part2

%build
%configure --enable-gtkmozembed=off %{subst_enable docs}
%make_build

%install
%makeinstall_std
rm -f %buildroot%python_sitelibdir/gtk-2.0/*.la

%files
%doc AUTHORS ChangeLog README NEWS
%python_sitelibdir/gtk-2.0/egg
%python_sitelibdir/gtk-2.0/gdl.so
%python_sitelibdir/gtk-2.0/gtkspell.so
%python_sitelibdir/gtk-2.0/gksu2/

%files devel
%_includedir/pygda-4.0/pygdavalue_conversions.h
%_pkgconfigdir/*
%_datadir/pygtk/2.0/defs/*.defs
%doc examples/*

%files devel-doc
%_datadir/gtk-doc/html/*

%files -n %bname-gtkhtml2
%python_sitelibdir/gtk-2.0/gtkhtml*

%files -n %bname-gda
%python_sitelibdir/gtk-2.0/gda*
%_datadir/pygtk/2.0/argtypes/gda*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.25.3-alt3.2.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.25.3-alt3.2
- Fixed build

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.25.3-alt3.1
- Rebuild with Python-2.7
- remove gtkmozembed part

* Thu Dec 24 2009 Alexey Rusakov <ktirf@altlinux.org> 2.25.3-alt3
- rebuilt with libgdl 2.28, now really fixing GNOME Bug #584126

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.25.3-alt2.1
- Rebuilt with python 2.6

* Tue Nov 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.3-alt2
- updated buildreqs
- fixed GNOME bug #584126

* Thu Sep 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.3-alt1
- 2.25.3

* Fri Jan 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.2-alt1
- new version

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.1-alt1
- 2.25.1
- drop upstreamed patch and hacks
- build libgda-4 wrapper
- new devel-doc subpackage

* Fri Nov 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.19.1-alt3
- build against libgdl-2.24

* Sat Aug 09 2008 Vitaly Lipatov <lav@altlinux.ru> 2.19.1-alt2
- build with new xulrunner-devel
- build with libgksu
- workaround for bugs #16330, 16634
- update buildreq

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.19.1-alt1
- new version 2.19.1 (with rpmrb script)
- add libSM-devel to buildreqs

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.14.3-alt1
- new version 2.14.3 (with rpmrb script)

* Wed Dec 06 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt3
- rebuild with new firefox

* Sat Sep 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt2
- rebuild with new firefox

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt1
- update buildreqs, enable gtkmozembed again

* Mon Sep 04 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt0.1
- new version 2.14.2
- disable gtkmozembed

* Tue Mar 28 2006 Vitaly Lipatov <lav@altlinux.ru> 2.13.3-alt0.2
- update buildreqs, check build on x86_64

* Tue Mar 07 2006 Vitaly Lipatov <lav@altlinux.ru> 2.13.3-alt0.1
- new version
- update buildreqs
- disable gda build
- the following modules moved to the package gnome-python-desktop:
  - gnomeapplet
  - gnomeprint, gnomeprint.ui
  - gtksourceview
  - wnck
  - totem.plparser
  - gtop
  - nautilusburn
  - mediaprofiles

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.12.1-alt0.1
- new version

* Fri Oct 14 2005 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt0.1
- new version

* Sat Sep 03 2005 Vitaly Lipatov <lav@altlinux.ru> 2.11.4-alt0.1
- 

* Sun Apr 10 2005 Vitaly Lipatov <lav@altlinux.ru> 2.10.0-alt2
- add require for gnomeprint in gtksourceview (fix bug #6442)

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.10.0-alt1
- new version
- build with python 2.4

* Mon Jan 24 2005 Vitaly Lipatov <lav@altlinux.ru> 2.9.4-alt1
- new version

* Tue Dec 14 2004 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt2
- move gtksourceview to separate subpackage (fix bug #5693)

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt1.1
- remove version setting from subpackages
- set python-module-pygnome as prefix for subpackages name

* Sat Dec 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt1
- first build for ALT Linux Sisyphus
