%define oname virtualenv-clone
%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-%oname
Version: 0.5.4
Release: alt2
Summary: script for cloning a non-relocatable virtualenv
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/virtualenv-clone/
Source: %name-%version.tar.gz
Patch0: %name-%version-%release.patch
Patch1: %oname-python39-support.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(virtualenv)
%endif

%description
A script for cloning a non-relocatable virtualenv.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%python3_build

%install
%python3_install

%check
sed -i '/\[testenv\]/a whitelist_externals =\
   \/bin\/cp\
   \/bin\/sed\
commands_pre =\
   \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/py.test\
   \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_INDEX=YES
export TOX_TESTENV_PASSENV='PIP_NO_INDEX'
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%doc LICENSE README.md
%python3_sitelibdir/clonevirtualenv.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/virtualenv_clone-%version-py%_python3_version.egg-info/
%_bindir/virtualenv-clone

%changelog
* Mon Apr 12 2021 Nikita Obukhov <nickf@altlinux.org> 0.5.4-alt2
- Add patch to support python3.9

* Mon Apr 06 2020 Nikita Obukhov <nickf@altlinux.org> 0.5.4-alt1
- Update to 0.5.4
- Mark virtualenv-clone as supporting python3.8

* Fri Dec 13 2019 Nikita Obukhov <nickf@altlinux.org> 0.5.3-alt1
- Initial Build

