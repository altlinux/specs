%define _unpackaged_files_terminate_build 1

%def_with check

Name: noctalia
Version: 5.1.0
Release: alt1

Summary: A sleek, customizable desktop shell crafted for Wayland
License: MIT
Group: Graphical desktop/Other

Url: https://docs.noctalia.dev
VCS: https://github.com/noctalia-dev/noctalia

Source: %name-%version.tar
Source1: %name.service
Patch0: %name-%version-alt.patch

# PACKAGING.md#runtime
Requires: pipewire
Requires: wireplumber
Requires: git-core

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson ninja-build gcc-c++
BuildRequires: libpam0-devel
BuildRequires: libstb-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-ft)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(jemalloc)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libical)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libjxl_threads)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libsodium)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libwebpdemux)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(md4c)
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(sdbus-c++)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(tomlplusplus)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wireplumber-0.5)
BuildRequires: pkgconfig(xkbcommon)

%if_with check
# for tests: annotation_raster needs a real "Sans" font
BuildRequires: fonts-ttf-dejavu
%endif

%add_findreq_skiplist %_datadir/noctalia/assets/templates/*/*.sh

%description
Noctalia is a full desktop shell for Wayland: bars, dock, launcher,
notifications, lock screen, wallpaper, settings and more. No Qt or GTK,
the UI is rendered with Wayland and OpenGL ES.

%prep
%setup
%patch0 -p1
%ifarch %ix86 armh
# libical 3.0 reads only the 32-bit TZif v1 block when time_t is 32-bit,
# and slim tzdata leaves that block empty: every TZID resolves as UTC.
sed -i "/^    'ical_parser',$/d" meson.build
%endif

%build
%meson -Dtests=enabled \
       -Djemalloc=enabled \
       -Db_ndebug=true
%meson_build

%install
%meson_install

%__builddir/noctalia completions bash > noctalia.bash
%__builddir/noctalia completions zsh > _noctalia
%__builddir/noctalia completions fish > noctalia.fish
install -Dm644 noctalia.bash %buildroot%_datadir/bash-completion/completions/noctalia
install -Dm644 _noctalia %buildroot%_datadir/zsh/site-functions/_noctalia
install -Dm644 noctalia.fish %buildroot%_datadir/fish/vendor_completions.d/noctalia.fish

install -Dm644 %SOURCE1 %buildroot%_userunitdir/noctalia.service

%check
%meson_test

%files
%doc LICENSE README.md
%_bindir/noctalia
%_datadir/noctalia
%_desktopdir/dev.noctalia.Noctalia.desktop
%_iconsdir/hicolor/scalable/apps/noctalia.svg
%_datadir/bash-completion/completions/noctalia
%_datadir/zsh/site-functions/_noctalia
%_datadir/fish/vendor_completions.d/noctalia.fish
%_userunitdir/noctalia.service

%changelog
* Thu Sep 17 2026 Egor Ignatov <egori@altlinux.org> 5.1.0-alt1
- First build for ALT.
