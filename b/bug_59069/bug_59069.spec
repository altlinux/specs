Name: bug_59069
Version: 1.0
Release: alt1

Group: System/Configuration/Packaging
Summary: Bug 59069
License: GPL-3.0
URL: https://bugzilla.altlinux.org/59069

ExclusiveArch: x86_64 %ix86 aarch64

Conflicts: libnvidia-ml < 595.91.07-alt3

%description
Bug https://bugzilla.altlinux.org/59069 .

%prep

%install
mkdir -p %buildroot/%_libdir/
ln -s libnvidianull.so %buildroot/%_libdir/libnvidia-ml.so

%files
%_libdir/libnvidia-ml.so

%changelog
* Mon Sep 07 2026 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
