%define _unpackaged_files_terminate_build 1
%define nname nmap
%define pypi_name python_nmap

Name: python3-module-%nname
Version: 0.7.1
Release: alt1

Summary: python-nmap is a python library which helps in using nmap port scanner
License: GPL-3.0-only
Group: Development/Python3

URL: https://bitbucket.org/xael/python-nmap
VCS: https://bitbucket.org/xael/python-nmap
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)

BuildArch: noarch

%description
python-nmap is a python library which helps in using nmap port scanner. It
allows to easilly manipulate nmap scan results and will be a perfect tool for
systems administrators who want to automatize scanning task and reports. It
also supports nmap script outputs. It can even be used asynchronously. Results
are returned one host at a time to a callback function defined by the user.

%prep
%setup

%build
rm nmap/test_nmap.py
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/%nname
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README.rst

%changelog
* Sun Dec 07 2025 David Sultaniiazov <x1z53@altlinux.org> 0.7.1-alt1
- Initial build.
