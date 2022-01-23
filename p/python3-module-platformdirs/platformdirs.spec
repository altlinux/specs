%define _unpackaged_files_terminate_build 1
%define oname platformdirs

%def_with check

Name: python3-module-%oname
Version: 2.4.1
Release: alt1

Summary: Determining appropriate platform-specific dirs
License: MIT
Group: Development/Python3
# Source-git: https://github.com/platformdirs/platformdirs.git
Url: https://pypi.org/project/platformdirs

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(toml)

%if_with check
BuildRequires: python3(appdirs)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
A small Python module for determining appropriate platform-specific dirs, e.g.
a "user data dir". When writing desktop application, finding the right location
to store user data and configuration varies per platform. Even for
single-platform apps, there may by plenty of nuances in figuring out the right
location.

%prep
%setup
%autopatch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false -- tests

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Jan 13 2022 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1.

* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0.

* Tue Sep 07 2021 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.1.0 -> 2.3.0.

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus.
