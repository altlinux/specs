%define pypi_name myst-parser
%define mod_name myst_parser

%def_with check

Name: python3-module-%pypi_name
Version: 5.0.0
Release: alt1
Summary: An extended commonmark compliant parser, with bridges to docutils/sphinx
License: MIT
Group: Development/Python3
Url: https://myst-parser.readthedocs.io/
Vcs: https://github.com/executablebooks/MyST-Parser

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-coverage
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-docutils
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-markdown-it-py
BuildRequires: python3-module-mdit-py-plugins
BuildRequires: python3-module-pygments
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-param-files
BuildRequires: python3-module-pytest-regressions
BuildRequires: python3-module-pyyaml
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx-pytest
BuildRequires: python3-module-linkify-it-py
BuildRequires: python3-module-sphinx-tests
BuildRequires: python3-module-packaging
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
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra --ignore tests/test_renderers \
                          --ignore tests/test_sphinx

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %pypi_name
%_bindir/myst-*

%changelog
* Wed Feb 04 2026 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Sat May 31 2025 Andrey Limachko <liannnix@altlinux.org> 4.0.1-alt2
- fixed FTBFS
- spec: exclude sphynx tests
- spec: exclude renderers tests

* Wed Feb 19 2025 Stanislav Levin <slev@altlinux.org> 4.0.1-alt1
- 4.0.0 -> 4.0.1.

* Wed Nov 13 2024 Andrey Limachko <liannnix@altlinux.org> 4.0.0-alt2
- NMU: fixed FTBFS.

* Mon Sep 02 2024 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- 2.0.0 -> 4.0.0.

* Wed Apr 24 2024 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2.1
- NMU: fixed FTBFS (rpm-build-pyproject 0.0.5).

* Fri Jan 26 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt2
- NMU: fixed FTBFS.

* Sun Jul 09 2023 Andrey Limachko <liannnix@altlinux.org> 2.0.0-alt1
- 2.0.0

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.2-alt1
- Initial build for ALT.
