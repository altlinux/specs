%define oname oslo.rootwrap

%def_with python3

Name: python-module-%oname
Version: 5.4.1
Release: alt1.1
Summary: Oslo Rootwrap

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch:      noarch

Provides: python-module-oslo-rootwrap = %EVR
Obsoletes: python-module-oslo-rootwrap < %EVR

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
%endif

%description
The Oslo Rootwrap allows fine filtering of shell commands to run as `root`
from OpenStack services.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack oslo.rootwrap library
Group: Development/Python3
Provides: python3-module-oslo-rootwrap = %EVR

%description -n python3-module-%oname
The Oslo Rootwrap allows fine filtering of shell commands to run as `root`
from OpenStack services.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo rootwrap handling library
Group: Development/Documentation
Provides: python-module-oslo-rootwrap-doc = %EVR

%description doc
Documentation for the Oslo rootwrap handling library.


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
mv %buildroot%_bindir/oslo-rootwrap \
   %buildroot%_bindir/python3-oslo-rootwrap
mv %buildroot%_bindir/oslo-rootwrap-daemon \
   %buildroot%_bindir/python3-oslo-rootwrap-daemon
popd
%endif

%python_install

%files
%doc README.rst LICENSE
%python_sitelibdir/*
%_bindir/oslo-rootwrap
%_bindir/oslo-rootwrap-daemon
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%_bindir/python3-oslo-rootwrap
%_bindir/python3-oslo-rootwrap-daemon
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.1-alt1
- 5.4.1
- add test packages

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 5.1.1-alt1
- 5.1.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 5.1.0-alt1
- 5.1.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0
- rename package from python-module-oslo-rootwrap to python-module-oslo.rootwrap
- add python3 package

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt1
- First build for ALT
