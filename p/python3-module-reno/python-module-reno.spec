%define pypi_name reno

%def_without docs

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1

Summary: Release Notes manager

License: Apache-2.0
Group: Development/Python3
Url: http://www.openstack.org/

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

Requires: git-core
BuildRequires: git-core

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.4
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-yaml >= 3.10.0
BuildRequires: python3-module-oslotest
BuildRequires: python3-module-nose
BuildRequires: python3-module-openstackdocstheme

%description
Reno is a release notes manager for storing
release notes in a git repository and then building documentation from them.

Managing release notes for a complex project over a long period
of time with many releases can be time consuming and error prone. Reno
helps automate the hard parts.

%package docs
Summary: reno documentation
Group: Development/Documentation

%description docs
Documentation for reno

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %pypi_name.

%prep
%setup

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python3_build

%if_with docs
# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%python3_install

%files
%doc README.rst
%_bindir/%pypi_name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files docs
%doc doc/build/html
%endif

%changelog
* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Build new version.

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- NMU: new version 3.2.0 (with rpmrb script)

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 2.11.3-alt1
- Automatically updated to 2.11.3.
- Build without python2.

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 2.11.2-alt1
- 2.11.2

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.2-alt1
- 1.6.2
- add git to requires

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial Package
