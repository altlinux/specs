%def_enable numpy
%def_enable docs
%define oname pygtk_git
%define qname gtk_git
%define _gtkdocdir %_datadir/gtk-doc/html

%define major 2.24
Name: python-module-%oname
Version: %major.1
Release: alt3.git20111002

Summary: Python bindings for the GTK+ widget set (from upstream git)

Group: Development/Python
License: LGPL
Url: http://www.pygtk.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.gnome.org/pygtk
Source: pygtk-%version.tar.bz2
Source1: pygtk_git.py

%setup_python_module %oname
%add_python_req_skip gdk

%py_provides argtypes_git
%py_provides %qname
%define pygobject_ver 2.28.3
%define pycairo_ver 1.8.11
%define gtk_version 2.24.4
%define glade_version 2.6.4

BuildPreReq: rpm-build-python python-devel gnome-common

# Automatically added by buildreq on Wed Feb 21 2007
BuildRequires: glibc-devel libglade-devel python-module-pycairo-devel
BuildPrereq: python-module-pygobject-devel python-modules-encodings xsltproc
BuildPreReq: libcairo-devel libatk-devel gdk-pixbuf-devel

# style.css from this package required to build documentation
BuildRequires: python-module-pygobject-devel-doc

BuildRequires: docbook-dtds docbook-style-xsl
BuildRequires: python-module-pycairo-devel >= %pycairo_ver
BuildRequires: libgtk+2-devel >= %gtk_version
BuildRequires: libglade2-devel >= %glade_version
BuildRequires: python-module-pygobject-devel >= %pygobject_ver
BuildRequires: rpm-build-compat
%{?_enable_numpy:BuildRequires: libnumpy-devel}
%{?_enable_docs:BuildRequires: python-module-sphinx-devel}

# Why we do not catch it automatically?
Requires: python-module-pycairo >= %pycairo_ver
Requires: python-module-pygobject >= %pygobject_ver

%description
PyGTK is an extension module for python that gives you access to the GTK+
widget set.  Just about anything you can write in C with GTK+ you can write
in python with PyGTK (within reason), but with all the benefits of python.


%package libglade
Summary: A wrapper for the libglade library for use with PyGTK
Group: Development/Python
Requires: %name = %version-%release libglade2
%py_provides libglade_git

%description libglade
This module contains a wrapper for the libglade library.  Libglade allows
a program to construct its user interface from an XML description, which
allows the programmer to keep the UI and program logic separate.

%package devel
Summary: files needed to build wrappers for GTK+ addon libraries
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-devel-data = %version-%release

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with pygtk.

%package devel-data
Summary: Data files needed to build wrappers for GTK+ addon libraries
Group: Development/Python
BuildArch: noarch

%description devel-data
This package contains data files required to build wrappers for GTK+
addon libraries so that they interoperate with pygtk.

%package demo
Summary: pygtk2 demo
Group: Development/Python

%description demo
This package contains pygtk2 demo

%if_enabled docs
%package doc
Summary: pygtk2 doc
Group: Development/Python
BuildArch: noarch

%description doc
This package contains pygtk2 doc

%package pickles
Summary: Pickles for pygtk2
Group: Development/Python

%description pickles
This package contains pickles for pygtk2.

%endif

%package tests
Summary: pygtk2 tests
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contains pygtk2 tests.


%prep
%setup

subst "s|@PYTHON@|%_bindir/env python|g" pygtk-codegen-2.0.in \
	examples/pygtk-demo/pygtk-demo.in

mv pygtk-codegen-2.0.in %oname-codegen-2.0.in
mv pygtk-2.0.pc.in %oname-2.0.pc.in

%if_enabled docs
%prepare_sphinx .
%endif

%build
%autoreconf
%configure --disable-static \
	%{subst_enable numpy} \
	%{subst_enable docs} \
	--enable-threads

%make_build

%if_enabled docs
%generate_pickles $PWD $PWD/docs/html %oname
%endif

%install
%makeinstall_std
install -d %buildroot%python_sitelibdir/gtk-2.0
mkdir -p %buildroot%_includedir/python%_python_version

#ifarch x86_64
#mv %buildroot%python_sitelibdir_noarch/gtk-2.0/* \
#	%buildroot%python_sitelibdir/gtk-2.0/
#endif
mv %buildroot%_includedir/pygtk-2.0 \
	%buildroot%_includedir/python%_python_version/%oname
