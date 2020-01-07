%define oname oslo.log

Name: python3-module-%oname
Version: 3.45.1
Release: alt1

Summary: OpenStack oslo.log library

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname

Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Provides: python3-module-oslo-log = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 3.1.1
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-six >= 1.11.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.20.0
BuildRequires: python3-module-oslo.i18n >= 3.20.0
BuildRequires: python3-module-oslo.utils >= 3.36.0
BuildRequires: python3-module-oslo.serialization >= 2.25.0
BuildRequires: python3-module-debtcollector >= 1.19.0
BuildRequires: python3-module-pyinotify >= 0.9.6
BuildRequires: python3-module-dateutil >= 2.5.3
BuildRequires: python3-module-monotonic >= 1.4

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

%description
OpenStack logging configuration library provides standardized configuration for
all openstack projects. It also provides custom formatters, handlers and
support for context specific logging (like resource id's etc).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo log handling library
Group: Development/Documentation
Provides: python-module-oslo-log-doc = %EVR

%description doc
Documentation for the Oslo log handling library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

sed 's/requests.packages.urllib3/urllib3/' -i oslo_log/_options.py

sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

# generate html docs
python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%_bindir/convert-json
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc build/sphinx/html

%changelog
* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 3.45.1-alt1
- Automatically updated to 3.45.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.44.1-alt1
- Automatically updated to 3.44.1.
- Build without python2.

* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 3.39.2-alt1
- 3.39.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.20.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 3.20.1-alt1
- 3.20.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- 3.16.0

* Thu Jun 16 2016 Lenar Shakirov <snejok@altlinux.ru> 3.3.0-alt2
- Fix urllib3 import in _options.py

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- Initial release
