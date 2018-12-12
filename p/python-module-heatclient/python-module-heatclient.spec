
%define oname heatclient

Name: python-module-%oname
Version: 1.16.1
Release: alt1
Summary: Python API and CLI for OpenStack Heat

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-cliff >= 2.8.0
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-osc-lib >= 1.8.0
BuildRequires: python-module-prettytable >= 0.7.2
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-swiftclient >= 3.2.0
BuildRequires: python-module-yaml >= 3.12
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-six >= 1.10.0


BuildRequires: python-module-sphinx
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-sphinxcontrib-httpdomain >= 1.3.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-swiftclient >= 3.2.0
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0


BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
#BuildRequires: python3-module-sphinxcontrib-httpdomain >= 1.3.0

%description
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    Python API and CLI for OpenStack Heat
Group: Development/Python3

%description -n python3-module-%oname
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Heat API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

This package contains auto-generated documentation.

%prep
%setup -n python-%oname-%version

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config.
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

rm -rf ../python3
cp -a . ../python3

sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/heat %buildroot%_bindir/heat.py2

pushd ../python3
%python3_install
popd

echo "%version" > %buildroot%python_sitelibdir/heatclient/versioninfo
echo "%version" > %buildroot%python3_sitelibdir/heatclient/versioninfo

python setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -fr build/sphinx/html/.doctrees build/sphinx/html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/heat.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/heat
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc build/sphinx/html

%changelog
* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt1
- 1.16.1

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.14.0-alt1
- new version 1.14.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0
- add python package

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.9-alt1
- First build for ALT (based on Fedora 0.2.9-1.fc21.src)

