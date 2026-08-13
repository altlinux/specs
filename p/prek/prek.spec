%define _unpackaged_files_terminate_build 1
%define pypi_name prek

%def_with check

Name: prek
Version: 0.4.13
Release: alt1

Summary: Better pre-commit, re-engineered in Rust
License: MIT
Group: Development/Tools
URL: https://prek.j178.dev
VCS: https://github.com/j178/prek

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-rust
BuildRequires: rpm-build-python3
BuildRequires: python3(maturin)

%if_with check
BuildRequires: git
BuildRequires: /dev/pts
%endif

%description
pre-commit is a framework to run hooks written in many languages, and it
manages the language toolchain and dependencies for running the hooks.

prek is a reimagined version of pre-commit, built in Rust. It is
designed to be a faster, dependency-free and drop-in alternative for it,
while also providing some additional long-requested features.

%package -n python3-module-%pypi_name
Summary: Python bindings for %name
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%pypi_name
This package contains python bindings for %name.

%prep
%setup -a1
%rust_prep

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%pyproject_build
./target/release/%name util generate-shell-completion bash > %name.bash
./target/release/%name util generate-shell-completion fish > %name.fish
./target/release/%name util generate-shell-completion zsh > %name.zsh

%install
%pyproject_install
install -Dm 644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name

%check
# snapshot test fails on i586 due to hash map ordering
%ifarch %ix86
%define skip_ix86_tests --skip hook_builder_build_fills_and_merges_attributes
%endif

# most tests require network access, run only unit tests
%rust_test --bin prek -- --skip http %{?skip_ix86_tests}

%files
%doc CHANGELOG.md CONTRIBUTING.md README.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%files -n python3-module-%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 13 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.4.13-alt1
- Updated to version 0.4.13.

* Mon Aug 03 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.4.12-alt1
- Updated to version 0.4.12.
- Added python3-module-prek subpackage (closes: #59643).

* Mon Jun 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.4.5-alt1
- Updated to version 0.4.5.

* Mon May 18 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.4.0-alt1
- Updated to version 0.4.0.

* Thu Apr 30 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.3.11-alt1
- Updated to version 0.3.11.

* Wed Apr 15 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.3.9-alt1
- Updated to version 0.3.9.

* Mon Mar 23 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.3.6-alt1
- Initial build for ALT.

