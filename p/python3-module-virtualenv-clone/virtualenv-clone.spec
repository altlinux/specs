%define oname virtualenv-clone
%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-%oname
Version: 0.5.7
Release: alt2
Summary: script for cloning a non-relocatable virtualenv
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/virtualenv-clone/
Vcs: https://github.com/edwardgeorge/virtualenv-clone
Source: %name-%version.tar
Patch0: venv-clone-%version-alt-py3.11-fix.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(virtualenv)
%endif

%description
A script for cloning a non-relocatable virtualenv.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE README.md
%python3_sitelibdir/clonevirtualenv.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/virtualenv_clone-%version.dist-info
%_bindir/virtualenv-clone

%changelog
* Fri Sep 15 2023 Anton Vyatkin <toni@altlinux.org> 0.5.7-alt2
- Fix FTBFS (migrate to pyproject macroses).

* Thu Feb 24 2022 Stanislav Levin <slev@altlinux.org> 0.5.7-alt1
- 0.5.4 -> 0.5.7.

* Mon Apr 12 2021 Nikita Obukhov <nickf@altlinux.org> 0.5.4-alt2
- Add patch to support python3.9

* Mon Apr 06 2020 Nikita Obukhov <nickf@altlinux.org> 0.5.4-alt1
- Update to 0.5.4
- Mark virtualenv-clone as supporting python3.8

* Fri Dec 13 2019 Nikita Obukhov <nickf@altlinux.org> 0.5.3-alt1
- Initial Build

