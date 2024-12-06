Name: radicle
Version: 1.1
Release: alt1

Summary: Radicle Heartwood Protocol & Stack
License: MIT Apache-2.0
Group: Development/Other
Url: https://radicle.xyz/

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
%setup
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 vendor
%else
tar xf %SOURCE1
%endif

%install
export GIT_HEAD=70f0cc35
export CARGO_HOME=${PWD}/cargo
for p in cli node remote-helper; do
cargo install %_smp_mflags --offline --no-track --path radicle-$p --root=%buildroot%_prefix
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
* Fri Dec 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1-alt1
- 1.1 released

* Wed Oct 23 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0-alt0.20241023
- initial
