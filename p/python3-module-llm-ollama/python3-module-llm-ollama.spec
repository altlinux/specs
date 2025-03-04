%define _unpackaged_files_terminate_build 1
%define pypi_name llm-ollama
%define pypi_nname llm-ollama
%define mod_name llm_ollama

%def_with check

Name: python3-module-%pypi_nname
Version: 0.9.0
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
%doc README.md
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- Built for ALT Sisyphus.

