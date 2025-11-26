%define pypi_name can
Name:    python3-module-%pypi_name
Version: 4.6.1
Release: alt1
Summary: Controller Area Network (CAN) support for Python
License: LGPL-3.0-only
URL:     https://github.com/hardbyte/python-can
VCS:     https://github.com/hardbyte/python-can
Source:  %name-%version.tar
Group:   Development/Python3

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-parameterized
BuildRequires: python3-module-canalystii
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-serial
BuildRequires: python3-module-wrapt

%description
The Controller Area Network is a bus standard designed to allow microcontrollers
and devices to communicate with each other. It has priority based bus
arbitration, reliable deterministic communication. It is used in cars, trucks,
boats, wheelchairs and more.
The can package provides controller area network support for Python developers;
providing common abstractions to different hardware devices, and a suite of
utilities for sending and receiving messages on a can bus.

%prep
%setup -n %name-%version

%build
%pyproject_build

%check
%pyproject_run_pytest -q --disable-warnings --maxfail=1 test

%install
%pyproject_install

%files
%doc README* CHANGELOG*
%_bindir/can_bridge
%_bindir/can_logconvert
%_bindir/can_logger
%_bindir/can_player
%_bindir/can_viewer
%python3_sitelibdir/can
%python3_sitelibdir/python_can-0.0.0.dist-info

%changelog
* Tue Oct 21 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 4.6.1-alt1
- Initial build.
