%def_disable snapshot

%define _name tilingshell
%define git_ver 15.1.0
%define ego_ver 99
%define beta %nil
%define uuid tilingshell@ferrarodomenico.com
%define xdg_name org.gnome.shell.extensions.%_name

%def_disable bootstrap

Name: gnome-shell-extension-%_name
Version: %ego_ver
Release: alt1%beta

%define gettext_domain %_name

Summary: Tiling Gnome Shell extension
Group: Graphical desktop/GNOME
License: GPL-2.0-only
Url: https://github.com/domferr/tilingshell

Vcs: https://github.com/domferr/tilingshell.git

#BuildArch: noarch
ExclusiveArch: x86_64

%if_disabled snapshot
Source: %url/archive/%version%beta/%name-%git_ver%beta.tar.gz
%else
Source: %_name-%git_ver%beta.tar
%endif
Source1: %_name-%git_ver-npm.tar

Requires: gnome-shell >= 44
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: npm eslint
#BuildRequires: esbuild
BuildRequires: /usr/bin/gjs
BuildRequires: /usr/bin/glib-compile-schemas /usr/bin/gapplication

%description
This is a Gnome Shell extension implementing modern windows tiling
system by extending GNOME's default 2 columns to any layout you want!
Can be installed on Gnome Shells on X11 and Wayland.

%prep
%setup -n %_name-%git_ver%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
npm install && npm audit fix &&
tar -cf %_name-%git_ver-npm.tar node_modules && \
mv %_name-%git_ver-npm.tar %_sourcedir/}

#Error: Cannot find package '/usr/src/RPM/BUILD/tilingshell-15.1.0/node_modules/esbuild/index.js' imported from /usr/src/RPM/BUILD/tilingshell-15.1.0/esbuild.mjs
#rm -rf node_modules/*esbuild
#mkdir -p node_modules/esbuild/bin/esbuild
#ln -sf %_bindir/esbuild node_modules/esbuild/bin/esbuild

%build
npm run build

%install
install -d -m 0755 %buildroot%_datadir/gnome-shell/extensions/%uuid
pushd dist
cp -p -r icons %buildroot%_datadir/gnome-shell/extensions/%uuid/
cp -p -r locale %buildroot%_datadir/locale
cp -a *.json *.js *.css %buildroot%_datadir/gnome-shell/extensions/%uuid/
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
* Sat Dec 21 2024 Yuri N. Sedunov <aris@altlinux.org> 99-alt1
- first build for Sisyphus


