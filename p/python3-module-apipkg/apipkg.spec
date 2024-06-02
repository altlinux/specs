%define oname apipkg

%def_with check

Name:           python3-module-%oname
Version:        3.0.2
Release:        alt1

Summary:        A Python namespace control and lazy-import mechanism

License:        MIT
Group:          Development/Python3
URL:            https://pypi.org/project/apipkg
VCS:            https://github.com/pytest-dev/apipkg

Source:        %name-%version.tar

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%description
With apipkg you can control the exported namespace of a Python package
and greatly reduce the number of imports for your users. It is a small pure
Python module that works on CPython 3.7+, Jython and PyPy. It cooperates well
with Python's help() system, custom importers (PEP302) and common
command-line completion tools.

Usage is very simple: you can require 'apipkg' as a dependency or you can
copy paste the ~200 lines of code into your project.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -k'not test_get_distribution_version'

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun Jun 02 2024 Grigory Ustinov <grenka@altlinux.org> 3.0.2-alt1
- Automatically updated to 3.0.2.

* Thu Jun 15 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt2
- Build with check.

* Fri Dec 02 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Build new version.
- Bootstrap without check.

* Mon Jul 16 2018 Grigory Ustinov <grenka@altlinux.org> 1.5-alt1
- Build new version.

* Tue Jun 19 2018 Grigory Ustinov <grenka@altlinux.org> 1.4-alt3
- Raise release to allow the safe upgrade from "Autoimports/Sisyphus".

* Fri Jun 08 2018 Grigory Ustinov <grenka@altlinux.org> 1.4-alt1
- Initial build for Sisyphus.
