%define _unpackaged_files_terminate_build 1
%define oname fields

%def_with check

Name: python3-module-%oname
Version: 5.0.0
Release: alt5

Summary: Container class boilerplate killer
License: BSD
Group: Development/Python3

BuildArch: noarch
Url: https://pypi.org/project/fields/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(attr)
BuildRequires: python3(characteristic)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_benchmark)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%description
Container class boilerplate killer.

%prep
%setup
%autopatch -p1

# this file is not needed in python3
rm src/fields/py2ordereddict.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt5
- Moved on modern pyproject macros.

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 5.0.0-alt4
- Fixed FTBFS (Python3.10).

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 5.0.0-alt3
- Stopped Python2 package build.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 5.0.0-alt2
- Fixed Pytest4.x compatibility error.

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.0-alt1
- Initial build for ALT.
