Name: an-anime-game-launcher
Version: 3.13.0
Release: alt1

Summary: An Anime Game launcher for Linux with telemetry disabling
License: GPL-3.0
Group: Games/Other
Url: https://github.com/an-anime-team/an-anime-game-launcher

Source: %name-%version.tar
Source1: vendor.tar
Source2: %name.desktop
Source3: icon.png

BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: libgtk4-devel
BuildRequires: libadwaita-devel

%description
%summary.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/an-anime-team/anime-game-core?tag=1.25.1"]
git = "https://github.com/an-anime-team/anime-game-core"
tag = "1.25.1"
replace-with = "vendored-sources"

[source."git+https://github.com/an-anime-team/anime-launcher-sdk?tag=1.22.0"]
git = "https://github.com/an-anime-team/anime-launcher-sdk"
tag = "1.22.0"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
cargo build %_smp_mflags --offline --release

%install
#.desktop and icons
mkdir -p %buildroot%_iconsdir
install -Dm644 %SOURCE3 %buildroot%_datadir/pixmaps/%name.png
ln -sf %_datadir/pixmaps/%name.png %buildroot%_iconsdir/moe.launcher.%name.png
install -Dm644 %SOURCE2 %buildroot%_datadir/applications/%name.desktop
  
#resource
mkdir -p %buildroot%_libdir/%name
cp -v target/release/anime-game-launcher %buildroot%_libdir/%name

#symlink to bin
mkdir -p %buildroot%_bindir
ln -sf %_libdir/%name/anime-game-launcher %buildroot%_bindir/%name

%check
#has no tests

%files
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%_iconsdir/moe.launcher.%name.png
%_libdir/%name

%changelog
* Fri Nov 01 2024 Anton Kurachenko <srebrov@altlinux.org> 3.13.0-alt1
- Initial build for Sisyphus.
