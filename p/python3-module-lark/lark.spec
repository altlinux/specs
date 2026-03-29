%define _unpackaged_files_terminate_build 1
%define pypi_name lark
%define mod_name %pypi_name
%define extra_name interegular

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1.1
Summary: A modern parsing library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/lark
Vcs: https://github.com/lark-parser/lark
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
# file conflict on site-packages/lark/
Provides: python3-module-lark-parser = %EVR
Obsoletes: python3-module-lark-parser <= 0.11.3-alt1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-interegular
BuildRequires: python3-module-regex
%endif

%description
Lark is a modern general-purpose parsing library for Python.
With Lark, you can parse any context-free grammar, efficiently, with very little
code.

%package -n %name+%extra_name
Summary: %summary
Group: Development/Python3
Requires: %name
%description -n %name+%extra_name
Extra '%extra_name' for %pypi_name.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python -m tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %name+%extra_name
%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1.1
- Demodernized packaging.

* Tue Oct 28 2025 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.2.2 -> 1.3.1.

* Wed Sep 25 2024 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.1.9 -> 1.2.2.

* Mon Feb 19 2024 Stanislav Levin <slev@altlinux.org> 1.1.9-alt1
- 1.1.7 -> 1.1.9.

* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 1.1.7-alt1
- 1.1.5 -> 1.1.7.

* Fri May 05 2023 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- Initial build for Sisyphus.
