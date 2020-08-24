%global oname pypowervm

Name: python3-module-%oname
Version: 1.1.24
Release: alt1

Summary: Python API wrapper for PowerVM

Group: Development/Python3
License: Apache-2.0
Url: http://github.com/powervm/pypowervm

Source: %oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-lxml >= 3.4.1
BuildRequires: python3-module-oslo.concurrency >= 3.8.0
BuildRequires: python3-module-oslo.context >= 2.12.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.log >= 3.11.0
BuildRequires: python3-module-oslo.utils >= 3.20.0
BuildRequires: python3-module-pyasn1-modules
BuildRequires: python3-module-pyasn1
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-taskflow >= 2.16.0

%description
pypowervm provides a Python-based API wrapper for interaction with IBM
PowerVM-based systems.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg info
rm -rf *.egg-info

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS ChangeLog README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Aug 24 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.24-alt1
- Updated to 1.1.24.
- Fixed license.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.23-alt1
- Automatically updated to 1.1.23.

* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.19-alt2
- Build without python2.

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.19-alt1
- Initial build for Sisyphus
