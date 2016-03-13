%define oname pytest-pep8

%def_with python3

Name: python-module-%oname
Version: 1.0.6
Release: alt1.hg20140427.1
Summary: pytest plugin to check PEP8 requirements
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-pep8/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/pytest-dev/pytest-pep8
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides pytest_pep8
%py_requires execnet pytest_cache

%description
pytest plugin to check PEP8 requirements.

%package -n python3-module-%oname
Summary: pytest plugin to check PEP8 requirements
Group: Development/Python3
%py3_provides pytest_pep8
%py3_requires execnet pytest_cache

%description -n python3-module-%oname
pytest plugin to check PEP8 requirements.

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

%files
%doc CHANGELOG *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.6-alt1.hg20140427.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.hg20140427
- Initial build for Sisyphus

