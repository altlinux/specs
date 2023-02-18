%define oname oslo.config
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 9.0.0
Release: alt2

Summary: OpenStack Oslo Configuration API

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.config

Source: %oname-%version.tar
Source1: %oname.watch

Patch: fix-oslo.config-test-under-bullseye.patch

BuildArch: noarch

Provides: python3-module-oslo-config = %EVR
%py3_provides oslo

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-rfc3986 >= 1.2.0
BuildRequires: python3-module-requests >= 2.18.0

%if_with check
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-mock >= 2.0
BuildRequires: python3-module-stestr >= 2.1.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-mypy >= 0.720
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-pre-commit >= 2.6.0
BuildRequires: python3-module-requests-mock
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.2.1
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
BuildRequires: python3-module-reno >= 2.5.0
%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

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
Provides: python3-module-oslo-config-doc = %EVR

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version
%patch -p1

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
install -pDm 644 man/osloconfig.1 %buildroot%_man1dir/osloconfig.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/oslo-config-generator
%_bindir/oslo-config-validator
%python3_sitelibdir/oslo_config
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_config/tests

%files tests
%python3_sitelibdir/oslo_config/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/osloconfig.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 9.0.0-alt2
- Fixed build with check.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 9.0.0-alt1
- Automatically updated to 9.0.0.

* Mon May 16 2022 Grigory Ustinov <grenka@altlinux.org> 8.8.0-alt1
- Automatically updated to 8.8.0.

* Thu Jul 29 2021 Ivan A. Melnikov <iv@altlinux.org> 8.0.2-alt2
- Add bootstrap knob to specfile.
- Add %%check.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 8.0.2-alt1
- Automatically updated to 8.0.2.
- Unify documentation building.
- Fix license.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 6.12.0-alt1
- Automatically updated to 6.12.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 6.11.1-alt1
- Automatically updated to 6.11.1.
- Build without python2.

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 6.4.1-alt1
- 6.4.1

* Thu May 24 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.22.1-alt2
- rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.22.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.1-alt1
- 3.22.1

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.0-alt1
- 3.22.0
- add test package

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 3.17.1-alt1
- 3.17.1

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.17.0-alt1
- 3.17.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.9.0-alt1
- 3.9.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
 (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0
- rename from python-module-oslo-config to python-module-oslo.config
- add python3 package

* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2.1-alt1
- First build for ALT
