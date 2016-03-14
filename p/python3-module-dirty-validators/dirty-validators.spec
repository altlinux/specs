%define oname dirty-validators
Name: python3-module-%oname
Version: 0.2.2
Release: alt1.git20150429.1
Summary: Validate library for python 3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/dirty-validators/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/alfred82santa/dirty-validators.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-dirty-models

%py3_provides dirty_validators
%py3_requires dirty_models

%description
Agnostic validators for python 3.

Features:

* Python 3 package.
* Easy to create a validator.
* Chained validations.
* Conditional validations.
* Specific error control messages.
* Dirty model integration
* No database dependent.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
nosetests3 -v --with-coverage -d --cover-package=dirty_validators

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20150429.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150429
- Initial build for Sisyphus

