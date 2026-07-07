%define pypi_name vncdotool

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Python API for vncdotool, a command line VNC client

License: MIT
Group: Development/Python3
URL: https://github.com/sibson/vncdotool

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

# PIL is imported conditionally (try/except) so the auto-dep scanner skips it,
# but it is required for the capture/expect features.
Requires: python3-module-pillow

%description
vncdotool is a command line VNC client. It can be useful to automate
interactions with virtual machines or hardware devices that are otherwise
difficult to control. This package provides the programmatic Python API
(vncdotool.api); the console scripts live in the vncdotool package.

%package -n %pypi_name
Summary: Command line VNC client
Group: Networking/Remote access
Requires: python3-module-%pypi_name = %EVR

%description -n %pypi_name
vncdotool is a command line VNC client. It can be useful to automate
interactions with virtual machines or hardware devices that are otherwise
difficult to control. This package provides the console scripts
(vncdo, vncdotool, vnclog).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n %pypi_name
%_bindir/vncdo
%_bindir/vncdotool
%_bindir/vnclog

%changelog
* Sat Jul 04 2026 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Sisyphus
