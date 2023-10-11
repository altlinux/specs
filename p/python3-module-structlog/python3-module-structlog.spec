%define pypi_name structlog

%def_disable check

Name: python3-module-%pypi_name
Version: 23.2.0
Release: alt1

Summary: structlog is the production-ready logging solution for Python
Group: Development/Python3
License: Apache-2.0 OR MIT
Url: https://pypi.python.org/pypi/%pypi_name
Vcs: https://github.com/hynek/structlog.git

Source: https://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(hatchling)
BuildRequires: python3(hatch-vcs) python3(hatch-fancy-pypi-readme)
%{?_enable_check:BuildRequires: python3(tox) python3(pytest)
BuildRequires: python3(pre_commit) python3(sphinx) python3(mypy)}

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
#%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README* COPYRIGHT CHANGELOG*

%changelog
* Wed Oct 11 2023 Yuri N. Sedunov <aris@altlinux.org> 23.2.0-alt1
- 23.2.0

* Tue Aug 8 2023 Yuri N. Sedunov <aris@altlinux.org> 23.1.0-alt1
- first build for Sisyphus



