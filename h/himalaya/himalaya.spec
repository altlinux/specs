%global _unpackaged_files_terminate_build 1

Name: himalaya
Version: 1.1.0
Release: alt1
Summary: CLI to manage your emails
License: MIT
Group: Networking/Mail
Url: https://pimalaya.org
VCS: https://github.com/pimalaya/himalaya

Source: %name-%version.tar
Source1: vendor.tar
Source2: %name.service

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
CLI to manage emails, based on email-lib.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
# install bin
%rust_install
# install man
mkdir -p %buildroot%_man1dir
%buildroot%_bindir/%name man %buildroot%_man1dir
# install shell completions
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
# install service file
mkdir -p %buildroot%_userunitdir
install -p -m 644 %SOURCE2 %buildroot%_userunitdir/%name.service

%files
%_bindir/%name
%_man1dir/%{name}*.1.*
%_userunitdir/%name.service
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%doc LICENSE

%changelog
* Sun Aug 24 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.1.0-alt1
- Updated to version 1.1.0.

* Sat Jun 17 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt2
- Added systemd service

* Fri Jun 16 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt1
- Initial build for ALT
