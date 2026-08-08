%define pypi_name pyatv

Name:    python3-module-%pypi_name
Version: 0.18.0
Release: alt1

Summary: A client library for Apple TV and AirPlay devices
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pyatv/
VCS:     https://github.com/postlund/pyatv

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

BuildArch: noarch

Source: %name-%version.tar

%description
A client library for Apple TV and AirPlay devices.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE.md README.md
%_bindir/atvlog
%_bindir/atvproxy
%_bindir/atvremote
%_bindir/atvscript
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Sat Aug 08 2026 Sergey Palcheh <minergenon@altlinux.org> 0.18.0-alt1
- Initial build for Sisyphus
