%def_disable snapshot
%define __name chunk
%define _name standard-%__name
%define pypi_name standard_%__name

%def_disable check

Name: python3-module-%_name
Version: 3.13.0
Release: alt1

Summary: Standard library chunk redistribution
License: Python
Group: Development/Python3
Url: https://pypi.org/project/standard-chunk/

Vcs: https://github.com/youknowone/python-deadlib.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check

%files
%python3_sitelibdir/%__name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Fri Oct 31 2025 Yuri N. Sedunov <aris@altlinux.org> 3.13.0-alt1
- first build for Sisyphus


