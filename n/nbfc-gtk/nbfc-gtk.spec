%define _unpackaged_files_terminate_build 1

Name: nbfc-gtk
Version: 0.4.0
Release: alt1

Summary: GUI for NBFC-Linux (GTK-based)
License: GPL-3.0
Group: System/Configuration/Other

Url: https://github.com/nbfc-linux/nbfc-gtk
# Source-url: https://github.com/nbfc-linux/nbfc-gtk/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: %_bindir/python3 rpm-build-python3

Requires: nbfc-linux

ExclusiveArch: x86_64

%description
%summary.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/nbfc-gtk


%changelog
* Mon Mar 23 2026 Boris Yumankulov <boria138@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Thu Jun 19 2025 Boris Yumankulov <boria138@altlinux.org> 0.2.1-alt1
- new version 0.2.1

* Sat May 24 2025 Boris Yumankulov <boria138@altlinux.org> 0.2.0-alt1
- initial build for ALT Sisyphus

