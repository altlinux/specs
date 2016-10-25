%define sname oslo.vmware
%def_with python3

Name: python-module-%sname
Version: 2.14.0
Release: alt1
Summary: Oslo VMware library for OpenStack projects
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar

Provides: python-module-oslo-vmware = %EVR

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-stevedore >= 1.16.0
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-pyaml >= 3.1.0
BuildRequires: python-module-lxml >= 2.3
BuildRequires: python-module-suds-jurko >= 0.6
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-urllib3 >= 1.15.1
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-stevedore >= 1.16.0
BuildRequires: python3-module-netaddr >= 0.7.12
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-oslo.concurrency >= 3.8.0
BuildRequires: python3-module-suds-jurko >= 0.6
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-requests >= 2.8.1
BuildRequires: python3-module-urllib3 >= 1.15.1
BuildRequires: python3-module-lxml >= 2.3

%endif

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%if_with python3
%package -n python3-module-%sname
Summary: Oslo VMware library for OpenStack projects
Group: Development/Python3
Provides: python3-module-oslo-vmware = %EVR

%description -n python3-module-%sname
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.
%endif

%package doc
Summary: Documentation for OpenStack common VMware library
Group: Development/Documentation

%description doc
Documentation for OpenStack common VMware library.

%prep
%setup

# Remove bundled egg-info
#rm -rf %sname.egg-info
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
# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.14.0-alt1
- 2.14.0

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.21.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.21.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.21.0-alt1
- 1.21.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- initial build
