%define oname zunclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.6.0
Release: alt1.1

Summary: OpenStack Client Library for Zun

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-zunclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-websocket-client >= 0.44.0
BuildRequires: python3-module-yaml >= 3.12

%if_with check
BuildRequires: python3-module-bandit >= 1.1.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-ddt >= 1.0.1
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-tempest >= 17.1.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-docker >= 2.4.2
BuildRequires: python3-module-doc8 >= 0.6.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-testresources >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.4
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
%endif

%description
It provides a Python API (the zunclient module) and a command-line tool (zun).

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
install -pDm 644 man/python-%oname.1 %buildroot%_man1dir/%oname.1
%endif

# install bash completion
install -pDm 644 tools/zun.bash_completion \
  %buildroot%_sysconfdir/bash_completion.d/zun.bash_completion

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/zun
%python3_sitelibdir/%oname
%python3_sitelibdir/python_zunclient-%version.dist-info
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/zun.bash_completion
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 4.6.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.6.0-alt1
- Automatically updated to 4.6.0.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt2
- Fixed unowned dir.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1
- Automatically updated to 4.5.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt2
- Remove doc knob for unifying.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Automatically updated to 4.0.1.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt1
- Automatically updated to 3.6.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.
- Build without python2.

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- Initial build.
