%define _unpackaged_files_terminate_build 1
%define oname zope.interface

%def_with python3
%def_disable check

Summary: Zope interfaces package
Name: python-module-%oname
Version: 4.3.3
#define subver c1
Url: http://www.python.org/pypi/zope.interface
%ifndef subver
Release: alt1
%else
Release: alt0.%subver
%endif
# git://github.com/zopefoundation/zope.interface.git
Source0: https://pypi.python.org/packages/44/af/cea1e18bc0d3be0e0824762d3236f0e61088eeed75287e7b854d65ec9916/%{oname}-%{version}.tar.gz
License: ZPL
Group: Development/Python

%setup_python_module %oname

#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-zope.fixers-tests
#BuildPreReq: python-module-zope.event-tests
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-repoze.sphinx.autointerface
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-repoze python-module-repoze.sphinx python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-setuptools python3-module-zope python3-module-zope.interface
#Manually removed python*-module-zope.fixers and python*-module-zope.event
BuildPreReq: python-module-alabaster python-module-coverage python-module-docutils
BuildPreReq: python-module-html5lib python-module-nose python-module-objects.inv python-module-pytest
BuildPreReq: python-module-repoze.sphinx.autointerface
BuildPreReq: python3-devel python3-module-coverage python3-module-nose
BuildPreReq: python3-module-pytest rpm-build-python3 time
#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zope.fixers-tests
#BuildPreReq: python3-module-zope.event-tests
#BuildPreReq: python3-module-nose
#BuildPreReq: python3-module-coverage
%endif

%description
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

%if_with python3
%package -n python3-module-%oname
Summary: Zope interfaces package (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

%package -n python3-module-%oname-tests
Summary: Tests for zope.interface (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.event

%description -n python3-module-%oname-tests
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

This package contains tests for zope.interface.
%endif

%package tests
Summary: Tests for zope.interface
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.event

%description tests
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

This package contains tests for zope.interface.

%package pickles
Summary: Pickles for zope.interface
Group: Development/Python

%description pickles
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

This package contains pickles for zope.interface.

%package docs
Summary: Documentation for zope.interface
Group: Development/Documentation
BuildArch: noarch

%description docs
This is a separate distribution of the zope.interface package used in
Zope 3, along with the packages it depends on.

This package contains documentation for zope.interface.

%prep
%setup -q -n %{oname}-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug build_ext
%if_with python3
pushd ../python3
%python3_build build_ext
popd
%endif

%install
%python_module_declare %python_sitelibdir/zope
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD/src
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
 
%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/zope/interface/tests
%exclude %python_sitelibdir/zope/interface/common/tests
%doc *.txt *.rst

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/zope/interface/tests
%python_sitelibdir/zope/interface/common/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/zope/interface/tests
%exclude %python3_sitelibdir/zope/interface/common/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/zope/interface/tests
%python3_sitelibdir/zope/interface/common/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.3.3-alt1
- automated PyPI update

* Tue Mar 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.3-alt1.dev0.git20150601.4
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 22 2016 Denis Medvedev <nbr@altlinux.org> 4.1.3-alt1.dev0.git20150601.3
- Fix deps for python 3.5

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.3-alt1.dev0.git20150601.2
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.1.3-alt1.dev0.git20150601.1
- NMU: Use buildreq for BR.

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1.dev0.git20150601
- New snapshot

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1.dev0.git20141227
- Version 4.1.3.dev0

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.dev.git20140319
- Version 4.1.2dev
- Added docs

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Moved all tests into tests subpackage

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Sat Mar 16 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.5-alt1
- Version 4.0.5

* Thu Jan 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt2
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.3-alt2.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt2
- Don't pack zope*egg-info

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.3-alt1
- Version 3.6.3

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Version 3.6.2

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Set as archdep package

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2
- Rebuilt with python 2.6

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.1.2
- Fixed file conflict with python-module-zope

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.1.1
- Fixed file conflict with python-module-zope (ALT #21981)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.3.0-alt1.1
- Rebuilt with python-2.5.

* Sun Feb 18 2007 Ivan Fedorov <ns@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Mon Nov 20 2006 Ivan Fedorov <ns@altlinux.ru> 3.1.0-alt1.c1
- 3.1.0c1

* Mon Oct 03 2005 Ivan Fedorov <ns@altlinux.ru> 3.0.1-alt1
- Initial build for ALT Linux.
