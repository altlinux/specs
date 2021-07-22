%define _unpackaged_files_terminate_build 1
%define oname mergedeep

%def_with check

Name: python3-module-%oname
Version: 1.3.4
Release: alt1

Summary: Deep merge function
License: MIT
Group: Development/Python3
# Source-git: https://github.com/clarketm/mergedeep.git
Url: https://pypi.org/project/mergedeep/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
Deep merge function.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

# don't package tests
rm %buildroot%python3_sitelibdir/%oname/test_mergedeep.py

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 1.3.4-alt1
- Initial build.
