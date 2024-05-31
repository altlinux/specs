Name:     pop-launcher
Version:  1.2.1
Release:  alt1

Summary:  Modular IPC-based desktop launcher service
License:  MPL-2.0
Group:    Graphical desktop/Other
Url:      https://github.com/pop-os/launcher

ExcludeArch: ppc64le

# Source-url: https://github.com/pop-os/launcher/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# auto predownloaded cargo modules during update version with rpmgs from etersoft-build-utils
Source1: %name-development-%version.tar

%filter_from_requires /gnome-terminal/d
%filter_from_requires /gnome-session/d

# https://bugzilla.altlinux.org/40901
Requires: /proc

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: just

%description
%summary.

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
%rust_build -p pop-launcher-bin

%install
just rootdir=%buildroot install_bin
just rootdir=%buildroot bin_path=%_bindir/%name install_scripts
just rootdir=%buildroot bin_path=%_bindir/%name install_plugins

%files
%doc README.md
%_bindir/%name
%_libexecdir/%name/

%changelog
* Fri May 31 2024 Roman Alifanov <ximper@altlinux.org> 1.2.1-alt1
- initial build for sisyphus

