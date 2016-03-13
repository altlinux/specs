%define oname cov-core

%def_with python3

Name: python-module-%oname
Version: 1.15.0
Release: alt1.git20141122.1
Summary: plugin core for use by pytest-cov, nose-cov and nose2-cov
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cov-core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/schlamar/cov-core.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-coverage
%endif

%py_provides cov_core
%py_provides cov_core_init

%description
This is a lib package for use by pytest-cov, nose-cov and nose2-cov.
Unless you're developing a coverage plugin for a test framework, you
probably want one of those.

%package -n python3-module-%oname
Summary: plugin core for use by pytest-cov, nose-cov and nose2-cov
Group: Development/Python3
%py3_provides cov_core
%py3_provides cov_core_init

%description -n python3-module-%oname
This is a lib package for use by pytest-cov, nose-cov and nose2-cov.
Unless you're developing a coverage plugin for a test framework, you
probably want one of those.

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
%doc *.rst *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.15.0-alt1.git20141122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.0-alt1.git20141122
- Version 1.15.0

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.0-alt1.git20140822
- Initial build for Sisyphus

