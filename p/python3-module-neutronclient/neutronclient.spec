%define oname neutronclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 8.1.0
Release: alt2

Summary: CLI and Client Library for OpenStack Networking

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-neutronclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 3.4.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-osc-lib >= 1.12.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-keystoneauth1 >= 3.8.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-simplejson >= 3.5.1

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-bandit >= 1.1.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-osprofiler >= 2.3.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-tempest >= 17.1.0
BuildRequires: python3-module-osc-lib-tests
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
%endif

%description
It provides a Python API (the neutronclient module) and a command-line tool
(neutron).

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

# install bash completion
install -pDm 644 tools/neutron.bash_completion \
  %buildroot%_sysconfdir/bash_completion.d/neutron.bash_completion

rm -rf %buildroot%python3_sitelibdir/%oname/tests/functional/hooks

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/neutron
%python3_sitelibdir/%oname
%python3_sitelibdir/python_neutronclient-%version-py%_python3_version.egg-info
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/neutron.bash_completion
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 8.1.0-alt2
- Fixed unowned dir.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 8.1.0-alt1
- Automatically updated to 8.1.0.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 7.1.1-alt3
- Build without docs.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 7.1.1-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 7.1.1-alt1
- Automatically updated to 7.1.1.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 6.14.0-alt1
- Automatically updated to 6.14.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 6.12.0-alt1
- Automatically updated to 6.12.0

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 6.9.1-alt1
- 6.9.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 6.1.0-alt1
- 6.1.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 6.0.0-alt1
- 6.0.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 4.1.2-alt1
- 4.1.2

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.1.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Wed Oct 14 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.12-alt1
- 2.3.12 (no changes)

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.11-alt1
- 2.3.11
- add python3 package

* Fri Aug 15 2014 Lenar Shakirov <snejok@altlinux.ru> 2.3.4-alt2
- Provides/Obsoletes: python-module-quantumclient added

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 2.3.4-alt1
- First build for ALT (based on Fedora 2.3.4-1.fc21.src)
