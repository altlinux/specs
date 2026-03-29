%define _unpackaged_files_terminate_build 1
%define pypi_name ufmt
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
Version: 2.9.1
Release: alt1.1
Summary: Safe, atomic formatting with black and usort
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/ufmt
Vcs: https://github.com/omnilib/ufmt
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-black
BuildRequires: python3-module-build
BuildRequires: python3-module-click
BuildRequires: python3-module-coverage
BuildRequires: python3-module-flake8
BuildRequires: python3-module-libcst
BuildRequires: python3-module-moreorless
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pygls
BuildRequires: python3-module-tomlkit
BuildRequires: python3-module-trailrunner
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-usort
%endif

%add_python_extra lsp

%description
%pypi_name is a safe, atomic code formatter for Python built on top of black and
usort. %pypi_name formats files in-memory, first with usort and then with black,
before writing any changes back to disk. This enables a combined, atomic step
in CI/CD workflows for checking or formatting files, without any with conflict
or intermediate changes between the import sorter and the code formatter.

%package -n %pypi_name
Summary: Executable for %pypi_name
Group: Development/Python3
Requires: %name

%description -n %pypi_name
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# don't ship tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
%pyproject_run -- python3 -m %mod_name.tests -v

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n %pypi_name
%_bindir/%pypi_name

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.9.1-alt1.1
- Demodernized packaging.

* Mon Feb 09 2026 Stanislav Levin <slev@altlinux.org> 2.9.1-alt1
- 2.9.0 -> 2.9.1.

* Fri Nov 14 2025 Stanislav Levin <slev@altlinux.org> 2.9.0-alt1
- 2.8.0 -> 2.9.0.

* Fri May 23 2025 Stanislav Levin <slev@altlinux.org> 2.8.0-alt2
- Fixed FTBFS (click 8.2.0).

* Fri Oct 25 2024 Stanislav Levin <slev@altlinux.org> 2.8.0-alt1
- 2.7.3 -> 2.8.0.

* Mon Sep 23 2024 Stanislav Levin <slev@altlinux.org> 2.7.3-alt1
- 2.7.0 -> 2.7.3.

* Mon Jun 17 2024 Stanislav Levin <slev@altlinux.org> 2.7.0-alt1
- 2.6.0 -> 2.7.0.

* Fri May 03 2024 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.5.1 -> 2.6.0.

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 2.5.1-alt1
- 2.5.0 -> 2.5.1.

* Thu Feb 22 2024 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- 2.3.0 -> 2.5.0.

* Thu Nov 09 2023 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.2.0 -> 2.3.0.

* Wed Aug 02 2023 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.0 -> 2.2.0.

* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.1 -> 2.1.0.

* Wed Nov 16 2022 Michael Shigorin <mike@altlinux.org> 2.0.1-alt2
- Fix BR: requisite for %%build, not just %%check.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 1.3.2 -> 2.0.1.

* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.3.1 -> 1.3.2.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
