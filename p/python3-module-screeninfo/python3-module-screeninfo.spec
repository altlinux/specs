%define pypi_name screeninfo

Name: python3-module-%pypi_name
Version: 0.8.1
Release: alt1
License: MIT

Summary: Fetch location and size of physical screens

Group: Development/Python3

Url: https://pypi.org/project/screeninfo
VCS: https://github.com/rr-/screeninfo.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-poetry-core

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE.md README.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Fri May 02 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.8.1-alt1
- Initial build
