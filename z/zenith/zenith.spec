Name: zenith
Version: 0.15.0
Release: alt1

Summary: In terminal graphical metrics for your *nix system
License: MIT
Group: Monitoring
Url: https://github.com/bvaisvil/zenith
VCS: https://github.com/bvaisvil/zenith

Source0: %name-%version.tar
Source1: vendor.tar

Patch1: 002-crate-nix-0.23-loongarch64-support.patch
Patch2: 003-crate-heim-loongarch64-support.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc clang-devel

%description
Zenith - sort of like top or htop but with zoom-able charts,
CPU, GPU, network, and disk usage

%prep
%setup -a1
#removed .cargo/config.toml 
rm -v .cargo/config.toml

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

[source.vendored-sources]
directory = "vendor"
EOF

%patch1 -p1
%patch2 -p1
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
     ./vendor/nix-0.23.2/.cargo-checksum.json \
     ./vendor/heim-*/.cargo-checksum.json

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
* Sat May 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.15.0-alt1
- 0.14.3 -> 0.15.0

* Tue Feb 17 2026 Ilya Sorochan <k0tran@altlinux.org> 0.14.3-alt2
- Add patches for nix and heim-* crates for loongarch64.

* Fri Feb 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.14.3-alt1
- Initial build for ALT Linux.

