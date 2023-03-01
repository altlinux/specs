%define _unpackaged_files_terminate_build 1
%define pypi_name tempora

%def_with check

Name: python3-module-%pypi_name
Version: 5.2.1
Release: alt1
Summary: Objects and routines pertaining to date and time (tempora)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tempora/
VCS: https://github.com/jaraco/tempora
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires:
BuildRequires: python3(pytz)
BuildRequires: python3(jaraco.functools)

BuildRequires: python3(freezegun)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_freezegun)
%endif

%description
Objects and routines pertaining to date and time (tempora).

%prep
%setup
%autopatch -p1

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%_bindir/calc-prorate
%python3_sitelibdir/tempora/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 01 2023 Stanislav Levin <slev@altlinux.org> 5.2.1-alt1
- 5.0.2 -> 5.2.1.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 5.0.2-alt1
- 4.1.1 -> 5.0.2.

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 1.12 -> 4.1.1.
- Enabled testing.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.12-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.11-alt1
- Initial build for Sisyphus
