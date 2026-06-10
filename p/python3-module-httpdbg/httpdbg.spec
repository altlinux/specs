%define _unpackaged_files_terminate_build 1
%define pypi_name httpdbg
%define module_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.7
Release: alt1

Summary: Tool to trace the HTTP(S) client requests in python code
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/httpdbg
Vcs: https://github.com/cle-b/httpdbg

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

Provides: httpdbg = %EVR
Obsoletes: httpdbg < %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-uvicorn
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A very simple tool to debug HTTP(S) client and server request.

%prep
%setup
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
# tests/ui
# Ignore this directory since required browser
# (chrome/firefox or other) inside hasher
%pyproject_run_pytest --ignore="tests/ui"

%files
%doc README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%_bindir/pyhttpdbg

%changelog
* Wed May 06 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.1.7-alt1
- Updated to new version v2.1.7.

* Wed Apr 01 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.1.6-alt1
- Updated to new version v2.1.6.

* Thu Feb 19 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.1.5-alt1
- Updated to new version v2.1.5.

* Mon Dec 29 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.0.0-alt1
- Updated to new version v2.0.0.

* Sun Apr 27 2025 Maxim Tulskiy <tulskijms@altlinux.org> 1.2.1-alt1
- Initial build for ALT Sisyphus.
