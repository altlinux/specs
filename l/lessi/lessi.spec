%global _unpackaged_files_terminate_build 1
%def_with check

Name: lessi
Version: 0.3.0
Release: alt1
Summary: A terminal pager with integrated sixel/kitty graphics support
License: MIT
Group: Text tools
URL: https://github.com/roblillack/lessi
VCS: https://github.com/roblillack/lessi

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
lessi is a terminal pager with integrated sixel and kitty graphics
protocol support. Think less, but with inline images. It provides
full ANSI support, less-compatible navigation and flags (-F, -R, -X,
defaults from the LESS environment variable, so it works as a Git
pager), mouse support, search, OSC 8 hyperlinks and renders inline
sixel/kitty images at their correct positions while scrolling.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Mon Nov 02 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.0-alt1
- Initial build for ALT.
