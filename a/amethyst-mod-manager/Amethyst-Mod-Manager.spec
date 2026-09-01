%define _unpackaged_files_terminate_build 1
%define oname io.github.Amethyst.ModManager

Name: amethyst-mod-manager
Version: 2.4.0
Release: alt1

Summary: A Linux native mod manager for a variety of games
License: GPL-3.0-or-later
Group: Games/Other

Url: https://github.com/ChrisDKN/Amethyst-Mod-Manager
Vcs: https://github.com/ChrisDKN/Amethyst-Mod-Manager

Source: %name-%version.tar
Source1: vendor.tar

Patch: runapp.patch

ExcludeArch: %ix86

Requires: python3-module-certifi

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires(pre): rpm-macros-rust
BuildRequires: meson
BuildRequires: rpm-build-rust
BuildRequires: /usr/bin/appstreamcli
BuildRequires: libsqlite3-devel

%description
%summary.

%prep
%setup -a1
%patch -p0
%rust_prep

%build
pushd native/amethyst_filegraph
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
%rust_build
popd
mv native/amethyst_filegraph/target/release/libamethyst_filegraph.so \
    src/amethyst_filegraph.abi3.so
%meson
%meson_build

%install
%meson_install
install -d %buildroot%python3_sitelibdir/%name
mv -fv %buildroot/usr/lib/python3/site-packages/* %buildroot%python3_sitelibdir/%name/
rm -rf %buildroot/usr/lib

%files
%doc *.md Changelog.txt
%_bindir/*
%_desktopdir/%oname.desktop
%_iconsdir/hicolor/*/apps/%oname.png
%_datadir/metainfo/%oname.metainfo.xml
%python3_sitelibdir/%name
%exclude %_datadir/licenses
%exclude %_datadir/doc/

%changelog
* Tue Sep 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0

* Wed Aug 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.3.0-alt1
- Initial build.
