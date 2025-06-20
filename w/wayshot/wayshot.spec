Name: wayshot
Version: 1.3.1
Release: alt1
License: BSD-2-Clause

Summary: Screenshot tool for wlroots based compositors

Group: Graphical desktop/Other

Url: https://github.com/waycrate/wayshot
Vcs: https://github.com/waycrate/wayshot.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
A native, blazing-fast screenshot tool for wlroots based compositors
such as sway and river written in Rust.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
* Fri Jun 20 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.3.1-alt1
- Initial build
