%define _unpackaged_files_terminate_build 1

Name: mate-netbook
Version: 1.27.0
Release: alt1

Summary: MATE utilities for netbooks
License: GPLv3
Group: Graphical desktop/MATE
Url: https://github.com/mate-desktop/mate-netbook

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: intltool
BuildRequires: itstool
BuildRequires: mate-common
BuildRequires: yelp-tools
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libfakekey)
BuildRequires: pkgconfig(libmatepanelapplet-4.0)
BuildRequires: pkgconfig(mate-desktop-2.0)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(unique-3.0)

Requires: mate-panel

%description
MATE utilities for netbooks are an applet and a daemon to maximize
windows and move their titles on the panel.

Installing these utilities is recommended for netbooks and similar
devices with low resolution displays.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
           --libexecdir=%{_libexecdir}/%{name}

%make_build

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sysconfdir}/xdg/autostart/mate-maximus-autostart.desktop
%{_bindir}/mate-maximus
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/mate-window-picker-applet
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/mate-panel/
%{_mandir}/man1/mate-maximus.1*


%changelog
* Sat Feb 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.27.0-alt1
- Initial build for Sisyphus
