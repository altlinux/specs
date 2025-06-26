%define pypi_name extension-helpers

%def_with check

Name:    python3-module-%pypi_name
Version: 1.4.0
Release: alt1

Summary: Helpers to assist with building Python packages with compiled C/Cython extensions
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/extension-helpers
VCS:     https://github.com/astropy/extension-helpers

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
The extension-helpers package includes convenience helpers to assist with
building Python packages with compiled C/Cython extensions. It is developed
by the Astropy project but is intended to be general and usable by any
Python package.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md *.rst
%python3_sitelibdir/extension_helpers
%python3_sitelibdir/extension_helpers-%version.dist-info

%changelog
* Thu Jun 26 2025 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Thu Apr 03 2025 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
