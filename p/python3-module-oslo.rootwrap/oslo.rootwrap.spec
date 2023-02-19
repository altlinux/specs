%define oname oslo.rootwrap
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 6.3.1
Release: alt2.1

Summary: OpenStack Oslo Rootwrap

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.rootwrap

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-rootwrap = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0

%if_with check
BuildRequires: python3-module-mock >= 2.0.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-pre-commit >= 2.6.0
BuildRequires: schedutils
BuildRequires: iproute2
BuildRequires: /proc
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 3.1.0
%endif

%description
The Oslo Rootwrap allows fine filtering of shell commands to run as `root`
from OpenStack services.

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
Provides: python3-module-oslo-rootwrap-doc = %EVR

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
install -pDm 644 man/oslorootwrap.1 %buildroot%_man1dir/oslorootwrap.1
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/oslo-rootwrap
%_bindir/oslo-rootwrap-daemon
%python3_sitelibdir/oslo_rootwrap
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/oslo_rootwrap/tests

%files tests
%python3_sitelibdir/oslo_rootwrap/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/oslorootwrap.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 6.3.1-alt2.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 6.3.1-alt2
- Fixed build with check.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 6.3.1-alt1
- Automatically updated to 6.3.1.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 6.0.2-alt1
- Automatically updated to 6.0.2.
- Fix license.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 5.17.1-alt1
- Automatically updated to 5.17.1.
- Added watch file.
- Renamed spec file.
- Build without python2.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 5.16.1-alt1
- Automatically updated to 5.16.1.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 5.16.0-alt1
- Automatically updated to 5.16.0

* Sat Dec 08 2018 Alexey Shabalin <shaba@altlinux.org> 5.14.1-alt1
- 5.14.1

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
