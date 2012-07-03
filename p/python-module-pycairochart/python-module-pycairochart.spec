%define oname pycairochart
Name: python-module-%oname
Version: 0.1.1
Release: alt0.1.2.1

Summary: Drawing Charts with python

License: GPL
Group: Development/Python
Url: http://www.bettercom.de/de/pycairochart

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.bettercom.de/misc/%oname-%version.tar.bz2

%setup_python_module cairochart

# Automatically added by buildreq on Sat Jun 03 2006
BuildRequires: python-modules-encodings

%description
The pyCairoChart module for python offers an easy way
to create 2D-Charts using the excellent cairo graphics library

%package devel
Summary: Development files for %oname
Group: Development/Python
Requires: %name = %version-%release

%description devel
Development files for %oname.

%prep
%setup -q -n CairoChart-%version

%install
ls -l
install -m 644 -D CairoChart.py %buildroot%python_sitelibdir/CairoChart.py

%files
%doc README.tmpl example.py
%python_sitelibdir/*

#%files devel
#%_includedir/pycairo
#%_pkgconfigdir/pycairo.pc
#%doc README NEWS ChangeLog examples

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt0.1.2.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt0.1.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.1.1-alt0.1.1
- Rebuilt with python-2.5.

* Sat Jun 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt0.1
- initial build for ALT Linux Sisyphus
