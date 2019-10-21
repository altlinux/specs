%define oname ironicclient

Name:       python3-module-%oname
Version:    3.1.0
Release:    alt1

Summary:    Client for OpenStack bare metal Service

Group:      Development/Python3
License:    ASL 2.0
Url:     http://docs.openstack.org/developer/python-%oname

Source:  https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-appdirs >= 1.3.0
BuildRequires: python3-module-dogpile.cache >= 0.6.2
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-osc-lib >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0

# doc
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0

%description
Ironic provision bare metal machines instead of virtual machines. It is a fork
of the Nova Baremetal driver. It is best thought of as a bare metal hypervisor
API and a set of plugins which interact with the bare metal hypervisors. By
default, it will use PXE and IPMI in concert to provision and turn on/off
machines, but Ironic also supports vendor-specific plugins which may
implement
additional functionality.

This is a client for the OpenStack Ironic API. There's a Python API
(the "ironicclient" module), and a command-line script ("ironic").

Installing this package gets you a shell command, that you can use to
interact with Ironic's API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Openstack DNS (Designate) API Client - Documentation
Group: Development/Documentation

%description doc
This package contains documentation files for %name.

%prep
%setup -n python-%oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_designateclient.egg-info

%build
%python3_build

%install
%python3_install

# Build HTML docs and man page
python3 setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -fr  doc/build/html/.doctrees  doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
#%%_bindir/ironic
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%exclude %python3_sitelibdir/*/tests

%files doc
%doc build/sphinx/html

%changelog
* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.
- Build without python2.

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 2.5.0-alt1
- Updated to 2.5.0.
- Added python3 support.

* Fri Oct 02 2015 Lenar Shakirov <snejok@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 0.3.1-alt1
- First build for ALT (based on Fedora 0.3.1-3.fc23.src)
