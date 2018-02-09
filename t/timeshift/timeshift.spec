Name: timeshift
Version: 18.2
Summary: System restore tool for Linux
Release: alt1
License: GPLv3
Group: Archiving/Backup
URL: https://github.com/teejee2008/timeshift.git
Source: %name-%version.tar

BuildRequires: vala libjson-glib-devel libgee0.8-devel libvte3-devel
Requires: rsync

%description
System restore tool for Linux. Creates filesystem snapshots using
rsync+hardlinks, or BTRFS snapshots. Supports scheduled snapshots, multiple back
up levels, and exclude filters. Snapshots can be restored while system is
running or from Live CD/USB.

%prep
%setup

%build
%make_build

%install
%makeinstall_std
rm -f %buildroot%_bindir/%name-uninstall
%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/*
%_sysconfdir/default/%name.json
%_desktopdir/%name-gtk.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/%name/images/*
%_datadir/metainfo/%name.appdata.xml
%_datadir/appdata/%name.appdata.xml
%_datadir/polkit-1/actions/in.teejeetech.pkexec.timeshift.policy

%changelog
* Fri Feb 9 2018 Mikhail Savostyanov <mik@altlinux.org> 18.2-alt1
- initial build for ALT
