%define _unpackaged_files_terminate_build 1
%define module_name aiocmd

Name: python3-module-%module_name
Version: 0.1.5
Release: alt1
Summary: Asyncio-based automatic CLI creation tool using prompt-toolkit
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/aiocmd
VCS: https://github.com/KimiNewt/aiocmd

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Coroutine-based CLI generator using prompt_toolkit,
similarly to the built-in cmd module.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %module_name}
%doc LICENSE

%changelog
* Tue Dec 03 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.5-alt1
- Initial build for ALT.
