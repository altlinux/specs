Name: websocat
Version: 1.7.0
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
cargo build --release --features=ssl

%install
install -pm755 -D target/release/websocat %buildroot%_bindir/websocat

%check
cargo test

%files
%_bindir/websocat
%doc doc.md moreexamples.md

%changelog
* Thu Apr 08 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.7.0-alt1
- Initial build for ALT Sisyphus.

