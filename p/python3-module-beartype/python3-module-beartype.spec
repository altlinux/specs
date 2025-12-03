%define _unpackaged_files_terminate_build 1

%define oname beartype

%def_with check

Name: python3-module-%oname
Version: 0.22.8
Release: alt1

Summary: Unbearably fast near-real-time hybrid runtime-static type-checking in pure Python
License: MIT
Group: Development/Python3
Url: https://github.com/beartype/beartype
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
# Not built in Sisyphus.
%add_pyproject_deps_check_filter equinox
%add_pyproject_deps_check_filter fastmcp
%add_pyproject_deps_check_filter jax
%add_pyproject_deps_check_filter nuitka
%add_pyproject_deps_check_filter pandera
%add_pyproject_deps_check_filter polars
# Not built on %ix86 in Sisyphus. Task 395141.
%add_pyproject_deps_check_filter torch

%pyproject_builddeps_metadata_extra test-tox
%endif

%description
Beartype is an open-source pure-Python PEP-compliant near-real-time hybrid
runtime-static third-generation type checker emphasizing efficiency, usability,
unsubstantiated jargon we just made up, and thrilling puns.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# test_poetry uses the Internet
%pyproject_run_pytest -vra -k 'not test_poetry'

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Wed Dec 03 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.22.8-alt1
- 0.19.0 -> 0.22.8

* Mon Feb 17 2025 Dmitry Lyalyaev <fruktime@altlinux.org> 0.19.0-alt1
- 0.18.5 -> 0.19.0

* Fri Sep 06 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 0.18.5-alt2
- fix URL address in spec file

* Wed Jun 19 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 0.18.5-alt1
- Initial build for ALT Linux
