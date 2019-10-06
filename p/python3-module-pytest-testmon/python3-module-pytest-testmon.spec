%global pypi_name pytest-testmon

Name: python3-module-%pypi_name
Version: 0.9.18
Release: alt1
Summary: A py.test plug-in which executes only tests affected by recent changes
Group: Development/Python
License: MIT
Url: http://testmon.org/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest
BuildRequires: python3-modules-sqlite3
%py3_provides pytest_testmon

%description
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH=$PWD py.test3

%files -n python3-module-%pypi_name
%doc README.rst LICENSE
%python3_sitelibdir/testmon
%python3_sitelibdir/pytest_testmon-%version-py?.?.egg-info

%changelog
* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 0.9.18-alt1
- first build for ALT