subst "s|\${includedir}/pygtk-2.0|\${includedir}/python%_python_version/%oname|g" \
	%buildroot/%_pkgconfigdir/*.pc

# something broken if gobject still here
test -f %buildroot%python_sitelibdir/gtk-2.0/gobject.so && exit 1
# don't like x11 symbols due directfb
#objdump -t %buildroot%python_sitelibdir/gtk-2.0/gtk/_gtk.so | grep -i x11 && exit 1

# forking

mv %buildroot%python_sitelibdir/gtk-2.0/gtk \
	%buildroot%python_sitelibdir/gtk-2.0/%qname

cp -fR tests %buildroot%python_sitelibdir/gtk-2.0/tests_git
touch %buildroot%python_sitelibdir/gtk-2.0/tests_git/__init__.py

mv %buildroot%_bindir/pygtk-demo \
	%buildroot%_bindir/%oname-demo
mv %buildroot%_datadir/pygtk \
	%buildroot%_datadir/%oname
mv %buildroot%_libdir/pygtk \
	%buildroot%_libdir/%oname
mv %buildroot%_gtkdocdir/pygtk %buildroot%_gtkdocdir/%oname

install -p -m644 %SOURCE1 %buildroot%python_sitelibdir

# pickles

%if_enabled docs
install -d %buildroot%python_sitelibdir/%oname
cp -fR pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc AUTHORS NEWS README MAPPING ChangeLog* THREADS TODO
%python_sitelibdir/%oname.py*
%python_sitelibdir/gtk-2.0/*
%exclude %python_sitelibdir/gtk-2.0/%qname/glade.*
%exclude %python_sitelibdir/gtk-2.0/tests_git

%files demo
%_bindir/%oname-demo
%_libdir/%oname/

%files libglade
%python_sitelibdir/gtk-2.0/gtk_git/glade.*

%files devel
%_bindir/%oname-codegen-2.0
%python_includedir/pygtk_git/pygtk/
%_pkgconfigdir/pygtk*.pc

%files devel-data
%_datadir/%oname/

%files tests
%python_sitelibdir/gtk-2.0/tests_git

%if_enabled docs
%files doc
%_gtkdocdir/%oname/

%files pickles
%doc %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle
%endif

%changelog
* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.24.1-alt3.git20111002
- Rebuilt with updated NumPy

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.24.1-alt2.git20111002
- Enabled docs

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.24.1-alt1.git20111002.1
- Rebuild with Python-2.7

* Wed Oct 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.24.1-alt1.git20111002
- New snapshot

* Mon Apr 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.24.1-alt1.git20110402
- Version 2.24.1

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.23.2-alt1.git20110312
- Version 2.23.2

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.23.0-alt1.git20101104.1
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.23.0-alt1.git20101104
- Version 2.23.0

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.17.1-alt1.git20100730.1
- Defined lost macro %%_gtkdocdir

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.17.1-alt1.git20100730
- New snapshot

* Tue Jun 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.17.1-alt1.git20100508
- Version 2.17.1

* Mon Mar 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.17.0-alt1.git20100220
- Fork from upstream git repository
- Added tests and pickles package
- Moved devel data files into separate package
- No examples (see original package)

* Wed Jan 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.17.0-alt1.1
- Rebuild with new NumPy

* Sun Dec 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.17.0-alt1
- 2.17.0

* Tue Nov 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt4
- updated buildreqs

* Mon Oct 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt3
- removed obsolete buildreq on python-module-Numeric (closes #21915)

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0
- NumPy support enabled

* Fri Mar 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.14.1-alt1
- 2.14.1

* Mon Feb 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt1
- 2.14.0

* Mon Dec 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.13.0-alt3
- requires latest python-module-pygobject, python-module-pycairo to
  avoid #18279 and similar bugs

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 2.13.0-alt2
- enabled x11 support (fix altbug #18115)
- built -doc and -examples subpackages as noarch

* Tue Sep 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.13.0-alt1
- 2.13.0

* Fri Mar 21 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12.1-alt1
- new version 2.12.1 (with rpmrb script)

* Thu Nov 01 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt2
- build without X11 binding, add test for it

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt1
- new version 2.12.0 (with rpmrb script)

* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.6-alt1
- new version 2.10.6 (with rpmrb script)

* Wed Feb 21 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.4-alt0.1
- new version, enable doc build, update buildreq
- disable GDK_TARGET_X11 (x11 specific functions)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.10.3-alt0.1
- new version 2.10.3 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.6-alt0.1
- add require pyobject version
- new version 2.9.6 (with rpmrb script)

* Mon Jul 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt0.1
- new version 2.9.0 (with rpmrb script)

* Sat Mar 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.8.4-alt2
- fixes for python-strict in requires (bug #4568 again)

* Thu Mar 09 2006 Vitaly Lipatov <lav@altlinux.ru> 2.8.4-alt1
- rebuild without gobject
- add test against gobject inside

* Sat Mar 04 2006 Vitaly Lipatov <lav@altlinux.ru> 2.8.4-alt0.1
- new version
- move gobject binding to standalone package
- remove COPYING link from doc
- remove gobject from this package (add buildreq to it)
- update buildrequires

* Thu Dec 08 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.2-alt2
- add require for python-module-pycairo (bug #8608)

* Tue Nov 22 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.2-alt1
- enable build cairo.gtk (#8011)

* Fri Oct 14 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.2-alt0.1
- new version

* Fri Oct 07 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt0.1
- new version

* Sun Sep 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt0.1
- new version
- move includes to python%__python_version/pygtk

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version
- build with python 2.4

* Mon Jan 24 2005 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt1
- new version

* Sat Dec 18 2004 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt3
- remove gtk_cell_view_set_value (due GTK API changes in 2.6.0)

* Thu Dec 16 2004 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt2
- add fix GTK API change (fix problem marked in bug #5678)

* Sat Dec 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1.1
- rebuild

* Sat Nov 06 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt1
- Added module directories to %%_findprov_lib_path

* Fri Nov 05 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt0.1
- Updated to 2.4.1
- Versioned dependencies as required by configure
- Buildreq
- Spec cleanup

* Fri Jul 23 2004 Vitaly Lipatov <lav@altlinux.ru> 2.3.94-alt1
- new version

* Fri Jul 23 2004 Vitaly Lipatov <lav@altlinux.ru> 2.3.93-alt2
- backport libglade from 2.3.92 (broken XML)

* Tue Jul 20 2004 Vitaly Lipatov <lav@altlinux.ru> 2.3.93-alt1
- new version

* Thu Jul 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.3.92-alt1
- new version (from unstable 2.4)

* Tue Jul 13 2004 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- renamed
- spec cleanup (according to python policy)
- remove COPYING
- new version

* Mon Feb 09 2004 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt5
- python23 build
- separate package for examples
- changed group to Development/Python
- added gl.so

Packager: Egor S. Orlov
* Wed Oct 29 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt4
- Added python22 requires
- Aded _gtk.so to the package

* Thu Oct 23 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt3
- Added URL

* Thu Oct 23 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt2
- hasher build
- added gtkglarea2(-devel) dependency

* Mon Sep 29 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt1
- New version

* Tue Nov 12 2002 AEN <aen@altlinux.ru> 1.99.12-alt1
- first build for Sisyphus

* Thu Oct 31 2002 Matt Wilson <msw@redhat.com>
- rebuild for multilib
- use %%configure

* Fri Aug 30 2002 Matt Wilson <msw@redhat.com>
- fix pixbuf leaks (#72137)
- five more pixbuf leaks plugged

* Wed Aug 28 2002 Jonathan Blandford <jrb@redhat.com>
- remover Packager tag

* Tue Aug 27 2002 Jonathan Blandford <jrb@redhat.com>
- add binding for gdk_atom_intern

* Mon Jul 29 2002 Matt Wilson <msw@redhat.com>
- 0.99.12

* Wed Jul 17 2002 Matt Wilson <msw@redhat.com>
- new version from CVS

* Thu Jun 27 2002 Tim Waugh <twaugh@redhat.com>
- Fix bug #65770.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 17 2002 Matt Wilson <msw@redhat.com>
- new version from CVS

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Jeremy Katz <katzj@redhat.com>
- 1.99.10

* Wed Feb 27 2002 Matt Wilson <msw@redhat.com>
- 1.99.8

* Mon Jan 28 2002 Matt Wilson <msw@redhat.com>
- added atkmodule.so to file list

* Thu Oct 18 2001 Matt Wilson <msw@redhat.com>
- fix devel filelist to match new header location

* Mon Oct 15 2001 Matt Wilson <msw@redhat.com>
- get the headers from their new version-specific location

* Thu Oct 11 2001 Matt Wilson <msw@redhat.com>
- fixed typo in devel filelist
- added macro that tests to see if we have libglade2, make the
  filelist a condition of that
- changed name to 'pygtk2' to avoid name conflict with pygtk
