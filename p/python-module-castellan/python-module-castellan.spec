%define oname castellan
%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1
Summary: Generic Key Manager interface for OpenStack
License: ASLv2.0
Group: Development/Python
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-cryptography >= 1.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.context >= 2.9.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.log >= 3.11.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-keystoneauth1 >= 2.16.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-cryptography >= 1.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.context >= 2.9.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.log >= 3.11.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-keystoneauth1 >= 2.16.0
%endif

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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc  doc/build/html

%changelog
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

