%define _unpackaged_files_terminate_build 1
%define pypi_name forbiddenfruit
%define module_name %pypi_name

Name: python3-module-%pypi_name
Version: 0.1.4
Release: alt1.git0c6accc5

Summary: Patch built-in python objects
License: GPLv3 and MIT
Group: Development/Python3
Url: https://pypi.org/project/forbiddenfruit/
Vcs: https://github.com/clarete/forbiddenfruit

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
This project allows Python code to extend built-in types.
If that's a good idea or not, you tell me. The first need this project attended
was allowing a Python assertion library to implement a similar API to RSpec
Expectations and should.js. But people got creative and used it to among other
things spy on things or to integrate profiling.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md COPYING.mit
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.1.4-alt1.git0c6accc5
- Initial build for ALT Sisyphus.

