%define pypi_name griffe-inherited-docstrings

%def_with check

Name:    python3-module-%pypi_name
Version: 1.1.3
Release: alt1

Summary: Griffe extension for inheriting docstrings

License: ISC
Group:   Development/Python3
URL:     https://pypi.org/project/griffe-inherited-docstrings
VCS:     https://github.com/mkdocstrings/griffe-inherited-docstrings

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pdm
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-griffe-lib
BuildRequires: python3-module-mkdocstrings
%endif

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

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/griffe_inherited_docstrings
%python3_sitelibdir/griffe_inherited_docstrings-%version.dist-info

%changelog
* Wed Mar 04 2026 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt1
- Automatically updated to 1.1.3.

* Wed Jan 21 2026 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus.
