%define oname oslo.concurrency

%def_with python3

Name: python-module-%oname
Version: 3.18.0
Release: alt1.1
Summary: OpenStack oslo.concurrency library
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Provides: python-module-oslo-concurrency = %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-enum34
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-fasteners >= 0.7
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-fasteners >= 0.7
%endif

%description
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack oslo.concurrency library
Group: Development/Python3
Provides: python3-module-oslo-concurrency = %EVR

%description -n python3-module-%oname
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo concurrency handling library
Group: Development/Documentation
Provides: python-module-oslo-concurrency-doc = %EVR

%description doc
Documentation for the Oslo concurrency handling library.

%prep
%setup -n %oname-%version

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
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/lockutils-wrapper %buildroot%_bindir/python3-lockutils-wrapper
popd
%endif

%python_install

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*
%_bindir/lockutils-wrapper
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%_bindir/python3-lockutils-wrapper
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.18.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 24 2017 Alexey Shabalin <shaba@altlinux.ru> 3.18.0-alt1
- 3.18.0
- add test packages

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- Initial release
