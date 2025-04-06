%define xdg_name es.danirod.Cartero

Name: cartero
Version: 0.2.1
Release: alt1
License: GPL-3.0

Summary: Make HTTP requests and test APIs

Group: Graphical desktop/Other

Url: https://github.com/danirod/cartero
Vcs: https://github.com/danirod/cartero.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-rust
BuildRequires: meson blueprint-compiler
BuildRequires: /proc

BuildRequires: gir(GtkSource) = 5

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(libadwaita-1)

BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libcurl)

%description
Cartero is a graphical HTTP client that can be used as a developer
tool to test web APIs and perform all kind of HTTP requests to web
servers. It is compatible with any REST, SOAP or XML-RPC API and it
supports multiple request methods as well as attaching body payloads
to compatible requests.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
export CFLAGS="-I%_includedir/curl"
export LDFLAGS="-L%_libdir -lcurl"
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/appdata/%xdg_name.appdata.xml
%_datadir/mime/packages/%xdg_name.xml
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_iconsdir/hicolor/*/mimetypes/*.svg

%changelog
* Sun Apr 06 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.1-alt1
- new version 0.2.1 (with rpmrb script)

* Thu Mar 27 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- new version (0.2.0) with rpmgs script

* Sun Feb 16 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.5-alt1
- new version 0.1.5 (with rpmrb script)

* Fri Jan 31 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.4-alt1
- Initial build
