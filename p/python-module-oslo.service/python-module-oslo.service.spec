%global oname oslo.service

%def_with python3

Name: python-module-%oname
Version: 1.19.1
Release: alt1.1
Summary: Oslo service library
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-webob >= 1.6.0
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-greenlet >= 0.3.2
BuildRequires: python-module-monotonic >= 0.6
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-oslo.config >= 3.18.0
BuildRequires: python-module-oslo.log >= 3.11.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-routes >= 1.12.3
BuildRequires: python-module-paste


BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-oslo-i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-oslo.concurrency >= 3.8.0
BuildRequires: python3-module-oslo.config >= 3.18.0
BuildRequires: python3-module-oslo.log >= 3.11.0
BuildRequires: python3-module-paste
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-greenlet >= 0.3.2
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-six >= 1.9.0
%endif

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
%doc README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc html

%changelog
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
