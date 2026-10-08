%define _unpackaged_files_terminate_build 1

Name: imgap
Version: 0.4.0
Release: alt1

Summary: Visualize differences between two images directly in your terminal
License: MIT and OFL-1.1
Group: Graphics
Url: https://github.com/roblillack/imgap
VCS: https://github.com/roblillack/imgap.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
imgap shows a visual comparison of two images right in the terminal:
both images side by side plus a heatmap of pixel differences, or an
interactive TUI with 2-up, swipe, onion skin and difference modes.

Output uses the Kitty graphics protocol, iTerm2 inline images or Sixel,
falling back to ANSI half-blocks. imgap understands the git external
diff calling convention and can be used as a git diff driver or difftool.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%doc README.md fonts/LICENSE.md
%_bindir/imgap

%changelog
* Thu Oct 08 2026 Ajrat Makhmutov <rauty@altlinux.org> 0.4.0-alt1
- Initial build.
