%define oname tooz

%def_with python3

Name: python-module-%oname
Version: 1.48.2
Release: alt1.1
Summary: Coordination library for distributed systems
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-stevedore >= 1.16.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-enum34
BuildRequires: python-module-voluptuous >= 0.8.9
BuildRequires: python-module-msgpack >= 0.4.0
BuildRequires: python-module-fasteners >= 0.7
BuildRequires: python-module-tenacity >= 3.2.1
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-futurist >= 0.11.0
BuildRequires: python-module-oslo.utils >= 3.15.0
BuildRequires: python-module-oslo.serialization >= 1.10.0

# for doc
BuildRequires: python-module-pymemcache
BuildRequires: python-module-pymysql
BuildRequires: python-module-sysv_ipc
BuildRequires: python-module-psycopg2
BuildRequires: python-module-redis-py
BuildRequires: python-module-kazoo
BuildRequires: python-module-zake

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-stevedore >= 1.5.0
BuildRequires: python3-module-voluptuous >= 0.8.9
BuildRequires: python3-module-msgpack >= 0.4.0
BuildRequires: python3-module-fasteners >= 0.7
BuildRequires: python3-module-tenacity >= 3.2.1
BuildRequires: python3-module-futurist >= 0.11.0
BuildRequires: python3-module-oslo.utils >= 3.15.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
%endif

%description
The Tooz project aims at centralizing the most common distributed
primitives like group membership protocol, lock service and leader
election by providing a coordination API helping developers to build distributed applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    Coordination library for distributed systems
Group: Development/Python3

%description -n python3-module-%oname
The Tooz project aims at centralizing the most common distributed
primitives like group membership protocol, lock service and leader
election by providing a coordination API helping developers to build distributed applications.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Coordination library
Group: Development/Documentation

%description doc
Documentation for Coordination library.

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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo


%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS ChangeLog LICENSE PKG-INFO README.rst
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
%doc doc/build/html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.48.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Alexey Shabalin <shaba@altlinux.ru> 1.48.2-alt1
- 1.48.2

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1.48.1-alt1
- 1.48.1

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.48.0-alt1
- 1.48.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.43.0-alt1
- 1.43.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.34.0-alt1
- 1.34.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.24.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.24.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.24.0-alt1
- 1.24.0

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt1
- Initial release
