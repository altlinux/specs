%define exID hideaccessibilitymenu@boni.scot

Name: gnome-shell-extension-hide-accessibility-menu
Version: 50.0
Release: alt1

Summary: Hide accessibility menu GNOME extension
License: GPL-3.0-or-later and GPL-2.0-or-later
Group:  Graphical desktop/GNOME

Url: https://gitlab.com/boniboyblue/gnome-shell-extension-hide-accessibility-menu
VCS: https://gitlab.com/boniboyblue/gnome-shell-extension-hide-accessibility-menu

BuildArch: noarch
Obsoletes: gnome-shell-extension-noa11y <= 7.0-alt3

Source: %name-%version.tar

Requires: gnome-shell >= 47.0

%description
Hide the accessibility menu icon on panel when running an accessibility option.

%prep
%setup

%build
%install
install -d %buildroot%_datadir/gnome-shell/extensions/%exID
cp -a *.js *.json %buildroot%_datadir/gnome-shell/extensions/%exID/

%files
%_datadir/gnome-shell/extensions/%exID/*
%doc *.md LICENSE 

%changelog
* Sat Mar 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 50.0-alt1
- Initial build.

