Name: cf-speedtest
Version: 0.4.8
Release: alt1
Summary: A command-line internet speed test tool
License: MIT
Group: System/Configuration/Networking
Url: https://github.com/12932/cf_speedtest
Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
cf_speedtest is an unofficial, cross-platform, command-line internet
speed test tool, powered by https://speed.cloudflare.com.
cf_speedtest leverages Cloudflare's own Speedtest API, it can achieve
much higher speeds than other tools.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install cf_speedtest

%files
%_bindir/cf_speedtest

%changelog
* Sat May 11 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.8-alt1
- Initial build for ALT.

