%define _unpackaged_files_terminate_build 1
%define pypi_name sdjson
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt1

Summary: Custom JSON Encoder for Python utilising functools.singledispatch to support custom encoders for both Python's built-in classes and user-created classes, without as much legwork
License: MIT
Group: Development/Python3
Url: https://pypi.org/projects/sdjson/
Vcs: https://github.com/domdfcoding/singledispatch-json

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
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# tests/test_protocols.py is broken for Python 3.11.
%pyproject_run_pytest -vra -k "not test_protocols.py"

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 0.5.0-alt1
- Updated to 0.5.0.

* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt2
- Fixed FTBFS.

* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- 0.3.1 -> 0.4.0
- use python3(whey) to build the package
- enable tests

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt1
- initial build for Sisyphus

