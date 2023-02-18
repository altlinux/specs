%define oname vitrageclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.6.0
Release: alt2

Summary: OpenStack Vitrage Client API Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-vitrageclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 3.1.1
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-networkx >= 2.3
BuildRequires: python3-module-pydot >= 1.4.1

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.5.1
BuildRequires: python3-module-oslotest >= 3.3.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.5.0
BuildRequires: python3-module-testtools >= 2.3.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.11.0
%endif

%description
This is a client library for Vitrage built to interface with the Vitrage API.
It provides a Python API (the vitrageclient module) and a command-line tool
(vitrage).

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
install -pDm 644 tools/vitrage.bash_completion \
  %buildroot%_sysconfdir/bash_completion.d/vitrage.bash_completion

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/vitrage
%python3_sitelibdir/%oname
%python3_sitelibdir/python_vitrageclient-%version-py%_python3_version.egg-info
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/vitrage.bash_completion
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.6.0-alt2
- Fixed unowned dir.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 4.6.0-alt1
- Automatically updated to 4.6.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus.
