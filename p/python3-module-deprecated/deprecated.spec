%define _unpackaged_files_terminate_build 1
%define oname deprecated

%def_with check

Name: python3-module-%oname
Version: 1.2.12
Release: alt1

Summary: Decorators to deprecate old python classes, functions or methods
License: MIT
Group: Development/Python3
# Source-git: https://github.com/tantale/deprecated.git
Url: https://pypi.org/project/Deprecated/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires
BuildRequires: python3(wrapt)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

# PyPI's name begins with capital letter
%py3_provides Deprecated

%description
Python @deprecated decorator to deprecate old python classes, functions or
methods.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false

%files
%doc README.md CHANGELOG.rst
%python3_sitelibdir/deprecated/
%python3_sitelibdir/Deprecated-%version-py%_python3_version.egg-info/

%changelog
* Tue Jun 22 2021 Stanislav Levin <slev@altlinux.org> 1.2.12-alt1
- Initial build for Sisyphus.
