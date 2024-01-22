%define _unpackaged_files_terminate_build 1
%define oname pytest-freezegun

%def_with check

Name: python3-module-%oname
Version: 0.4.2
Release: alt3

Summary: Wrap tests with fixtures in freeze_time
License: MIT
Group: Development/Python3
# https://github.com/ktosiek/pytest-freezegun
Url: https://pypi.org/project/pytest-freezegun/

Source: %name-%version.tar.gz
Patch: %name-%version-alt.patch
Patch1: drop-distutils.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%py3_provides %oname

%if_with check
BuildRequires: python3(freezegun)
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
Wrap tests with fixtures in freeze_time.

Features:
- Freeze time in both the test and fixtures
- Access the freezer when you need it

%prep
%setup
%patch -p1
%patch1 -p0

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.rst
%python3_sitelibdir/pytest_freezegun.py
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/pytest_freezegun-%version.dist-info

%changelog
* Mon Jan 22 2024 Anton Vyatkin <toni@altlinux.org> 0.4.2-alt3
- Fixed FTBFS.

* Sat Oct 14 2023 Anton Vyatkin <toni@altlinux.org> 0.4.2-alt2
- Dropped dependency on distutils.

* Mon Oct 26 2020 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus.

