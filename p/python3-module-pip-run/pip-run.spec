%define _unpackaged_files_terminate_build 1
%define pypi_name pip-run

%def_with check

Name: python3-module-%pypi_name
Version: 8.8.2
Release: alt1

Summary: Install packages and run Python with them
License: MIT
Group: Development/Python3
# Source-git: https://github.com/jaraco/pip-run.git
Url: https://pypi.org/project/pip-run

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires=
BuildRequires: python3(pip)
BuildRequires: python3(autocommand)
BuildRequires: python3(path)
BuildRequires: python3(packaging)

BuildRequires: python3(pytest)
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

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

rm -r %buildroot%python3_sitelibdir/pip_run/tests/

%check
%tox_check_pyproject

%files
%doc README.rst
%_bindir/pip-run
%python3_sitelibdir/pip-run.py
%python3_sitelibdir/__pycache__/pip-run.*
%python3_sitelibdir/pip_run/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 21 2022 Stanislav Levin <slev@altlinux.org> 8.8.2-alt1
- 8.8.1 -> 8.8.2.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 8.8.1-alt1
- 8.8.0 -> 8.8.1.

* Tue Feb 08 2022 Stanislav Levin <slev@altlinux.org> 8.8.0-alt1
- Initial build for Sisyphus.
