Name:    SGDBoop
Version: 1.4.1
Release: alt1

Summary: A program used for applying custom artwork to Steam using SteamGridDB
License: Zlib
Group:   Games/Other
URL:     https://www.steamgriddb.com/boop
VCS:     https://github.com/SteamGridDB/SGDBoop

Source: %name-%version.tar

BuildRequires: gcc make pkg-config libgtk+3-devel libcurl-devel

%description
SGDBoop is a tool that automatically applies assets from SteamGridDB directly
to your Steam library, removing the need to download and set them manually.

%prep
%setup

%build
%make_build

%install
install -Dm755 SGDBoop %buildroot%_bindir/SGDBoop

install -Dm644 res/linux/com.steamgriddb.SGDBoop.desktop \
%buildroot%_desktopdir/com.steamgriddb.SGDBoop.desktop

install -Dm644 res/com.steamgriddb.SGDBoop.svg \
%buildroot%_iconsdir/hicolor/scalable/apps/com.steamgriddb.SGDBoop.svg

install -Dm644 com.steamgriddb.SGDBoop.appdata.xml \
%buildroot%_datadir/metainfo/com.steamgriddb.SGDBoop.appdata.xml

%files
%doc LICENSE README.md
%_bindir/SGDBoop
%_desktopdir/com.steamgriddb.SGDBoop.desktop
%_iconsdir/hicolor/scalable/apps/com.steamgriddb.SGDBoop.svg
%_datadir/metainfo/com.steamgriddb.SGDBoop.appdata.xml

%changelog
* Wed Jul 29 2026 Sergey Palcheh <minergenon@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
