%define pypi_name pylibsrtp

Name:    python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: Python wrapper around the libsrtp library
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/pylibsrtp/
VCS:     https://github.com/aiortc/pylibsrtp

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-cffi libsrtp2-devel libssl-devel

Source: %name-%version.tar

%description
pylibsrtp is a Python wrapper around libsrtp, making it possible to
encrypt and decrypt Secure Real-time Transport Protocol (SRTP) packets
from Python code.

SRTP is a profile of the Real-time Transport Protocol (RTP) which
provides confidentiality, message authentication, and replay protection.
It is defined by RFC 3711.

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
* Sat Aug 08 2026 Sergey Palcheh <minergenon@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
