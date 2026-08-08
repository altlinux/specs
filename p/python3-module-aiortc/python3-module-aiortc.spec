%define pypi_name aiortc

Name:    python3-module-%pypi_name
Version: 1.15.0
Release: alt1

Summary: WebRTC and ORTC implementation for Python using asyncio
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/aiortc/
VCS:     https://github.com/aiortc/aiortc

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

BuildArch: noarch

Source: %name-%version.tar

%description
aiortc is a library for Web Real-Time Communication (WebRTC) and Object
Real-Time Communication (ORTC) in Python. It is built on top of asyncio,
Python's standard asynchronous I/O framework.

The API closely follows its Javascript counterpart while using pythonic
constructs:

promises are replaced by coroutines
events are emitted using pyee.EventEmitter

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
* Sat Aug 08 2026 Sergey Palcheh <minergenon@altlinux.org> 1.15.0-alt1
- Initial build for Sisyphus
