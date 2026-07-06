%define _unpackaged_files_terminate_build 1
%define pypi_name llm-ollama
%define mod_name llm_ollama

%def_with check

Name: python3-module-%pypi_name
Version: 0.16.1
Release: alt1

Summary:  LLM plugin providing access to models running on an Ollama server
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/llm-ollama/
Vcs: https://github.com/taketwo/llm-ollama

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 06 2026 Anton Zhukharev <ancieg@altlinux.org> 0.16.1-alt1
- Updated to 0.16.1.

* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 0.15.1-alt1
- Updated to 0.15.1.

* Mon Mar 10 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1.

* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- Built for ALT Sisyphus.
