%define oname zope.pytest
Name: python-module-%oname
Version: 0.1
Release: alt3.1
Summary: zope pytest integration
License: ZPL
Group: Development/Python
Url: http://packages.python.org/zope.pytest
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
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

%py_requires zope.configuration zope.component zope.testing
%py_requires zope.event zope.processlifetime zope.app.publication
%py_requires zope.app.wsgi webob simplejson zope.app.appsetup
%py_requires zope.app.zcmlfiles zope.browserpage zope.securitypolicy
%py_requires infrae.testbrowser ZODB3

%description
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

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

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

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added documentation and pickles

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

