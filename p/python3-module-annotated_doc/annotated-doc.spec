%define _unpackaged_files_terminate_build 1
%define pypi_name annotated-doc
%define module_name annotated_doc
%def_with check

Name: python3-module-%module_name
Version: 0.0.6
Release: alt1

Summary: Document parameters, class attributes, return types, and variables inline, with Annotated
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/annotated-doc/
Vcs: https://github.com/fastapi/annotated-doc
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
BuildRequires: python3-module-pytest-timeout
%endif
%pyproject_configure_pypi_package

%description
Document parameters, class attributes, return types, and variables
inline, with Annotated.

Reasons to use annotated-doc:
* No micro-syntax to learn for newcomers, it's just Python syntax.
* Editing would be already fully supported by default by any editor
  (current or future) supporting Python syntax, including syntax
  errors, syntax highlighting, etc.
* Rendering would be relatively straightforward to implement by static
  tools (tools that don't need runtime execution), as the information
  can be extracted from the AST they normally already create.
* Deduplication of information: the name of a parameter would be
  defined in a single place, not duplicated inside of a docstring.
* Elimination of the possibility of having inconsistencies when
  removing a parameter or class variable and forgetting to remove its
  documentation.
* Minimization of the probability of adding a new parameter or class
  variable and forgetting to add its documentation.
* Elimination of the possibility of having inconsistencies between the
  name of a parameter in the signature and the name in the docstring
  when it is renamed.
* Access to the documentation string for each symbol at runtime,
  including existing (older) Python versions.
* A more formalized way to document other symbols, like type aliases,
  that could use Annotated.
* Support for apps using FastAPI, Typer and others.
* AI Accessibility: AI tools will have an easier way understanding each
  parameter as the distance from documentation to parameter is much
  closer.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --session-timeout=600

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.6-alt1
- Updated to 0.0.6.

* Tue Jul 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.5-alt1
- Updated to 0.0.5.

* Sat Nov 29 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.4-alt1
- Initial build for ALT Sisyphus.
