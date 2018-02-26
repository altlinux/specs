%define origname gnuplot-py

Name: python-module-gnuplot
Version: 1.8
Release: alt4.1

Summary: Python interface to Gnuplot

License: LGPL
Group: Development/Python
Url: http://%origname.sourceforge.net/
# https://gnuplot-py.svn.sourceforge.net/svnroot/gnuplot-py
Source: %origname-%version.tar.gz
Source1: doc.tar.gz
Patch: %name-alt-python2.6.patch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 19 2006
BuildRequires: python-devel python-modules
BuildRequires: python-modules-compiler python-modules-encodings
BuildPreReq: libnumpy-devel

%description
Gnuplot.py is a Python package that allows you to create graphs
from within Python using the gnuplot plotting program.

%package doc
Summary: Documentation for Gnuplot.py
Group: Development/Documentation
BuildArch: noarch

%description doc
Gnuplot.py is a Python package that allows you to create graphs
from within Python using the gnuplot plotting program.

This package contains documentation for Gnuplot.py.

%prep
%setup -q -n %origname-%version
tar -xzf %SOURCE1
#if "%__python_version" != "2.5"
#patch -p2
#endif

%build
# remove crap
rm -f gp_cygwin.py gp_java.py gp_mac* gp_win32.py gnuplot_Suites.py

%python_build
chmod 644 *.txt

%install
%python_install --record=INSTALLED_FILES

# Avoid bytecompile :)
#unset RPM_PYTHON

install -d %buildroot%_docdir/%name
cp -fR doc/* %buildroot%_docdir/%name/

%files -f INSTALLED_FILES
%python_sitelibdir/*
%doc ANNOUNCE.txt CREDITS.txt FAQ.txt NEWS.txt README.txt

%files doc
%_docdir/%name

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt4.1
- Rebuild with Python-2.7

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt4
- Rebuilt with reformed NumPy

* Fri Jan 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt3
- Rebuilt without python-module-Numeric

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2
- Rebuilt with python 2.6

* Thu Oct 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Version 1.8
- Added patch for Python 2.6 (ALT #21767)

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 1.7-alt2.1
- Rebuilt with python-2.5.

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 1.7-alt2
- Build as noarch.

* Wed Apr 19 2006 Victor Forsyuk <force@altlinux.ru> 1.7-alt1
- Initial build.
