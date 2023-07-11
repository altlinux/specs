%define _unpackaged_files_terminate_build 1

%define oname markdown-it
%define mname markdown_it
%define pypi_name markdown-it-py

%def_with check

Name: python3-module-%oname
Version: 3.0.0
Release: alt1
Summary: Python port of markdown-it. Markdown parsing, done right!
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/markdown-it-py/
Vcs: https://github.com/executablebooks/markdown-it-py
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra testing
%pyproject_builddeps_metadata_extra linkify
%endif

Provides: python3-module-%pypi_name = %EVR

%description
Markdown parser done right.

* Follows the CommonMark spec for baseline parsing
* Configurable syntax: you can add new rules and even replace existing ones.
* Pluggable: Adds syntax extensions to extend the parser (see the plugin list).
* High speed (see our benchmarking tests)
* Safe by default

This is a Python port of markdown-it, and some of its associated plugins.
For more details see: https://markdown-it-py.readthedocs.io.

%package -n %oname
Summary: Python port of markdown-it. Markdown parsing, done right!
Group: Development/Python3
Requires: %name = %EVR

%description -n %oname
Markdown parser done right.

* Follows the CommonMark spec for baseline parsing
* Configurable syntax: you can add new rules and even replace existing ones.
* Pluggable: Adds syntax extensions to extend the parser (see the plugin list).
* High speed (see our benchmarking tests)
* Safe by default

This is a Python port of markdown-it, and some of its associated plugins.
For more details see: https://markdown-it-py.readthedocs.io.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject
%pyproject_run_pytest -ra tests

%files
%doc README.md
%python3_sitelibdir/%mname/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n %oname
%_bindir/%oname

%changelog
* Tue Jul 11 2023 Andrey Limachko <liannnix@altlinux.org> 3.0.0-alt1
- 2.2.0 -> 3.0.0.

* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 1.1.0 -> 2.2.0.

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Initial build for ALT.
