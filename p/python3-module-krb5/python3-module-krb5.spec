%define _unpackaged_files_terminate_build 1

%define pypi_name krb5

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.1
Release: alt1

Summary: Python krb5 API interface
License: MIT
Group:   Development/Python3
URL:     https://github.com/jborean93/pykrb5

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: python3(cython)
BuildRequires: libkrb5-devel

%if_with check
BuildRequires: python3(k5test)
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
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Dec 04 2023 Andrey Limachko <liannnix@altlinux.org> 0.5.1-alt1
- New version 0.5.1.

* Sun Jul 09 2023 Andrey Limachko <liannnix@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
