%define oname plumbum

%def_with check
%def_with docs

Name: python3-module-%oname
Version: 1.8.1
Release: alt1

Summary: Plumbum: shell combinators library

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/plumbum

# https://github.com/tomerfiliba/plumbum.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with docs
BuildRequires: python3-module-sphinx
%endif

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-psutil
BuildRequires: /proc
%endif

BuildArch: noarch

%py3_provides %oname

# Experimental concurrent machine support in ``experimental/parallel.py``
# Used only in experiments/test_parallel.py
%add_python3_req_skip parallel

%description
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

Apart from shell-like syntax and handy shortcuts, the library provides
local and remote command execution (over SSH), local and remote
file-system paths, easy working-directory and environment manipulation,
and a programmatic Command-Line Interface (CLI) application toolkit. Now
let's see some code!

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

This package contains tests for %oname.

%if_with docs
%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

This package contains documentation for %oname.
%endif

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%if_with docs
export PYTHONPATH=$PWD
# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install
touch experiments/__init__.py
cp -fR experiments %buildroot%python3_sitelibdir/%oname/

%check
%tox_create_default_config
%tox_check_pyproject -- -k 'not test_home'

%files
%doc examples *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/*/test*

%if_with docs
%files docs
%doc html/*
%endif

%changelog
* Thu Jan 12 2023 Grigory Ustinov <grenka@altlinux.org> 1.8.1-alt1
- Automatically updated to 1.8.1.

* Thu Oct 06 2022 Grigory Ustinov <grenka@altlinux.org> 1.8.0-alt1
- Automatically updated to 1.8.0.

* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.7.2-alt1
- Automatically updated to 1.7.2.
- Build with check.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 1.6.9-alt1
- Automatically updated to 1.6.9.

* Thu Sep 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.6.3-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.3-alt1
- Updated to upstream version 1.6.3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.3-alt1.git20141103.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.3-alt1.git20141103.1
- NMU: Use buildreq for BR.

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.git20141103
- Initial build for Sisyphus

