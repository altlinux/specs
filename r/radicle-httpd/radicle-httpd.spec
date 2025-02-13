Name: radicle-httpd
Version: 0.18.1
Release: alt1

Summary: A Radicle HTTP daemon exposing a JSON HTTP API
License: MIT Apache-2.0
Group: System/Servers
Url: https://radicle.xyz/

Requires: radicle-seed-node

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc
BuildRequires: /usr/bin/asciidoctor

%description
Heartwood is the third iteration of the Radicle Protocol, a powerful
peer-to-peer code collaboration and publishing stack.
This package contains daemon providing JSON HTTP API to a running
radicle seed node.

%prep
%setup
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 vendor
%else
tar xf %SOURCE1
%endif

%install
export CARGO_HOME=${PWD}/cargo
cargo install %_smp_mflags --offline --no-track --path . --root=%buildroot%_prefix

mkdir -p %buildroot{%_man1dir,%_localstatedir/radicle}
install -pm0644 -D systemd/radicle-httpd.service %buildroot%_unitdir/radicle-httpd.service
asciidoctor --doctype manpage --backend manpage --destination-dir=%buildroot%_man1dir radicle-httpd.1.adoc

%files
%doc LICENSE-*
%_bindir/radicle-httpd
%_man1dir/radicle-httpd.1*
%_unitdir/radicle-httpd.service

%changelog
* Thu Feb 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.18.1-alt1
- initial

