Name:     onagre
Version:  1.1.0
Release:  alt1

Summary:  A general purpose application launcher for X and wayland inspired by rofi/wofi and alfred
License:  MIT
Group:    Graphical desktop/Other
Url:      https://github.com/onagre-launcher/onagre/

ExcludeArch: ppc64le i586

# Source-url: https://github.com/onagre-launcher/onagre/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# auto predownloaded cargo modules during update version with rpmgs from etersoft-build-utils
Source1: %name-development-%version.tar

Requires: pop-launcher qalculate

# https://bugzilla.altlinux.org/40901
Requires: /proc

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

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
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.md
%_bindir/%name

%changelog
* Wed May 29 2024 Roman Alifanov <ximper@altlinux.org> 1.1.0-alt1
- initial build for sisyphus

