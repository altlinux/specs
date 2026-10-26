%define _unpackaged_files_terminate_build 1

Name: stplr-dbus
Version: 0.1.1
Release: alt1

Summary: D-Bus service for Stapler
License: GPL-2.0-or-later
Group: System/Configuration/Packaging
Url: https://gitlab.basealt.space/fomchenkovda/stplr-dbus
VCS: https://gitlab.basealt.space/fomchenkovda/stplr-dbus

Requires: stplr

Source: %name-%version.tar

BuildRequires: libpolkitqt6-qt6-devel

%description
%summary

%prep
%setup

%build
%cmake \
    -DBUILD_TESTS=OFF \
    -DENABLE_INTEGRATION_TESTS=OFF \
    #
%cmake_build

%install
%cmake_install

%files
%_bindir/stplr-dbus-service
%_unitdir/stplr.service
%_datadir/dbus-1/system.d/org.alt.stplr.conf
%_datadir/dbus-1/system-services/org.alt.stplr.service
%_datadir/dbus-1/interfaces/org.alt.stplr.xml
%_datadir/polkit-1/actions/org.alt.stplr.policy

%changelog
* Mon Oct 26 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.1.1-alt1
- change the package build scheme

* Wed Oct 21 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.1.0-alt1
- initial build for ALT Linux
