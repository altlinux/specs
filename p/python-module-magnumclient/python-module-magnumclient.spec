%def_with python3

Name:       python-module-magnumclient
Version:    2.0.0
Release:    alt1
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
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-keystoneauth1 >= 2.1.0
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-requests >= 2.8.1
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-os-client-config >= 1.13.1
BuildRequires: python-module-prettytable >= 0.7

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-argparse
BuildRequires: python3-module-requests >= 2.8.1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-keystoneauth1 >= 2.1.0
BuildRequires: python3-module-os-client-config >= 1.13.1
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
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
* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt0.b1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt0.b1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt0.b1
- Initial release for Sisyphus

