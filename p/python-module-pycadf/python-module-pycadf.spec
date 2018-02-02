%global oname pycadf

%def_with python3

Name: python-module-%oname
Version: 2.5.0
Release: alt1.1
Summary: DMTF Cloud Audit (CADF) data model

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-sphinx >= 1.1.2
BuildRequires: python-module-oslosphinx >= 2.5.0
BuildRequires: python-module-oslotest
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-pytz
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-debtcollector >= 1.2.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-pytz
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-debtcollector >= 1.2.0
%endif

%description
DMTF Cloud Audit (CADF) data model

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: DMTF Cloud Audit (CADF) data model
Group: Development/Python3

%description -n python3-module-%oname
DMTF Cloud Audit (CADF) data model

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for DMTF Cloud Audit (CADF) data model
Group: Development/Documentation

%description doc
Documentation for the DMTF Cloud Audit (CADF) data model.

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
export PYTHONPATH="$( pwd ):$PYTHONPATH"
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
mkdir -p %buildroot%_sysconfdir
mv %buildroot/usr/etc/%oname %buildroot%_sysconfdir

%files
%doc README.rst LICENSE
%dir %_sysconfdir/%oname
%config(noreplace) %_sysconfdir/%oname/*.conf
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0
- add test packages

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 1.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem at altlinux.org> 1.1.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- add python3 module

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- First build for ALT (based on Fedora 0.5.1-1.fc21.src)

