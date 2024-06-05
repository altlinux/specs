%define _unpackaged_files_terminate_build 1

Name: btrfs-assistant
Version: 2.1.1
Summary: GUI management tool to make managing a Btrfs filesystem easier
Release: alt1
License: GPL-3.0
Group: Archiving/Backup
URL: https://gitlab.com/btrfs-assistant/btrfs-assistant
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libbtrfs-devel
BuildRequires: libappstream-glib
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel

%description
Btrfs Assistant is a GUI management tool to make managing a Btrfs filesystem easier.

The primary features it offers are:
* An easy to read overview of Btrfs metadata;
* A simple view of subvolumes with or without Snapper/Timeshift snapshots;
* Run and monitor scrub and balance operations;
* A pushbutton method for removing subvolumes;
* A management front-end for Snapper with enhanced restore functionality:
    * View, create and delete snapshots;
    * Restore snapshots in a variety of situations:
        * When the filesystem is mounted in a different distro;
        * When booted off a snapshot;
        * From a live ISO;
    * View, create, edit, remove Snapper configurations;
    * Browse snapshots and restore individual files;
    * Browse diffs of a single file across snapshot versions;
    * Manage Snapper systemd units;
* A front-end for Btrfs Maintenance:
    * Manage systemd units;
    * Easily manage configuration for defrag, balance and scrub settings.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%name.metainfo.xml

%files
%_bindir/%name
%_bindir/%name-bin
%_bindir/%name-launcher
%_sysconfdir/%name.conf
%_desktopdir/%name.desktop
%_datadir/metainfo/%name.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/polkit-1/actions/org.%name.pkexec.policy

%changelog
* Wed May 29 2024 Anastasia Osmolovskaya <lola@altlinux.org> 2.1.1-alt1
- Updated to version 2.1.1.

* Mon May 13 2024 Anastasia Osmolovskaya <lola@altlinux.org> 2.1-alt1
- Updated to version 2.1.

* Sat Mar 16 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.0-alt1
- Updated to version 2.0.
- Built with qt6.

* Wed Jan 17 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.9-alt1
- Updated to version 1.9.

* Mon Dec 25 2023 Alexander Makeenkov <amakeenk@altlinux.org> 1.8-alt1
- Initial build for ALT.

