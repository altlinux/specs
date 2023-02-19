%define oname oslo.privsep
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.1.0
Release: alt1

Summary: OpenStack library for privilege separation

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.privsep

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-privsep = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-cffi >= 1.14.0
BuildRequires: python3-module-eventlet >= 0.21.0
BuildRequires: python3-module-msgpack >= 0.6.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-greenlet >= 0.4.14
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
This library helps applications perform actions which require more or less privileges
than they were started with in a safe, easy to code and easy to use manner.
For more information on why this is generally a good idea please read over
the principle of least privilege and the specification which created this library.

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
Provides: python3-module-oslo-privsep-doc = %EVR

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
install -pDm 644 man/osloprivsep.1 %buildroot%_man1dir/osloprivsep.1
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/privsep-helper
%python3_sitelibdir/oslo_privsep
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_privsep/tests

%files tests
%python3_sitelibdir/oslo_privsep/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/osloprivsep.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.

* Mon May 16 2022 Grigory Ustinov <grenka@altlinux.org> 2.8.0-alt1
- Automatically updated to 2.8.0.
- Unified (thx for felixz@).

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt1
- Automatically updated to 2.1.1.
- Renamed spec file.
- Fix license.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.33.3-alt1
- Automatically updated to 1.33.3
- Build without python2.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.33.1-alt1
- Automatically updated to 1.33.1

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.29.2-alt1
- 1.29.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.16.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.13.1-alt1
- 1.13.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.13.0-alt1
- Initial package.
