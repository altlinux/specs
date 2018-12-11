%define oname stestr

Name: python-module-%oname
Version: 2.2.0
Release: alt1
Summary: stestr is parallel Python test runner
Group: Development/Python
License: ASL 2.0
Url: http://stestr.readthedocs.io/en/latest
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-future
BuildRequires: python-module-cliff >= 2.8.0
BuildRequires: python-module-subunit >= 1.3.0
BuildRequires: python-module-fixtures >= 3.0.0
BuildRequires: python-module-testtools >= 2.2.0
BuildRequires: python-module-yaml >= 3.10.0
BuildRequires: python-module-voluptuous >= 0.8.9

BuildRequires: python-module-sphinx >= 1.5.1
BuildRequires: python-module-subunit2sql >= 1.8.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-future
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-subunit >= 1.3.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-yaml >= 3.10.0
BuildRequires: python3-module-voluptuous >= 0.8.9

BuildRequires: python3-module-sphinx >= 1.5.1
BuildRequires: python3-module-subunit2sql >= 1.8.0

%description
stestr is parallel Python test runner designed to execute unittest test suites
using multiple processes to split up execution of a test suite.
It also will store a history of all test runs to help in debugging failures
and optimizing the scheduler to improve speed. To accomplish this goal
it uses the subunit protocol to facilitate streaming and storing results from multiple workers.

stestr originally started as a fork of the testrepository project.
But, instead of being an interface for any test runner that used subunit,
like testrepository, stestr concentrated on being a dedicated test runner for python projects.
While stestr was originally forked from testrepository it is not backwards compatible with testrepository.
At a high level the basic concepts of operation are shared between the two projects but the actual usage is not exactly the same.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: stestr is parallel Python test runner 
Group: Development/Python3

%description -n python3-module-%oname
stestr is parallel Python test runner designed to execute unittest test suites
using multiple processes to split up execution of a test suite.
It also will store a history of all test runs to help in debugging failures
and optimizing the scheduler to improve speed. To accomplish this goal
it uses the subunit protocol to facilitate streaming and storing results from multiple workers.

stestr originally started as a fork of the testrepository project.
But, instead of being an interface for any test runner that used subunit,
like testrepository, stestr concentrated on being a dedicated test runner for python projects.
While stestr was originally forked from testrepository it is not backwards compatible with testrepository.
At a high level the basic concepts of operation are shared between the two projects but the actual usage is not exactly the same.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for stestr
Group: Development/Documentation

%description doc
Documentation for stestr.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info


rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd


# disabling git call for last modification date from git repo
#sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python_install
mv %buildroot%_bindir/%oname %buildroot%_bindir/%oname.py2

pushd ../python3
%python3_install
popd


%files
%doc AUTHORS ChangeLog LICENSE PKG-INFO README.rst
%_bindir/%oname.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc doc/build/html

%changelog
* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 2.2.0-alt1
- Initial release
