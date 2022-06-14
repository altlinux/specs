%define _unpackaged_files_terminate_build 1
%define oname tox-console-scripts

%def_with check

Name: python3-module-%oname
Version: 0.3.2
Release: alt1

Summary: Tox plugin for installation of console scripts for system site packages
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-console-scripts/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
%endif

%py3_provides %oname

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
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3

tox.py3 --sitepackages -vvr

%files
%python3_sitelibdir/tox_console_scripts/
%python3_sitelibdir/tox_console_scripts-%version-py%_python3_version.egg-info/

%changelog
* Fri Jun 10 2022 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1
- 0.2 -> 0.3.2.

* Wed Mar 10 2021 Stanislav Levin <slev@altlinux.org> 0.2-alt1
- 0.1 -> 0.2.

* Wed Dec 30 2020 Stanislav Levin <slev@altlinux.org> 0.1-alt1
- Initial build.
