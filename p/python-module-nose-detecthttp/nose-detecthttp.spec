%define _unpackaged_files_terminate_build 1
%define oname nose-detecthttp

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1
Summary: A nose plugin to detect tests making http calls
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-detecthttp
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/venmo/nose-detecthttp.git
Source0: https://pypi.python.org/packages/c9/a0/e489bf2595218d63c790b406a72493412db6032657746b9c2672afceee16/%{oname}-%{version}.tar.gz
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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.dev.git20141124.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.dev.git20141124
- Initial build for Sisyphus

