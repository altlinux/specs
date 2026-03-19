%define oname allowlockedremotedesktop@kamens.us

Name: gnome-shell-extension-allowlockedremotedesktop
Version: 5000
Release: alt1

Summary: Allow remote desktop connections when the screen is locked

License: GPL-2.0-or-later
Group: Graphical desktop/GNOME

Url: https://extensions.gnome.org/extension/4338/allow-locked-remote-desktop
Vcs: https://github.com/jikamens/allow-locked-remote-desktop

BuildArch: noarch

Source: %name-%version.tar

Requires: gnome-shell >= 45.0

BuildRequires: /usr/bin/gnome-extensions unzip

%description
GNOME Shell extension to allow remote desktop connections when the screen is locked.

%prep
%setup

%build
make

%install
install -d %buildroot%_datadir/gnome-shell/extensions/%oname
unzip -q %{oname}.shell-extension.zip \
	-d %buildroot%_datadir/gnome-shell/extensions/%oname/

%files
%_datadir/gnome-shell/extensions/%oname
%doc README.md

%changelog
* Fri Mar 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 5000-alt1
- 4900 -> 5000 (GNOME 50 supported)

* Mon Feb 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 4900-alt1
- Initial build for ALT Linux. 

