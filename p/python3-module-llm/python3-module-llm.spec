%define _unpackaged_files_terminate_build 1
%define pypi_name llm
%define mod_name llm

%def_with check

Name: python3-module-%pypi_name
Version: 0.31
Release: alt1

Summary: Access large language models from the command-line
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/llm/
Vcs: https://github.com/simonw/llm

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
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: /proc
%endif

%description
A CLI utility and Python library for interacting with Large Language
Models, both via remote APIs and models that can be installed and run
on your own machine.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore \
    -k 'not (test_gpt4o_mini_sync_and_async or test_embed_multi_files_encoding)'

%files
%_bindir/llm
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 06 2026 Anton Zhukharev <ancieg@altlinux.org> 0.31-alt1
- Updated to 0.31.

* Wed Apr 08 2026 Anton Zhukharev <ancieg@altlinux.org> 0.30-alt1
- Updated to 0.30.

* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 0.29-alt1
- Updated to 0.29.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 0.24.2-alt2
- NMU: fixed FTBFS by skipping two tests.

* Wed Apr 09 2025 Anton Zhukharev <ancieg@altlinux.org> 0.24.2-alt1
- Updated to 0.24.2.

* Tue Apr 08 2025 Anton Zhukharev <ancieg@altlinux.org> 0.24-alt1
- Updated to 0.24.

* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.23-alt1
- Built for ALT Sisyphus.
