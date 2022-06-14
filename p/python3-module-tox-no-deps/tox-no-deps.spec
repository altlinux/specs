%define _unpackaged_files_terminate_build 1
%define oname tox-no-deps

%def_with check

Name: python3-module-%oname
Version: 0.2.0
Release: alt1

Summary: Tox plugin for skipping the installation of all deps and extras
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-no-deps/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %oname

%description
This plugin skips the installation of all deps and extras of all the Tox
environments. The dependencies of tested package if any are not touched.

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
export TOX_TESTENV_PASSENV='PIP_NO_INDEX'

tox.py3 --sitepackages --console-scripts -vvr -- -vra

%files
%python3_sitelibdir/tox_no_deps/
%python3_sitelibdir/tox_no_deps-%version-py%_python3_version.egg-info/

%changelog
* Tue Jun 14 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- 0.1 -> 0.2.0.

* Sat Mar 27 2021 Stanislav Levin <slev@altlinux.org> 0.1-alt1
- Initial build for Sisyphus.
