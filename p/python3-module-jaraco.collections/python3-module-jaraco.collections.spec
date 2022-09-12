%define _unpackaged_files_terminate_build 1
%define  modulename jaraco.collections

%def_enable check

Name:    python3-module-%modulename
Version: 3.5.2
Release: alt1

Summary: Collection objects similar to those in stdlib by jaraco
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.collections

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_enabled check
BuildRequires: python3-module-jaraco.classes
BuildRequires: python3-module-jaraco.text
%endif

BuildArch: noarch

Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

%py3_provides %modulename

%description
%summary

%prep
%setup
%patch0 -p1
# fix version tag handle by SCM
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
%tox_check_pyproject

%files
%python3_sitelibdir/jaraco/*
%python3_sitelibdir/%modulename-%version.dist-info/


%changelog
* Mon Sep 12 2022 Danil Shein <dshein@altlinux.org> 3.5.2-alt1
- new version 3.5.2
  + migrate to pyproject macroses

* Thu Nov 19 2020 Danil Shein <dshein@altlinux.org> 3.0.0-alt1
- update version to 3.0.0
- build with check enabled

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 2.1-alt1
- first build for ALT

