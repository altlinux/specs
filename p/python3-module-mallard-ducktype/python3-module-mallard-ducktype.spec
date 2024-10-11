%define modname mallard-ducktype
%define pypi_name mallard_ducktype

%def_enable check

Name: python3-module-%modname
Version: 1.0.2
Release: alt2

Summary: Parse Ducktype files and convert them to Mallard
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Source: https://github.com/projectmallard/%modname/archive/%version/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)

%description
Parse Ducktype files and convert them to Mallard.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
pushd tests
    ./runtests
popd


%files
%_bindir/ducktype
%python3_sitelibdir_noarch/mallard/__init__.py
%python3_sitelibdir_noarch/mallard/__pycache__/*
%python3_sitelibdir_noarch/mallard/ducktype/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc AUTHORS README.md COPYING


%changelog
* Fri Oct 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- switched build to %%pyproject* macros, improved %%check (ALT #51697)

* Tue Jul 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Apr 30 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Apr 10 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Thu Feb 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- first build for Sisyphus

