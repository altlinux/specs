%define _unpackaged_files_terminate_build 1
%define pypi_name iniconfig

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1
Summary: A small and simple INI-file parser
License: MIT
Group: Development/Tools
Url: https://pypi.org/project/iniconfig/
VCS: https://github.com/pytest-dev/iniconfig
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(hatch-vcs)
BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
%summary

%prep
%setup
%patch -p1

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
%pyproject_run_pytest -vra

%files
%doc CHANGELOG README.rst
%python3_sitelibdir/iniconfig/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.1.1 -> 2.0.0.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.0 -> 1.1.1.
- Built Python3 package from its ows src.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Fixed testing against Pytest 5.

* Sat Mar 16 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build.

