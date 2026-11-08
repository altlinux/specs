Name: python3-module-py-rust-stemmers
Version: 0.1.8
Release: alt1

Summary: Python wrapper around the rust-stemmers library
License: MIT
Group: Development/Python
URL: https://pypi.org/project/py-rust-stemmers
VCS: https://github.com/qdrant/py-rust-stemmers

Source0: %name-%version.tar
Source1: pyproject_deps.json
Source2: crates.tar

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
%summary

%prep
%setup -a2
%ifdef bootstrap
cargo vendor
tar cf %SOURCE2 .cargo vendor
%endif
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/py_rust_stemmers
%python3_sitelibdir/py_rust_stemmers-%version.dist-info

%changelog
* Sat Nov 07 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.8-alt1
- 0.1.8 released

