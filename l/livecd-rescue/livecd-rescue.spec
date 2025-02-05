# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: livecd-rescue
Version: 0.1
Release: alt1

Summary: The systemd target and services for Live Rescue
License: GPL-2.0-or-later
Group: System/Base

Url: https://www.altlinux.org/Rescue
Source: %name-%version.tar

Requires: systemd
Requires: livecd-rescue-utility
Requires: livecd-rescue-launcher

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%systemd_unitdir/live-rescue.target.wants
install -m644 live-rescue.target %buildroot%systemd_unitdir/live-rescue.target
install -m644 live-rescue-issue.service %buildroot%systemd_unitdir/live-rescue-issue.service
ln -s ../live-rescue-issue.service %buildroot%systemd_unitdir/live-rescue.target.wants/live-rescue-issue.service
install -m644 live-rescue-launcher.service %buildroot%systemd_unitdir/live-rescue-launcher.service
ln -s ../live-rescue-launcher.service %buildroot%systemd_unitdir/live-rescue.target.wants/live-rescue-launcher.service

%files
%systemd_unitdir/live-rescue.target
%systemd_unitdir/live-rescue-issue.service
%systemd_unitdir/live-rescue-launcher.service
%dir %systemd_unitdir/live-rescue.target.wants
%systemd_unitdir/live-rescue.target.wants/live-rescue-issue.service
%systemd_unitdir/live-rescue.target.wants/live-rescue-launcher.service

%changelog
* Wed Feb 05 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
