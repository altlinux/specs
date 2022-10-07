%define _unpackaged_files_terminate_build 1

%define oname hatch-fancy-pypi-readme
%define modname hatch_fancy_pypi_readme

# tomli is tomllib(stdlib) on Python 3.11
%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

%def_with check

Name: python3-module-%oname
Version: 22.8.0
Release: alt1

Summary: Fancy PyPI READMEs with Hatch

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatch-fancy-pypi-readme/
VCS: https://github.com/hynek/hatch-fancy-pypi-readme.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(hatchling)

%if_with check
%if %tomli
BuildRequires: python3(tomli)
%endif
BuildRequires: python3(pytest)
BuildRequires: python3(build)
BuildRequires: python3(wheel)
%endif

%py3_provides %oname

%if %tomli
%py3_requires tomli
%endif

%description
hatch-fancy-pypi-readme is a Hatch metadata plugin for everyone who cares
about the first impression of their project's PyPI landing page.

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
%_bindir/%oname
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Fri Oct 07 2022 Stanislav Levin <slev@altlinux.org> 22.8.0-alt1
- 22.3.0 -> 22.8.0.

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.ru> 22.3.0-alt1
- Initial build for Sisyphus
