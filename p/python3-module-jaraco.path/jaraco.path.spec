%define _unpackaged_files_terminate_build 1
%define oname jaraco.path

%def_with check

Name: python3-module-%oname
Version: 3.3.1
Release: alt1

Summary: Cross platform hidden file detection
License: MIT
Group: Development/Python3
# Source-git: https://github.com/jaraco/jaraco.path.git
Url: https://pypi.org/project/jaraco.path/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(toml)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%py3_provides %oname

%description
%oname provides cross platform hidden file detection.

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
tox.py3 --sitepackages --console-scripts --no-deps -vvr -- -vra

%files
%doc README.rst
%python3_sitelibdir/jaraco/__pycache__/path.cpython-*.py*
%python3_sitelibdir/jaraco/path.py
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- Initial build for Sisyphus.
