%define pypi_name CustomTkinter

Name:    python3-module-%pypi_name
Version: 5.3.0
Release: alt1

Summary: A modern and customizable python UI-library based on Tkinter

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/customtkinter
VCS:     https://github.com/TomSchimansky/CustomTkinter

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

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
%python3_sitelibdir/customtkinter
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jan 26 2026 Grigory Ustinov <grenka@altlinux.org> 5.3.0-alt1
- Automatically updated to 5.3.0.

* Thu Nov 07 2024 Grigory Ustinov <grenka@altlinux.org> 5.2.2-alt1
- Initial build for Sisyphus (Closes: #51982).
