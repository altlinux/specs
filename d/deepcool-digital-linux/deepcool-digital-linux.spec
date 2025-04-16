%define _unpackaged_files_terminate_build 1
%define bin_name deepcool-digital-linux
%define service_name deepcool-digital

Name: deepcool-digital-linux
Version: 0.7.5
Release: alt1
Summary: Utility to control DeepCool digital devices on Linux
License: GPL-3.0
Group: System/Configuration/Hardware
Url: https://github.com/Nortank12/deepcool-digital-linux
Vcs: https://github.com/Nortank12/deepcool-digital-linux.git
Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: libudev-devel

%description
This CLI program is meant to replicate the functionality of the
original DeepCool Digital Windows program for controlling
DeepCool digital devices on Linux.

%prep
%setup -a 1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
install -d %buildroot%_sbindir
install -Dm 755 "target/release/%bin_name" "%buildroot%_sbindir/%bin_name"

install -d %buildroot%_unitdir
cat > %buildroot%_unitdir/%service_name.service <<EOF
[Unit]
Description=DeepCool Digital Control Utility

[Service]
ExecStart=%_sbindir/%bin_name

[Install]
WantedBy=multi-user.target
EOF

%post
%systemd_post_with_restart %service_name.service

%preun
%systemd_preun %service_name.service

%files
%_sbindir/%bin_name
%_unitdir/%service_name.service
%doc README.md

%changelog
* Mon Apr 07 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.7.5-alt1
- Initial build
