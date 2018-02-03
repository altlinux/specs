%define oname nose-cov

%def_with python3

Name: python-module-%oname
Version: 1.6
Release: alt1.1.1
Summary: nose plugin for coverage reporting, including subprocesses and multiprocessing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-cov/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-cov-core
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-cov-core
%endif

%py_provides nose_cov

%description
This plugin produces coverage reports. It also supports coverage of
subprocesses.

All features offered by the coverage package should be available, either
through nose-cov or through coverage's config file.

%package -n python3-module-%oname
Summary: nose plugin for coverage reporting, including subprocesses and multiprocessing
Group: Development/Python3
%py3_provides nose_cov

%description -n python3-module-%oname
This plugin produces coverage reports. It also supports coverage of
subprocesses.

All features offered by the coverage package should be available, either
through nose-cov or through coverage's config file.

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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

