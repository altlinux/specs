%define oname yaql
%def_with docs
%def_with check

Name: python3-module-%oname
Version: 3.0.0
Release: alt1

Summary: YAQL - Yet Another Query Language

Group: Development/Python3
License: Apache-2.0
URL: https://pypi.org/project/yaql

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr
BuildRequires: python3-module-babel
BuildRequires: python3-module-ply
BuildRequires: python3-module-dateutil

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
%endif

%if_with check
BuildRequires: python3-module-stestr
%endif

BuildArch: noarch

%description
YAQL (Yet Another Query Language) is an embeddable and extensible query language,
that allows performing complex queries against arbitrary objects.
It has a vast and comprehensive standard library of frequently 
used querying functions and can be extend even further with user-specified functions.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: yaql documentation
Group: Development/Documentation

%description doc
Documentation for yaql
%endif

%prep
%setup -n %oname-%version
# Remove bundled egg-info
rm -rf %oname.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc README.rst
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files doc
%doc html
%_man1dir/%oname.1.xz
%endif

%changelog
* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Build new version.
- Build with docs.
- Build with check.

* Fri Jun 10 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Build new version.

* Thu May 21 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt3
- Fixed FTBFS.
- Fixed Url.

* Fri Jan 10 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt2
- Build without python2.
- Fix license.

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.3-alt1
- 1.1.3

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- Initial Package
