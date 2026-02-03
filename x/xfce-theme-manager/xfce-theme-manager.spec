%define _unpackaged_files_terminate_build 1

Name: xfce-theme-manager
Version: 0.3.9
Release: alt1

Summary: Integrated theme manager for xfce4
License: GPL-3.0-or-later
Group: Graphical desktop/XFce
Url: https://github.com/KeithDHedger/Xfce-Theme-Manager

Source: %name-%version.tar

BuildRequires(pre): rpm-build-xfce4

BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(libxfconf-0)

Requires: unzip

%description
A theme manager allowing easy configuration of themes,
window borders, controls, icons and cursors for Xfce

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;Settings;DesktopSettings;X-XFCE-SettingsDialog;X-XFCE-PersonalSettings;X-XFCE|" Xfce-Theme-Manager/resources/pixmaps/Xfce-Theme-Manager.desktop

%build
%xfce4reconf
%configure
%make_build

%install
%makeinstall_std

rm -rfv %buildroot%_datadir/Xfce-Theme-Manager/docs

%check
%make_build check

%files
%doc NEWS README.md screenshots
%_bindir/xfce-theme-manager
%dir %_datadir/Xfce-Theme-Manager
%_datadir/Xfce-Theme-Manager/*
%_desktopdir/Xfce-Theme-Manager.desktop
%_man1dir/xfce-theme-manager.1.*
%_mandir/*/man1/xfce-theme-manager.1.*
%_pixmapsdir/xfce-theme-manager.png

%changelog
* Mon Feb 03 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.9-alt1
- Initial build for Sisyphus
