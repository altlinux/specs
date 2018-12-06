%define oname castellan

Name: python-module-%oname
Version: 0.19.0
Release: alt1
Summary: Generic Key Manager interface for OpenStack
License: ASLv2.0
Group: Development/Python
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-sphinx python-module-sphinx-pickles
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-cryptography >= 2.1
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.context >= 2.19.2
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-cryptography >= 2.1
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0

%description
Generic Key Manager interface for OpenStack

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Generic Key Manager interface for OpenStack
Group: Development/Python3

%description -n python3-module-%oname
Generic Key Manager interface for OpenStack

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Generic Key Manager interface for OpenStack
Group: Development/Documentation

%description doc
Documentation for Generic Key Manager interface for OpenStack

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

#python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

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

#%files doc
#%doc  doc/build/html

%changelog
* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 0.19.0-alt1
- 0.19.0

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- 0.5.0
- add tests packages

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1
- Initial build for Sisyphus

