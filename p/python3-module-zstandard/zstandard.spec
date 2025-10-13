Name: python3-module-zstandard
Version: 0.25.0
Release: alt1

Summary: Python bindings for zstandard compression library
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/zstandard/
VCS: https://github.com/indygreg/python-zstandard

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildRequires(pre): rpm-build-pyproject
#BuildRequires: pkgconfig(libzstd) 1.5.5 too old
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
rm -r zstandard
%pyproject_run_pytest

%files
%python3_sitelibdir/zstandard
%python3_sitelibdir/zstandard-%version.dist-info

%changelog
* Mon Oct 06 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.25.0-alt1
- 0.25.0 released

* Wed May 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21.0-alt1
- 0.21.0 released

* Wed Dec 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.0-alt1
- initial
