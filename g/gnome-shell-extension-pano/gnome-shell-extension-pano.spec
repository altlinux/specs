%def_enable snapshot

%define _name pano
%define __name gnome-shell-%_name
%define ver_major 23
%define beta .alpha3
%define uuid pano@elhan.io
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain %uuid

%def_disable bootstrap

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt0.1%beta

Summary: Next-gen Clipboard manager for Gnome Shell
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://github.com/oae/gnome-shell-pano

Vcs: https://github.com/oae/gnome-shell-pano.git

#Error: Your current platform "linux" and architecture "ia32" combination is not yet supported by the native Rollup build.
ExclusiveArch: x86_64
BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%_name-%version%beta.tar.gz
%else
Source: %__name-%version%beta.tar
%endif
Source1: %_name-%version%beta-node.tar

Requires: gnome-shell >= 45
Requires: typelib(Adw) = 1
Requires: typelib(Gda) = 6.0
Requires: libgda6-sqlite
Requires: typelib(Soup) = 3.0
Requires: typelib(GSound) = 1.0

BuildRequires: yarn node /proc
BuildRequires: /usr/bin/glib-compile-schemas

%description
%summary

%prep
%setup -n %__name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:yarn install
tar cf %_sourcedir/%_name-%version%beta-node.tar node_modules/}

%build
yarn run --offline build

%install
# install main extension files
install -d -m 0755 %buildroot%_datadir/gnome-shell/extensions/%uuid
pushd dist
cp -p -r dbus images thirdparty icons %buildroot%_datadir/gnome-shell/extensions/%uuid
cp -p -r locale %buildroot%_datadir/locale
cp -a *.json *.js *.css %buildroot%_datadir/gnome-shell/extensions/%uuid/
# install the schema file
install -D -p -m 0644 \
    schemas/%xdg_name.gschema.xml \
    %buildroot%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
popd


%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Thu Oct 03 2024 Yuri N. Sedunov <aris@altlinux.org> 23-alt0.1.alpha3
- v23-alpha3

* Tue Mar 26 2024 Yuri N. Sedunov <aris@altlinux.org> 22-alt2
- updated to v22-7-gf1756e4 (gnome-46 supported)

* Fri Nov 17 2023 Yuri N. Sedunov <aris@altlinux.org> 22-alt1
- 22

* Sun Nov 5 2023 Yuri N. Sedunov <aris@altlinux.org> 20-alt1
- first build for Sisyphus

