%define  oname tzdata

%def_with check

Name:    python3-module-%oname
Version: 2022.6
Release: alt1

Summary: Python package wrapping the IANA time zone database

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/tzdata

# https://github.com/python/tzdata
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest-subtests
%endif

BuildArch: noarch

%description
This is a Python package containing zic-compiled binaries for the IANA time zone
database. It is intended to be a fallback for systems that do not have
system time zone data installed (or don't have it installed in a
standard location), as a part of PEP 615

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 2022.6-alt1
- Initial build for Sisyphus.
