%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-enabler

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: Pytest plugin for configuration of another plugins
License: MIT
Group: Development/Python3
VCS: https://github.com/jaraco/pytest-enabler.git
Url: https://pypi.org/project/pytest-enabler/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# dependencies=
BuildRequires: python3(toml)
BuildRequires: python3(jaraco.context)
BuildRequires: python3(jaraco.functools)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
%pypi_name plugin allows configuration of Pytest plugins if present, but omits
the settings if the plugin is not present.

%prep
%setup
%autopatch -p1

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
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
%tox_check_pyproject -- -vra

%files
%doc README.rst
%python3_sitelibdir/pytest_enabler/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Nov 25 2022 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.3.0 -> 2.0.0.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.1 -> 1.3.0.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
