%define oname zope.pytest

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt4
Summary: zope pytest integration
License: ZPL
Group: Development/Python
Url: http://packages.python.org/zope.pytest
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-zope.browserpage
BuildPreReq: python-module-zope.app.appsetup python-module-docutils
BuildPreReq: python-module-zope.app.zcmlfiles python-module-zope.schema
BuildPreReq: python-module-zope.securitypolicy python-module-simplejson
BuildPreReq: python-module-infrae.testbrowser
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.component python-module-zope.testing
BuildPreReq: python-module-zope.event python-module-zope.processlifetime
BuildPreReq: python-module-zope.app.publication python-module-zope.app.wsgi
BuildPreReq: python-module-ZODB3 python-module-webob
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.configuration zope.component zope.testing
%py_requires zope.event zope.processlifetime zope.app.publication
%py_requires zope.app.wsgi webob simplejson zope.app.appsetup
%py_requires zope.app.zcmlfiles zope.browserpage zope.securitypolicy
%py_requires infrae.testbrowser ZODB3

%description
This package contains a set of helper functions to test Zope/Grok
using pytest. It currently lacks special support for doctesting.

%package -n python3-module-%oname
Summary: zope pytest integration
Group: Development/Python3
%py3_requires zope.configuration zope.component zope.testing
%py3_requires zope.event zope.processlifetime zope.app.publication
%py3_requires zope.app.wsgi webob simplejson zope.app.appsetup
%py3_requires zope.app.zcmlfiles zope.browserpage zope.securitypolicy
%py3_requires infrae.testbrowser ZODB3

%description -n python3-module-%oname
This package contains a set of helper functions to test Zope/Grok
using pytest. It currently lacks special support for doctesting.

%package pickles
Summary: Pickles for zope.pytest
Group: Development/Python

%description pickles
This package contains a set of helper functions to test Zope/Grok
using pytest. It currently lacks special support for doctesting.

This package contains pickles for zope.pytest.

%package docs
Summary: Documentation for zope.pytest
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains a set of helper functions to test Zope/Grok
using pytest. It currently lacks special support for doctesting.

This package contains documentation for zope.pytest.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

export PYTHONPATH=$PWD/src
pushd doc
%make html
%make pickle

popd
%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

mkdir -p %buildroot%python_sitelibdir/%name
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%name/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/%name/pickle

%files pickles
%python_sitelibdir/%name/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added documentation and pickles

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

