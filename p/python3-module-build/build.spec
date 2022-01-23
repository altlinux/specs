%define _unpackaged_files_terminate_build 1
%define oname build

%def_with check

Name: python3-module-%oname
Version: 0.7.0
Release: alt1

Summary: Simple, correct PEP 517 build frontend
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pypa/build.git
Url: https://pypi.org/project/build

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires:
BuildRequires: python3(packaging)
BuildRequires: python3(pep517)
BuildRequires: python3(tomli)

BuildRequires: python3(pytest)
BuildRequires: python3(pytest_rerunfailures)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

BuildArch: noarch

%description
A simple, correct PEP 517 build frontend.

build will invoke the PEP 517 hooks to build a distribution package. It is a
simple build tool and does not perform any dependency management.

%package -n pyproject-build
Summary: Executable for python-build
Group: Development/Python3
# not autodetected dep
Requires: python3-module-%oname

%description -n pyproject-build
%summary

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
export NO_INTERNET=YES
export TOX_TESTENV_PASSENV='NO_INTERNET'
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%files -n pyproject-build
%_bindir/pyproject-build

%changelog
* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
