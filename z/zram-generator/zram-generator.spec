Name: zram-generator
Version: 1.1.2
Release: alt1

Summary: Systemd unit generator for zram swap devices

License: MIT
Group: System/Configuration/Other
Url: https://github.com/systemd/zram-generator

# Source-url: https://github.com/systemd/zram-generator/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

Source2: blacklist-zswap.conf

BuildRequires: rust-cargo
BuildRequires: %_bindir/ronn groff-base
BuildRequires: pkgconfig(systemd)

%description
This is a systemd unit generator that enables swap on zram.
(With zram, there is no physical swap device. Part of the available RAM
is used to store compressed pages, essentially trading CPU cycles for memory.

%prep
%setup -a1

mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
%make_build man

%install
%makeinstall_std

mkdir -p %buildroot/etc/modprobe.d/
install -m 0644 %SOURCE2 %buildroot/etc/modprobe.d/blacklist-zswap.conf

%files
%config(noreplace) /etc/modprobe.d/blacklist-zswap.conf
/usr/lib/systemd/system-generators/zram-generator
%_unitdir/systemd-zram-setup@.service
%_docdir/zram-generator/zram-generator.conf.example
%_man5dir/zram-generator.conf.5.xz
%_man8dir/zram-generator.8.xz

%changelog
* Tue Jun 18 2024 Boris Yumankulov <boria138@altlinux.org> 1.1.2-alt1
- initial build for ALT Sisyphus

