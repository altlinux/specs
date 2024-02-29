%define pypi_name python-docs-theme

Name:    python3-module-%pypi_name
Version: 2024.2
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
* Thu Feb 29 2024 Grigory Ustinov <grenka@altlinux.org> 2024.2-alt1
- Initial build for Sisyphus.
