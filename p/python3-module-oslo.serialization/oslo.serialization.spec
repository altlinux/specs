%define oname oslo.serialization
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.1.0
Release: alt1

Summary: OpenStack Oslo Serialization library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.serialization

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-serialization = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-msgpack >= 0.5.2
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-pytz >= 2013.6

%if_with check
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
%endif

%description
The oslo serialization library provides support for representing objects
in transmittable and storable formats, such as JSON and MessagePack.

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
Provides: python3-module-oslo-serialization-doc = %EVR

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
install -pDm 644 man/osloserialization.1 %buildroot%_man1dir/osloserialization.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_serialization
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_serialization/tests

%files tests
%python3_sitelibdir/oslo_serialization/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/osloserialization.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 4.3.0-alt1
- Automatically updated to 4.3.0.
- Unified (thx for felixz@).

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Automatically updated to 3.1.1.
- Renamed spec file.
- Fix license.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.29.2-alt1
- Automatically updated to 2.29.2.
- Build without python2.

* Fri Aug 23 2019 Grigory Ustinov <grenka@altlinux.org> 2.29.1-alt1
- new version 2.29.1

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 2.27.0-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.16.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 2.16.0-alt1
- 2.16.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.13.0-alt1
- 2.13.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- Initial release
