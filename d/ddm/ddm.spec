%define _libexecdir %_prefix/libexec

%define soverdc 0
%define soverda 0

Name: ddm
Version: 0.3.6
Release: alt1

Summary: DDM is a fork of SDDM for DDE

License: GPL-2.0-or-later and LGPL-2.1-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/ddm
Vcs: https://github.com/linuxdeepin/ddm

# Source-url: https://github.com/linuxdeepin/ddm/archive/%version/%name-%version.tar.xz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: ddm-0.3.0-alt-pam.patch

BuildRequires(pre): rpm-macros-dqt6 rpm-build-ninja
BuildRequires: gcc-c++ extra-cmake-modules dqt6-base-devel dqt6-declarative-devel dqt6-tools-devel libpam0-devel libXau-devel libsystemd-devel treeland-protocols libwayland-client-devel libdqt6-quicktemplates2 libdqt6-quickcontrols2 libdqt6-quicktest

%description
%summary.

%package common
Summary: Data files for DDM
Group: Graphical desktop/Other
BuildArch: noarch
AutoReq: no

%description common
The package provides data files for DDM.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: libddm-common-devel = %EVR

%description devel
The package provides development files for DDM.

%package -n libddm-common%soverdc
Summary: ddm-common library for DDM
Group: System/Libraries

%description -n libddm-common%soverdc
The package provides ddm-common library for DDM.

%package -n libddm-common-devel
Summary: Development files for libddm-common
Group: Development/C++

%description -n libddm-common-devel
The package provides development files for libddm-common.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%DQ6build \
  -DUID_MIN=1000 \
  -DUID_MAX=60000 \
  -DDBUS_CONFIG_FILENAME="ddm_org.freedesktop.DisplayManager.conf" \
  -DSESSION_COMMAND="%_sysconfdir/X11/Xsession"

%install
%DQ6install
mkdir -p %buildroot%_localstatedir/ddm/
mkdir -p %buildroot%_logdir/
touch %buildroot%_logdir/ddm.log

%pre
# DDM runs as DDE user.
getent group dde >/dev/null || groupadd -r dde
getent passwd dde >/dev/null || \
    useradd -r -g dde -d %_localstatedir/ddm -s /bin/false \
    -c "Simple Wayland Display Manager for DDE" dde
exit 0

%files
%doc LICENSES/ README*.md debian/changelog
%config(noreplace) %_sysconfdir/pam.d/ddm
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.deepin.DisplayManager.conf
%config(noreplace) %_sysconfdir/dbus-1/system.d/ddm_org.freedesktop.DisplayManager.conf
%_bindir/ddm
%_unitdir/ddm.service
%dir %_unitdir/treeland.service.d/
%_unitdir/treeland.service.d/10-dde-seatd.conf
%_sysusersdir/dde.conf
%_tmpfilesdir/ddm.conf
%attr(750,dde,dde) %dir %_localstatedir/ddm/
%attr(600,dde,dde) %ghost %_logdir/ddm.log

%files common
%dir %_datadir/ddm/
%dir %_datadir/ddm/scripts/
%_datadir/ddm/scripts/*

%files devel
%dir %_libdir/cmake/DDM/
%_libdir/cmake/DDM/DDMConfig*.cmake

%files -n libddm-common%soverdc
%_libdir/libddm-common.so.%soverdc
%_libdir/libddm-common.so.%version

%files -n libddm-common-devel
%_libdir/libddm-common.so
%dir %_includedir/ddm/
%dir %_includedir/ddm/common/
%_includedir/ddm/common/*.h
%dir %_libdir/cmake/DDM/
%_libdir/cmake/DDM/Common*.cmake

%changelog
* Fri Jun 19 2026 Leontiy Volodin <lvol@altlinux.org> 0.3.6-alt1
- New version 0.3.6.

* Thu Jun 11 2026 Leontiy Volodin <lvol@altlinux.org> 0.3.5-alt1
- New version 0.3.5.

* Tue May 12 2026 Leontiy Volodin <lvol@altlinux.org> 0.3.4-alt1
- New version 0.3.4.

* Wed Mar 04 2026 Leontiy Volodin <lvol@altlinux.org> 0.3.3-alt1
- New version 0.3.3.

* Fri Feb 27 2026 Leontiy Volodin <lvol@altlinux.org> 0.3.2-alt1
- New version 0.3.2.
- Fixed permissions.

* Fri Oct 31 2025 Leontiy Volodin <lvol@altlinux.org> 0.2.2-alt1
- New version 0.2.2.

* Fri Sep 19 2025 Leontiy Volodin <lvol@altlinux.org> 0.2.1-alt1
- New version 0.2.1.
- Updated license tag.

* Tue Sep 02 2025 Leontiy Volodin <lvol@altlinux.org> 0.2.0-alt1
- New version 0.2.0.

* Wed Aug 06 2025 Leontiy Volodin <lvol@altlinux.org> 0.1.11-alt1
- New version 0.1.11.

* Wed Feb 05 2025 Leontiy Volodin <lvol@altlinux.org> 0.1.10-alt1
- New version 0.1.10.
- Fixed preinstall command.

* Mon Dec 30 2024 Leontiy Volodin <lvol@altlinux.org> 0.1.9-alt1.1
- Fixed url and vcs tag.
- Updated license tag.

* Mon Dec 30 2024 Leontiy Volodin <lvol@altlinux.org> 0.1.9-alt1
- Initial build for ALT Sisyphus.
