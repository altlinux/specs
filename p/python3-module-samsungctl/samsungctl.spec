Name: python3-module-samsungctl
Version: 0.7.1
Release: alt2

Summary: Python library for remote controlling Samsung TV sets
License: MIT
Group: Development/Python
Url: https://pypi.org/project/samsungctl
VCS: https://github.com/ape/samsungctl

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
Python library for remote controlling Samsung TV sets via a TCP/IP connection.
It currently supports both pre-2016 TVs as well most of the modern Tizen-OS TVs
with Ethernet or Wi-Fi connectivity.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/samsungctl
%python3_sitelibdir/samsungctl
%python3_sitelibdir/samsungctl-%version.dist-info

%changelog
* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.1-alt2
- moved to pyproject

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.1-alt1
- initial
