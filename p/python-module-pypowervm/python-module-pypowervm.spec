%global oname pypowervm

Name: python-module-%oname
Version: 1.1.19
Release: alt1
Summary: Python API wrapper for PowerVM

Group: Development/Python
License: ASL 2.0
Url: http://github.com/powervm/pypowervm
Source: %oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-lxml >= 3.4.1
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-oslo.context >= 2.12.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.log >= 3.11.0
BuildRequires: python-module-oslo.utils >= 3.20.0
BuildRequires: python-module-pyasn1-modules
BuildRequires: python-module-pyasn1
BuildRequires: python-module-pytz >= 2013.6
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-taskflow >= 2.16.0

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
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python API wrapper for PowerVM
Group: Development/Python3

%description -n python3-module-%oname
pypowervm provides a Python-based API wrapper for interaction with IBM
PowerVM-based systems.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg info
rm -rf *.egg-info

cp -fR . ../python3

%build
%python_build


pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc AUTHORS ChangeLog README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc AUTHORS ChangeLog README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.19-alt1
- Initial build for Sisyphus
