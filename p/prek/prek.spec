%define _unpackaged_files_terminate_build 1

%def_with check

Name: prek
Version: 0.4.5
Release: alt1

Summary: Better pre-commit, re-engineered in Rust
License: MIT
Group: Development/Tools
Url: https://prek.j178.dev
VCS: https://github.com/j178/prek

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

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

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

# generate shell completions and strip buildroot path
COMPLETE=bash %buildroot%_bindir/%name | sed 's|%buildroot||g' > %name.bash
COMPLETE=fish %buildroot%_bindir/%name | sed 's|%buildroot||g' > %name.fish
COMPLETE=zsh %buildroot%_bindir/%name | sed 's|%buildroot||g' > %name.zsh
install -Dm 644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name

%check
# most tests require network access, run only unit tests
%rust_test --bin prek -- --skip http

%files
%doc CHANGELOG.md CONTRIBUTING.md README.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
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

