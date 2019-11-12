%define oname blessed

%def_disable check

Name: python3-module-%oname
Version: 1.14.2
Release: alt2

Summary: A feature-filled fork of Erik Rose's blessings project
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/blessed/
# https://github.com/jquast/blessed.git
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-tox python3-module-wcwidth
BuildRequires: python3-module-coverage python3-module-pytest-flakes
BuildRequires: python3-module-pytest-xdist python3-module-pytest-pep8
BuildRequires: python3-module-pytest-cov python3-module-mock
BuildRequires: python3-modules-curses

%py3_provides %oname
Requires: /dev/pts
%py3_requires wcwidth curses


%description
A feature-filled fork of Erik Rose's blessings project.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A feature-filled fork of Erik Rose's blessings project.

This package contains tests for %oname.

%prep
%setup -n %oname-%version

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
export LC_ALL=en_US.UTF-8
py.test-%_python3_version \
    --strict --flakes \
    --junit-xml=results.{envname}.xml --verbose \
    --cov blessed blessed/tests --cov-report=term-missing

%files
%doc *.rst docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.14.2-alt2
- disable python2

* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.14.2-alt1
- Version 1.14.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.5-alt1.git20150112.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.5-alt1.git20150112.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.5-alt1.git20150112
- Initial build for Sisyphus
