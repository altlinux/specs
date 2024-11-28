%def_disable snapshot

%define _name ddterm
%define ver_major 55
%define beta %nil
%define uuid %_name@amezin.github.com
%define xdg_name com.github.amezin.%_name

%def_disable check

%def_disable bootstrap

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt0.9%beta

%define gettext_domain %name

Summary: Drop Down Terminal Extension for GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/ddterm/gnome-shell-extension-ddterm

Vcs: https://github.com/ddterm/gnome-shell-extension-ddterm.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif
Source1: %name-%version-npm.tar
Patch1: %name-%version-alt-no_npm.patch

Requires: gnome-shell >= 47
Requires: typelib(Adw) = 1 typelib(Vte) = 3.91

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson npm xvfb-run
BuildRequires: /usr/bin/gjs
BuildRequires: /usr/bin/gtk-builder-tool /usr/bin/gtk4-builder-tool
BuildRequires: /usr/bin/glib-compile-schemas /usr/bin/gapplication xsltproc
%{?_enable_check:BuildRequires: eslint desktop-file-utils /usr/bin/appstreamcli}

%description
%summary

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%patch1 -b .no_npm
%{?_enable_bootstrap:
npm install && npm audit fix &&
tar -cf %name-%version-npm.tar node_modules && \
mv %name-%version-npm.tar %_sourcedir/}

%build
mkdir -p %__builddir && touch %__builddir/npm-install.stamp
export DDTERM_POST_INSTALL_STAMP=${PWD}/%__builddir/npm-install.stamp
%meson
xvfb-run %meson_build

%install
%meson_install
%find_lang %gettext_domain

%check
xvfb-run %__meson_test

%files -f %gettext_domain.lang
%_bindir/%xdg_name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Thu Nov 28 2024 Yuri N. Sedunov <aris@altlinux.org> 55-alt0.9
- first build for Sisyphus


