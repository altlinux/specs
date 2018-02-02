%define oname oslo.reports

%def_with python3

Name: python-module-%oname
Version: 1.17.1
Release: alt1.1
Summary: Openstack common reports library

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch:      noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-jinja2 >= 2.8
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-psutil >= 1.2.1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.18.0

BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-jinja2 >= 2.8
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-psutil >= 1.2.1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.18.0

BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx

%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

OpenStack library for creating Guru Meditation Reports and other reports.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-oslo.reports
Summary: Openstack common reports library
Group: Development/Python3

%description -n python3-module-oslo.reports
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

OpenStack library for creating Guru Meditation Reports and other reports.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo common reports library
Group: Development/Documentation

%description doc
Documentation for the Oslo common reports library.


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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

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
%doc html
%doc README.rst LICENSE

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.17.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1.17.1-alt1
- 1.17.1

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.17.0-alt1
- 1.17.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- First build for ALT

