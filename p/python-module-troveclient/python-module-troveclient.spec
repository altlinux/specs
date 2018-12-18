%define oname troveclient

Name:    python-module-%oname
Version: 2.16.0
Release: alt1
Summary: Client library for OpenStack DBaaS API
Group:   Development/Python
License: ASL 2.0
Url:     http://docs.openstack.org/developer/python-%oname
Source:  https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-prettytable >= 0.7.2
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-simplejson >= 3.5.1
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-swiftclient >= 3.2.0
BuildRequires: python-module-mistralclient >= 3.1.0
BuildRequires: python-module-osc-lib >= 1.8.0
BuildRequires: python-module-openstackclient >= 3.12.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-sphinxcontrib-apidoc
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-httplib2 >= 0.9.1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-swiftclient >= 3.2.0
BuildRequires: python3-module-mistralclient >= 3.1.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-openstackclient >= 3.12.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinxcontrib-apidoc
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-httplib2 >= 0.9.1

%description
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100 percent (or less ;) ) of the Trove API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:   Client library for OpenStack DBaaS API
Group: Development/Python3

%description -n python3-module-%oname
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100 percent (or less ;) ) of the Trove API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack DBaaS API
Group: Development/Documentation

%description doc
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100 percent (or less ;) ) of the Trove API.

This package contains auto-generated documentation.

%prep
%setup -n python-%oname-%version

# Remove bundled egg-info
rm -rf %name.egg-info

# Let RPM handle the requirements
rm -f {test-,}requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/trove %buildroot%_bindir/trove.py2

pushd ../python3
%python3_install
popd

sphinx-build -b html doc/source html

# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%files
%doc README.rst LICENSE
%python_sitelibdir/*
%_bindir/trove.py2
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/compat/tests

%files tests
%python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/compat/tests

%files -n python3-module-%oname
%_bindir/trove
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/compat/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/compat/tests

%files doc
%doc html

%changelog
* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 2.16.0-alt1
- 2.16.0

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 2.14.0-alt1
- new version 2.14.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.8.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 01 2017 Alexey Shabalin <shaba@altlinux.ru> 2.8.0-alt1
- 2.8.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.8-alt1
- 1.0.8
- add python3 package

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.5-alt1
- First build for ALT (based on Fedora 1.0.5-1.fc21.src)

