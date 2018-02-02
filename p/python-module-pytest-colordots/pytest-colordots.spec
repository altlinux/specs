%define oname pytest-colordots

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.1
Summary: Colorizes the progress indicators
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pytest-colordots

# https://github.com/svenstaro/pytest-colordots.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(colorama) python2.7(pytest)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(colorama) python3(pytest)
%endif

%py_provides pytest_colordots

%description
Colorizes the progress indicators

This is an adoption of pytest-greendots which sadly does not have an
upstream repository.

%if_with python3
%package -n python3-module-%oname
Summary: Colorizes the progress indicators
Group: Development/Python3
%py3_provides pytest_colordots

%description -n python3-module-%oname
Colorizes the progress indicators

This is an adoption of pytest-greendots which sadly does not have an
upstream repository.
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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1-alt1
- Updated to upstream version 1.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20141120.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20141120.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141120
- Initial build for Sisyphus

