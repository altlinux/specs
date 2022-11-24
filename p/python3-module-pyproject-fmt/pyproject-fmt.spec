%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject-fmt

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.1
Release: alt1

Summary: Format pyproject.toml file
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject-fmt
VCS: https://github.com/tox-dev/pyproject-fmt.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(hatchling)
BuildRequires: python3(hatch-vcs)

%if_with check
# dependencies=
BuildRequires: python3(packaging)
BuildRequires: python3(tomlkit)

BuildRequires: python3(pytest)
BuildRequires: python3(pytest-mock)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

%description
%summary.

%prep
%setup
%autopatch -p1

# hatch-vcs can use setuptools_scm which implements a file_finders entry point
# which returns all files tracked by SCM. Though that is version detection usage
# only (at least for now), it's safer to provide a real git tree.
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
%tox_check_pyproject -- -vra tests

%files
%doc README.md
%_bindir/%pypi_name
%python3_sitelibdir/pyproject_fmt/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 24 2022 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.4.0 -> 0.4.1.

* Wed Nov 23 2022 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.5 -> 0.4.0.

* Sat Aug 13 2022 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1
- 0.3.3 -> 0.3.5.

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus.
