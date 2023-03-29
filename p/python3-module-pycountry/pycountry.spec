%define oname pycountry

%def_with check

Name: python3-module-%oname
Version: 22.3.5
Release: alt1

Summary: ISO country, subdivision, language, currency and script definitions
License: LGPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/pycountry/
Vcs: https://github.com/flyingcircusio/pycountry

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest-cov
%endif

%description
ISO country, subdivision, language, currency and script definitions and
their translations.

%package tests
Summary: Tests for %oname
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description tests
Tests for ISO country, subdivision, language, currency and script
definitions and their translations.

This package contains tests for %oname

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests


%changelog
* Wed Mar 29 2023 Anton Vyatkin <toni@altlinux.org> 22.3.5-alt1
- New version 22.3.5.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1
- Version 1.10

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Version 1.8

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev0
- Version 1.3.dev0

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.8-alt1.1
- Fixed build

* Fri Mar 15 2013 Aleksey Avdeev <solo@altlinux.ru> 0.14.8-alt1
- Version 0.14.8
- Add %%name-tests subpackage
- Added module for Python 3

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.5-alt1
- Initial build for Sisyphus
