%define pypi_name darkdetect

Name:    python3-module-%pypi_name
Version: 0.8.0
Release: alt1

Summary: Detect OS Dark Mode from Python

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/darkdetect
VCS:     https://github.com/albertosottile/darkdetect

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# Remove dependency on python3(winreg)
rm -v %buildroot/%python3_sitelibdir/%pypi_name/_windows_detect.py
# Remove also mac detect
rm -v %buildroot/%python3_sitelibdir/%pypi_name/_mac_detect.py

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 07 2024 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus.
