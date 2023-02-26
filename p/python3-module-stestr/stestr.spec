%define oname stestr

%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.0.1
Release: alt1.1

Summary: stestr is parallel Python test runner

Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/stestr

# https://github.com/mtreinish/stestr
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-cliff
BuildRequires: python3-module-testtools
BuildRequires: python3-module-subunit
BuildRequires: python3-module-voluptuous
%endif

%if_with check
BuildRequires: python3-module-future
BuildRequires: python3-module-ddt
BuildRequires: python3-module-yaml
%endif

%description
stestr is parallel Python test runner designed to execute unittest test suites
using multiple processes to split up execution of a test suite.
It also will store a history of all test runs to help in debugging failures
and optimizing the scheduler to improve speed. To accomplish this goal
it uses the subunit protocol to facilitate streaming and storing results
from multiple workers.

stestr originally started as a fork of the testrepository project.
But, instead of being an interface for any test runner that used subunit,
like testrepository, stestr concentrated on being a dedicated test runner
for python projects.
While stestr was originally forked from testrepository it is not
backwards compatible with testrepository.
At a high level the basic concepts of operation are shared between the two
projects but the actual usage is not exactly the same.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for stestr
Group: Development/Documentation

%description doc
Documentation for stestr.

%prep
%setup

# Remove bundled egg-info
rm -rf %oname.egg-info

%build
export PBR_VERSION=%version
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%buildroot%_bindir/%oname init
# local tox.ini is too creepy
%tox_create_default_config
%tox_check_pyproject -- -k 'not test_history_list and not test_history_remove'

%files
%doc LICENSE *.rst
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Sun Feb 26 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1.1
- Fixed FTBFS.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Build new version.
- Build with check.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 2.5.1-alt1
- Automatically updated to 2.5.1.

* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt2
- Build without python2.

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 2.2.0-alt1
- Initial release.
