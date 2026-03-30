%define _unpackaged_files_terminate_build 1

%define pypi_name krb5

%def_with check

Name:    python3-module-%pypi_name
Version: 0.7.1
Release: alt1.1

Summary: Python krb5 API interface
License: MIT
Group:   Development/Python3
URL:     https://github.com/jborean93/pykrb5

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3(cython)
BuildRequires: libkrb5-devel

%if_with check
BuildRequires: python3(k5test)
BuildRequires: python3-module-pytest
%endif

Source: %pypi_name-%version.tar

%description
This library provides Python functions that wraps the Kerberos 5 C API.
Due to the complex nature of this API it is highly recommended to use
something like python-gssapi which exposes the Kerberos authentication
details through GSSAPI.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt1.1
- Demodernized packaging.

* Mon Jul 14 2025 Andrey Limachko <liannnix@altlinux.org> 0.7.1-alt1
- New version 0.7.1.
- Remove unneeded header file python_krb5.h. (Closes: #55209)

* Thu Feb 06 2025 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.1
- NMU: fixed FTBFS (tox 4).

* Mon Dec 04 2023 Andrey Limachko <liannnix@altlinux.org> 0.5.1-alt1
- New version 0.5.1.

* Sun Jul 09 2023 Andrey Limachko <liannnix@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
