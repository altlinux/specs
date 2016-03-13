%define oname flup
%define version 1.0.3
%define release alt2
%define subrel hg20120223
%setup_python_module %oname

%def_with python3

Summary: Random assortment of WSGI servers, middleware
Name: python-module-%oname
Version: %version
Release: alt2.hg20120223.1.1
# http://hg.saddi.com/flup-server
Source0: %modulename.tar.bz2
License: BSD
Group: Development/Python
URL: http://www.saddi.com/software/flup/
Packager: Python Development Team <python at packages.altlinux.org>

BuildArch: noarch
#BuildPreReq: python-module-setuptools python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%description
Random assortment of WSGI servers, middleware

%if_with python3
%package -n python3-module-%oname
Summary: Random assortment of WSGI servers, middleware (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Random assortment of WSGI servers, middleware
%endif

%package docs
Summary: Documentation for flup
Group: Development/Documentation
BuildArch: noarch

%description docs
Random assortment of WSGI servers, middleware

This package contains documentation for flup.

%package pickles
Summary: Pickles for flup
Group: Development/Documentation
BuildArch: noarch

%description pickles
Random assortment of WSGI servers, middleware

This package contains pickles for flup.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx docs/source

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

#docs

%make -C docs pickle
%make -C docs html

%install
%python_install --optimize=2 --record=INSTALLED_FILES
%if_with python3
pushd ../python3
%python3_install
popd
%endif

#docs

cp -fR docs/build/pickle %buildroot%python_sitelibdir_noarch/%oname/

%files -f INSTALLED_FILES
%exclude %python_sitelibdir_noarch/%oname/pickle

%files docs
%doc docs/build/html

%files pickles
%python_sitelibdir_noarch/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir_noarch/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt2.hg20120223.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt2.hg20120223.1
- NMU: Use buildreq for BR.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt2.hg20120223
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 17 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.3-alt1.hg20120223.1
- Rebuild with Python-3.3
- Fix non-identical noarch packages (python{,3}-module-flup)

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20120223
- New snapshot
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1.hg20101014.1.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20101014.1
- Rebuilt with python-module-sphinx-devel

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20101014
- New snapshot

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20100525.1
- Added docs and pickles

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20100525
- Version 1.0.3 (ALT #23628)

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.svn2016
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.5-alt0.svn2016.1
- Rebuilt with python-2.5.

* Sat Jul 01 2006 Ivan Fedorov <ns@altlinux.ru> 0.5-alt0.svn2016
- update to svn r2016

* Wed Oct 19 2005 Ivan Fedorov <ns@altlinux.ru> 0.5-alt0.svn1823
- Initial build for ALT Linux.
