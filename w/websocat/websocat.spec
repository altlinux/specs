Name: websocat
Version: 1.9.0
Release: alt1

Summary: Netcat, curl and socat for WebSockets

License: MIT
Group: Networking/Other
Url: https://github.com/vi/websocat

VCS: https://github.com/vi/websocat.git
Source: %name-%version.tar
Source1: vendor.tar
Source99: websocat.watch

BuildRequires(pre): /proc
BuildRequires(pre): rust-cargo
BuildRequires: libssl-devel
BuildRequires: perl-Pod-Usage

%description
%summary.

%prep
%setup -a1
mkdir .cargo
cat <<EOF >.cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build \
	--release \
	--features=seqpacket,signal_handler,ssl,unix_stdio \
	--no-default-features \
	#

%install
install -pm755 -D target/release/websocat %buildroot%_bindir/websocat

%check
cargo test
./test.sh

%files
%_bindir/websocat
%doc doc.md moreexamples.md

%changelog
* Thu Dec 09 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.9.0-alt1
- Update to v1.9.0.

* Wed May 12 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.1-alt1
- Updated to v1.8.1.
- Built against OpenSSL libs.
- Built with the following features: seqpacket, signal_handler, ssl and
  unix_stdio.
- Fixed %%check.

* Sat Apr 17 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.0-alt1
- Updated to v1.8.0.

* Thu Apr 08 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.7.0-alt1
- Initial build for ALT Sisyphus.

