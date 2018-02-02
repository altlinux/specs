%define oname pytest-oot

%def_with python3

Name: python-module-%oname
Version: 0.2.6
Release: alt1.1.1
Summary: Run object-oriented tests in a simple format
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-oot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides pytest_oot

%description
Run object-oriented tests in a simple format.

%package -n python3-module-%oname
Summary: Run object-oriented tests in a simple format
Group: Development/Python3
%py3_provides pytest_oot

%description -n python3-module-%oname
Run object-oriented tests in a simple format.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO example
%python_sitelibdir/*
%exclude %python_sitelibdir/example

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO example
%python3_sitelibdir/*
%exclude %python3_sitelibdir/example
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.6-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1
- Version 0.2.6

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

