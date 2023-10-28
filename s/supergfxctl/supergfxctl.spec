Name: supergfxctl
Version: 5.1.2
Release: alt1

Summary: Super graphics mode controller

License: MPL-2.0
Group: System/Kernel and hardware
Url: https://gitlab.com/asus-linux/supergfxctl

# Source-url: https://gitlab.com/asus-linux/supergfxctl/-/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libudev)
#BuildRequires: pkgconfig(systemd)

%description
supergfxctl is a super graphics mode controller for laptops with hybrid nvidia.

%prep
%setup -a 1

mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build --features "daemon cli"

%install
mkdir -p "%buildroot%_bindir"
install -D -m 0755 target/release/supergfxd %buildroot%_bindir/supergfxd
install -D -m 0755 target/release/supergfxctl %buildroot%_bindir/supergfxctl
install -D -m 0644 data/90-supergfxd-nvidia-pm.rules %buildroot%_udevrulesdir/90-supergfxd-nvidia-pm.rules
install -D -m 0644 data/org.supergfxctl.Daemon.conf  %buildroot%_sysconfdir/dbus-1/system.d/org.supergfxctl.Daemon.conf
install -D -m 0644 data/supergfxd.service %buildroot%_unitdir/supergfxd.service
install -D -m 0644 data/supergfxd.preset %buildroot%_presetdir/99-supergfxd.preset

install -D -m 0644 README.md %buildroot%_docdir/%name/README.md

%files
%doc LICENSE
%_bindir/supergfxd
%_bindir/supergfxctl
%_unitdir/supergfxd.service
%_presetdir/99-supergfxd.preset
%_udevrulesdir/90-supergfxd-nvidia-pm.rules
%_sysconfdir/dbus-1/system.d/org.supergfxctl.Daemon.conf
%_docdir/%name/*

%changelog
* Sat Oct 28 2023 Vitaly Lipatov <lav@altlinux.ru> 5.1.2-alt1
- initial build for ALT Sisyphus (thanks, ROSA!)
