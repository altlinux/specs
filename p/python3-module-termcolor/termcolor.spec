%define _unpackaged_files_terminate_build 1
%define pypi_name termcolor
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1.1
Summary: ANSI color formatting for output in terminal
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/termcolor/
Vcs: https://github.com/termcolor/termcolor
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
export TERM=xterm
%pyproject_run_pytest -ra

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1.1
- Demodernized packaging.

* Thu Feb 05 2026 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- 3.2.0 -> 3.3.0.

* Mon Oct 27 2025 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 3.1.0 -> 3.2.0.

* Wed May 21 2025 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 3.0.1 -> 3.1.0.

* Fri Apr 04 2025 Stanislav Levin <slev@altlinux.org> 3.0.1-alt1
- 3.0.0 -> 3.0.1.

* Tue Apr 01 2025 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.5.0 -> 3.0.0.

* Mon Oct 07 2024 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- 2.4.0 -> 2.5.0.

* Fri Mar 01 2024 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0.

* Fri Apr 28 2023 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 1.1.0 -> 2.3.0.

* Wed Jul 14 2021 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt2.git20130510
- Build python3 module only

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20130510
- Initial build for Sisyphus
