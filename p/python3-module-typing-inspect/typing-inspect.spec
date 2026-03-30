%define _unpackaged_files_terminate_build 1
%define pypi_name typing-inspect

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1.1
Summary: Runtime inspection of types defined in typing module
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/typing-inspect/
Vcs: https://github.com/ilevkivskyi/typing_inspect
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-flake8
BuildRequires: python3-module-mypy-extensions
BuildRequires: python3-module-pytest
BuildRequires: python3-module-typing-extensions
%endif

%description
The typing_inspect module defines experimental API for runtime inspection of
types defined in the Python standard typing module. Works with typing version
3.7.4 and later.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.md
%python3_sitelibdir/typing_inspect.py
%python3_sitelibdir/__pycache__/typing_inspect.cpython-*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1.1
- Demodernized packaging.

* Thu May 25 2023 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.0 -> 0.9.0.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.6.0 -> 0.8.0.

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.

