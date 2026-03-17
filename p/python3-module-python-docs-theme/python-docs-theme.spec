%define pypi_name python-docs-theme

Name:    python3-module-%pypi_name
Version: 2026.3
Release: alt1

Summary: The Sphinx theme for the CPython docs and related projects

License: Python-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/python-docs-theme
VCS:     https://github.com/python/python-docs-theme

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

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
%python3_sitelibdir/python_docs_theme
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 17 2026 Grigory Ustinov <grenka@altlinux.org> 2026.3-alt1
- Automatically updated to 2026.3.

* Wed Mar 04 2026 Grigory Ustinov <grenka@altlinux.org> 2026.2-alt1
- Automatically updated to 2026.2.

* Wed Jan 14 2026 Grigory Ustinov <grenka@altlinux.org> 2025.12-alt1
- Automatically updated to 2025.12.

* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 2025.9.2-alt1
- Automatically updated to 2025.9.2.

* Wed Sep 17 2025 Grigory Ustinov <grenka@altlinux.org> 2025.9.1-alt1
- Automatically updated to 2025.9.1.

* Wed May 28 2025 Grigory Ustinov <grenka@altlinux.org> 2025.5-alt1
- Automatically updated to 2025.5.

* Tue May 06 2025 Grigory Ustinov <grenka@altlinux.org> 2025.4.1-alt1
- Automatically updated to 2025.4.1.

* Wed Apr 30 2025 Grigory Ustinov <grenka@altlinux.org> 2025.4-alt1
- Automatically updated to 2025.4.

* Wed Feb 05 2025 Grigory Ustinov <grenka@altlinux.org> 2025.2-alt1
- Automatically updated to 2025.2.

* Mon Dec 23 2024 Grigory Ustinov <grenka@altlinux.org> 2024.12-alt1
- Automatically updated to 2024.12.

* Thu Oct 31 2024 Grigory Ustinov <grenka@altlinux.org> 2024.10-alt1
- Automatically updated to 2024.10.

* Wed Jun 26 2024 Grigory Ustinov <grenka@altlinux.org> 2024.6-alt1
- Automatically updated to 2024.6.

* Wed Apr 10 2024 Grigory Ustinov <grenka@altlinux.org> 2024.4-alt1
- Automatically updated to 2024.4.

* Mon Mar 25 2024 Grigory Ustinov <grenka@altlinux.org> 2024.3-alt1
- Automatically updated to 2024.3.

* Thu Feb 29 2024 Grigory Ustinov <grenka@altlinux.org> 2024.2-alt1
- Initial build for Sisyphus.
