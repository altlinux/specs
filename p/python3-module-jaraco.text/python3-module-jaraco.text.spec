%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.text

%def_with check

Name: python3-module-%pypi_name
Version: 3.11.0
Release: alt1

Summary: Module for text manipulation
License: MIT
Group:   Development/Python3
URL: https://pypi.org/project/jaraco.text/
VCS: https://github.com/jaraco/jaraco.text

Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# deps
BuildRequires: python3(jaraco.functools)
BuildRequires: python3(jaraco.context)
BuildRequires: python3(autocommand)
BuildRequires: python3(inflect)
BuildRequires: python3(more_itertools)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
%summary

%prep
%setup
%patch0 -p1

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
%python3_sitelibdir/jaraco/*
%python3_sitelibdir/jaraco.text-%version.dist-info/

%changelog
* Mon Dec 12 2022 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.2.0 -> 3.11.0.

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 3.2.0-alt2
- install missing in previous build Lorem\ ipsum.txt

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 3.2.0-alt1
- first build for ALT

