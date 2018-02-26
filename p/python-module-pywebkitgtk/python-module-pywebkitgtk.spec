%define oname pywebkitgtk
%define python_gtk_dir %python_sitelibdir/webkit
%define version 1.1.8
%define release alt1.1
%setup_python_module pywebkitgtk

Name: python-module-pywebkitgtk
Version: %version
Release: %release.1
Summary: Python Bindings for WebKit-gtk
Packager: Alexey Shabalin <shaba at altlinux.ru>
Group: Development/Python
License: GPLv2+
Url: http://code.google.com/p/pywebkitgtk/
Source: %name-%version.tar

Provides: %oname = %version-%release

BuildRequires: libwebkitgtk2-devel libxslt-devel python-module-pygtk-devel python-module-pygobject-devel

%description
The purpose of pywebkitgtk is to bring an alternative web engine to
Python/GTK+ application developers who might need a web browser engine for
their next application or developers wishing to have a better browser engine
that they can access to using the Python programming language.

%prep
%setup
# Link with current python
sed -i -e 's,^\(webkit_la_LIBADD = \$(DEPS_LIBS)\),\1 -lpython%_python_version,g' Makefile.am

%build
rm -f aclocal.m4 m4/l*.m4
ACLOCAL="aclocal -I ./m4" %autoreconf
%configure --disable-static
%make

%install
%make_install DESTDIR=%buildroot install
find %buildroot -name '*.la' -exec rm {} \;

%files
%doc AUTHORS COPYING MAINTAINERS NEWS README demos
%_datadir/pywebkitgtk
%python_gtk_dir

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.8-alt1.1.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.8-alt1.1
- Rebuilt for debuginfo

* Fri Oct 08 2010 Alexey Shabalin <shaba@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1.1
- Rebuilt with python 2.6

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Thu Aug 20 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Wed Jul 01 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Fri Apr 10 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- 1.0.2
- drop patches (upstream fixed)

* Wed Oct 29 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- initial build for ALTLinux

