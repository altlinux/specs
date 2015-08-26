%define sname openstackclient

Name: python-module-%sname
Version: 1.0.4
Release: alt1
Summary: OpenStack Command-line Client

Group: Development/Python
License: ASL 2.0
Url: http://github.com/openstack/python-openstackclient
Source: %name/%name-%version.tar

Patch1: 0001-Fix-image-create-location-attribute.patch

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-cliff >= 1.10.0
BuildRequires: python-module-oslo.config >= 1.9.3
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.utils >= 1.4.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-six
BuildRequires: python-module-requests >= 2.2.0
BuildRequires: python-module-stevedore >= 1.3.0
BuildRequires: python-module-glanceclient >= 0.15.0
BuildRequires: python-module-keystoneclient >= 1.1.0
BuildRequires: python-module-novaclient >= 2.22.0
BuildRequires: python-module-cinderclient >= 1.1.0
BuildRequires: python-module-neutronclient >= 2.3.11

Requires: python-module-cliff
Requires: python-module-oslo.config
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
%patch1 -p1

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
* Wed Aug 26 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial package

