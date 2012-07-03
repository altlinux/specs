%define rel -5
%define oname gtkhst
Name: libgtkhst
Version: 0.4.0
Release: alt3.1.1

Summary: GTK widgets and object for data histograming

License: GPL
Group: Development/C
Url: http://sourceforge.net/projects/gtkhst/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%oname/%oname-%version%rel.tar.bz2
Patch: %name-%version.patch

BuildPreReq: gtk-doc

# Automatically added by buildreq on Thu Jan 03 2008
BuildRequires: gcc-c++ libgtk+2-devel python-module-pygtk-devel

%description
gtkhst is a collection of gobjects and gtk+ widgets, used to display
them, that allow an easy histograming and monitoring of data.

%package devel
Summary: Libraries, includes, etc. for gtkhst
Group: Development/C
Requires: %name = %version

%description devel
Libraries, includes, etc. for gtkhst

%package -n python-module-%oname
Summary: Python bindings for gtkhst
Group: Development/Python
Requires: %name = %version

%description -n python-module-%oname
gtkhst-python provides the python bindings for gtkhst

%prep
%setup -q -n %oname-%version%rel
#patch

%build
#__aclocal -I scripts
#__autoconf
%configure --enable-python
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/lib*.so.*

%files devel
%doc test/*.c test/*.h
%_libdir/lib*.so
%_includedir/*
%_pkgconfigdir/gtkhst.pc
%_datadir/gtk-doc/html/gtk-hst/*

%files -n python-module-%oname
%doc python/tsthst.py python/tstgobj.py
%python_sitelibdir/%oname

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt3.1.1
- Rebuild with Python-2.7

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3.1
- Rebuilt with python 2.6

* Wed Oct 14 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt3
- new version 0.4.0-5 (with rpmrb script)

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt2
- new version (0.4.0-4)

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Feb 25 2005 Carlos Lacasta <lacasta@localhost.localdomain> -
- Initial build.

