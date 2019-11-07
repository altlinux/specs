%define oname designateclient

Name:    python3-module-%oname
Version: 3.0.0
Release: alt1

Summary: Openstack DNS (Designate) API Client

License: Apache-2.0
Group:   Development/Python3
Url:     http://docs.openstack.org/developer/python-%oname

Source:  https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0

%description
This is a client for the OpenStack Designate API. There's a Python API
(the designateclient module), and a command-line tool (designate).

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

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

%install
%python3_install

# Build HTML docs and man page
python3 setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -fr  doc/build/html/.doctrees  doc/build/html/.buildinfo

%files
%doc README.rst
#%%_bindir/designate
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/functionaltests

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/functionaltests

%files doc
%doc doc/build/html

%changelog
* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.11.0-alt1
- Automatically updated to 2.11.0

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 2.10.0-alt1
- 2.10.0

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.6.0-alt2
- rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0
- enable build python3 module

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.2-alt2
- BuildReq: python-module-subunit -> python-module-python-subunit

* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.2-alt1
- First build for ALT (based on OpenSuSe 1.0.2-1.1.src)

