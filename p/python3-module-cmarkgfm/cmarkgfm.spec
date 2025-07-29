%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-cmarkgfm
Version: 2024.11.20
Release: alt1

Summary: Python bindings for GitHub's cmark
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/cmarkgfm/
Vcs: https://github.com/theacodes/cmarkgfm.git

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source100: %name-%version-third_party-cmark.tar
%pyproject_runtimedeps_metadata

Requires: libcmark-gfm-devel

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Minimalist Python bindings to GitHub's fork of cmark.

%prep
%setup -a100
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.txt
%python3_sitelibdir/cmarkgfm/
%python3_sitelibdir/cmarkgfm-%version.dist-info/
# Build script.
%exclude %python3_sitelibdir/cmarkgfm/build_cmark.py

%changelog
* Tue Jul 22 2025 Sergey Zhidkih <rx1513@altlinux.org> 2024.11.20-alt1
- Initial build.
