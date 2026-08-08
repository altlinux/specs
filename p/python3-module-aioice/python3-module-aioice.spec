%define pypi_name aioice

Name:    python3-module-%pypi_name
Version: 0.10.2
Release: alt1

Summary: An implementation of Interactive Connectivity Establishment (RFC 5245)
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/aioice/
VCS:     https://github.com/aiortc/aioice

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

BuildArch: noarch

Source: %name-%version.tar

%description
aioice is a library for Interactive Connectivity Establishment (RFC 5245)
in Python. It is built on top of asyncio, Python's standard asynchronous
I/O framework.

Interactive Connectivity Establishment (ICE) is useful for applications
that establish peer-to-peer UDP data streams, as it facilitates NAT
traversal. Typical usecases include SIP and WebRTC.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Sat Aug 08 2026 Sergey Palcheh <minergenon@altlinux.org> 0.10.2-alt1
- Initial build for Sisyphus
