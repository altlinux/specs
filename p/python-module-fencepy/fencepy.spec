%define oname fencepy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2
Release: alt1.git20141231.1.1
Summary: Standardized fencing off of python virtual environments on a per-project basis
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/fencepy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ajk8/fencepy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-virtualenv python-module-sh
BuildPreReq: python-module-pytest-pep8 python-module-pytest-cov
BuildPreReq: python-module-coveralls git /dev/pts
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-virtualenv python3-module-sh
BuildPreReq: python3-module-pytest-pep8 python3-module-pytest-cov
BuildPreReq: python3-module-coveralls
%endif

%py_provides %oname

%description
Standardized fencing off of python virtual environments on a per-project
basis. The idea is to take a directory as an input and create and manage
a python virtual environment in a known location.

%package -n python3-module-%oname
Summary: Standardized fencing off of python virtual environments on a per-project basis
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Standardized fencing off of python virtual environments on a per-project
basis. The idea is to take a directory as an input and create and manage
a python virtual environment in a known location.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20141231.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20141231.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20141231
- Initial build for Sisyphus

