%define major 2.10
%define oname pygtksourceview
Name: python-module-%oname
Version: %major.1
Release: alt1.1

Summary: python bindings for the version 2 of the GtkSourceView library

License: LGPL
Group: Development/Python
Url: http://www.pygtk.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://ftp.gnome.org/pub/gnome/sources/%oname/%major/%oname-%version.tar.bz2

BuildPreReq: python-module-pygtk-devel >= 2.10.0
BuildPreReq: python-module-pygobject-devel >= 2.15.2
# Horror (style.css from this package required to build documentation)
BuildPreReq: python-module-pygobject-devel-doc
BuildPreReq: libgtksourceview-devel >= 2.9.7
BuildRequires: gtk-doc docbook-dtds docbook-style-xsl xsltproc gnome-common

%description
Contains python bindings for the version 2 of the
GtkSourceView library.

%package devel
Summary: development files for GtkSourceView python binding
Group: Development/Python
Requires: %name = %version-%release

%description devel
This package contains development files for GtkSourceView python binding

%package devel-doc
Summary: development documentation for GtkSourceView python binding
Group: Development/Python
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains development documentation for GtkSourceView python binding

%prep
%setup -q -n %oname-%version

%build
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog README NEWS
%python_sitelibdir/gtksourceview2.so
%exclude %python_sitelibdir/*.la

%files devel
%_pkgconfigdir/*
%_datadir/pygtk/2.0/defs/*.defs

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.10.1-alt1.1
- Rebuild with Python-2.7

* Sun Apr 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.1-alt1
- 2.10.1

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.10.0-alt1
- 2.10.0

* Tue Feb 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.9.2-alt1
- 2.9.2

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.1
- Rebuilt with python 2.6

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Aug 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.7.0-alt1
- 2.7.0

* Mon Mar 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0
- updated buildreqs
- new devel-doc noarch subpackage

* Fri Mar 21 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- remove provides/obsoletes for gtksourceview1

* Sat Dec 01 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Linux Sisyphus
