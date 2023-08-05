Name: zerotier-one
Version: 1.10.6
Release: alt1

Summary: ZeroTier network virtualization service

License: ZeroTier BSL 1.1
Group: Networking/Other
Url: https://www.zerotier.com

# Source-url: https://github.com/zerotier/ZeroTierOne/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Cargo modules for build rust code in the zeroidc dir
Source1: %name-development-%version.tar

ExcludeArch: armh

BuildRequires: udev-rules clang libstdc++-devel
BuildRequires: rust-cargo
BuildRequires: libssl-devel libminiupnpc-devel

# for man pages
BuildRequires: /usr/bin/ronn

Requires: udev-rules
Requires(pre): %_sbindir/useradd, %_bindir/getent

%description
ZeroTier is a software defined networking layer for Earth.

It can be used for on-premise network virtualization, as a peer to peer VPN
for mobile teams, for hybrid or multi-data-center cloud deployments, or just
about anywhere else secure software defined virtual networking is useful.

This is our OS-level client service. It allows Mac, Linux, Windows,
FreeBSD, and soon other types of clients to join ZeroTier virtual networks
like conventional VPNs or VLANs. It can run on native systems, VMs, or
containers (Docker, OpenVZ, etc.).

%prep
%setup -a1
mkdir -p zeroidc/.cargo
cat <<EOF >> zeroidc/.cargo/config
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/glimberg/rust-jwt"]
git = "https://github.com/glimberg/rust-jwt.git"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "../vendor"
EOF


%build
%make_build ZT_USE_MINIUPNPC=1 one

%pre
%_bindir/getent passwd zerotier-one || %_sbindir/useradd -r -d /var/lib/zerotier-one -s /sbin/nologin zerotier-one

%install
%makeinstall_std
mkdir -p %buildroot%_unitdir/
cp debian/zerotier-one.service %buildroot%_unitdir/%name.service

%files
%_sbindir/zerotier-cli
%_sbindir/zerotier-idtool
%_sbindir/zerotier-one
%_man1dir/*
%_man8dir/*
/var/lib/zerotier-one/
%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name
%changelog
* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 1.10.6-alt1
- initial build for ALT Sisyphus

