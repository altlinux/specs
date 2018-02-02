%define oname oslo.i18n

%def_with python3

Name: python-module-%oname
Version: 3.12.0
Release: alt1.1
Summary: OpenStack i18n library
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/oslo.i18n
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

Provides: python-module-oslo-i18n = %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-sphinx >= 1.2.1
BuildRequires: python-module-oslosphinx >= 4.7.0
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-fixtures
BuildRequires: python-module-oslo.config >= 3.14.0
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-fixtures
%endif

%description
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack i18n library
Group: Development/Documentation
Provides: python-module-oslo-i18n-doc = %EVR

%description doc
Documentation for the oslo.i18n library.

%package -n python3-module-%oname
Summary:    OpenStack common configuration library
Group: Development/Python3
Provides: python3-module-oslo-i18n = %EVR

%description -n python3-module-%oname
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

This package contains tests for %oname.


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


# generate html docs
python setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}


%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS ChangeLog CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
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
%doc doc/build/html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.12.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0
- add tests package

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.9.0-alt1
- 3.9.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.5.0-alt1
- 3.5.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial release
