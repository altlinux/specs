%define oname glanceclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.3.0
Release: alt1

Summary: OpenStack Image API Client Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-glanceclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-keystoneauth1 >= 3.6.2
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-warlock >= 1.2.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-wrapt >= 1.7.0
BuildRequires: python3-module-OpenSSL >= 17.1.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-ddt >= 1.2.1
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-tempest >= 17.1.0
BuildRequires: python3-module-requests-mock >= 1.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
There's a Python API (the glanceclient module), and a command-line script
(glance). Each implements 100 percent of the OpenStack Glance API.

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
install -pDm 644 man/glance.1 %buildroot%_man1dir/%oname.1
%endif

# install bash completion
install -pDm 644 tools/glance.bash_completion \
  %buildroot%_sysconfdir/bash_completion.d/glance.bash_completion

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/glance
%python3_sitelibdir/%oname
%python3_sitelibdir/python_glanceclient-%version-py%_python3_version.egg-info
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/glance.bash_completion
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.3.0-alt1
- Automatically updated to 4.3.0.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt2
- Fixed unowned dir.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Automatically updated to 3.1.1.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 2.17.0-alt1
- Automatically updated to 2.17.0.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.16.0-alt1
- Automatically updated to 2.16.0

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 2.13.0-alt1
- 2.13.0

* Tue Oct 09 2018 Grigory Ustinov <grenka@altlinux.org> 2.12.1-alt1
- Updated to 2.12.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0
- add test packages

* Tue Feb 21 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt2
- add patch for workaround requests >= 2.12

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
 (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- fix work with system urllib3

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.17.2-alt1
- 0.17.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.17.0-alt1
- 0.17.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt1
- 0.16.1
- add python3 package

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 0.12.0-alt1
- First build for ALT (based on Fedora 0.12.0-1.fc20.src)

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.1-alt1
- Initial release for Sisyphus (based on Fedora)

