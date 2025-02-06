%define _unpackaged_files_terminate_build 1
%define pypi_name pcre2

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.2
Release: alt1

Summary: Python bindings for the PCRE2 library created by Philip Hazel
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/pcre2/
Vcs: https://github.com/grtetrault/pcre2.py

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: setup.py
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter scikit-build
%add_pyproject_deps_build_filter cmake
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
%autopatch -p1
install -v %SOURCE2 setup.py
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
* Thu Feb 06 2025 Anton Zhukharev <ancieg@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Thu Apr 25 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Thu Sep 28 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt2
- Cleaned up the package content.

* Thu Sep 28 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- Built for ALT Sisyphus.

