%global _unpackaged_files_terminate_build 1

Name: awatcher
Version: 0.3.1
Release: alt1
Summary: Activity and idle watchers
License: MPL-2.0
Group: System/Servers
Url: https://github.com/2e3s/awatcher

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: libssl-devel

%description
Awatcher is a window activity and idle watcher
with an optional tray and UI for statistics.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/ActivityWatch/aw-server-rust?rev=656f3c9"]
git = "https://github.com/ActivityWatch/aw-server-rust"
rev = "656f3c9"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
debug = true
strip = false
EOF

%build
%rust_build --features=default

%install
%rust_install
mkdir -p %buildroot%_userunitdir
cp config/awatcher.service %buildroot%_userunitdir

%files
%_bindir/awatcher
%_userunitdir/awatcher.service
%doc LICENSE

%changelog
* Wed Jun 18 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.1-alt1
- Initial build for ALT.
