%define modname langdetect
%def_enable check

Name: python3-module-%modname
Version: 1.0.9
Release: alt2

Summary: Python3 language-detection library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/Mimino666/langdetect.git

Source: https://pypi.io/packages/source/l/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest) python3(six)}

%description
Port of Nakatani Shuyo's language-detection library (version from
03/03/2014) to Python.

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
py.test-3

%files
%python3_sitelibdir_noarch/*
%doc README* NOTICE

%changelog
* Fri Oct 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt2
- switched build to %%pyproject* macros (ALT #51696)

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- first build for Sisyphus




