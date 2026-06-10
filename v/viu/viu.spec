%global _unpackaged_files_terminate_build 1

Name: viu
Version: 1.6.1
Release: alt1
Summary: Terminal image viewer with native support for iTerm and Kitty
License: MIT
Group: Graphics
URL: https://crates.io/crates/viu
VCS: https://github.com/atanunq/viu

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A small command-line application to view images from the terminal written in Rust.
Features:
- Native iTerm and Kitty support
- Animated GIF support
- Accept media through stdin
- Custom dimensions
- Transparency
- Experimental Sixel support (behind either sixel or icy_sixel feature flags)

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%_bindir/viu

%changelog
* Wed Jun 10 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.1-alt1
- Initial build for ALT.
