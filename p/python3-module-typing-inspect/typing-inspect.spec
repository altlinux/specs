%define _unpackaged_files_terminate_build 1
%define pypi_name typing-inspect

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.0
Release: alt1

Summary: Runtime inspection of types defined in typing module
License: MIT
Group: Development/Python3
# Source-git: https://github.com/ilevkivskyi/typing_inspect.git
Url: https://pypi.org/project/typing-inspect/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# runtime deps
BuildRequires: python3(mypy_extensions)
BuildRequires: python3(typing_extensions)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

# PyPI name(dash, underscore)
%py3_provides %pypi_name

# nested import
%py3_requires typing_extensions

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
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/typing_inspect.py
%python3_sitelibdir/__pycache__/typing_inspect.cpython-*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.6.0 -> 0.8.0.

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.

