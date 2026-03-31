Name: radicle
Version: 1.8.0
Release: alt1

Summary: Radicle Heartwood Protocol & Stack
License: MIT Apache-2.0
Group: Development/Other
URL: https://radicle.xyz/

Requires: git-core

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc
BuildRequires: /usr/bin/asciidoctor

%package seed-node
Summary: Radicle seed node
Group: System/Servers
Requires(pre): radicle = %version-%release

%define desc\
Heartwood is the third iteration of the Radicle Protocol, a powerful\
peer-to-peer code collaboration and publishing stack. The repository\
contains a full implemention of Heartwood, complete with a user-friendly\
command-line interface (`rad`) and network daemon (`radicle-node`).

%description %desc

%description seed-node %desc
This package contains things needed for radicle seed node.

%prep
%setup -a1
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
%endif

%install
export GIT_HEAD=d9915d275fd07d2
for p in cli node remote-helper; do
cargo install %_smp_mflags --offline --no-track --path crates/radicle-$p --root=%buildroot%_prefix
done

mkdir -p %buildroot{%_man1dir,%_localstatedir/radicle}
install -pm0644 -D systemd/radicle.sysusers %buildroot%_sysusersdir/radicle.conf
install -pm0644 -D systemd/radicle.tmpfiles %buildroot%_tmpfilesdir/radicle.conf
install -pm0644 -D systemd/radicle-seed.service %buildroot%_unitdir/radicle-seed.service

for f in *.1.adoc; do
  asciidoctor --doctype manpage --backend manpage --destination-dir=%buildroot%_man1dir $f
done		

%files
%doc LICENSE-* README.*
%_bindir/rad
%_bindir/radicle-node
%_bindir/git-remote-rad
%_man1dir/rad.1*
%_man1dir/rad-id.1*
%_man1dir/rad-patch.1*
%_man1dir/git-remote-rad.1*
%_man1dir/radicle-node.1*

%files seed-node
%_sysusersdir/radicle.conf
%_tmpfilesdir/radicle.conf
%_unitdir/radicle-seed.service
%_localstatedir/radicle

%changelog
* Tue Mar 31 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.0-alt1
- 1.8.0 released

* Fri Mar 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.1-alt1
- 1.7.1 released

* Thu Mar 19 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.0-alt1
- 1.7.0 released

* Wed Jan 28 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.1-alt1
- 1.6.1 released

* Wed Jan 14 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.0-alt1
- 1.6.0 released

* Wed Oct 01 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.0-alt1
- 1.5.0 released

* Mon Sep 08 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.0-alt1
- 1.4.0 released

* Fri Aug 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.0-alt1
- 1.3.0 released

* Mon Jul 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.1-alt1
- 1.2.1 released

* Tue Jun 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2-alt1
- 1.2 released

* Thu Feb 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1-alt2
- v1.1-32-g3b5fac17

* Fri Dec 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1-alt1
- 1.1 released

* Wed Oct 23 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0-alt0.20241023
- initial
