%define modname toposort
%def_enable check

Name: python3-module-%modname
Version: 1.6
Release: alt1.1

Summary: %modname implements a topological sort algorithm
Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/%modname

#VCS: https://bitbucket.org/ericvsmith/toposort.git
Source: https://pypi.io/packages/source/t/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
%summary

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 setup.py test

%files
%python3_sitelibdir_noarch/*
%doc README* CHANGES* NOTICE

%changelog
* Mon May 30 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1.1
- fixed BR

* Tue Mar 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6

* Tue Jul 21 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- first build for Sisyphus




