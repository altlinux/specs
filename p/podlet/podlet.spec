%define _unpackaged_files_terminate_build 1

Name: podlet
Version: 0.3.0
Release: alt1
Url: https://crates.io/crates/podlet
Vcs: https://github.com/containers/podlet.git
Summary: Podlet generates Podman Quadlet files from a Podman command, compose file, or existing object
License: Apache-2.0
Group: System/Configuration/Other
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: /proc
BuildRequires: rust-cargo

%description
%summary.

%prep
%setup
%patch0 -p1

%build
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/%name -t %buildroot%_bindir

%check
cargo test %_smp_mflags --release --no-fail-fast

%files
%_bindir/%name

%changelog
* Tue Mar 11 2025 Artyom Sinyugin <writers@altlinux.org> 0.3.0-alt1
- Initial build.
