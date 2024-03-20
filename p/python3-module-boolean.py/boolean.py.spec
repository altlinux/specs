%define _unpackaged_files_terminate_build 1
%define pypi_name boolean.py

%def_with check

Name: python3-module-%pypi_name
Version: 4.0
Release: alt2
Summary: Define boolean algebras, create and parse boolean expressions and create custom boolean DSL
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/boolean.py
VCS: https://github.com/bastikr/boolean.py.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This library helps you deal with boolean expressions and algebra with variables
and the boolean functions AND, OR, NOT.

You can parse expressions from strings and simplify and compare expressions. You
can also easily create your custom algreba and mini DSL and create custom
tokenizers to handle custom expressions.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

# don't ship tests
rm %buildroot%python3_sitelibdir/boolean/test_boolean.py

%check
%pyproject_run_pytest -ra boolean

%files
%doc README.rst
%python3_sitelibdir/boolean/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Mar 20 2024 Stanislav Levin <slev@altlinux.org> 4.0-alt2
- Mapped PyPI name to distro's one.

* Wed Oct 05 2022 Stanislav Levin <slev@altlinux.org> 4.0-alt1
- Initial build for Sisyphus.
