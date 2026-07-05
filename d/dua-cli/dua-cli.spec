%global _unpackaged_files_terminate_build 1
%global bin_name dua

Name: dua-cli
Version: 2.37.1
Release: alt1
Summary: View disk space usage and delete unwanted data
License: MIT
Group: File tools
URL: https://lib.rs/crates/dua-cli
VCS: https://github.com/Byron/dua-cli

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
dua (Disk Usage Analyzer) is a tool to conveniently learn about the
usage of disk space of a given directory. It's parallel by default
and will max out your SSD, providing relevant information as fast
as possible. Optionally delete superfluous data, and do so more
quickly than rm.

%prep
%setup -a 1
%rust_prep

%build
%rust_build
target/release/%bin_name completions bash > %bin_name.bash
target/release/%bin_name completions zsh > %bin_name.zsh
target/release/%bin_name completions fish > %bin_name.fish

%install
%rust_install %bin_name
install -Dm 0644 %bin_name.bash %buildroot%_datadir/bash-completion/completions/%bin_name
install -Dm 0644 %bin_name.zsh %buildroot%_datadir/zsh/site-functions/_%bin_name
install -Dm 0644 %bin_name.fish %buildroot%_datadir/fish/vendor_completions.d/%bin_name.fish

%check
# skip tests that fail due to filesystem-specific directory sizes
%rust_test -- --skip it_can_handle_ending_traversal

%files
%_bindir/%bin_name
%_datadir/zsh/site-functions/_%bin_name
%_datadir/bash-completion/completions/%bin_name
%_datadir/fish/vendor_completions.d/%bin_name.fish

%changelog
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.37.1-alt1
- Updated to version 2.37.1.

* Fri Jun 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.36.0-alt1
- Updated to version 2.36.0.

* Thu May 21 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.34.0-alt1
- Initial build for ALT.
