%def_enable snapshot

%define beta %nil
%define rdn_name sm.puri.Phosh.OskStub

# enabled by default
%def_disable default_osk
%def_enable man
%def_enable check

Name: phosh-osk-stub
Version: 0.41.1
Release: alt1%beta

Summary: Phosh OSK Stub
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/guidog/phosh-osk-stub

Vcs: https://gitlab.gnome.org/guidog/phosh-osk-stub.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/guidog/phosh-osk-stub/-/archive/v%version/%name-v%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif

Provides: osk-wayland

Requires: dconf
Requires: hunspell-en_US hunspell-ru-lebedev

BuildRequires(pre): rpm-macros-meson rpm-macros-alternatives
BuildRequires: meson
BuildRequires: /usr/bin/appstreamcli desktop-file-utils
BuildRequires: pkgconfig(gio-2.0) >= 2.68
BuildRequires: pkgconfig(gtk+-wayland-3.0) >= 3.22
BuildRequires: pkgconfig(libhandy-1) >= 1.5
BuildRequires: pkgconfig(wayland-client) >= 1.14
BuildRequires: pkgconfig(wayland-protocols) >= 1.12
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(libfeedback-0.0)
BuildRequires: pkgconfig(libsystemd)
# compliters: default -- hunspell
BuildRequires: pkgconfig(hunspell)
%{?_enable_man:BuildRequires: /usr/bin/rst2man}
%{?_enable_check:BuildRequires: at-spi2-core xvfb-run}
%description
Phosh OSK Stub in an experimental keyboard for quick prototyping and to
debug input related issues in phosh.

For a production ready on-screen keyboard see squeekboard.

The purpose of phosh-osk-stub:
- allow experimentation without the risk of breaking end user systems
- be helpful when debugging input-method related issues
- be quick and easy to (cross)compile
- allow to move GObject bits and Widgets over to squeekboard easily if
  desired (hence provide API documentation)

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_enable_man:-Dman=true} \
    %{?_disable_default_osk:-Ddefault_osk=false}
%nil
%meson_build

%install
%meson_install

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/osk-wayland	%_bindir/%name 80
EOF

%find_lang %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_bindir/%name
%_altdir/%name
%{?_enable_default_osk:%_desktopdir/sm.puri.OSK0.desktop}
%{?_disable_default_osk:%_desktopdir/%rdn_name.desktop}
%_datadir/glib-2.0/schemas/sm.puri.phosh.osk.enums.xml
%_datadir/glib-2.0/schemas/sm.puri.phosh.osk.gschema.xml
%{?_enable_man:%_man1dir/%name.1*}
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS


%changelog
* Wed Aug 21 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.1-alt1
- 0.41.1

* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt1
- 0.41.0

* Thu Aug 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt0.9.rc1
- 0.41.0.rc1

* Sat Apr 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0

* Thu Mar 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1
- 0.37.0

* Sat Feb 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.36.0-alt1
- 0.36.0

* Fri Jan 05 2024 Yuri N. Sedunov <aris@altlinux.org> 0.35.0-alt1
- 0.35.0

* Tue Dec 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt1
- 0.34.0

* Thu Nov 23 2023 Yuri N. Sedunov <aris@altlinux.org> 0.33.0-alt1
- first build for Sisyphus



