%define _unpackaged_files_terminate_build 1

%define oname beartype

%def_with check

Name: python3-module-%oname
Version: 0.19.0
Release: alt1

Summary: Unbearably fast near-real-time hybrid runtime-static type-checking in pure Python.
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
%pyproject_builddeps_metadata_extra test
%endif

%description
Beartype is an open-source pure-Python PEP-compliant near-real-time hybrid
runtime-static third-generation type checker emphasizing efficiency, usability,
unsubstantiated jargon we just made up, and thrilling puns.

%prep
%setup
%pyproject_deps_resync_build

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -k 'not test_is_hint_pep593_beartype'

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Mon Feb 17 2025 Dmitry Lyalyaev <fruktime@altlinux.org> 0.19.0-alt1
- 0.18.5 -> 0.19.0

* Fri Sep 06 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 0.18.5-alt2
- fix URL address in spec file

* Wed Jun 19 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 0.18.5-alt1
- Initial build for ALT Linux
