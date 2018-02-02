%define oname oslo.db

%def_with python3

Name: python-module-%oname
Version: 4.17.1
Release: alt1.1
Summary: OpenStack oslo.db library
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Provides: python-module-oslo-db = %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-alembic >= 0.8.4
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.context >= 2.9.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-migrate >= 0.9.6 python-module-migrate-tests
BuildRequires: python-module-stevedore >= 1.17.1
BuildRequires: python-module-six >= 1.9.0

BuildRequires: python-module-fixtures >= 1.3.1
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-eventlet
BuildRequires: python-module-oslotest

BuildRequires: python-module-testresources python-module-testscenarios

Requires: python-module-SQLAlchemy
Requires: python-module-oslo.i18n
Requires: python-module-migrate
Requires: python-module-stevedore

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-alembic >= 0.8.4
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.context >= 2.9.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-migrate python3-module-migrate-tests
BuildRequires: python3-module-eventlet
BuildRequires: python3-module-oslotest
BuildRequires: python3-module-stevedore >= 1.17.1
BuildRequires: python3-module-six >= 1.9.0

BuildRequires: python3-module-testresources python3-module-testscenarios
%endif

%description
The OpenStack Oslo database handling library. Provides database connectivity
to the different backends and helper utils.

%package doc
Summary: Documentation for the Oslo database handling library
Group: Development/Documentation
Provides: python-module-oslo-db-doc = %EVR

%description doc
Documentation for the Oslo database handling library.

%package tests
Summary: Tests for the Oslo database handling library
Group: Development/Python
Requires: %name = %EVR

%description tests
Tests for the Oslo database handling library.

%if_with python3
%package -n python3-module-%oname
Summary:    OpenStack common configuration library
Group: Development/Python3
Provides: python3-module-oslo-db = %EVR

Requires: python3-module-oslo.i18n
Requires: python3-module-migrate
Requires: python3-module-stevedore
Requires: python3-module-SQLAlchemy
Requires: python3-module-iso8601

%description -n python3-module-%oname
The OpenStack Oslo database handling library. Provides database connectivity
to the different backends and helper utils.

%package -n python3-module-%oname-tests
Summary: Tests for the Oslo database handling library
Group: Development/Python
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Tests for the Oslo database handling library.

%endif

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
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*

%files doc
%doc doc/build/html

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.17.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 4.17.1-alt1
- 4.17.1

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 4.17.0-alt1
- 4.17.0

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.13.5-alt1
- 4.13.5

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 4.13.3-alt1
- 4.13.3

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 4.7.0-alt1
- 4.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial release
