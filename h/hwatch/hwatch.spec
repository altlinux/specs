%global _unpackaged_files_terminate_build 1

Name: hwatch
Version: 0.4.2
Release: alt1
Summary: Alternative watch command
License: MIT
Group: Monitoring
Url: https://crates.io/crates/hwatch
VCS: https://github.com/blacknon/hwatch

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A modern alternative to the watch command,
records the differences in execution results
and can check this differences at after.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install
install -Dm 0644 completion/bash/hwatch-completion.bash \
                 %buildroot%_datadir/bash-completion/completions/%name.bash
install -Dm 0644 completion/fish/hwatch.fish \
                 %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 0644 completion/zsh/_hwatch %buildroot/%_datadir/zsh/site-functions/_%name

%files
%_bindir/%name
%_datadir/bash-completion/completions/%name.bash
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%doc LICENSE

%changelog
* Sat May 09 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.2-alt1
- Updated to version 0.4.2.

* Sun Apr 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.0-alt1
- Initial build for ALT.
