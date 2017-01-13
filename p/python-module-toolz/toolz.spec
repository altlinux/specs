%define _unpackaged_files_terminate_build 1
%define oname toolz

%def_with python3

Name: python-module-%oname
Version: 0.8.2
Release: alt1
Summary: List processing tools and functional utilities
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/toolz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/75/9c/a26de5efd56009e15af607bff6d2a395631e3c20e7c64b861c9bc4b34288/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
A set of utility functions for iterators, functions, and dictionaries.

%package -n python3-module-%oname
Summary: List processing tools and functional utilities
Group: Development/Python3

%description -n python3-module-%oname
A set of utility functions for iterators, functions, and dictionaries.

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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

