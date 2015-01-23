%define oname yamltypes

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1
Summary: Tools for validating, documenting, and editing json and yaml data
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yamltypes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-module-yaml
BuildPreReq: python-module-dictns python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-yaml
BuildPreReq: python3-module-dictns python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires yaml dictns

%description
Tools for validating, documenting, and editing json and yaml data.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Tools for validating, documenting, and editing json and yaml data.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Tools for validating, documenting, and editing json and yaml data
Group: Development/Python3
%py3_provides %oname
%py3_requires yaml dictns

%description -n python3-module-%oname
Tools for validating, documenting, and editing json and yaml data.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Tools for validating, documenting, and editing json and yaml data.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

