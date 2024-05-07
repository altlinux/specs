%define _unpackaged_files_terminate_build 1

Name: sniffnet
Version: 1.3.0
Release: alt1

Summary: Application to comfortably monitor your network traffic
License: Apache-2.0 or MIT
Group: Networking/Other
Url: https://sniffnet.net/
Vcs: https://github.com/GyulyVGC/sniffnet

Source0: %name-%version.tar
Source1: vendor.tar

Requires(post,preun): libcap-utils

BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libalsa-devel
BuildRequires: fontconfig-devel
BuildRequires: libpcap-devel
BuildRequires: desktop-file-utils

%description
%summary

%prep
%setup -a1
mkdir .cargo
cat << EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
%ifarch i586 armh
# Use less optimisation otherwise it causes "out of memory" error on 32-bit
# machines.
lto = "thin"
codegen-units = 16
%endif
EOF

%build
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/%name -t %buildroot%_bindir
resources="resources/packaging/linux"
desktop-file-install --dir %buildroot%_desktopdir $resources/sniffnet.desktop
for icon in $resources/graphics/*; do
    resolution=$(basename $icon | grep -Eo "[[:digit:]]+x[[:digit:]]+")
    install -pDm644 "$icon" \
        %buildroot%_iconsdir/hicolor/$resolution/apps/%name.png
done

%post
setcap cap_net_raw,cap_net_admin=eip %_bindir/%name

%preun
setcap '' %_bindir/%name

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%doc README.md LICENSE*

%changelog
* Tue May 07 2024 Alexandr Shashkin <dutyrok@altlinux.org> 1.3.0-alt1
- 1.1.3 -> 1.3.0.
- Added desktop file (Closes: 47273).

* Mon Jul 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus

