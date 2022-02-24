%define oname virtualenv-clone
%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-%oname
Version: 0.5.7
Release: alt1
Summary: script for cloning a non-relocatable virtualenv
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/virtualenv-clone/
Source: %name-%version.tar.gz
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(virtualenv)
%endif

%description
A script for cloning a non-relocatable virtualenv.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOX_TESTENV_PASSENV='PIP_NO_INDEX'
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr

%files
%doc LICENSE README.md
%python3_sitelibdir/clonevirtualenv.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/virtualenv_clone-%version-py%_python3_version.egg-info/
%_bindir/virtualenv-clone

%changelog
* Thu Feb 24 2022 Stanislav Levin <slev@altlinux.org> 0.5.7-alt1
- 0.5.4 -> 0.5.7.

* Mon Apr 12 2021 Nikita Obukhov <nickf@altlinux.org> 0.5.4-alt2
- Add patch to support python3.9

* Mon Apr 06 2020 Nikita Obukhov <nickf@altlinux.org> 0.5.4-alt1
- Update to 0.5.4
- Mark virtualenv-clone as supporting python3.8

* Fri Dec 13 2019 Nikita Obukhov <nickf@altlinux.org> 0.5.3-alt1
- Initial Build

