%define exID status-area-horizontal-spacing@mathematical.coffee.gmail.com
%define nameU status-area-horizontal-spacing
%define nameS org.gnome.shell.extensions.status-area-horizontal-spacing

Name: gnome-shell-extension-status-area-horizontal-spacing
Version: 2.9.3
Release: alt2

Summary: Reduces the horizontal spacing between icons/indicators in the status area

BuildArch: noarch

License: GPL-2.0-only
Group:  Graphical desktop/GNOME
Url: https://gitlab.com/p91paul/status-area-horizontal-spacing-gnome-shell-extension
VCS: https://gitlab.com/p91paul/status-area-horizontal-spacing-gnome-shell-extension

Source: %nameU-%version.tar

Requires: gnome-shell >= 47.0

%description
A GNOME shell extension that reduces the horizontal spacing between icons/indicators in the status area.

%prep
%setup -n %nameU-%version

subst 's|"49"|"49", "50"|' %exID/metadata.json

%build
%install
install -d %buildroot%_datadir/gnome-shell/extensions/%exID
cd %exID
install -D -p -m 0644 \
    schemas/%nameS.gschema.xml \
    %buildroot%_datadir/glib-2.0/schemas/%nameS.gschema.xml
cp -a *.js *.json %buildroot%_datadir/gnome-shell/extensions/%exID/

%files
%_datadir/gnome-shell/extensions/%exID/*
%_datadir/glib-2.0/schemas/*.xml
%doc *.md LICENSE 

%changelog
* Fri Mar 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.9.3-alt2
- fixed for GNOME 50

* Sun Oct 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.9.3-alt1
- 2.9.1 -> 2.9.3

* Mon Jun 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.9.1-alt1
- Initial build for Sisyphus (git.4759e3b111).

