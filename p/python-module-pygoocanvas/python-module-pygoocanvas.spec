%define oname pygoocanvas
%define ver_major 0.14
%define version %ver_major.1
%define release alt1.1
%setup_python_module pygoocanvas
%define _gtk_docdir %_datadir/gtk-doc/html

Name: python-module-pygoocanvas
Version: %version
Release: %release.1
Summary: GooCanvas python bindings
Packager: Alexey Shabalin <shaba at altlinux.ru>
Url: http://developer.berlios.de/projects/pygoocanvas/
License: LGPL
Group: Development/Python
Source: %gnome_ftp/%oname/%ver_major/%name-%version.tar
Patch0: %name-%version-%release.patch

BuildPreReq: rpm-build-gnome

# From configure.ac
BuildPreReq: python-module-pygobject-devel >= 2.10.1
BuildPreReq: python-module-pygtk-devel >= 2.10.0
BuildPreReq: libgoocanvas-devel >= 0.14
BuildPreReq: python-module-pycairo-devel >= 1.8.4

BuildRequires: gcc-c++ gtk-doc   
BuildRequires: gnome-doc-utils
BuildRequires: docbook-style-xsl
BuildPreReq: python-module-pygobject-devel-doc

Provides: %oname = %version-%release

%description
This package includes Python bindings for GooCanvas. It is
needed to run programs written in Python and using GooCanvas
set.

%package devel
Summary: GooCanvas python bindings - Development files
Group: Development/Python
Requires: %name = %version

%description devel
This package includes development files of python bindings for GooCanvas.

%prep
%setup -q
sed -i -e 's,^\(goocanvasmodule_la_LIBADD = $(PYGOOCANVAS_LIBS)\),\1 -lpython%__python_version,g' Makefile.am

%build
./autogen.sh
%configure --enable-gtk-doc
%make_build

%install
%makeinstall

%files
%python_sitelibdir/*

%files devel
%doc %_gtk_docdir/*
%_pkgconfigdir/*.pc

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14.1-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt1.1
- Rebuilt with python 2.6

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1
- move gtk docs to devel package

* Wed Oct 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Sun Aug 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- initial build for ALTLinux

