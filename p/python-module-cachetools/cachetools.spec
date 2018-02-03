%define oname cachetools

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt1.1
Summary: Extensible memoizing collections and decorators
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cachetools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tkem/cachetools.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose
%endif

%py_provides %oname

%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library @lru_cache function
decorator.

%package -n python3-module-%oname
Summary: Extensible memoizing collections and decorators
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library @lru_cache function
decorator.

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
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20141230.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141230
- Initial build for Sisyphus

