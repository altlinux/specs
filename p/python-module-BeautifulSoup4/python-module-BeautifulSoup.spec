# test new macroses
%define python_build CFLAGS="%optflags" python setup.py build
%define python_install python setup.py install --root %buildroot --optimize=2

%def_without python3

%define oname BeautifulSoup4
Name: python-module-%oname
Version: 4.0.3
Release: alt2

Summary: HTML/XML parser for quick-turnaround applications like screen-scraping

License: PSF
Group: Development/Python
Url: http://www.crummy.com/software/BeautifulSoup/

BuildArch: noarch

%setup_python_module %oname

Source: BeautifulSoup-%version.tar.bz2

# Automatically added by buildreq on Sat May 26 2007
BuildRequires: python-devel python-modules-compiler python-modules-encodings
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

%package tests
Summary: Tests for BeautifulSoup4
Group: Development/Python
Requires: %name = %version-%release

%description tests
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

This package contains tests for BeautifulSoup4.

%if_with python3
%package -n python3-module-%oname
Summary: HTML/XML parser for quick-turnaround applications like screen-scraping (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

%package -n python3-module-%oname-tests
Summary: Tests for BeautifulSoup4 (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

This package contains tests for BeautifulSoup4.
%endif

%prep
%setup -n BeautifulSoup-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/bs4/test*

%files tests
%python_sitelibdir/bs4/test*

%if_with python3
%doc *.txt
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/bs4/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/bs4/test*
%endif

%changelog
* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Extracted tests into separate package

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.8.1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8.1-alt1
- Version 3.0.8.1

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.6-alt1.1
- Rebuilt with python 2.6

* Mon Jun 09 2008 Vitaly Lipatov <lav@altlinux.ru> 3.0.6-alt1
- new version 3.0.6 (with rpmrb script) - fix bug #14975

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt1
- change buildarch to noarch

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 3.0.4-alt0.1
- initial build for ALT Linux Sisyphus

