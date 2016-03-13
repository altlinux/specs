%define oname nose-detecthttp

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.dev.git20141124.1
Summary: A nose plugin to detect tests making http calls
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-detecthttp
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/venmo/nose-detecthttp.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-vcrpy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-vcrpy
%endif

%py_provides detecthttp

%description
A nose plugin that can detect tests making external http calls.

%package -n python3-module-%oname
Summary: A nose plugin to detect tests making http calls
Group: Development/Python3
%py3_provides detecthttp

%description -n python3-module-%oname
A nose plugin that can detect tests making external http calls.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.dev.git20141124.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.dev.git20141124
- Initial build for Sisyphus

