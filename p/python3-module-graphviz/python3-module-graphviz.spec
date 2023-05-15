%define _unpackaged_files_terminate_build 1
%define  modulename graphviz
%def_enable check

Name:    python3-module-%modulename
Version: 0.20.1
Release: alt1

Summary: Simple Python interface for Graphviz
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/graphviz/
VCS:     https://github.com/xflr6/graphviz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_enabled check
# related https://bugzilla.altlinux.org/42311
BuildRequires: fonts-ttf-dejavu
BuildRequires: graphviz

BuildRequires: python3-module-pytest-mock
%endif

BuildArch: noarch
Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

%description
%summary

%prep
%setup
%patch0 -p1

sed -i '/^mock_use_standalone_module/d' setup.cfg

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Mon May 15 2023 Anton Vyatkin <toni@altlinux.org> 0.20.1-alt1
- New version 0.20.1 (Closes: #42049).

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.19.1-alt2
- Fixed FTBFS (workaround for libpango-1.50.5).

* Fri Dec 17 2021 Anton Farygin <rider@altlinux.ru> 0.19.1-alt1
- 0.19.1

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 0.19-alt1
- 0.19

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 0.13.2-alt1
- first build for ALT

