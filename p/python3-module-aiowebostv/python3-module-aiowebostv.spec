%define _unpackaged_files_terminate_build 1
%define module_name aiowebostv

Name: python3-module-%module_name
Version: 0.4.0
Release: alt1
Summary: Python library to control LG webOS based TV devices
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/home-assistant-libs/aiowebostv
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %module_name}

%changelog
* Fri Apr 19 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.0-alt1
- Updated to version 0.4.0.

* Sat Feb 10 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.3-alt1
- Initial build for ALT.
