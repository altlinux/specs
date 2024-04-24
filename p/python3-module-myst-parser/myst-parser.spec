%define _unpackaged_files_terminate_build 1

%define pypi_name myst-parser
%define mod_name myst_parser

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt2.1
Summary: An extended commonmark compliant parser, with bridges to docutils/sphinx
License: MIT
Group: Development/Python3
Url: https://myst-parser.readthedocs.io/
Vcs: https://github.com/executablebooks/MyST-Parser

BuildArch: noarch

Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name

# Fix tests broken by recent sphinx releases, up to sphinx v7.2.6
Patch: 4f670fc04c438b57a9d4014be74e9a62cc0deba4.patch

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx-tests
BuildRequires: python3-module-sphinx-pytest
%pyproject_builddeps_metadata_extra testing
%pyproject_builddeps_metadata_extra linkify
%endif

%description
MyST is a rich and extensible flavor of Markdown
meant for technical documentation and publishing.

MyST is a flavor of markdown that is designed for simplicity,
flexibility, and extensibility. This repository serves
as the reference implementation of MyST Markdown, as well
as a collection of tools to support working with MyST in Python and Sphinx.
It contains an extended CommonMark-compliant parser using markdown-it-py,
as well as a Sphinx extension that allows you to write MyST Markdown in Sphinx.

See the MyST Parser documentation for more information.

%package -n %pypi_name
Summary: An extended commonmark compliant parser, with bridges to docutils/sphinx
Group: Development/Python3
Requires: %name = %EVR

%description -n %pypi_name
MyST is a rich and extensible flavor of Markdown
meant for technical documentation and publishing.

MyST is a flavor of markdown that is designed for simplicity,
flexibility, and extensibility. This repository serves
as the reference implementation of MyST Markdown, as well
as a collection of tools to support working with MyST in Python and Sphinx.
It contains an extended CommonMark-compliant parser using markdown-it-py,
as well as a Sphinx extension that allows you to write MyST Markdown in Sphinx.

See the MyST Parser documentation for more information.

%prep
%setup -n %pypi_name-%version
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject
## TODO: fix excluded tests
%pyproject_run_pytest -ra tests --ignore tests/test_sphinx

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %pypi_name
%_bindir/myst-*

%changelog
* Wed Apr 24 2024 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2.1
- NMU: fixed FTBFS (rpm-build-pyproject 0.0.5).

* Fri Jan 26 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- NMU: fixed FTBFS.

* Sun Jul 09 2023 Andrey Limachko <liannnix@altlinux.org> 2.0.0-alt1
- 2.0.0

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.2-alt1
- Initial build for ALT.
