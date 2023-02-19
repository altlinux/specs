%define oname designateclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.2.0
Release: alt1

Summary: OpenStack DNS-as-a-Service - Client

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-designateclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-stevedore >= 1.20.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-tempest >= 25.0.0
BuildRequires: python3-module-osc-lib-tests
BuildRequires: python3-module-jsonschema >= 3.2.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-requests-mock >= 1.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 3.1.0
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
There's a Python API (the designateclient module), and a command-line tool
(designate).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%python3_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

%if_with docs
# install man page
install -pDm 644 man/python-%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/python_designateclient-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/functionaltests

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/functionaltests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.2.0-alt1
- Automatically updated to 5.2.0.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.11.0-alt1
- Automatically updated to 2.11.0

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 2.10.0-alt1
- 2.10.0

* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.6.0-alt2
- rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0
- enable build python3 module

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.2-alt2
- BuildReq: python-module-subunit -> python-module-python-subunit

* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.2-alt1
- First build for ALT (based on OpenSuSe 1.0.2-1.1.src)

