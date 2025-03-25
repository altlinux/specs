%define _unpackaged_files_terminate_build 1

Name: spaceman
Version: 0.1.3
Release: alt1

Summary: GNU spaceman, treemap disk usage analyzer
Group: File tools
License: GPL-3.0
Url: https://github.com/salihgerdan/spaceman

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: rpm-build-rust
BuildRequires: libgtk4-devel
BuildRequires: libpango-devel


%description
The GNU `spaceman' program is treemap disk usage analyzer: In search of lost space (a.k.a. wata-analyzer).

%prep
%setup -a1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
install -Dm 755 spaceman.desktop %buildroot%_datadir/applications/spaceman.desktop
install -Dm 755 target/release/spaceman %buildroot%_bindir/spaceman
install -Dm 755 spaceman.png %buildroot%_datadir/pixmaps/spaceman.png


%files
%doc LICENSE README.md
%_bindir/spaceman
%_datadir/applications/spaceman.desktop
%_datadir/pixmaps/spaceman.png

%changelog
* Tue Oct 10 2024 Dmitrii Chuprov <cheese@altlinux.org> 0.1.3-alt1
- Initial build for ALT.
