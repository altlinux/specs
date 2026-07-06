Name: an-anime-game-launcher
Version: 3.19.7
Release: alt1

Summary: An Anime Game launcher for Linux with telemetry disabling
License: GPL-3.0
Group: Games/Other
Url: https://github.com/an-anime-team/an-anime-game-launcher
Vcs: https://github.com/an-anime-team/an-anime-game-launcher.git

ExclusiveArch: x86_64

Source: %name-%version.tar
Source1: vendor.tar
Source2: %name.desktop
Source3: icon.png

BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: libgtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: libssl-devel
BuildRequires: protobuf-compiler
Requires: git-core
Requires: p7zip

%description
%summary.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/an-anime-team/anime-game-core?tag=1.38.8"]
git = "https://github.com/an-anime-team/anime-game-core"
tag = "1.38.8"
replace-with = "vendored-sources"

[source."git+https://github.com/an-anime-team/anime-launcher-sdk?tag=1.35.10"]
git = "https://github.com/an-anime-team/anime-launcher-sdk"
tag = "1.35.10"
replace-with = "vendored-sources"

[source."git+https://github.com/dawn-winery/sophon-tools.git?tag=v0.1.6"]
git = "https://github.com/dawn-winery/sophon-tools.git"
tag = "v0.1.6"
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
* Mon Jul 06 2026 Anton Kurachenko <srebrov@altlinux.org> 3.19.7-alt1
- New version 3.19.7.

* Sat May 16 2026 Anton Kurachenko <srebrov@altlinux.org> 3.19.4-alt1
- New version 3.19.4.

* Sun May 10 2026 Anton Kurachenko <srebrov@altlinux.org> 3.19.3-alt1
- New version 3.19.3.

* Sun May 03 2026 Anton Kurachenko <srebrov@altlinux.org> 3.19.1-alt1
- New version 3.19.1.

* Sat Nov 15 2025 Anton Kurachenko <srebrov@altlinux.org> 3.18.0-alt1
- New version 3.18.0.

* Sun Sep 21 2025 Anton Kurachenko <srebrov@altlinux.org> 3.17.0-alt1
- New version 3.17.0.

* Fri Sep 05 2025 Anton Kurachenko <srebrov@altlinux.org> 3.15.6-alt2
- Dropped aarch64 build (Closes: #55875).

* Sat Aug 23 2025 Anton Kurachenko <srebrov@altlinux.org> 3.15.6-alt1
- New version 3.15.6.

* Thu Aug 14 2025 Anton Kurachenko <srebrov@altlinux.org> 3.15.5-alt1
- New version 3.15.5.

* Tue Jul 29 2025 Anton Kurachenko <srebrov@altlinux.org> 3.15.2-alt1
- New version 3.15.2.

* Mon Jul 28 2025 Anton Kurachenko <srebrov@altlinux.org> 3.15.1-alt1
- New version 3.15.1.

* Tue Jul 22 2025 Anton Kurachenko <srebrov@altlinux.org> 3.15.0-alt1
- New version 3.15.0.

* Mon Jun 23 2025 Anton Kurachenko <srebrov@altlinux.org> 3.14.3-alt1
- New version 3.14.3.

* Wed Jun 18 2025 Anton Kurachenko <srebrov@altlinux.org> 3.14.2-alt1
- New version 3.14.2.

* Sat May 24 2025 Anton Kurachenko <srebrov@altlinux.org> 3.14.1-alt1
- New version 3.14.1.

* Tue May 13 2025 Anton Kurachenko <srebrov@altlinux.org> 3.14.0-alt1
- New version 3.14.0.
- Added VCS tag.

* Tue Apr 29 2025 Anton Kurachenko <srebrov@altlinux.org> 3.13.1-alt2
- Added git-core, p7zip and libwebp-tools to Requires (Closes: #54029).

* Sun Apr 27 2025 Anton Kurachenko <srebrov@altlinux.org> 3.13.1-alt1
- New version 3.13.1.

* Fri Nov 01 2024 Anton Kurachenko <srebrov@altlinux.org> 3.13.0-alt1
- Initial build for Sisyphus.
