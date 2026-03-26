%define _unpackaged_files_terminate_build 1

Name: nbfc-qt
Version: 0.5.0
Release: alt1

Summary: GUI for NBFC-Linux (Qt-based)
License: GPL-3.0
Group: System/Configuration/Other

Url: https://github.com/nbfc-linux/nbfc-qt
# Source-url: https://github.com/nbfc-linux/nbfc-qt/archive/refs/tags/%version.tar.gz
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
%_bindir/nbfc-qt
%_bindir/nbfc-qt-tray

%changelog
* Mon Mar 23 2026 Boris Yumankulov <boria138@altlinux.org> 0.5.0-alt1
- new version 0.5.0

* Sun Jul 06 2025 Boris Yumankulov <boria138@altlinux.org> 0.4.3-alt1
- new version 0.4.3

* Thu Jun 19 2025 Boris Yumankulov <boria138@altlinux.org> 0.4.2-alt1
- new version 0.4.2

* Sun May 25 2025 Boris Yumankulov <boria138@altlinux.org> 0.4.1-alt1
- new version 0.4.1

* Fri May 23 2025 Boris Yumankulov <boria138@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Sat May 10 2025 Boris Yumankulov <boria138@altlinux.org> 0.3.12-alt1
- initial build for ALT Sisyphus


