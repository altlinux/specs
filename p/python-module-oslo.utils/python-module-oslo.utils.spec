%define oname oslo.utils

%def_with python3

Name: python-module-%oname
Version: 3.22.1
Release: alt1.1
Summary: OpenStack Oslo Utility library
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/oslo.utils
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

Provides: python-module-oslo-utils = %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-funcsigs >= 0.4
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-monotonic >= 0.6
BuildRequires: python-module-pytz >= 2013.6
BuildRequires: python-module-netaddr >= 0.7.13
BuildRequires: python-module-netifaces >= 0.10.4
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-pyparsing >= 2.0.7
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx >= 4.7.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-reno >= 1.8.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-netaddr >= 0.7.13
BuildRequires: python3-module-netifaces >= 0.10.4
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-debtcollector
BuildRequires: python3-module-pyparsing >= 2.0.7
%endif

%description
The OpenStack Oslo Utility library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack Oslo Utility library
Group: Development/Python3
Provides: python3-module-oslo-utils = %EVR

%description -n python3-module-%oname
The OpenStack Oslo Utility library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo Utility library
Group: Development/Documentation
Provides: python-module-oslo-utils-doc = %EVR

%description doc
Documentation for the Oslo Utility library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info
# Let RPM handle the dependencies
rm -f requirements.txt
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
%doc README.rst LICENSE
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
%doc doc/build/html LICENSE

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.22.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.1-alt1
- 3.22.1

* Tue May 02 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.0-alt1
- 3.22.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- 3.16.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.5.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial package.
