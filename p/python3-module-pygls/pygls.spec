%define _unpackaged_files_terminate_build 1
%define pypi_name pygls
%define mod_name %pypi_name

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1.1
Summary: A pythonic generic language server
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pygls
Vcs: https://github.com/openlawlibrary/pygls
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov

BuildRequires: python3-module-attrs
BuildRequires: python3-module-cattrs
BuildRequires: python3-module-lsprotocol
%endif

%add_python_extra ws

%description
%pypi_name (pronounced like "pie glass") is a pythonic generic implementation of
the Language Server Protocol for use as a foundation for writing your own
Language Servers in just a few lines of code.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1.1
- Demodernized packaging.

* Fri Mar 20 2026 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.0 -> 2.1.0.

* Sat Nov 01 2025 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Mon Jun 17 2024 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
