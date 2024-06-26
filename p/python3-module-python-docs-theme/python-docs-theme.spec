%define pypi_name python-docs-theme

Name:    python3-module-%pypi_name
Version: 2024.6
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
%doc LICENSE *.rst
%python3_sitelibdir/python_docs_theme
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jun 26 2024 Grigory Ustinov <grenka@altlinux.org> 2024.6-alt1
- Automatically updated to 2024.6.

* Wed Apr 10 2024 Grigory Ustinov <grenka@altlinux.org> 2024.4-alt1
- Automatically updated to 2024.4.

* Mon Mar 25 2024 Grigory Ustinov <grenka@altlinux.org> 2024.3-alt1
- Automatically updated to 2024.3.

* Thu Feb 29 2024 Grigory Ustinov <grenka@altlinux.org> 2024.2-alt1
- Initial build for Sisyphus.
