Name: czkawka
Version: 8.0.0
Release: alt1
License: MIT
Group: File tools
Summary: A simple, fast and free app to remove unnecessary files
Url: https://github.com/qarmin/czkawka
Source0: %name-%version.tar

BuildRequires: rpm-build-rust
BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: hicolor-icon-theme
BuildRequires: libraw-devel
BuildRequires: libheif-devel
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(pango)

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
License:        MIT
Group:          File tools
Summary:        Slint frontend of Czkawka

%description -n %name-krokiet
Krokiet is new Czkawka frontend written in Slint, which uses Rust in
opposite to Gtk 4 frontend which uses mostly C code.

%prep
%setup
mkdir -p .cargo
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

%build
cargo build %_smp_mflags --offline --release

%install
install -Dm755 target/release/%{name}_{cli,gui} -t %buildroot%_bindir
install -Dm755 target/release/krokiet -t %buildroot%_bindir
install -Dm644 data/icons/com.github.qarmin.czkawka{,.Devel}.svg -t %buildroot%_datadir/icons/hicolor/scalable/apps
install -Dm644 data/icons/com.github.qarmin.czkawka-symbolic.svg -t %buildroot%_datadir/icons/hicolor/symbolic/apps
install -Dm644 data/com.github.qarmin.czkawka.desktop -t %buildroot%_datadir/applications
install -Dm644 data/com.github.qarmin.czkawka.metainfo.xml -t %buildroot%_datadir/metainfo

%files
%doc %{name}_gui/LICENSE README.md instructions/Instruction.md Changelog.md
%_bindir/%{name}_gui
%_datadir/icons/hicolor/scalable/apps/*.svg
%_datadir/icons/hicolor/symbolic/apps/*.svg
%_datadir/applications/com.github.qarmin.czkawka.desktop
%_datadir/metainfo/com.github.qarmin.czkawka.metainfo.xml

%files -n %name-cli
%doc %{name}_cli/README.md
%_bindir/%{name}_cli

%files -n %name-krokiet
%doc krokiet/README.md
%_bindir/krokiet

%changelog
* Wed Oct 23 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 8.0.0-alt1
- update version

* Mon Jun 10 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 7.0.0-alt2
- correct packages name

* Tue Feb 20 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 7.0.0-alt1
- update version

* Fri Nov 03 2023 Ratkin Daniil-Vitkor <krf10@altlinux.org> 6.1.0-alt1
- Initial build for ALT Linux

