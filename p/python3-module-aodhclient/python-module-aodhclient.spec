%define oname aodhclient

Name:       python3-module-%oname
Version:    1.3.0
Release:    alt1

Summary:    Python API and CLI for OpenStack Aodh

Group:      Development/Python3
License:    ASL 2.0
Url:        http://docs.openstack.org/developer/%oname

Source:     https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.4
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-cliff >= 1.14.0
BuildRequires: python3-module-osc-lib >= 1.0.1
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-keystoneauth1 >= 1.0.0
BuildRequires: python3-module-debtcollector
BuildRequires: python3-module-pyparsing

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.11.0
BuildRequires: python3-module-osprofiler
BuildRequires: python3-module-reno >= 1.6.2

%description
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Aodh API Client
Group:  Development/Documentation

%description doc
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool
(aodh).

%prep
%setup -n %oname-%version

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%build
%python3_build

%install
%python3_install

# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-3 -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%_bindir/aodh
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.1.1-alt1
- 1.1.1

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- add test packages

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- Initial release for Sisyphus
