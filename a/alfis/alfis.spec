Name: alfis
Version: 0.10.0
Release: alt1

Summary: Alternative Free Identity System - DNS server on its own blockchain
License: AGPL-3.0
Group: Networking/DNS
Url: https://alfis.name
Vcs: https://github.com/Revertron/Alfis

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo
BuildRequires: pkg-config
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: libX11-devel
BuildRequires: libsqlite3-devel

%description
ALFIS (ALternative Free Identity System) is an implementation of a Domain
Name System based on a small, slowly growing blockchain. It is lightweight,
self-contained, supported on multiple platforms and contains DNS-resolver
on its own to resolve domain records contained in blockchain and forward
DNS requests of ordinary domain zones to upstream forwarders.

%prep
%setup -a 1
%autopatch -p1
# Drop upstream cross-build config: %rust_prep appends to .cargo/config.toml
# and its last line has no trailing newline, which would corrupt the TOML.
rm -rf .cargo
%rust_prep

%build
%ifarch i586
# LLVM runs out of memory while LTO-compiling the final binary on i586
export CARGO_PROFILE_RELEASE_LTO=off
%endif
%rust_build

%check
%ifarch i586
export CARGO_PROFILE_RELEASE_LTO=off
%endif
# These tests query 8.8.8.8 directly and need network access.
%rust_test -- --skip dns::client::tests::test_udp_client --skip dns::client::tests::test_tcp_client

%install
%rust_install
install -Dm644 contrib/systemd/%name.service %buildroot%_unitdir/%name.service
install -Dm644 contrib/systemd/%name.sysusers %buildroot%_sysusersdir/%name.conf
install -Dm644 contrib/systemd/%name.tmpfiles %buildroot%_tmpfilesdir/%name.conf
install -Dm644 contrib/name.%name.Alfis.desktop %buildroot%_datadir/applications/%name.desktop
for size in 16 22 24 32 36 48 64 72 96 128 192 256; do
    install -Dm644 img/logo/%{name}_icon${size}.png %buildroot%_datadir/icons/hicolor/${size}x${size}/apps/%name.png
done
install -Dm644 img/logo/%{name}_icon.svg %buildroot%_datadir/icons/hicolor/scalable/apps/%name.svg

%post
%sysusers_create_package %name contrib/systemd/%name.sysusers
%tmpfiles_create_package %name contrib/systemd/%name.tmpfiles
# Generate a config on first install if /etc/alfis.conf is missing
if [ ! -e /etc/%name.conf ]; then
    %_bindir/%name -g > /etc/%name.conf
    chmod 644 /etc/%name.conf
fi
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/scalable/apps/%name.svg
%doc README.md

%changelog
* Mon Aug 10 2026 Vladislav Tatjanin <l27001@altlinux.org> 0.10.0-alt1
- Initial build.

