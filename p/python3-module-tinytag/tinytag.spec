%define _unpackaged_files_terminate_build 1
%define pypi_name tinytag

Name: python3-module-%pypi_name
Version: 2.3.0
Release: alt1

Summary: Python library for reading audio file metadata
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/tinytag
Vcs: https://github.com/tinytag/tinytag

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core python3-module-wheel

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

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 31 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.3.0-alt1
- 2.2.1 -> 2.3.0

* Tue Apr 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.2.1-alt1
- Initial build for ALT Linux.

