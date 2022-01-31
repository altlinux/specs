%define _unpackaged_files_terminate_build 1

Name: proxmox-mini-journalreader
Summary: Minimal systemd Journal Reader
Version: 1.3
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/proxmox-mini-journalreader.git
Source: %name-%version.tar
Patch: %name-%version.patch

Provides: pve-mini-journalreader = %EVR
Obsoletes: pve-mini-journalreader < %EVR

BuildRequires: libsystemd-devel

%description
A minimal application to read the last X lines of the systemd journal or the
last X lines before a cursor.

%prep
%setup
%patch -p1

%build
%make_build -C src

%install
%makeinstall_std -C src

%files
%_bindir/*

%changelog
* Mon Jan 24 2022 Alexey Shabalin <shaba@altlinux.org> 1.3-alt1
- Initial build as separate package.

