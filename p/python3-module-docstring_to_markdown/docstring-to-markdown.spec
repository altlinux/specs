%define _unpackaged_files_terminate_build 1
%define pypi_name docstring-to-markdown
%define mod_name docstring_to_markdown

%def_with check

Name: python3-module-%mod_name
Version: 0.12
Release: alt1
Summary: On the fly conversion of Python docstrings to markdown
License: LGPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/docstring-to-markdown/
Vcs: https://github.com/python-lsp/docstring-to-markdown
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
On the fly conversion of Python docstrings to markdown.
It can recognise reStructuredText and convert multiple
of its features to Markdown.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -o=addopts=-Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 17 2023 Stanislav Levin <slev@altlinux.org> 0.12-alt1
- 0.11 -> 0.12.

* Sat Dec 10 2022 Ivan A. Melnikov <iv@altlinux.org> 0.11-alt1
- Initial build for Sisyphus
