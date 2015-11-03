%def_with python3

Name:       python-module-magnumclient
Version:    1.0.0
Release:    alt0.b1
Summary:    Client Library for OpenStack Magnum Container Management API
License:    ASL 2.0
URL:        http://pypi.python.org/pypi/python-magnumclient
Source:    %name-%version.tar
Group:      Development/Python

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-d2to1
BuildRequires: python-module-argparse
BuildRequires: python-module-requests >= 2.5.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-oslo.config >= 2.3.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-yaml >= 3.1.0
BuildRequires: python-module-stevedore >= 1.5.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-argparse
BuildRequires: python3-module-requests >= 2.5.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-oslo.config >= 2.3.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-requests >= 2.5.2
BuildRequires: python3-module-yaml >= 3.1.0
BuildRequires: python3-module-stevedore >= 1.5.0
%endif

%description
There is a Python library for accessing the API (magnumclient module),
and a command-line script (magnum).

%if_with python3
%package -n python3-module-magnumclient
Summary:    Client Library for OpenStack Magnum Container Management API
Group: Development/Python3

%description -n python3-module-magnumclient
Client library and command line utility for interacting with Openstack
Magnum API.
%endif

%package doc

Summary:    Documentation for OpenStack Magnum Container Management API
Group:  Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Magnum Container Management API.

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_magnumclient.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

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
mv %buildroot%_bindir/magnum %buildroot%_bindir/python3-magnum
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/magnum
%python_sitelibdir/*

%if_with python3
%files -n python3-module-magnumclient
%_bindir/python3-magnum
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE html

%changelog
* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt0.b1
- Initial release for Sisyphus

