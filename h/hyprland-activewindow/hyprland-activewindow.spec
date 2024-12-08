Name: hyprland-activewindow
Version: 1.0.5
Release: alt1
License: MIT

Summary: A multi-monitor aware Hyprland active window title outputer

Group: Graphical desktop/Other

Url: https://github.com/FieldofClay/hyprland-activewindow

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
A multi-monitor aware Hyprland active window title outputer.
Follows the specified monitor and outputs the
current active window title. Designed to be used with Eww,
but may function with other bars.

%prep
%setup -a1

mkdir -p .cargo
cat <<EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
* Sun Dec 08 2024 Kirill Unitsaev <fiersik@altlinux.org> 1.0.5-alt1
- Initial build
