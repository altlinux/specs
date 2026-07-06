%define _unpackaged_files_terminate_build 1
%define pypi_name openai
%define mod_name openai

# check requires the Internet connection
%def_without check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 2.44.0
Release: alt1

Summary: The official Python library for the OpenAI API
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/openai/
Vcs: https://github.com/openai/openai-python

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%add_pyproject_deps_runtime_filter pandas-stubs
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pandas-stubs
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The OpenAI Python library provides convenient access to the
OpenAI REST API from any Python 3.8+ application. The library includes
type definitions for all request params and response fields, and
offers both synchronous and asynchronous clients powered by httpx.

%add_python_extra aiohttp
%add_python_extra datalib
%add_python_extra realtime
%add_python_extra voice-helpers

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.lock
%endif

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
* Mon Jul 06 2026 Anton Zhukharev <ancieg@altlinux.org> 2.44.0-alt1
- Updated to 2.44.0.

* Thu Mar 26 2026 Anton Zhukharev <ancieg@altlinux.org> 2.30.0-alt1
- Updated to 2.30.0.

* Thu Mar 19 2026 Anton Zhukharev <ancieg@altlinux.org> 2.29.0-alt1
- Updated to 2.29.0.

* Tue Jun 24 2025 Anton Zhukharev <ancieg@altlinux.org> 1.91.0-alt1
- Updated to 1.91.0.

* Thu Apr 24 2025 Anton Zhukharev <ancieg@altlinux.org> 1.76.0-alt1
- Updated to 1.76.0.

* Wed Apr 09 2025 Anton Zhukharev <ancieg@altlinux.org> 1.72.0-alt1
- Updated to 1.72.0.

* Tue Apr 08 2025 Anton Zhukharev <ancieg@altlinux.org> 1.71.0-alt1
- Updated to 1.71.0.

* Tue Apr 01 2025 Anton Zhukharev <ancieg@altlinux.org> 1.70.0-alt1
- Updated to 1.70.0.

* Fri Mar 28 2025 Anton Zhukharev <ancieg@altlinux.org> 1.69.0-alt1
- Updated to 1.69.0.

* Mon Mar 24 2025 Anton Zhukharev <ancieg@altlinux.org> 1.68.2-alt1
- Updated to 1.68.2.

* Fri Mar 21 2025 Anton Zhukharev <ancieg@altlinux.org> 1.68.0-alt1
- Updated to 1.68.0.

* Fri Mar 14 2025 Anton Zhukharev <ancieg@altlinux.org> 1.66.3-alt1
- Updated to 1.66.3.

* Wed Mar 12 2025 Anton Zhukharev <ancieg@altlinux.org> 1.66.2-alt1
- Updated to 1.66.2.

* Mon Mar 10 2025 Anton Zhukharev <ancieg@altlinux.org> 1.65.5-alt1
- Updated to 1.65.5.

* Sun Mar 09 2025 Anton Zhukharev <ancieg@altlinux.org> 1.65.4-alt1
- Updated to 1.65.4.

* Wed Mar 05 2025 Anton Zhukharev <ancieg@altlinux.org> 1.65.3-alt1
- Updated to 1.65.3.

* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 1.65.2-alt1
- Built for ALT Sisyphus.
