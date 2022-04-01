%define _unpackaged_files_terminate_build 1
%define  modulename graphviz
%def_enable check

Name:    python3-module-%modulename
Version: 0.19.1
Release: alt2

Summary: Simple Python interface for Graphviz
License: MIT
Group:   Development/Python3
URL:     https://github.com/xflr6/graphviz

BuildRequires(pre): rpm-build-python3

%if_enabled check
# related https://bugzilla.altlinux.org/42311
BuildRequires: fonts-ttf-dejavu
BuildRequires: graphviz

BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest-mock

BuildRequires: python3-module-tox
BuildRequires: python3-module-tox-no-deps
%endif

BuildArch: noarch
Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

%description
%summary

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps -v --develop

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info/

%changelog
* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.19.1-alt2
- Fixed FTBFS (workaround for libpango-1.50.5).

* Fri Dec 17 2021 Anton Farygin <rider@altlinux.ru> 0.19.1-alt1
- 0.19.1

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 0.19-alt1
- 0.19

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 0.13.2-alt1
- first build for ALT

