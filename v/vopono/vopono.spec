%define _unpackaged_files_terminate_build 1

Name: vopono
Version: 0.10.15
Release: alt1
Summary: Tool to run applications through VPN tunnels

License: GPL-3.0
Group: Networking/Other
URL: https://github.com/jamesmcm/vopono
Vcs: https://github.com/jamesmcm/vopono.git

Source: %name-%version.tar
Source1: vendor.tar
Source2: vopono.service
Patch0: alt-fix-imports-and-versions.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust rust-cargo
BuildRequires: /proc

%description
Vopono is a tool to run applications through VPN tunnels via temporary network
namespaces. This allows you to run only a handful of applications through
different VPNs simultaneously, whilst keeping your main connection as normal.

%prep
%setup -a1
%autopatch -p1

mkdir -p .cargo
cat << EOF > .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install
install -Dm 0644 %SOURCE2 %buildroot%_systemd_dir/system/vopono.service

%post
%post_service vopono

%preun
%preun_service vopono

%files
%doc README.md USERGUIDE.md LICENSE
%_bindir/vopono
%_systemd_dir/system/vopono.service

%changelog
* Tue Feb 10 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.10.15-alt1
- Initial build.
