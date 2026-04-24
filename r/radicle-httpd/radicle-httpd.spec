Name: radicle-httpd
Version: 0.25.0
Release: alt1

Summary: A Radicle HTTP daemon exposing a JSON HTTP API
License: MIT Apache-2.0
Group: System/Servers
URL: https://radicle.dev/
VCS: https://seed.radicle.xyz/z4V1sjrXqjvFdnCUbxPFqd5p4DtH5

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
%setup -a1
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
%endif

%install
export GIT_HEAD=5a3337de
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
* Fri Apr 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.25.0-alt1
- 0.25.0 released

* Mon Mar 02 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.24.0-alt1
- 0.24.0 released

* Mon Jan 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.23.0-alt1
- 0.23.0 released

* Mon Jan 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.22.0-alt1
- 0.22.0 released

* Mon Dec 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.21.0-alt1
- 0.21.0 released

* Mon Jul 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.20.0-alt1
- 0.20.0 released

* Mon Jun 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.19.1-alt1
- 0.19.1 released

* Thu Jun 05 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.19.0-alt1
- 0.19.0 released

* Fri May 30 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.18.2-alt1
- 0.18.2 released

* Thu Feb 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.18.1-alt1
- initial

