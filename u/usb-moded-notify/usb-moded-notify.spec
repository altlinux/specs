%define _unpackaged_files_terminate_build 1

Name: usb-moded-notify
Version: 0.4.2
Release: alt1
Summary: Desktop notification for usb-signaller
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.postmarketos.org/postmarketOS/usb-moded-notify
VCS: https://gitlab.postmarketos.org/postmarketOS/usb-moded-notify.git

BuildArch: noarch

AutoProv: nopython3

Source: %name-%version.tar

# Exclude dymanic module from requires
%filter_from_requires /^python3(gi\.repository\.GLib) < 0$/d

Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(Notify)

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: just

%description
A very simple daemon that listens for usb-moded dialog request events and shows
a notification with action buttons, allowing users to select different usb-moded
modes. Don't expect too much from this.

%prep
%setup

%build

%install
export DESTDIR=%buildroot
export PREFIX=%prefix
just install

%files
%doc README.*
%_bindir/%name
%_userunitdir/%name.service
%exclude %_sysconfdir/user/init.d/%name

%changelog
* Wed Oct 28 2026 Vasiliy Doylov <neko@altlinux.org> 0.4.2-alt1
- Initial build for ALT.
