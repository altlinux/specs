%define rname honkers-railway-launcher
%define fname moe.launcher.the-honkers-railway-launcher

Name:    the-honkers-railway-launcher
Version: 1.15.1
Release: alt1

Summary: The Honkers Railway launcher for Linux with automatic patching and telemetry disabling
License: GPL-3.0-or-later
Group:   Games/Other
URL:     https://github.com/an-anime-team/the-honkers-railway-launcher
VCS:     https://github.com/an-anime-team/the-honkers-railway-launcher

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

# Out of memory
ExcludeArch: i586

BuildRequires(pre): rpm-build-rust
BuildRequires: libadwaita-devel
BuildRequires: protobuf-compiler
BuildRequires: /proc

Requires: git-core
Requires: p7zip
Requires: gst-plugins-base1.0
Requires: cabextract

%description
%summary.

%prep
%setup -a1
install -vpD %SOURCE2 .cargo/config.toml

sed -i 's/Exec=AppRun/Exec=%rname/' assets/%rname.desktop
sed -i 's/Icon=icon/Icon=%rname/' assets/%rname.desktop
echo 'StartupWMClass=moe.laucher.%name' >> assets/%rname.desktop

%build
%rust_build

%install
install -Dm755 target/release/%rname -t %buildroot%_bindir
install -Dm644 assets/%rname.desktop -t %buildroot%_desktopdir
install -Dm644 assets/images/icon.png %buildroot%_iconsdir/%fname.png
install -Dm644 assets/images/icon.png %buildroot%_pixmapsdir/%rname.png
install -Dm644 assets/%fname.metainfo.xml -t %buildroot%_datadir/metainfo

# %check
# there is no tests for now

%files
%doc *.md
%_bindir/%rname
%_desktopdir/%rname.desktop
%_iconsdir/%fname.png
%_pixmapsdir/%rname.png
%_datadir/metainfo/%fname.metainfo.xml

%changelog
* Wed Jun 10 2026 Ilya Sorochan <k0tran@altlinux.org> 1.15.1-alt1
- Update version.

* Thu May 28 2026 Ilya Sorochan <k0tran@altlinux.org> 1.15.0-alt1
- Initial build for Sisyphus.

