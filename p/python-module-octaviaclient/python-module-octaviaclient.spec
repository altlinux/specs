%def_disable doc

%define oname octaviaclient

Name:       python-module-%oname
Version:    1.6.0
Release:    alt1
Summary:    Octavia client for OpenStack Load Balancing
Group:      Development/Python
License:    ASL 2.0
Url:        http://docs.openstack.org/developer/%oname
Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-appdirs >= 1.3.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-cliff >= 2.8.0
BuildRequires: python-module-cmd2
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-funcsigs >= 1.0.0
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-monotonic >= 0.6
BuildRequires: python-module-netaddr >= 0.7.18
BuildRequires: python-module-netifaces >= 0.10.4
BuildRequires: python-module-neutronclient >= 6.7.0
BuildRequires: python-module-openstackclient >= 3.12.0
BuildRequires: python-module-os-client-config >= 1.28.0
BuildRequires: python-module-osc-lib >= 1.8.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.serialization
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-pyparsing >= 2.1.0
BuildRequires: python-module-pytz >= 2013.6
BuildRequires: python-module-yaml >= 3.12
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-simplejson >= 3.5.1
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-unicodecsv >= 0.8.0
BuildRequires: python-module-wrapt >= 1.7.0

# doc
BuildRequires: python-module-sphinx >= 1.6.2
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-appdirs >= 1.3.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-cmd2
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-netifaces >= 0.10.4
BuildRequires: python3-module-neutronclient >= 6.7.0
BuildRequires: python3-module-openstackclient >= 3.12.0
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-pyparsing >= 2.1.0
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-wrapt >= 1.7.0

# doc
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0


%description
Octavia client for OpenStack Load Balancing

This is an OpenStack Client (OSC) plugin for Octavia, an OpenStack
Load Balancing project.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Octavia client for OpenStack Load Balancing
Group: Development/Python3

%description -n python3-module-%oname
Octavia client for OpenStack Load Balancing

This is an OpenStack Client (OSC) plugin for Octavia, an OpenStack
Load Balancing project.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Octavia client
Group:  Development/Documentation

%description doc
Octavia client for OpenStack Load Balancing

This is an OpenStack Client (OSC) plugin for Octavia, an OpenStack
Load Balancing project.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

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

pushd ../python3
%python3_install
popd


%if_enabled doc
# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
python3 setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo
%endif

%files
%doc LICENSE README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%if_enabled doc
%files doc
%doc LICENSE html
%endif

%changelog
* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- Initial build.
