%define _unpackaged_files_terminate_build 1
%define pypi_name configupdater

%def_with check

Name: python3-module-%pypi_name
Version: 3.1
Release: alt1

Summary: Parser like ConfigParser but for updating configuration files
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pyscaffold/configupdater.git
Url: https://pypi.org/project/configupdater

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

BuildArch: noarch

%description
The sole purpose of ConfigUpdater is to easily update an INI config file with no
changes to the original file except the intended ones. This means comments, the
ordering of sections and key/value-pairs as wells as their cases are kept as in
the original file. Thus ConfigUpdater provides complementary functionality to
Python's ConfigParser which is primarily meant for reading config files and
writing new ones.

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
export TOXENV=py3-all
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false --develop

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/ConfigUpdater-%version-py%_python3_version.egg-info/

%changelog
* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 3.1-alt1
- Initial build for Sisyphus.
