%define _unpackaged_files_terminate_build 1
%define pypi_name readthedocs-sphinx-ext
%define mod_name readthedocs_ext

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.5
Release: alt2

Summary: This holds code specific for Read the Docs and Sphinx

License: BSD-1-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/readthedocs-sphinx-ext
BuildArch: noarch

# https://github.com/rtfd/readthedocs-sphinx-ext
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools

BuildRequires: python3-module-sphinx

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
Tooling for a better Read the Docs Sphinx build experience.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 15 2024 Stanislav Levin <slev@altlinux.org> 2.2.5-alt2
- Migrated from removed setuptools' test command (see #50996).

* Wed Jan 31 2024 Grigory Ustinov <grenka@altlinux.org> 2.2.5-alt1
- Automatically updated to 2.2.5.

* Mon Jun 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1
- Automatically updated to 2.2.1.

* Wed Oct 26 2022 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Automatically updated to 2.2.0.

* Thu Sep 15 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.9-alt1
- Automatically updated to 2.1.9.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.8-alt1
- Automatically updated to 2.1.8.

* Wed Sep 09 2020 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt1
- Automatically updated to 2.1.1.

* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt1
- Version updated to 1.0.1
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1.git20141102.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.git20141102
- Initial build for Sisyphus

