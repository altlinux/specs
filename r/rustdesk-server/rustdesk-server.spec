Name: rustdesk-server
Version: 1.1.12
Release: alt1

Summary: RustDesk Server Program
License: AGPL-3.0
Group: Networking/Other
Url: https://rustdesk.com/
Vcs: https://github.com/rustdesk/rustdesk-server.git

ExcludeArch: ppc64le

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-alt-vendoring-config.patch
Patch1: %name-%version-alt-hbbs-unit-fix.patch

BuildRequires: rust-cargo
BuildRequires: /proc

%description
Self-host your own RustDesk server, it is free and open source.

%prep
%setup -a1
%autopatch -p1

%build
cargo build %_smp_mflags --offline --release

%install
install -d %buildroot%_sharedstatedir/%name
install -d %buildroot%_logdir/%name
install -D target/release/hbbr -t %buildroot%_bindir/
install -D target/release/hbbs -t %buildroot%_bindir/
install -D target/release/rustdesk-utils -t %buildroot%_bindir/
install -D systemd/rustdesk-hbbr.service -t %buildroot%_unitdir/
install -D systemd/rustdesk-hbbs.service -t %buildroot%_unitdir/

%check
#has no tests

%post
%post_service rustdesk-hbbr
%post_service rustdesk-hbbs

%preun
%preun_service rustdesk-hbbr
%preun_service rustdesk-hbbs

%files
%doc README* LICENSE
%_bindir/hbbr
%_bindir/hbbs
%_bindir/rustdesk-utils
%_unitdir/rustdesk-hbbs.service
%_unitdir/rustdesk-hbbr.service
%_sharedstatedir/%name
%_logdir/%name

%changelog
* Tue Dec 10 2024 Anton Kurachenko <srebrov@altlinux.org> 1.1.12-alt1
- Initial build for Sisyphus.
