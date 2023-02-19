%define oname oslo.reports
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.0.0
Release: alt1.1

Summary: OpenStack Oslo reports library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.reports

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-reports = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-jinja2 >= 2.10
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-psutil >= 3.2.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0

%if_with check
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-greenlet >= 0.4.15
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: /proc
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc
BuildRequires: python3-module-oslo.config >= 5.2.0
%endif

%description
When things go wrong in (production) deployments of OpenStack collecting
debug data is a key first step in the process of triaging & ultimately
resolving the problem. Projects like Nova has extensively used logging
capabilities which produce a vast amount of data. This does not, however,
enable an admin to obtain an accurate view on the current live state
of the system. For example, what threads are running, what config parameters
are in effect, and more.

The project oslo.reports hosts a general purpose error report generation
framework, known as the "guru meditation report" to address the issues
described above.

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
Provides: python3-module-oslo-reports-doc = %EVR

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
install -pDm 644 man/osloreports.1 %buildroot%_man1dir/osloreports.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_reports
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/oslo_reports/tests

%files tests
%python3_sitelibdir/oslo_reports/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/osloreports.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1
- Automatically updated to 2.4.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.
- Fix license.
- Removed watch file.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.31.1-alt1
- Automatically updated to 1.31.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.30.0-alt1
- Automatically updated to 1.30.0.
- Build without python2.

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.28.0-alt1
- 1.28.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.17.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1.17.1-alt1
- 1.17.1

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.17.0-alt1
- 1.17.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- First build for ALT

