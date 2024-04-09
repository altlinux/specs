%define oname jschema-to-python
%define pypi_name jschema_to_python

%def_with check

Name:    python3-module-%oname
Version: 1.2.3
Release: alt1

Summary: Generate source code for a set of Python classes from a JSON schema.

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/jschema-to-python
VCS:     https://github.com/microsoft/jschema-to-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jsonpickle
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
export PBR_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Apr 09 2024 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt1
- Initial build for Sisyphus.
