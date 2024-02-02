%define _unpackaged_files_terminate_build 1
%define oname semver
%def_with check

Name: python3-module-%oname
Version: 3.0.2
Release: alt1

Summary: Python package to work with Semantic Versioning

Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/semver/

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

%description
A Python module for semantic versioning. Simplifies comparing versions.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst LICENSE.txt
%_bindir/pysemver
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Fri Feb 02 2024 Grigory Ustinov <grenka@altlinux.org> 3.0.2-alt1
- Build new version.

* Thu Mar 31 2022 Stanislav Levin <slev@altlinux.org> 2.13.0-alt2
- Fixed FTBFS (Python 3.10).

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 2.13.0-alt1
- new version 2.13.0 (with rpmrb script)

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt2
- cleanup spec, enable tests

* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt1
- Initial build
