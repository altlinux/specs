%define oname invocations

%def_with python3

Name: python-module-%oname
Version: 0.6.2
Release: alt2.git20141113
Summary: Reusable Invoke tasks
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/invocations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyinvoke/invocations.git
Source: %name-%version.tar
Buildarch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-invoke
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-invoke
%endif

%py_provides %oname

%description
Invocations is a collection of reusable Invoke tasks/task modules,
including (but not limited to) Python project management tools such as
documentation building and dependency organization.

It has no stand-alone components and is designed to be imported into
your pre-existing Invoke task files.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Invocations is a collection of reusable Invoke tasks/task modules,
including (but not limited to) Python project management tools such as
documentation building and dependency organization.

It has no stand-alone components and is designed to be imported into
your pre-existing Invoke task files.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Reusable Invoke tasks
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Invocations is a collection of reusable Invoke tasks/task modules,
including (but not limited to) Python project management tools such as
documentation building and dependency organization.

It has no stand-alone components and is designed to be imported into
your pre-existing Invoke task files.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Invocations is a collection of reusable Invoke tasks/task modules,
including (but not limited to) Python project management tools such as
documentation building and dependency organization.

It has no stand-alone components and is designed to be imported into
your pre-existing Invoke task files.

This package contains tests for %oname.

%prep
%setup

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
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2.git20141113
- Added necessary requirements
- Enabled testing

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20141113
- Initial build for Sisyphus

