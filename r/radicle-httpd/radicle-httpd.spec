Name: radicle-httpd
Version: 0.29.0
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
Source2: npm-cache.tar

BuildRequires: rust-cargo /proc
BuildRequires: /usr/bin/asciidoctor
BuildRequires: npm

%package -n radicle-web
Summary: Radicle HTTP webapp
Group: System/Servers
BuildArch: noarch

%description
Heartwood is the third iteration of the Radicle Protocol, a powerful
peer-to-peer code collaboration and publishing stack.
This package contains daemon providing JSON HTTP API to a running
radicle seed node.

%description -n radicle-web
Heartwood is the third iteration of the Radicle Protocol, a powerful
peer-to-peer code collaboration and publishing stack.
This package contains webapp used with radicle-httpd daemon.

%prep
%setup -a1 -a2
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
rm -rf npm-cache/*
npm ci --cache npm-cache --cpu=arm64 --os=linux --libc=glibc
npm ci --cache npm-cache --cpu=x64   --os=linux --libc=glibc
tar cf %SOURCE2 npm-cache
%endif
npm ci --offline --cache npm-cache

%build
export GIT_HEAD=7acf0739
cargo build %_smp_mflags --release --offline --manifest-path crates/radicle-httpd/Cargo.toml
cargo build %_smp_mflags --release --offline --manifest-path crates/radicle-search/Cargo.toml
VITE_RUNTIME_CONFIG=true npm run build

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -pm0755 -t %buildroot%_bindir target/release/radicle-{httpd,search}
install -pm0644 -D crates/radicle-httpd/systemd/radicle-httpd.service %buildroot%_unitdir/radicle-httpd.service
asciidoctor --doctype manpage --backend manpage --destination-dir=%buildroot%_man1dir crates/radicle-httpd/radicle-httpd.1.adoc
cp -p crates/radicle-search/README.md README.radicle-search.md
cp -a build %buildroot%_datadir/radicle-web

%files
%doc CHANGELOG* LICENSE* README*
%_bindir/radicle-httpd
%_bindir/radicle-search
%_man1dir/radicle-httpd.1*
%_unitdir/radicle-httpd.service

%files -n radicle-web
%_datadir/radicle-web

%changelog
* Sun Oct 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.29.0-alt1
- 0.29.0 released

* Tue Sep 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.28.0-alt1
- 0.28.0 released

* Fri Jul 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.26.0-alt1
- 0.26.0 released

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

