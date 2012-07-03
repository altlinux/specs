# test new macroses
%define python_build CFLAGS="%optflags" python setup.py build
%define python_install python setup.py install --root %buildroot --optimize=2

%def_with python3

%define oname BeautifulSoup
Name: python-module-%oname
Version: 3.2.1
Release: alt2

Summary: HTML/XML parser for quick-turnaround applications like screen-scraping

License: PSF
Group: Development/Python
Url: http://www.crummy.com/software/BeautifulSoup/

BuildArch: noarch

%setup_python_module %oname

Source: %oname-%version.tar.bz2

# Automatically added by buildreq on Sat May 26 2007
BuildRequires: python-devel python-modules-compiler python-modules-encodings
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3 python3-module-sgmllib
%endif

%description
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.

%if_with python3
%package -n python3-module-%oname
Summary: HTML/XML parser for quick-turnaround applications like screen-scraping (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Beautiful Soup parses a (possibly invalid) XML or HTML document into a
tree representation. It provides methods and Pythonic idioms that make
it easy to navigate, search, and modify the tree.
%endif

%prep
%setup -n %oname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build
%if_with python3
pushd ../python3
for i in *.py; do
	2to3 -w $i
done
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt2
- Added module for Python 3

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

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

