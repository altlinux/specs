%define oname designateclient

Name:    python-module-%oname
Version: 2.10.0
Release: alt1
Summary: Openstack DNS (Designate) API Client
License: Apache-2.0
Group:   Development/Python
Url:     http://docs.openstack.org/developer/python-%oname
Source:  https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-cliff >= 2.8.0
BuildRequires: python-module-jsonschema >= 2.0.0
BuildRequires: python-module-osc-lib >= 1.8.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-requests >= 2.14.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-debtcollector >= 1.2.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-oslotest >= 3.2.0
BuildRequires: python-module-requests-mock >= 1.1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-jsonschema >= 2.0.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-requests >= 2.10.0
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
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:   Openstack DNS (Designate) API Client
Group: Development/Python3

%description -n python3-module-%oname
This is a client for the OpenStack Designate API. There's a Python API
(the designateclient module), and a command-line tool (designate).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
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

rm -rf ../python3
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/designate %buildroot%_bindir/designate.py2

pushd ../python3
%python3_install
popd

# Build HTML docs and man page
python3 setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -fr  doc/build/html/.doctrees  doc/build/html/.buildinfo

%files
%doc README.rst
%_bindir/designate.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/functionaltests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/functionaltests

%files -n python3-module-%oname
%_bindir/designate
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/functionaltests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/functionaltests

%files doc
%doc doc/build/html

%changelog
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

