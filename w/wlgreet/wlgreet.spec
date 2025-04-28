%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: wlgreet
Version: 0.5.0
Release: alt3
Summary: Wayland greeter for greetd
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://git.sr.ht/~kennylevinsen/wlgreet
VCS: https://git.sr.ht/~kennylevinsen/wlgreet
Source: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name-conf-sway
Source3: %name-conf-hyprland

#Support loongarch64 fix
Patch3500: wlgreet-0.5.0-alt-loongarch64_nix_vendor_fix.patch

BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: cargo-vendor-checksum

Requires: greetd
Provides: greetd-greeter

%description
Raw wayland greeter for greetd, to be run under sway or similar.

Note that cage is currently not supported
due to it lacking wlr-layer-shell-unstable support.

%package config-sway
Summary: Configuration for launching wlgreet with Sway
Group: Graphical desktop/Other
BuildArch: noarch
Requires: wlgreet

%description config-sway
%summary.

%package config-hyprland
Summary: Configuration for launching wlgreet with Hyprland.
Group: Graphical desktop/Other
BuildArch: noarch
Requires: wlgreet

%description config-hyprland
%summary.

%prep
%setup -a1
%patch3500 -p1

# Checksum update for patched files
cargo-vendor-checksum \
    --vendor %_builddir/%name-%version/vendor -f \
	nix/src/sys/ioctl/linux.rs \
	nix-0.22.3/src/sys/ioctl/linux.rs \
	nix-0.24.3/src/sys/ioctl/linux.rs

mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
cargo build \
	--release \
	%{?_smp_mflags} \
	--offline \
	%nil

%install
install -Dm755 target/release/wlgreet %buildroot%_bindir/wlgreet

# configs
install -vD %SOURCE2 %buildroot%_sysconfdir/greetd/wlgreet-conf-sway
install -vD %SOURCE3 %buildroot%_sysconfdir/greetd/wlgreet-conf-hyprland

mkdir -p %buildroot%_altdir
mkdir -p %buildroot%_sysconfdir/greetd/greeters

for i in sway hyprland; do
cat > %buildroot%_sysconfdir/greetd/greeters/wlgreet-$i.toml <<EOF
[terminal]
vt = 1

[default_session]
command = "$i -c %_sysconfdir/greetd/wlgreet-conf-$i"
user = "_greeter"
EOF
done

# sway
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/wlgreet-sway.toml 15" \
	> %buildroot%_altdir/greetd-wlgreet-sway
# hyprland
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/wlgreet-hyprland.toml 20" \
	> %buildroot%_altdir/greetd-wlgreet-hyprland

%check
cargo test --release

%files
%doc LICENSE
%doc README.md
%_bindir/*

%files config-sway
%_altdir/greetd-wlgreet-sway
%config(noreplace) %_sysconfdir/greetd/greeters/wlgreet-sway.toml
%config(noreplace) %_sysconfdir/greetd/wlgreet-conf-sway

%files config-hyprland
%_altdir/greetd-wlgreet-hyprland
%config(noreplace) %_sysconfdir/greetd/greeters/wlgreet-hyprland.toml
%config(noreplace) %_sysconfdir/greetd/wlgreet-conf-hyprland

%changelog
* Sun Mar 09 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.5.0-alt3
- NMU:
  + add hyprland and sway configs
  + add greetd-greeter provides

* Sat Jun 22 2024 Aleksei Kalinin <kaa@altlinux.org> 0.5.0-alt2
- NMU: Patched vendor nix for loongarch64 support

* Fri May 03 2024 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- 0.3 -> 0.5.0

* Thu Nov 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.3-alt3
- NMU: fixed FTBFS on LoongArch.

* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt2
- Applied stricter build checks.

* Fri Mar 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt1
- Initial build for ALT.
