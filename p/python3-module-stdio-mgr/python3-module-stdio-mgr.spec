%define modname stdio-mgr
%define pypi_name stdio_mgr

Name: python3-module-%modname
Version: 1.0.1
Release: alt1

Summary: Testing library for CLI Python applications
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/stdio-mgr/

Vcs: https://www.github.com/bskinn/stdio-mgr
Source: http://pypi.io/packages/source/s/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-setuptools python3(attr)

%description
%summary

%prep
%setup -n %modname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Tue Nov 15 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus


