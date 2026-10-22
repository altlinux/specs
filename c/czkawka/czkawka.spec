Name: czkawka
Version: 12.0.2
Release: alt1
License: MIT
Group: File tools
Summary: A simple, fast and free app to remove unnecessary files
Url: https://github.com/qarmin/czkawka
Source0: %name-%version.tar
Source1: clear_icons-%version.tar

BuildRequires: rpm-build-rust
BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: hicolor-icon-theme
BuildRequires: libraw-devel
BuildRequires: libheif-devel
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel

ExcludeArch: %ix86 armh aarch64

%description
Czkawka ("hiccup" in Polish) is a simple, fast
and free app to remove unnecessary files from your computer.

%package -n %name-cli
License:        MIT
Group:          File tools
Summary:        CLI frontend of Czkawka

%description -n %name-cli
CLI frontend of Czkawka.

%package -n %name-krokiet
Group:          File tools
Summary:        Slint frontend of Czkawka
Provides:       %name = %version-%release
Obsoletes:      %name < %version-%release

%description -n %name-krokiet
Krokiet is new Czkawka frontend written in Slint, which uses Rust in
opposite to Gtk 4 frontend which uses mostly C code.

%prep
%setup
cat >> .cargo/config.toml << EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false

EOF

tar -xf %SOURCE1 -C .
cp -f clear_icons-%version/* krokiet/icons/

%build
cargo build %_smp_mflags --offline --release -p czkawka_cli -p krokiet

%install
install -Dm755 target/release/czkawka_cli -t %buildroot%_bindir
install -Dm755 target/release/krokiet -t %buildroot%_bindir
install -Dm644 data/icons/io.github.qarmin.krokiet.svg -t %buildroot%_datadir/icons/hicolor/scalable/apps
install -Dm644 data/io.github.qarmin.krokiet.desktop -t %buildroot%_datadir/applications
install -Dm644 data/io.github.qarmin.krokiet.metainfo.xml -t %buildroot%_datadir/metainfo

%files -n %name-cli
%doc %{name}_cli/README.md
%_bindir/%{name}_cli

%files -n %name-krokiet
%doc krokiet/LICENSE_* krokiet/README.md
%_bindir/krokiet
%_datadir/icons/hicolor/scalable/apps/io.github.qarmin.krokiet.svg
%_datadir/applications/io.github.qarmin.krokiet.desktop
%_datadir/metainfo/io.github.qarmin.krokiet.metainfo.xml

%changelog
* Wed Oct 21 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 12.0.2-alt1
- update version, stop package deprecating gtk gui

* Mon Apr 06 2026 Daniil-Viktor Ratkin <krf10@altlinux.org> 11.0.1-alt1
- update version

* Wed Oct 23 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 8.0.0-alt1
- update version

* Mon Jun 10 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 7.0.0-alt2
- correct packages name

* Tue Feb 20 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 7.0.0-alt1
- update version

* Fri Nov 03 2023 Ratkin Daniil-Vitkor <krf10@altlinux.org> 6.1.0-alt1
- Initial build for ALT Linux

