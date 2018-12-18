%define oname oslo.cache

Name: python-module-%oname
Version: 1.30.2
Release: alt1
Summary: Cache storage for Openstack projects

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch


%py_requires dogpile.cache

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-dogpile.cache >= 0.6.2
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-memcached >= 1.56
BuildRequires: python-module-pymongo >= 3.0.2
BuildRequires: python-module-etcd3gw >= 0.2.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-openstackdocstheme
BuildRequires: python-module-sphinxcontrib-apidoc

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-dogpile.cache >= 0.6.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-memcached >= 1.56
BuildRequires: python3-module-pymongo >= 3.0.2
BuildRequires: python3-module-etcd3gw >= 0.2.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 1.8.0
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc

%description
Cache storage for Openstack projects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Cache storage for Openstack projects.
Group: Development/Python3

%py3_requires dogpile.cache

%description -n python3-module-%oname
Cache storage for Openstack projects.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Cache storage for Openstack projects
Group: Development/Documentation

%description doc
Documentation for Cache storage for Openstack projects.


%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd


# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install

pushd ../python3
%python3_install
popd



%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc html
%doc README.rst LICENSE

%changelog
* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.30.2-alt1
- 1.30.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.17.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.17.0-alt1
- 1.17.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- First build for ALT
