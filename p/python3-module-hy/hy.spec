Name: python3-module-hy
Version: 1.3.1
Release: alt1

Summary: Lisp dialect that's embedded in Python
License: MIT
Group: Development/Python
URL: https://pypi.org/project/hy
VCS: https://github.com/hylang/hy

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(test)
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
Hy is a Lisp dialect that's embedded in Python. Since Hy transforms its Lisp code
into Python abstract syntax tree (AST) objects, you have the whole beautiful world
of Python at your fingertips, in Lisp form.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%_bindir/hy
%_bindir/hy2py
%_bindir/hyc
%python3_sitelibdir/hy
%python3_sitelibdir/hy-%version.dist-info

%changelog
* Wed Nov 11 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.1-alt1
- 1.3.1 released

* Wed Apr 29 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.0-alt1
- 1.2.0 released
