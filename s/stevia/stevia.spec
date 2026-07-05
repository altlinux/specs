%def_enable snapshot

%define _name stevia
%define binary_name phosh-osk-%_name
%define ver_major 0.56
%define beta %nil
%define rdn_name mobi.phosh.Stevia

# enabled by default
%def_disable default_osk
%def_disable gtk_doc
%def_enable man
%def_enable check

Name: %_name
Version: %ver_major.0
Release: alt1%beta

Summary: Stevia is a default keyboard for Phosh
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/World/Phosh/stevia

Vcs: https://gitlab.gnome.org/World/Phosh/stevia.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Phosh/stevia/-/archive/v%version/%name-v%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Patch1: stevia-0.49.0-alt-meson.patch

#Provides: osk-wayland
# required by Phosh >= 0.50 (ALT #56838)
Provides: %_userunitdir/mobi.phosh.OSK.service
Provides: %binary_name = %EVR
Conflicts: phosh-osk-stub
Obsoletes: phosh-osk-stub < 0.48
Provides: phosh-osk-stub = %EVR

%define gmobile_ver 0.2.0
%define gsds_ver 47
%define systemd_ver 241

Requires: dconf
Requires: hunspell-en_US hunspell-ru-lebedev
Requires: fzf words
Requires: varnam-schemes

BuildRequires(pre): rpm-macros-meson rpm-macros-alternatives
BuildRequires: meson
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= 2.68
BuildRequires: pkgconfig(gtk+-wayland-3.0) >= 3.22
BuildRequires: pkgconfig(gmobile) >= %gmobile_ver
BuildRequires: pkgconfig(libhandy-1) >= 1.5
BuildRequires: pkgconfig(wayland-client) >= 1.14
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= %gsds_ver
BuildRequires: pkgconfig(libfeedback-0.0)
BuildRequires: pkgconfig(dconf)
BuildRequires: pkgconfig(libsystemd) >= %systemd_ver
# compliters: default -- hunspell
BuildRequires: pkgconfig(hunspell)
# https://bugzilla.altlinux.org/54897
BuildRequires: fzf
BuildRequires: pkgconfig(govarnam)
# Japanese, Chinese and Korean support
#BuildRequires: pkgconfig(uim)
%{?_enable_gtk_doc:BuildRequires: gobject-introspection-devel gi-docgen}
%{?_enable_man:BuildRequires: /usr/bin/rst2man}
%{?_enable_check:BuildRequires: at-spi2-core xvfb-run words varnam-schemes}
%description
%{summary}.
The purpose of Stevia is:

- to allow experimentation without the risk of breaking end user systems
- be helpful when debugging input-method related issues
- be quick and easy to (cross)compile
- allow to move GObject bits and Widgets over to squeekboard easily if
  desired (hence provide API documentation)

Features:

- easy to swap out with squeekboard (implements phosh's [sm.puri.OSK0]() DBus
  interface) for low risk experimentation
- easy to temporarily replace running instance ('--replace' option)
- no language boundaries within the codebase to lower the entrance barrier
- use current GTK and GObject patterns (actions, bindings, ...)
- use GNOME libs and technologies wherever possible (GSettings, json-glib, ...)
- [character popover](https://gitlab.gnome.org/guidog/stevia/-/raw/main/screenshots/pos-popover.png)
- [emoji layout](https://gitlab.gnome.org/guidog/stevia/-/raw/main/screenshots/pos-emoji.png)
- cursor navigation via space-bar long-press
- word correction via hunspell
- use any program as completer via a 'pipe' completer ([Example](https://social.librem.one/@agx/110260534404795348))
- [word completion](https://social.librem.one/@agx/109428599061094716)
  based on the presage library
- experimental input of Indic languages using [varnam](https://github.com/varnamproject)
- allow for secondary completers to amend completion results
- allow to prevent keyboard unfold for certain apps (via app-id)
- allow to prevent keyboard unfold when a hardware keyboard is presen

%prep
%setup -n %name-%version%beta
%patch1

%build
%meson \
    %{subst_enable_meson_bool gtk_doc gtk_doc} \
    %{subst_enable_meson_bool man man} \
    %{subst_enable_meson_bool default_osk default_osk}
%nil
%meson_build

%install
%meson_install

%{?_disable_default_osk:
mv %buildroot%_userunitdir/%rdn_name.service \
    %buildroot%_datadir/%binary_name/

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_userunitdir/mobi.phosh.OSK.service	%_datadir/%binary_name/%rdn_name.service 80
EOF
}

%find_lang --output=%name.lang %binary_name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_bindir/%binary_name
%{?_enable_default_osk:%_desktopdir/sm.puri.OSK0.desktop
%_userunitdir/mobi.phosh.OSK.service}
%{?_disable_default_osk:%_desktopdir/%rdn_name.desktop
%_datadir/%binary_name/%rdn_name.service
%_altdir/%_name}
%dir %_datadir/%binary_name
%_datadir/%binary_name/layouts.json
%dir %_datadir/%binary_name/completers
%_datadir/%binary_name/completers/hunspell.completer
%_datadir/glib-2.0/schemas/mobi.phosh.osk.enums.xml
%_datadir/glib-2.0/schemas/mobi.phosh.osk.gschema.xml
%{?_enable_man:%_man1dir/%binary_name.1*}
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS


%changelog
* Sun Jul 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.56.0-alt1
- 0.56.0

* Mon May 18 2026 Yuri N. Sedunov <aris@altlinux.org> 0.55.0-alt1
- 0.55.0

* Sat Apr 04 2026 Yuri N. Sedunov <aris@altlinux.org> 0.54.0-alt1
- 0.54.0

* Sat Feb 14 2026 Yuri N. Sedunov <aris@altlinux.org> 0.53.0-alt1
- 0.53.0

* Fri Jan 16 2026 Yuri N. Sedunov <aris@altlinux.org> 0.52.1-alt1
- 0.52.1

* Sat Jan 03 2026 Yuri N. Sedunov <aris@altlinux.org> 0.52.0-alt1
- 0.52.0

* Sun Nov 16 2025 Yuri N. Sedunov <aris@altlinux.org> 0.51.0-alt1.1
- tried to fix mobi.phosh.OSK alternative to avoid duplicate names

* Sat Nov 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.51.0-alt1
- 0.51.0

* Mon Oct 13 2025 Yuri N. Sedunov <aris@altlinux.org> 0.50.1-alt1
- 0.50.1

* Mon Oct 06 2025 Yuri N. Sedunov <aris@altlinux.org> 0.50.0-alt1
- 0.50.0

* Fri Aug 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.49.0-alt1
- 0.49.0

* Sat Jun 28 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48.0-alt1
- 0.48.0

* Mon Jun 23 2025 Yuri N. Sedunov <aris@altlinux.org> 0.48-alt0.9.rc1
- first build for Sisyphus



