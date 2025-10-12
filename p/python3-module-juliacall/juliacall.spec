%define modulename juliacall

Name:    python3-module-%modulename
Version: 0.9.28
Release: alt1

Summary: Python and Julia in harmony
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/juliacall
VCS:     https://github.com/JuliaPy/PythonCall.jl

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 0.9.28-alt1
- Automatically updated to 0.9.28.

* Tue Sep 02 2025 Grigory Ustinov <grenka@altlinux.org> 0.9.27-alt1
- Automatically updated to 0.9.27.

* Thu Jul 24 2025 Grigory Ustinov <grenka@altlinux.org> 0.9.26-alt1
- Automatically updated to 0.9.26.

* Thu Jul 03 2025 Grigory Ustinov <grenka@altlinux.org> 0.9.25-alt1
- Initial build for Sisyphus
