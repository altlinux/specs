%define _unpackaged_files_terminate_build 1
%define oname jaraco.envs

%def_with check

Name: python3-module-%oname
Version: 2.3.0
Release: alt1

Summary: Classes for orchestrating Python virtual environments
License: MIT
Group: Development/Python3
# Source-git: https://github.com/jaraco/jaraco.envs.git
Url: https://pypi.org/project/jaraco.envs/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
# dependencies=
BuildRequires: python3(path)
BuildRequires: python3(virtualenv)
BuildRequires: python3(tox)

BuildRequires: python3(pytest)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

BuildArch: noarch

%py3_provides %oname
%py3_requires virtualenv
%py3_requires tox

%description
%oname provides classes for orchestrating Python virtual environments.

%prep
%setup
%autopatch -p1

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
git init
git config user.email author@example.com
git config user.name author
git add .
git commit -m 'release'
git tag '%version'

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr --develop -- -vra

%files
%doc README.rst
%python3_sitelibdir/jaraco/__pycache__/envs.cpython-*.py*
%python3_sitelibdir/jaraco/envs.py
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.2.0 -> 2.3.0.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.1 -> 2.2.0.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus.
