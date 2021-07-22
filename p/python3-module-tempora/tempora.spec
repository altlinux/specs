%define _unpackaged_files_terminate_build 1
%define modulename tempora

%def_with check

Name: python3-module-%modulename
Version: 4.1.1
Release: alt1

Summary: Objects and routines pertaining to date and time (tempora)
License: MIT
Group: Development/Python3
Url: https://github.com/jaraco/tempora

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(toml)

%if_with check
# install_requires:
BuildRequires: python3(pytz)
BuildRequires: python3(jaraco.functools)

BuildRequires: python3(freezegun)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_freezegun)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Objects and routines pertaining to date and time (tempora).

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/%modulename/tests/

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false

%files
%_bindir/calc-prorate
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info/

%changelog
* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 1.12 -> 4.1.1.
- Enabled testing.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.12-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.11-alt1
- Initial build for Sisyphus
