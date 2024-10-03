%define oname novaclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 18.7.0
Release: alt1

Summary: Client library for OpenStack Compute API

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-novaclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 3.0.0
BuildRequires: python3-module-keystoneauth1 >= 3.5.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.20.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-stevedore >= 2.0.1
BuildRequires: python3-module-hacking >= 6.1.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-osprofiler >= 1.4.0

%if_with check
BuildRequires(pre): openssl
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-cinderclient >= 3.3.0
BuildRequires: python3-module-glanceclient >= 2.8.0
BuildRequires: python3-module-neutronclient >= 6.7.0
BuildRequires: python3-module-bandit >= 1.1.0
BuildRequires: python3-module-coverage >= 4.4.1
BuildRequires: python3-module-ddt >= 1.0.1
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-openstacksdk >= 0.11.2
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-tempest >= 17.1.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
There's a Python API (the novaclient module), and a command-line script (nova).
Each implements 100 percent of the OpenStack Nova API.

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
%pyproject_build

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
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/nova.1 %buildroot%_man1dir/%oname.1
%endif

# install bash completion
install -pDm 644 tools/nova.bash_completion \
  %buildroot%_sysconfdir/bash_completion.d/nova.bash_completion

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/nova
%python3_sitelibdir/%oname
%python3_sitelibdir/python_novaclient-%version.dist-info
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/nova.bash_completion
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Thu Oct 03 2024 Grigory Ustinov <grenka@altlinux.org> 18.7.0-alt1
- Automatically updated to 18.7.0.

* Tue May 28 2024 Grigory Ustinov <grenka@altlinux.org> 18.6.0-alt1
- Automatically updated to 18.6.0.

* Mon Oct 16 2023 Grigory Ustinov <grenka@altlinux.org> 18.3.0-alt1.1
- Dropped build dependency on python3-module-reno.

* Fri Jul 28 2023 Grigory Ustinov <grenka@altlinux.org> 18.3.0-alt1
- Automatically updated to 18.3.0.

* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 18.1.0-alt2.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 18.1.0-alt2
- Fixed unowned dir.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 18.1.0-alt1
- Automatically updated to 18.1.0.

* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 17.0.0-alt4
- Fixed FTBFS (disabled docs).

* Mon Jul 06 2020 Grigory Ustinov <grenka@altlinux.org> 17.0.0-alt3
- Solved installation conflict (Closes: #38677).

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 17.0.0-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 17.0.0-alt1
- Automatically updated to 17.0.0.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 16.0.0-alt1
- Automatically updated to 16.0.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 15.1.0-alt1
- Automatically updated to 15.1.0.
- Build without python2.

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 11.0.0-alt1
- Updated to 11.0.0.

* Mon Mar 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.1.2-alt2
- Updated build dependencies.

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 7.1.2-alt1
- 7.1.2

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 7.1.1-alt1
- 7.1.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 6.0.0-alt1
- 6.0.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 3.3.1-alt1
- 3.3.1

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 2.30.2-alt1
- 2.30.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.30.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.30.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2.30.1-alt1
- 2.30.1

* Fri Oct 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.2-alt2
- drop Requires: python-module-keyring

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.2-alt1
- 2.23.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.0-alt1
- 2.23.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0
- add python3 package

* Thu Jul 24 2014 Lenar Shakirov <snejok@altlinux.ru> 2.17.0-alt1
- New version (based on Fedora 2.17.0-2.fc21.src)

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 2.8.0.26-alt1
- Initial release for Sisyphus (based on Fedora)

