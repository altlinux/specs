%def_enable snapshot
%define ver_major 0.2
%define rdn_name null.daknig.dewduct

%def_disable bootstrap
%def_enable check

Name: dewduct
Version: %ver_major.2
Release: alt1

Summary: DewDuct is a Youtube player for Linux on desktop and mobile
License: GPL-3.0-or-later
Group: Video
Url: https://github.com/DaKnig/DewDuct

Vcs: https://github.com/DaKnig/DewDuct.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

Requires: mpv yt-dlp

BuildRequires(pre): rpm-build-rust
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: /usr/bin/appstreamcli

%description
DewDuct is a Youtube player for Linux on desktop and mobile.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build
appstreamcli make-desktop-file data/%rdn_name.metainfo.xml %rdn_name.desktop

%install
%rust_install
mkdir -p %buildroot%_datadir/{applications,metainfo}
install -p -m644 data/%rdn_name.metainfo.xml %buildroot%_datadir/metainfo/%rdn_name.metainfo.xml
appstreamcli make-desktop-file data/%rdn_name.metainfo.xml %buildroot%_datadir/applications/%rdn_name.desktop

%check
%rust_test

%files
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sat Jun 01 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- first build for Sisyphus (v0.2.2-3-g46e00d3)


