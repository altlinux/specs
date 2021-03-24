%define _unpackaged_files_terminate_build 1
%define oname tox-console-scripts

%def_with check

Name: python3-module-%oname
Version: 0.2
Release: alt1

Summary: Tox plugin for installation of console scripts for system site packages
License: MIT
Group: Development/Python3
Url: https://github.com/stanislavlevin/tox-console-scripts.git

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
%endif

BuildArch: noarch

%description
It's possible to use system site packages within Python virtual environment,
but there is no way to install console or gui scripts into such environment.

With the help of this plugin the corresponding scripts will be automatically
generated for system site packages calculated as dependencies of current
environment.

%prep
%setup
%autopatch -p1

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
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

tox.py3 --sitepackages -vvr

%files
%python3_sitelibdir/tox_console_scripts/
%python3_sitelibdir/tox_console_scripts-%version-py%_python3_version.egg-info/

%changelog
* Wed Mar 10 2021 Stanislav Levin <slev@altlinux.org> 0.2-alt1
- 0.1 -> 0.2.

* Wed Dec 30 2020 Stanislav Levin <slev@altlinux.org> 0.1-alt1
- Initial build.
