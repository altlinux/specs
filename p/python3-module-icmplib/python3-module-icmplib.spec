%define pypi_name icmplib

Name: python3-module-%pypi_name
Version: 3.0.4
Release: alt1

Summary: Modern implementation of the ICMP protocol in Python
Group: Development/Python3
License: LGPL-3.0
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/ValentinBELYN/icmplib.git

BuildArch: noarch

Source: https://pypi.io/packages/source/i/%pypi_name/%pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3(wheel) python3(setuptools)

%description
icmplib is a brand new and modern implementation of the ICMP protocol in Python.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Tue Jul 23 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- first build for Sisyphus



