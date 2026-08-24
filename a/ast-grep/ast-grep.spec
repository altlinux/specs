%define _unpackaged_files_terminate_build 1

%define ast_grep_py crates/pyo3
# drop exporting optflags to properly fix linking inner tree-sitter in python
# bindings (this doesn't affect %%rust_build due to is not used in it at all).
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: ast-grep
Version: 0.45.1
Release: alt2

Summary: A CLI tool for code structural search, lint and rewriting
License: MIT
Group: Development/Tools
Url: https://ast-grep.github.io
VCS: https://github.com/ast-grep/ast-grep

# Source-url: https://github.com/ast-grep/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-build-python3
BuildRequires: cargo-vendor-checksum
BuildRequires: rust-cargo
BuildRequires: python3-module-maturin
BuildRequires: python3-module-pytest
BuildRequires: python3(yq.tomlq)
BuildRequires: python3-dev

%description
ast-grep(sg) is a CLI tool for code structural search, lint, and
rewriting.

%package -n python3-module-ast-grep-py
Summary: Structural Search and Rewrite code at large scale using precise AST pattern
Group: Development/Python3

%description -n python3-module-ast-grep-py
ast-grep python binding.

%prep
%setup -a1
rm -rf .cargo
%rust_prep
cargo-vendor-checksum --vendor vendor --all

## enable python limited api
tomlq -i -t '.features.python += ["pyo3/abi3"]' %ast_grep_py/Cargo.toml

%build
%rust_build

cd %ast_grep_py
%pyproject_build

%install
%rust_install

cd %ast_grep_py
%pyproject_install

%check
cd %ast_grep_py
rm -r ast_grep_py
%pyproject_run_pytest -vra

%files
%doc README.md
%_bindir/%name

%files -n python3-module-ast-grep-py
%python3_sitelibdir/ast_grep_py/
%python3_sitelibdir/ast_grep_py-%version.dist-info/

%changelog
* Mon Aug 24 2026 Anton Zhukharev <ancieg@altlinux.org> 0.45.1-alt2
- NMU: package python bindings (ast-grep-py)

* Mon Aug 10 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.45.1-alt1
- new version

* Fri Jul 24 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.45.0-alt1
- new version

* Mon Jul 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.44.1-alt1
- new version

* Mon Jun 22 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.44.0-alt1
- new version

* Wed May 27 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.43.0-alt1
- new version

* Wed May 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.42.3-alt1
- new version

* Tue May 12 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.42.2-alt1
- new version

* Tue Apr 06 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.42.1-alt1
- new version

* Tue Mar 17 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.42.0-alt1
- new version

* Wed Mar 11 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.41.1-alt1
- new version

* Thu Feb 26 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.41.0-alt1
- new version

* Mon Feb 16 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.40.5-alt1
- initial build for ALT Linux