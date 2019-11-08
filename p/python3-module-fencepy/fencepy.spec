%define oname fencepy

%def_disable check

Name: python3-module-%oname
Version: 0.2
Release: alt2

Summary: Standardized fencing off of python virtual environments on a per-project basis
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/fencepy/
# https://github.com/ajk8/fencepy.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-virtualenv python3-module-sh
BuildRequires: python3-module-pytest-pep8 python3-module-pytest-cov
BuildRequires: python3-module-coveralls

%py3_provides %oname


%description
Standardized fencing off of python virtual environments on a per-project
basis. The idea is to take a directory as an input and create and manage
a python virtual environment in a known location.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Nov 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20141231.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20141231.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20141231
- Initial build for Sisyphus

