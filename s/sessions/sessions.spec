%define app_id com.pojtinger.felicitas.Sessions
%define import_path github.com/pojntfx/sessions

Name: sessions
Version: 0.1.15
Release: alt2

Summary: Focus with timed work intervals
License: AGPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/pojntfx/sessions/
Vcs: https://github.com/pojntfx/sessions/

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-vendor.tar
Patch: %name-%version-alt.patch
Patch1: sessions-0.1.15-alt-build.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: appstream
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(graphene-1.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: gettext-tools
BuildRequires: /usr/bin/glib-compile-resources
BuildRequires: /usr/bin/glib-compile-schemas

%description
Sessions is a simple visual timer application designed specifically for the
pomodoro technique, helping you stay productive by breaking work into focused
sessions with regular breaks.

It enables you to:
- Start focused work sessions with customizable timer durations
- Track your progress with a clean, distraction-free interface
- Take regular breaks to maintain productivity

%prep
%setup -a 1
%patch -p 1
%patch1 -p0

%build
go generate ./...

export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

desktop-file-install --dir=%buildroot/%_datadir/applications assets/meta/%app_id.desktop

install -D -m 0644 assets/resources/metainfo.xml %buildroot%_datadir/metainfo/%app_id.metainfo.xml
install -D -m 0644 assets/meta/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%app_id.svg
install -D -m 0644 assets/resources/index.gschema.xml %buildroot%_datadir/glib-2.0/schemas/%app_id.gschema.xml
install -D -m 0644 assets/resources/index.gresource %buildroot%_datadir/%name/%app_id.gresource

mkdir -p %buildroot%_datadir/locale

pushd .build/src/%import_path/po
rm -v *.po *.pot *.go LINGUAS
cp -p -r * %buildroot%_datadir/locale/
popd

%find_lang --with-gnome %name

%files -f %name.lang
%attr(401,root,root) %_bindir/%name
%_datadir/applications/com.pojtinger.felicitas.Sessions.desktop
%_iconsdir/hicolor/scalable/apps/com.pojtinger.felicitas.Sessions.svg
%_datadir/metainfo/com.pojtinger.felicitas.Sessions.metainfo.xml
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/%name
%doc README.md

%changelog
* Fri Apr 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.15-alt2
- fixed permissions for normally native work, not flatpak

* Thu Apr 02 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.15-alt1
- 0.1.3 -> 0.1.15 (git.2662231d6e)

* Wed Aug 13 2025 x1z53 <x1z53@altlinux.org> 0.1.3-alt1
- Initial build

