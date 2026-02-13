Name: zenith
Version: 0.14.3
Release: alt1

Summary: In terminal graphical metrics for your *nix system
License: MIT
Group: Monitoring
Url: https://github.com/bvaisvil/zenith
VCS: https://github.com/bvaisvil/zenith

Source0: %name-%version.tar
Source1: vendor.tar
# openSUSE patch for build in aarch64
Patch: 001-strip-cargo-config.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc clang-devel

%description
Zenith - sort of like top or htop but with zoom-able charts,
CPU, GPU, network, and disk usage

%prep
%setup -a1
%patch -p1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/bvaisvil/darwin-libproc"]
git = "https://github.com/bvaisvil/darwin-libproc"
replace-with = "vendored-sources"

[source."git+https://github.com/bvaisvil/heim.git?branch=zenith_changes"]
git = "https://github.com/bvaisvil/heim.git"
branch = "zenith_changes"
replace-with = "vendored-sources"

[source."git+https://github.com/bvaisvil/sysinfo.git?branch=zenith_changes_15.1_mem_fix"]
git = "https://github.com/bvaisvil/sysinfo.git"
branch = "zenith_changes_15.1_mem_fix"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install
install -Dm 0644 assets/%name.png %buildroot%_pixmapsdir/%name.png
install -Dm 0644 assets/%name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc *.md LICENSE
%_bindir/%name
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Fri Feb 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.14.3-alt1
- Initial build for ALT Linux.

