%define oname fixtures2

%def_with python3

Name: python-module-%oname
Version: 0.1.7
Release: alt1.git20171218.1
Summary: Extension of the fixtures test framework
License: Free
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/fixtures2/

# https://github.com/CooledCoffee/fixtures2.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-mox python-module-fixtures python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-mox python3-module-fixtures python3-module-pytest python3-module-html5lib
%endif

%py_provides %oname
%py_requires mox fixtures

%description
Fixtures2 is an extension of the fixtures test framework.

%if_with python3
%package -n python3-module-%oname
Summary: Extension of the fixtures test framework
Group: Development/Python3
%py3_provides %oname
%py3_requires mox fixtures

%description -n python3-module-%oname
Fixtures2 is an extension of the fixtures test framework.
%endif

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
export PYTHONPATH=%buildroot%python_sitelibdir
py.test -vv
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.7-alt1.git20171218.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt1.git20171218
- Updated to upstream version 0.1.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20140528.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20140528.1
- NMU: Use buildreq for BR.

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20140528
- Initial build for Sisyphus

