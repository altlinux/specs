%define exID noa11y@popov895.ukr.net
%define nameU noa11y

Name: gnome-shell-extension-noa11y
Version: 7.0
Release: alt3

Summary: Hides the accessibility button on the top bar

BuildArch: noarch

License: MIT
Group:  Graphical desktop/GNOME
Url: https://github.com/popov895/noa11y
VCS: https://github.com/popov895/noa11y

Source: %nameU-%version.tar

Requires: gnome-shell >= 47.0

%description
A simple GNOME extension that hides the accessibility button on the top bar.

%prep
%setup -n %nameU-%version

#fixed for Gnome 49
subst 's|"47"|"47", "48", "49", "50"|' metadata.json

%build
%install
install -d %buildroot%_datadir/gnome-shell/extensions/%exID
cp -a *.js *.json LICENSE %buildroot%_datadir/gnome-shell/extensions/%exID/

%files
%_datadir/gnome-shell/extensions/%exID/*
%doc *.md LICENSE 

%changelog
* Fri Mar 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 7.0-alt3
- fixed for GNOME 50

* Thu Oct 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 7.0-alt2
- fixed for GNOME 49

* Mon Jun 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 7.0-alt1
- Initial build for Sisyphus.

