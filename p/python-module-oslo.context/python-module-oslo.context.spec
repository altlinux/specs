%define oname oslo.context

%def_with python3

Name: python-module-%oname
Version: 2.12.2
Release: alt1.1
Summary: OpenStack oslo.context library
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Provides: python-module-oslo-context = %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-sphinx >= 1.1.2
BuildRequires: python-module-oslosphinx >= 2.5.0
BuildRequires: python-module-fixtures
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-positional >= 1.1.1
BuildRequires: python-module-reno >= 1.8.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-positional >= 1.1.1
%endif

%description
The Oslo context library has helpers to maintain useful information
about a request context. The request context is usually populated in
the WSGI pipeline and used by various modules such as logging.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack oslo.context library
Group: Development/Python3
Provides: python3-module-oslo-context = %EVR

%description -n python3-module-%oname
The Oslo context library has helpers to maintain useful information
about a request context. The request context is usually populated in
the WSGI pipeline and used by various modules such as logging.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo context handling library
Group: Development/Documentation
Provides: python-module-oslo-context-doc = %EVR

%description doc
Documentation for the Oslo context handling library.

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
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
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
%doc html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.12.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Wed May 24 2017 Alexey Shabalin <shaba@altlinux.ru> 2.12.1-alt1
- 2.12.1
- add test packages

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.9.0-alt1
- 2.9.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial release
