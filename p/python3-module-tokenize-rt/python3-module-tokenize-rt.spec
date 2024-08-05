%define _unpackaged_files_terminate_build 1
%define pypi_name tokenize-rt
%define mod_name tokenize_rt

%def_with check

Name: python3-module-%pypi_name
Version: 6.0.0
Release: alt1

Summary: A wrapper around the stdlib `tokenize` which roundtrips
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tokenize-rt/
Vcs: https://github.com/asottile/tokenize-rt

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The stdlib tokenize module does not properly roundtrip. This wrapper
around the stdlib provides two additional tokens ESCAPED_NL and
UNIMPORTANT_WS, and a Token data type. Use src_to_tokens and
tokens_to_src to roundtrip.

This library is useful if you're writing a refactoring tool based on
the python tokenization.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 05 2024 Anton Zhukharev <ancieg@altlinux.org> 6.0.0-alt1
- Updated to 6.0.0.

* Tue Aug 01 2023 Anton Zhukharev <ancieg@altlinux.org> 5.2.0-alt1
- Updated to 5.2.0.

* Wed Jul 26 2023 Anton Zhukharev <ancieg@altlinux.org> 5.1.0-alt1
- Updated to 5.1.0.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 5.0.0-alt1
- 4.2.1 -> 5.5.0

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 4.2.1-alt1
- initial build for Sisyphus

