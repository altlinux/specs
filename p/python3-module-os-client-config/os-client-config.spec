%define oname os-client-config

%def_without check
#ifarch %ix86 x86_64
#def_with check
#else
#def_without check
#endif

Name: python3-module-%oname
Version: 2.1.0
Release: alt2.2
Summary: OpenStack Client Configuration Library
Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
%if_with check
BuildRequires: python3-module-yaml >= 3.1.0
BuildRequires: python3-module-appdirs >= 1.3.0
BuildRequires: python3-module-keystoneauth1 >= 2.1.0
BuildRequires: python3-module-requestsexceptions >= 1.1.1
BuildRequires: python3-module-testtools
BuildRequires: python3-module-testscenarios
BuildRequires: python3-module-subunit
BuildRequires: python3-module-extras
BuildRequires: python3-module-openstacksdk >= 0.13.0
BuildRequires: python3-module-oslotest
BuildRequires: python3-module-glanceclient
%endif

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

%description
The os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you don't
have to know extra info to use OpenStack

* If you have a config file, you will get the clouds listed in it
* If you have environment variables, you will get a cloud named `envvars`
* If you have neither, you will get a cloud named `defaults` with base defaults


%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack os-client-config library
Group: Development/Documentation

%description doc
Documentation for the os-client-config library.

%prep
%setup -n %oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python3_build

#python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
#rm -fr doc/build/html/.buildinfo

%install
%python3_install

%check
python3 setup.py test

%files
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Oct 16 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt2.2
- Dropped build dependency on python3-module-reno.

* Thu Mar 31 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt2.1
- Fixed build.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt2
- drop unneeded BR: python3-module-subunit-tests

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.33.0-alt1
- Automatically updated to 1.33.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.32.0-alt1
- Automatically updated to 1.32.0

* Fri May 03 2019 Ivan A. Melnikov <iv@altlinux.org> 1.31.2-alt2
- enable tests on %%ix86 and x86_64
- remove test packages from BR when tests are disabled

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 1.31.2-alt1
- 1.31.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.26.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.26.0-alt1
- 1.26.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.21.1-alt1
- 1.21.1

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.4-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt1
- Initial packaging
