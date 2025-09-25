%define _unpackaged_files_terminate_build 1
%global import_path github.com/Julien-cpsn/desktop-tui

Name: desktop-tui
Version: 0.3.1
Release: alt1
Summary: A desktop environment without graphics.
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/Julien-cpsn/desktop-tui

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: libncursesw-devel

%description
A desktop environment without graphics (tmux-like).

%prep
%setup -a 1
%autopatch -p1

%build
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/%name

%changelog
* Thu Sep 25 2025 Pavel Shilov <zerospirit@altlinux.org> 0.3.1-alt1
- Initail build for Sisuphus.