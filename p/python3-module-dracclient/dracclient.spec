%define oname dracclient

Name: python3-module-%oname
Version: 3.1.1
Release: alt1
Summary: Library for managing machines with Dell iDRAC cards
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname
Source:%name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-lxml >= 2.3

%description
%summary.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
%summary

This package contains auto-generated documentation.

%prep
%setup

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%python3_build

%install
%python3_install

#python3 setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

#%%files doc
#%%doc doc/build/html

%changelog
* Thu Oct 31 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus.
