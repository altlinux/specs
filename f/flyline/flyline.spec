Name:    flyline
Version: 1.7.1
Release: alt1

Summary: A Bash plugin that provides a modern line editing interface
License: GPL-3.0-only
Group:   Shells
URL:     https://github.com/HalFrgrd/flyline
VCS:     https://github.com/HalFrgrd/flyline

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
Requires: bash

%description
Flyline: a Bash plugin to replace readline for a modern line editing
experience: syntax highlighting, agent integration, rich prompts,
tooltips, fuzzy history search, and more!

To activate flyline in the current shell, run:
    enable -f %_libdir/%name/libflyline.so flyline

To enable it permanently, add this line to your ~/.bashrc:
    enable flyline 2>/dev/null || \
        enable -f %_libdir/%name/libflyline.so flyline

%prep
%setup -a1
%rust_prep
# Replace git dependency sources with vendored copies (offline build)
cat >> .cargo/config.toml <<'EOF'

[source."git+https://github.com/HalFrgrd/ansi-to-tui.git?branch=main"]
git = "https://github.com/HalFrgrd/ansi-to-tui.git"
branch = "main"
replace-with = "vendored-sources"

[source."git+https://github.com/HalFrgrd/flash.git?rev=59af2ab94aaa6b7a407d09549605b1d3bc81256c"]
git = "https://github.com/HalFrgrd/flash.git"
rev = "59af2ab94aaa6b7a407d09549605b1d3bc81256c"
replace-with = "vendored-sources"

[source."git+https://github.com/HalFrgrd/flycomp.git?rev=754be16d7a2130ad12b6d038d42a8933c92c103f"]
git = "https://github.com/HalFrgrd/flycomp.git"
rev = "754be16d7a2130ad12b6d038d42a8933c92c103f"
replace-with = "vendored-sources"

[source."git+https://github.com/HalFrgrd/ratatui.git?branch=inline_viewport_improvments"]
git = "https://github.com/HalFrgrd/ratatui.git"
branch = "inline_viewport_improvments"
replace-with = "vendored-sources"

[source."git+https://github.com/HalFrgrd/skim?rev=7908ee85a5f6cd49575925fcc0bdef3999409d26"]
git = "https://github.com/HalFrgrd/skim"
rev = "7908ee85a5f6cd49575925fcc0bdef3999409d26"
replace-with = "vendored-sources"

[source."git+https://github.com/HalFrgrd/termina.git?rev=5b67693f2c5173c61a13d18517e2cebfc96a6a9d"]
git = "https://github.com/HalFrgrd/termina.git"
rev = "5b67693f2c5173c61a13d18517e2cebfc96a6a9d"
replace-with = "vendored-sources"
EOF

%build
%rust_build

%install
# flyline is a Bash loadable builtin (cdylib), not an executable
install -Dm 755 target/release/libflyline.so %buildroot%_libdir/%name/libflyline.so

%files
%doc LICENSE-GPLv3 LICENSE-MIT README.md
%dir %_libdir/%name
%_libdir/%name/libflyline.so

%changelog
* Sat Sep 05 2026 Sergey Palcheh <minergenon@altlinux.org> 1.7.1-alt1
- Initial build for Sisyphus
