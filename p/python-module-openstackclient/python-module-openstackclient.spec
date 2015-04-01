%define sname openstackclient

Name: python-module-%sname
Version: 1.0.3
Release: alt1
Summary: OpenStack Command-line Client

Group: Development/Python
License: ASL 2.0
Url: http://github.com/openstack/python-openstackclient
Source: %name/%name-%version.tar

Patch0001: 0001-Remove-runtime-dependency-on-python-pbr.patch

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-cliff
BuildRequires: python-module-oslo.i18n
BuildRequires: python-module-oslo.utils
BuildRequires: python-module-oslo.serialization
BuildRequires: python-module-six
BuildRequires: python-module-requests
BuildRequires: python-module-stevedore

Requires: python-module-cliff
Requires: python-module-oslo.i18n
Requires: python-module-oslo.utils
Requires: python-module-oslo.serialization
Requires: python-module-glanceclient
Requires: python-module-keystoneclient
Requires: python-module-novaclient
Requires: python-module-cinderclient
Requires: python-module-neutronclient
Requires: python-module-six
Requires: python-module-requests
Requires: python-module-stevedore

%description
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

%package doc
Summary: Documentation for OpenStack Nova API Client
Group: Development/Documentation

%description doc
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

This package contains auto-generated documentation.

%prep
%setup
%patch0001 -p1

# We provide version like this in order to remove runtime dep on pbr
sed -i s/REDHATOPENSTACKCLIENTVERSION/%version/ openstackclient/__init__.py

# We handle requirements ourselves, pkg_resources only bring pain
rm -rf requirements.txt test-requirements.txt

# Remove bundled egg-info
rm -rf python_openstackclient.egg-info

%build
%python_build

%install
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man

install -p -D -m 644 man/openstack.1 %buildroot%_mandir/man1/openstack.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/openstack
%python_sitelibdir/*
%_man1dir/openstack.1*

%files doc
%doc html

%changelog
* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial package

