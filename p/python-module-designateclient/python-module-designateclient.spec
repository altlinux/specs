%define component designateclient
%def_with python3

Name: python-module-%component
Version: 2.3.0
Release: alt1
Summary: Openstack DNS (Designate) API Client
License: Apache-2.0
Group: Development/Python
Url: http://launchpad.net/python-designateclient
Source: %name-%version.tar

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-cliff >= 1.15.0
BuildRequires: python-module-jsonschema >= 2.0.0
BuildRequires: python-module-osc-lib >= 1.0.2
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-keystoneauth1 >= 2.10.0
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-stevedore >= 1.16.0
BuildRequires: python-module-debtcollector >= 1.2.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-cliff >= 1.15.0
BuildRequires: python3-module-jsonschema >= 2.0.0
BuildRequires: python3-module-osc-lib >= 1.0.2
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-keystoneauth1 >= 2.10.0
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-stevedore >= 1.16.0
BuildRequires: python3-module-debtcollector >= 1.2.0
%endif

%description
This is a client for the OpenStack Designate API. There's a Python API
(the designateclient module), and a command-line tool (designate).

%if_with python3
%package -n python3-module-%component
Summary:   Openstack DNS (Designate) API Client
Group: Development/Python3

%description -n python3-module-%component
This is a client for the OpenStack Designate API. There's a Python API
(the designateclient module), and a command-line tool (designate).
%endif

%package doc
Summary: Openstack DNS (Designate) API Client - Documentation
Group: Development/Documentation

%description doc
This package contains documentation files for %name.

%prep
%setup
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_designateclient.egg-info
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/designate %buildroot%_bindir/python3-designate
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python_sitelibdir/*/functionaltests
rm -fr %buildroot%python3_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/functionaltests

# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo


%files
%doc README.rst
%_bindir/designate
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%component
%_bindir/python3-designate
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
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

