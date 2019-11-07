%global oname pycadf

Name: python3-module-%oname
Version: 2.10.0
Release: alt1
Summary: DMTF Cloud Audit (CADF) data model

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-debtcollector >= 1.2.0

BuildRequires: python3-module-sphinx >= 1.1.2
BuildRequires: python3-module-reno >= 1.8.0
BuildRequires: python3-module-openstackdocstheme

%description
DMTF Cloud Audit (CADF) data model

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
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

%build
%python3_build

# generate html docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

mkdir -p %buildroot%_sysconfdir
mv %buildroot/usr/etc/%oname %buildroot%_sysconfdir

%files
%doc README.rst LICENSE
%dir %_sysconfdir/%oname
%config(noreplace) %_sysconfdir/%oname/*.conf
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc html

%changelog
* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.10.0-alt1
- Automatically updated to 2.10.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Automatically updated to 2.9.0

* Tue Dec 18 2018 Alexey Shabalin <shaba@altlinux.org> 2.8.0-alt1
- 2.8.0

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

