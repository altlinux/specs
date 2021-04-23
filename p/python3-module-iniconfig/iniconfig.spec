%define _unpackaged_files_terminate_build 1
%define oname iniconfig

%def_with check

Name: python3-module-%oname
Version: 1.1.1
Release: alt1

Summary: A small and simple INI-file parser
License: MIT
Group: Development/Tools
# Source-git: https://github.com/RonnyPfannschmidt/iniconfig.git
Url: https://pypi.org/project/iniconfig/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
%summary

%prep
%setup
%patch -p1

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
export TOX_TESTENV_PASSENV='SETUPTOOLS_SCM_PRETEND_VERSION'
export TOXENV=py3

tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc CHANGELOG LICENSE README.txt
%python3_sitelibdir/iniconfig/
%python3_sitelibdir/iniconfig-%version-py%_python3_version.egg-info/

%changelog
* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.0 -> 1.1.1.
- Built Python3 package from its ows src.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- Fixed testing against Pytest 5.

* Sat Mar 16 2019 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build.

