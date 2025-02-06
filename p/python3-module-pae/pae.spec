%define  oname pae

%def_with check

Name:    python3-module-%oname
Version: 0.1.0
Release: alt1.1

Summary: Pre-authentication encoding (PAE) implementation in Python

License: MIT
Group:   Development/Python3
URL:     https://github.com/MatthiasValvekens/python-pae

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-poetry-core
%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
This minimal library offers an implementation of (a variant of) PASETO's
pre-authentication encoding (PAE) scheme in Python, with some extra tools
to handle data types other than lists of byte arrays.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/python_pae
%python3_sitelibdir/python_pae-%version.dist-info

%changelog
* Thu Feb 06 2025 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.1
- NMU: fixed FTBFS (tox 4).

* Fri Jul 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
