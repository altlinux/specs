%define _unpackaged_files_terminate_build 1
%define pypi_name pcre2

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt2

Summary: Python bindings for the PCRE2 library created by Philip Hazel
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/pcre2/
Vcs: https://github.com/grtetrault/pcre2.py

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: python3-module-pcre2-0.3.0-alt-use-bare-cython.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libpcre2-devel

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/test-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 28 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt2
- Cleaned up the package content.

* Thu Sep 28 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- Built for ALT Sisyphus.

