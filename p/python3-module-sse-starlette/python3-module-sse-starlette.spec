%define _unpackaged_files_terminate_build 1
%define pypi_name sse-starlette
%define mod_name sse_starlette

%def_with check

Name: python3-module-%pypi_name
Version: 3.6.0
Release: alt1

Summary: SSE plugin for Starlette
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/sse-starlette/
Vcs: https://github.com/sysid/sse-starlette

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%pyproject_configure_with_check_filter testcontainers
%pyproject_configure_with_check_deps metadata_extra examples
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0

%description
Server Sent Events for Starlette and FastAPI.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
rm -fv tests/{experimentation,integration}/test_multiple_consumers*.py
%pyproject_run_pytest -vra -m "not (integration or e2e)"

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Nov 06 2026 Anton Zhukharev <ancieg@altlinux.org> 3.6.0-alt1
- Updated to 3.6.0.

* Tue Jul 21 2026 Anton Zhukharev <ancieg@altlinux.org> 3.4.6-alt1
- Updated to 3.4.6.

* Tue Mar 31 2026 Anton Zhukharev <ancieg@altlinux.org> 3.3.4-alt1
- Updated to 3.3.4.

* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 3.3.3-alt1
- Updated to 3.3.3.

* Sat Mar 14 2026 Anton Zhukharev <ancieg@altlinux.org> 3.3.2-alt1
- Updated to 3.3.2.

* Thu May 29 2025 Anton Zhukharev <ancieg@altlinux.org> 2.3.5-alt1
- Updated to 2.3.5.

* Mon Mar 10 2025 Anton Zhukharev <ancieg@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1.

* Thu Aug 01 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.3-alt1
- Updated to 2.1.3.

* Thu Jul 25 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.2-alt1
- Updated to 2.1.2.

* Wed Jul 24 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt1
- Built for ALT Sisyphus.
