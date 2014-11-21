%define oname yanc

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20141022
Summary: Yet another nose colorer
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/yanc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/0compute/yanc.git
Source: %name-%version.tar
# https://github.com/0compute/makeenv
Source1: makeenv.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: gmsl
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-coverage
%endif

%py_provides %oname

%description
YANC is color output plugin for nose that plays nicely with others.

To enable the plugin pass --with-yanc to nosetests.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
YANC is color output plugin for nose that plays nicely with others.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Yet another nose colorer
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
YANC is color output plugin for nose that plays nicely with others.

To enable the plugin pass --with-yanc to nosetests.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
YANC is color output plugin for nose that plays nicely with others.

This package contains tests for %oname.

%prep
%setup

#rmdir .makeenv
tar -xf %SOURCE1

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141022
- Version 0.3.1

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20130830
- Initial build for Sisyphus

