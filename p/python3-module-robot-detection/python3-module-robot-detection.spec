%define pypi_name robot-detection

Name: python3-module-robot-detection
Version: 0.4
Release: alt1
Summary: Detect web crawlers from HTTP User-Agent headers

License: GPL-3.0-or-later
Group: Development/Python3
URL: https://github.com/amandasaurus/robot-detection
# Source-url: %__pypi_url robot-detection
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Library for detecting if a HTTP User Agent header is likely to be a bot.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/robot_detection.py
%python3_sitelibdir/__pycache__/robot_detection.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- initial build for ALT Sisyphus

