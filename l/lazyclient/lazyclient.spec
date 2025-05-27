%define _unpackaged_files_terminate_build 1

Name: lazyclient
Version: 1.4.3
Release: alt1

Summary: PostgreSQL client in the terminal, written in Rust, with a user-friendly UI
License: Apache-2.0
Group: Databases

Url: https://altlinux.space/gorohovskynikolay/lazyclient
Vcs: https://altlinux.space/gorohovskynikolay/lazyclient
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires: rust-cargo
BuildRequires: pkgconfig(openssl)

%description
%summary.

%prep
%setup -a 1
install -vD %SOURCE2 .cargo/config.toml

%build
cargo build %{?_smp_mflags} --release --offline

%install
install -D target/release/%name %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/%name
cp -r locales %buildroot%_datadir/%name

%files
%_bindir/%name
%_datadir/%name
%doc README.md

%changelog
* Tue May 27 2025 David Sultaniiazov <x1z53@altlinux.org> 1.4.3-alt1
- Initial build
