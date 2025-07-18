%global srcname Nping

Name:    nping
Version: 0.4.0
Release: alt1

Summary: Nping mean NB Ping, A Ping Tool in Rust with Real-Time Data and Visualizations
License: MIT
Group:   Other
Url:     https://github.com/hanshuaikang/Nping
VCS:     https://github.com/hanshuaikang/Nping.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: gcc-c++

%description
Nping is a Ping tool developed in Rust using the ICMP protocol. It supports
concurrent Ping for multiple addresses, visual chart display, real-time data
updates, and other features.

%prep
%setup -a1

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
install -Dm 755 target/release/nping -t %buildroot%_bindir/

%files
%doc LICENSE README.*
%_bindir/%name

%changelog
* Mon Jul 14 2025 Sergey Palcheh <minergenon@altlinux.org> 0.4.0-alt1
- initial build for ALT Sisyphus

