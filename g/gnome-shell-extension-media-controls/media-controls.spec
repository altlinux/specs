%define exID mediacontrols@cliffniff.github.com
%define nameU media-controls
%define nameS org.gnome.shell.extensions.mediacontrols

Name: gnome-shell-extension-media-controls
Version: 2.4.4
Release: alt2

Summary: A mpris client for the Gnome shell

BuildArch: noarch

License: MIT
Group:  Graphical desktop/GNOME
Url: https://extensions.gnome.org/extension/4470/media-controls/
VCS: https://github.com/sakithb/media-controls

ExcludeArch: i586

Source0: %nameU-%version.tar
Source1: node_modules.tar 

Requires: gnome-shell >= 48.0

BuildRequires(Pre): rpm-build-nodejs
#BuildRequires: blueprint-compiler
BuildRequires: /usr/bin/gnome-extensions
BuildRequires: unzip %_bindir/glib-compile-schemas node npm

%description
Show controls and information of the currently playing media in the panel.

%prep
%setup -n %nameU-%version -a1
rm pnpm-lock.yaml
sed -i 's/pnpm/npm/g' package.json

subst 's|"49"|"49", "50"|' src/metadata.json

%build
npm run build
mkdir -p dist/builds/ok/
unzip dist/builds/%exID.shell-extension.zip -d dist/builds/ok/

%install
install -d %buildroot%_datadir/gnome-shell/extensions/%exID
cd dist/builds/ok/
cp -p -r helpers types utils %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -p -r locale %buildroot%_datadir/locale
install -D -p -m 0644 \
    schemas/%nameS.gschema.xml \
    %buildroot%_datadir/glib-2.0/schemas/%nameS.gschema.xml
cp -a *.json *.js *.css %buildroot%_datadir/gnome-shell/extensions/%exID/
cp -a %nameS.gresource %buildroot%_datadir/gnome-shell/extensions/%exID/

%files
%_datadir/gnome-shell/extensions/%exID/*
%_datadir/glib-2.0/schemas/*.xml
%_datadir/locale/*/LC_MESSAGES/*.mo
%doc *.md LICENSE 

%changelog
* Fri Mar 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.4.4-alt2
- fixed for GNOME 50

* Thu Feb 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.4.4-alt1
- 2.4.3 -> 2.4.4

* Sun Jan 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.4.3-alt1
- 2.4.2 -> 2.4.3

* Tue Jan 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.4.2-alt1
- 2.4.1 -> 2.4.2

* Fri Dec 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1

* Thu Dec 11 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0

* Mon Dec 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.3.0-alt1
- 2.2.0 -> 2.3.0

* Thu Oct 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.0-alt3
- update to git.c6d1e16

* Sat Jul 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.0-alt2
- only for Gnome 48 or later

* Tue Jul 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.2.0-alt1
- 2.1.0 -> 2.2.0

* Sun Jun 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.1.0-alt2
- Fix FTBFS: exclude i586 arch due to idle time limit exceeded.

* Thu Apr 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux.
