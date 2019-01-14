%def_enable doc

%define oname zunclient

Name:       python-module-%oname
Version:    2.1.0
Release:    alt1
Summary:    Client Library for Zun
Group:      Development/Python
License:    ASL 2.0
Url:        http://docs.openstack.org/developer/%oname
Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-openstackclient >= 3.12.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-osc-lib >= 1.8.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-websocket-client >= 0.44.0
BuildRequires: python-module-docker >= 2.4.2
BuildRequires: python-module-yaml >= 3.12

# doc
BuildRequires: python-module-sphinx >= 1.6.2
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-openstackclient >= 3.12.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-websocket-client >= 0.44.0
BuildRequires: python3-module-docker >= 2.4.2
BuildRequires: python3-module-yaml >= 3.12

# doc
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0


%description
This is a client library for Zun built on the Zun API.
It provides a Python API (the zunclient module)
and a command-line tool (zun).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    Client Library for Zun
Group: Development/Python3

%description -n python3-module-%oname
This is a client library for Zun built on the Zun API.
It provides a Python API (the zunclient module)
and a command-line tool (zun).

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
This is a client library for Zun built on the Zun API.
It provides a Python API (the zunclient module)
and a command-line tool (zun).

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
mv %buildroot%_bindir/zun %buildroot%_bindir/zun.py2

pushd ../python3
%python3_install
popd


%if_enabled doc
# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
python3 setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -rf doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

%files
%doc LICENSE README.rst
%_bindir/zun.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/zun
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%if_enabled doc
%files doc
%doc LICENSE doc/build/html
%endif

%changelog
* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- Initial build.
