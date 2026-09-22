Name:    xremap
Version: 0.15.13
Release: alt1

Summary: Key remapper for X11 and Wayland
License: MIT
Group:   System/Configuration/Other
URL:     https://github.com/xremap/xremap

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libwayland-client-devel libudev-devel

%description
xremap is a key remapper for Linux. Unlike xmodmap, it supports app-specific
remapping and Wayland.

%prep
%setup -a1
%rust_prep

%build
%rust_build --features full,udev

%install
%rust_install
mkdir -p %buildroot%_datadir/bash-completion/completions \
         %buildroot%_datadir/zsh/site-functions \
         %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/xremap --completions bash > %buildroot%_datadir/bash-completion/completions/xremap
%buildroot%_bindir/xremap --completions zsh > %buildroot%_datadir/zsh/site-functions/_xremap
%buildroot%_bindir/xremap --completions fish > %buildroot%_datadir/fish/vendor_completions.d/xremap.fish
install -Dm0644 example/xremap.service %buildroot%_userunitdir/xremap.service

%files
%doc LICENSE README.md
%_bindir/xremap
%_datadir/bash-completion/completions/xremap
%dir %_datadir/zsh
%dir %_datadir/zsh/site-functions
%_datadir/zsh/site-functions/_xremap
%dir %_datadir/fish
%dir %_datadir/fish/vendor_completions.d
%_datadir/fish/vendor_completions.d/xremap.fish
%dir %_userunitdir
%_userunitdir/xremap.service

%changelog
* Tue Sep 22 2026 Sergey Palcheh <minergenon@altlinux.org> 0.15.13-alt1
- Initial build for Sisyphus

