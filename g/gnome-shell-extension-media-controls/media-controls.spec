%define exID mediacontrols@cliffniff.github.com
%define nameU media-controls
%define nameS org.gnome.shell.extensions.mediacontrols

Name: gnome-shell-extension-media-controls
Version: 2.1.0
Release: alt1

Summary: A mpris client for the Gnome shell

BuildArch: noarch

License: MIT
Group:  Graphical desktop/GNOME
Url: https://extensions.gnome.org/extension/4470/media-controls/
VCS: https://github.com/sakithb/media-controls

Source0: %nameU-%version.tar
Source1: node_modules.tar 

Requires: gnome-shell >= 47.0

BuildRequires(Pre): rpm-build-nodejs
BuildRequires: blueprint-compiler /usr/bin/gnome-extensions
BuildRequires: unzip %_bindir/glib-compile-schemas

%description
Show controls and information of the currently playing media in the panel.

%prep
%setup -n %nameU-%version -a1

%build
sh mediacontrols.sh release
mkdir -p dist/builds/ok/
unzip dist/builds/%exID.shell-extension.zip -d dist/builds/ok/

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%exID/
cd dist/builds/ok/
cp -p -r dbus helpers %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -p -r locale %buildroot%_datadir/locale
install -D -p -m 0644 \
    schemas/%nameS.gschema.xml \
    %buildroot%_datadir/glib-2.0/schemas/%nameS.gschema.xml
cp -p -r types utils %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -a *.json *.js *.css %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -a %nameS.gresource %buildroot%_datadir/gnome-shell/extensions/%exID/

%files
%_datadir/gnome-shell/extensions/%exID/*
%_datadir/glib-2.0/schemas/*.xml
%_datadir/locale/*/LC_MESSAGES/*.mo
%doc *.md LICENSE 

%changelog
* Thu Apr 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux.
