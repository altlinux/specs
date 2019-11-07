%define oname gnocchiclient

Name: python3-module-%oname
Version: 7.0.5
Release: alt1

Summary: Python client library for Gnocchi

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname

Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.4

BuildRequires: python3-module-cliff >= 2.10
BuildRequires: python3-module-ujson
BuildRequires: python3-module-keystoneauth1 >= 2.0.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-futurist
BuildRequires: python3-module-iso8601
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-debtcollector
BuildRequires: python3-module-monotonic
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-sphinxcontrib-apidoc

%description
Gnocchi is a multi-tenant timeseries, metrics and resources database.
This is a client for OpenStack gnocchi API

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Gnocchi API Client
Group: Development/Documentation

%description doc
Gnocchi is a multi-tenant timeseries, metrics and resources database.
This package contains auto-generated documentation.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf gnocchiclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%python3_build

%install
%python3_install

export PATH=$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=.
export LANG=en_US.utf8
python3 setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -rf doc/build/html/.doctrees doc/build/html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%_bindir/gnocchi
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc doc/build/html

%changelog
* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 7.0.5-alt1
- Build new version without python2.
- Enable docs.

* Thu Aug 10 2017 Alexey Shabalin <shaba@altlinux.ru> 3.3.1-alt1
- 3.3.1
- add tests packages
- disable build doc package

* Tue Nov 15 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- initial build


