%define _unpackaged_files_terminate_build 1
%define oname jaraco.context

%def_with check

Name: python3-module-%oname
Version: 4.1.1
Release: alt1

Summary: Context managers by Jaraco
License: MIT
Group: Development/Python3
# Source-git: https://github.com/jaraco/jaraco.context.git
Url: https://pypi.org/project/jaraco.context/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

BuildArch: noarch

%py3_provides %oname

%description
%oname provides context managers by Jaraco.

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
tox.py3 --sitepackages --console-scripts --no-deps -vvr -- -vra

%files
%doc README.rst
%python3_sitelibdir/jaraco/__pycache__/context.cpython-*.py*
%python3_sitelibdir/jaraco/context.py
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 4.0.0 -> 4.1.1.

* Sat Mar 27 2021 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus.
