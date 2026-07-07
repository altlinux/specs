%define _unpackaged_files_terminate_build 1
%define pypi_name pdoc
%define module_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 16.0.0
Release: alt1

Summary: API Documentation for Python Projects
License: MIT-0
Group: Development/Python3
Url: https://pypi.org/project/pdoc/
Vcs: https://github.com/mitmproxy/pdoc/
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

Conflicts: python3-module-pdoc3

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: node
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

# Do not provide python3(pdoc) to avoid duplicate provides with
# python3-module-pdoc3
AutoProv: yes, nopython3

%description
API Documentation for Python Projects.

pdoc's main feature is a focus on simplicity: pdoc aims to do one thing
and do it well.
- Documentation is plain Markdown.
- First-class support for type annotations and all other modern Python3
  features.
- Builtin web server with live reloading.
- Customizable HTML templates.
- Understands numpydoc and Google-style docstrings.
- Standalone HTML output without additional dependencies.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%_bindir/%pypi_name

%changelog
* Tue Jul 07 2026 Andrey Kuzma <kuzmaav@altlinux.org> 16.0.0-alt1
- Initial build for Sisyphus.
