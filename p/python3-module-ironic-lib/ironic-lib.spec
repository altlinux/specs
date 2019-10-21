%define oname ironic-lib

Name: python3-module-%oname
Version: 2.21.0
Release: alt1
Summary:  A python library of common ironic utilities
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-zeroconf >= 0.19.1

%description
A common library to be used exclusively by projects under the Ironic governance.

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
Documentation for %oname

%prep
%setup

%build
%python3_build

# generate html docs
#python3 setup.py build_sphinx
# remove the sphinx-build leftovers
#rm -rf build/sphinx/html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc AUTHORS ChangeLog README.rst
%python3_sitelibdir/ironic_lib
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

#%%files doc
#%%doc build/sphinx/html

%changelog
* Thu Oct 31 2019 Grigory Ustinov <grenka@altlinux.org> 2.21.0-alt1
- Initial build for Sisyphus.
