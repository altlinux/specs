%global oname oslo.service

Name: python-module-%oname
Version: 1.31.7
Release: alt1
Summary: Oslo service library
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-webob >= 1.7.1
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-greenlet >= 0.4.10
BuildRequires: python-module-monotonic >= 0.6
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-oslo.concurrency >= 3.25.0
BuildRequires: python-module-oslo.config >= 5.1.0
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-routes >= 2.3.1
BuildRequires: python-module-paste >= 2.0.2


BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-greenlet >= 0.4.10
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.concurrency >= 3.25.0
BuildRequires: python3-module-oslo.config >= 5.1.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-routes >= 2.3.1
BuildRequires: python3-module-paste >= 2.0.2

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0

%description
Library for running OpenStack services

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Oslo service library
Group: Development/Python3

%description -n python3-module-%oname
Library for running OpenStack services

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Oslo service documentation
Group: Development/Documentation
%description doc
Documentation for oslo.service


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
%doc README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc html

%changelog
* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.31.7-alt1
- 1.31.7

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.19.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.19.1-alt1
- 1.19.1

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 1.19.0-alt1
- 1.19.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- Initial package.
