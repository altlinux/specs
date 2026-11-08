Name: python3-module-pdfplumber
Version: 0.11.10
Release: alt1

Summary: Plumb a PDF for detailed information about each char, rectangle, and line
License: MIT
Group: Development/Python
URL: https://pypi.org/project/pdfplumber
VCS: https://github.com/jsvine/pdfplumber

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%ifnarch aarch64 x86_64
%add_pyproject_deps_runtime_filter '^pypdfium2$'
%endif
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%ifnarch aarch64 x86_64
%add_pyproject_deps_build_filter '^pypdfium2$'
%add_pyproject_deps_check_filter '^pypdfium2$'
%endif
%pyproject_builddeps_build
%pyproject_builddeps_metadata
# dev tools from requirements-dev.txt that are not needed to run the tests
%add_pyproject_deps_check_filter '^jupyterlab$'
%add_pyproject_deps_check_filter '^nbexec$'
%add_pyproject_deps_check_filter '^pandas-stubs$'
%add_pyproject_deps_check_filter '^py$'
%add_pyproject_deps_check_filter '^types-pillow$'
%pyproject_builddeps_check
# tests/test_repair.py shells out to Ghostscript
BuildRequires: ghostscript

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt

%build
%pyproject_build

%install
%pyproject_install

%check
# upstream addopts force coverage reporting; keep the test run plain
%pyproject_run_pytest -o addopts= \
%ifnarch aarch64 x86_64
||:
%endif

%files
%_bindir/pdfplumber
%python3_sitelibdir/pdfplumber
%python3_sitelibdir/pdfplumber-%version.dist-info

%changelog
* Sat Nov 07 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.11.10-alt1
- initial
