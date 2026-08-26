%define _unpackaged_files_terminate_build 1
%define oname io.github.Amethyst.ModManager

Name: amethyst-mod-manager
Version: 2.3.0
Release: alt1

Summary: A Linux native mod manager for a variety of games
License: GPL-3.0-or-later
Group: Games/Other

Url: https://github.com/ChrisDKN/Amethyst-Mod-Manager
Vcs: https://github.com/ChrisDKN/Amethyst-Mod-Manager

BuildArch: noarch
AutoProv: nopython3

Source: %name-%version.tar

Patch: runapp.patch

%add_python3_path %_datadir/%name

Requires: python3-module-certifi

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: meson
BuildRequires: /usr/bin/appstreamcli

%description
%summary.

%prep
%setup
%patch -p0

%build
%meson
%meson_build

%install
%meson_install
install -d %buildroot%_datadir/%name
mv -fv %buildroot/usr/lib/python3/site-packages/* %buildroot%_datadir/%name/
rm -rf %buildroot/usr/lib

%files
%doc *.md
%_bindir/*
%_desktopdir/%oname.desktop
%_iconsdir/hicolor/*/apps/%oname.png
%_datadir/metainfo/%oname.metainfo.xml
%_datadir/%name
%exclude %_datadir/licenses
%exclude %_datadir/doc/

%changelog
* Wed Aug 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.3.0-alt1
- Initial build.
