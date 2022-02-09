%define _unpackaged_files_terminate_build 1
%define pypi_name pip-run

%def_with check

Name: python3-module-%pypi_name
Version: 8.8.0
Release: alt1

Summary: Install packages and run Python with them
License: MIT
Group: Development/Python3
# Source-git: https://github.com/jaraco/pip-run.git
Url: https://pypi.org/project/pip-run

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires=
BuildRequires: python3(pip)
BuildRequires: python3(autocommand)
BuildRequires: python3(path)
BuildRequires: python3(packaging)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(nbformat)
BuildRequires: python3(pygments)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

# hidden with `sys.executable -m pip`
%py3_requires pip

%description
pip-run provides on-demand temporary package installation for a single
interpreter run.

%prep
%setup
%autopatch -p1

%build
# https://github.com/pypa/setuptools_scm/#environment-variables
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export NO_INTERNET=YES
export TOXENV=py3
export TOX_TESTENV_PASSENV='NO_INTERNET'
tox.py3 --sitepackages --no-deps --console-scripts -vvr -s false

%files
%doc README.rst
%_bindir/pip-run
%python3_sitelibdir/pip-run.py
%python3_sitelibdir/__pycache__/pip-run.*
%python3_sitelibdir/pip_run/
%python3_sitelibdir/pip_run-%version-py%_python3_version.egg-info/

%changelog
* Tue Feb 08 2022 Stanislav Levin <slev@altlinux.org> 8.8.0-alt1
- Initial build for Sisyphus.
