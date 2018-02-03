%define oname ceilometerclient
%def_with python3

Name: python-module-%oname
Version: 2.8.1
Release: alt1.1
Summary: Python API and CLI for OpenStack Ceilometer
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-keystoneauth1 >= 2.1.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.17.0
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-requests >= 2.8.1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-stevedore >= 1.10.0
BuildRequires: python-module-keystoneauth1

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-keystoneauth1 >= 2.1.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.17.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-requests >= 2.5.2
BuildRequires: python3-module-stevedore >= 1.10.0
BuildRequires: python3-module-keystoneauth1
%endif

%description
This is a client library for Ceilometer built on the Ceilometer API. It
provides a Python API (the ceilometerclient module) and a command-line tool
(ceilometer).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:  Python API and CLI for OpenStack Ceilometer
Group: Development/Python3

%description -n python3-module-%oname
This is a client library for Ceilometer built on the Ceilometer API. It
provides a Python API (the ceilometerclient module) and a command-line tool
(ceilometer).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Ceilometer API Client
Group: Development/Documentation

%description doc
This is a client library for Ceilometer built on the Ceilometer API. It
provides a Python API (the ceilometerclient module) and a command-line tool
(ceilometer).

This package contains auto-generated documentation.

%prep
%setup -n python-%oname-%version

# Remove bundled egg-info
rm -rf python_ceilometerclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

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

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/ceilometer %buildroot%_bindir/python3-ceilometer
%endif

%python_install

python setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%_bindir/ceilometer
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%_bindir/python3-ceilometer
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc doc/build/html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 2.8.1-alt1
- 2.8.1
- add test packages

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Wed Oct 14 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.13-alt1
- 1.0.13
- add puthon3 package

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.10-alt1
- First build for ALT (based on Fedora 1.0.10-2.fc21.src)

