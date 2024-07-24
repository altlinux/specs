%define _unpackaged_files_terminate_build 1
%define pypi_name llama-cpp-python
%define mod_name llama_cpp

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.83
Release: alt1

Summary: Python bindings for the llama.cpp library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/llama-cpp-python/
Vcs: https://github.com/abetlen/llama-cpp-python

# libllama archs
ExclusiveArch: x86_64 aarch64

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

Requires: libllama-devel
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra server
BuildRequires: libllama-devel
%endif

%description
Simple Python bindings for @ggerganov's llama.cpp library.
This package provides:

* Low-level access to C API via ctypes interface.
* High-level Python API for text completion
  - OpenAI-like API
  - LangChain compatibility
  - LlamaIndex compatibility
* OpenAI compatible web server
  - Local Copilot replacement
  - Function Calling support
  - Vision API support
  - Multiple Models

Documentation is available at https://llama-cpp-python.readthedocs.io/en/latest.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# move python-module to arch-dependant-directory
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%check
%pyproject_run_pytest -vra

%files
%doc CHANGELOG.md LICENSE.md README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 24 2024 Anton Zhukharev <ancieg@altlinux.org> 0.2.83-alt1
- Built for ALT Sisyphus.

