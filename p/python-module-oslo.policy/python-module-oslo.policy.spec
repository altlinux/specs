%define oname oslo.policy

Name: python-module-%oname
Version: 1.38.1
Release: alt1
Summary: RBAC policy enforcement library for OpenStack
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.context >= 2.21.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-yaml >= 3.12
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-stevedore >= 1.20.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-openstackdocstheme

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.21.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.20.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme

%description
RBAC policy enforcement library for OpenStack

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: RBAC policy enforcement library for OpenStack
Group: Development/Python3

%description -n python3-module-%oname
RBAC policy enforcement library for OpenStack

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo policy handling library
Group: Development/Documentation

%description doc
Documentation for the Oslo policy handling library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
#rm -rf %oname.egg-info

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
for bin_files in oslopolicy-list-redundant oslopolicy-policy-generator oslopolicy-sample-generator oslopolicy-checker; do
    mv %buildroot%_bindir/$bin_files %buildroot%_bindir/$bin_files.py2
done

pushd ../python3
%python3_install
popd

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*
%_bindir/*.py2
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%python3_sitelibdir/*
%_bindir/*
%exclude %_bindir/*.py2
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc html

%changelog
* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.38.1-alt1
- 1.38.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.18.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.18.0-alt1
- 1.18.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- Initial release
