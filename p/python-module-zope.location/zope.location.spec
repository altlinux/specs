%define oname zope.location

%def_with python3

Name: python-module-%oname
Version: 4.0.4
Release: alt2.dev0.git20150128
Summary: Zope Location
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.location/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.location.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-repoze.sphinx.autointerface
BuildPreReq: python-module-zope.interface-tests
BuildPreReq: python-module-zope.schema-tests
BuildPreReq: python-module-zope.proxy-tests
BuildPreReq: python-module-zope.configuration-tests
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-coverage
BuildPreReq: python-module-zope.copy-tests
BuildPreReq: python-module-%oname-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-zope.interface
BuildPreReq: python3-module-zope.schema
BuildPreReq: python3-module-zope.proxy
BuildPreReq: python3-module-zope.configuration-tests
BuildPreReq: python3-module-zope.component
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-coverage
BuildPreReq: python3-module-zope.copy-tests
BuildPreReq: python3-module-%oname-tests
%endif

%py_requires zope zope.interface zope.schema zope.component zope.proxy
%py_requires zope.configuration

%description
In Zope3, location are special objects that has a structural location.

%package -n python3-module-%oname
Summary: Zope Location
Group: Development/Python3
%py3_requires zope zope.interface zope.schema zope.component zope.proxy
%py3_requires zope.configuration

%description -n python3-module-%oname
In Zope3, location are special objects that has a structural location.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Location
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.configuration.tests zope.copy.tests

%description -n python3-module-%oname-tests
In Zope3, location are special objects that has a structural location.

This package contains tests for Zope Location.

%package tests
Summary: Tests for Zope Location
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.configuration.tests zope.copy.tests

%description tests
In Zope3, location are special objects that has a structural location.

This package contains tests for Zope Location.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2.dev0.git20150128
- New snapshot

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev.git20141027
- New snapshot

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1.dev.git20140319
- Version 4.0.4dev

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.1-alt1
- Version 3.9.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus

