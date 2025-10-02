Name: python3-module-abi3audit
Version: 0.0.22
Release: alt1

Summary: Python abi3 consistency scanner
License: MIT
Group: Development/Python
Url: https://pypi.org/project/abi3audit/
VCS: https://github.com/pypa/abi3audit

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_runtimedeps_metadata

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# tests are mostly online
%pyproject_run_pytest test ||:

%files
%_bindir/abi3audit
%python3_sitelibdir/abi3audit
%python3_sitelibdir/abi3audit-%version.dist-info

%changelog
* Thu Oct 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.22-alt1
- initial

