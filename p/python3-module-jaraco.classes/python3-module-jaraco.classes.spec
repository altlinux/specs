%define _unpackaged_files_terminate_build 1
%define  modulename jaraco.classes

%def_enable check

Name:    python3-module-%modulename
Version: 3.2.2
Release: alt1

Summary: Utility functions for Python class constructs
License: MIT
Group:   Development/Python3
URL:     https://github.com/jaraco/jaraco.classes

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_enabled check
BuildRequires: python3-module-more-itertools
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

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
* Mon Sep 12 2022 Danil Shein <dshein@altlinux.org> 3.2.2-alt1
- update version to 3.2.2
  + migrate to pyproject macroses

* Wed Nov 18 2020 Danil Shein <dshein@altlinux.org> 3.1.0-alt1
- update version to 3.1.0
- build with check enabled

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 2.0-alt1
- first build for ALT

