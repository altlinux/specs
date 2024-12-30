%define _libexecdir %_prefix/libexec

%define soverdc 0
%define soverda 0

Name: ddm
Version: 0.1.9
Release: alt1

Summary: DDM is a fork of SDDM for DDE

License: GPL-2.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/treeland
Vcs: git://github.com/linuxdeepin/treeland.git

Source: %url/archive/%version/%name-%version.tar.xz
Patch: ddm-0.1.9-alt-pam.patch

BuildRequires(pre): rpm-macros-dqt6 rpm-build-ninja
BuildRequires: gcc-c++ extra-cmake-modules dqt6-base-devel dqt6-declarative-devel dqt6-tools-devel libpam0-devel libXau-devel libsystemd-devel

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
Requires: libddm-auth-devel = %EVR

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

%package -n libddm-auth%soverda
Summary: ddm-auth library for DDM
Group: System/Libraries

%description -n libddm-auth%soverda
The package provides ddm-auth library for DDM.

%package -n libddm-auth-devel
Summary: Development files for libddm-auth
Group: Development/C++

%description -n libddm-auth-devel
The package provides development files for libddm-auth.

%prep
%setup
%autopatch -p1

%build
export LC_ALL=C.UTF-8
%DQ6build \
  -DUID_MIN=1000 \
  -DUID_MAX=60000 \
  -DDBUS_CONFIG_FILENAME="ddm_org.freedesktop.DisplayManager.conf" \
  -DSESSION_COMMAND="%_sysconfdir/X11/Xsession"

%install
%DQ6install

%pre
# DDM runs as its own user.
getent group ddm >/dev/null || groupadd -r ddm
getent passwd ddm >/dev/null || \
    useradd -r -g ddm -d %_localstatedir/ddm -s /bin/bash \
    -c "ddm user" ddm
exit 0

%files
%doc LICENSES/ README*.md
%config(noreplace) %_sysconfdir/pam.d/ddm-autologin
%config(noreplace) %_sysconfdir/pam.d/ddm
%config(noreplace) %_sysconfdir/pam.d/ddm-greeter
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.deepin.DisplayManager.conf
%config(noreplace) %_sysconfdir/dbus-1/system.d/ddm_org.freedesktop.DisplayManager.conf
%_bindir/ddm
%_libexecdir/ddm-helper
%_libexecdir/ddm-helper-start-wayland
%_libexecdir/ddm-helper-start-single-wayland
%_libexecdir/ddm-helper-start-x11user
%_unitdir/ddm.service
%_unitdir/seatd.service.d/override.conf
%_sysusersdir/dde.conf
%_tmpfilesdir/ddm.conf

%files common
%dir %_datadir/ddm/
%dir %_datadir/ddm/flags/
%_datadir/ddm/flags/*.png
%dir %_datadir/ddm/faces/
%_datadir/ddm/faces/*.icon
%_datadir/ddm/faces/.face.icon
%dir %_datadir/ddm/scripts/
%_datadir/ddm/scripts/*

%files devel
%dir %_libdir/cmake/DDM/
%_libdir/cmake/DDM/DDMConfig.cmake

%files -n libddm-common%soverdc
%_libdir/libddm-common.so.%{soverdc}*

%files -n libddm-common-devel
%_libdir/libddm-common.so
%dir %_includedir/ddm/
%dir %_includedir/ddm/common/
%_includedir/ddm/common/*.h
%dir %_libdir/cmake/DDM/
%_libdir/cmake/DDM/Common*.cmake

%files -n libddm-auth%soverda
%_libdir/libddm-auth.so.%{soverda}*

%files -n libddm-auth-devel
%_libdir/libddm-auth.so
%dir %_includedir/ddm/
%dir %_includedir/ddm/auth/
%dir %_includedir/ddm/auth/*.h
%dir %_libdir/cmake/DDM/
%_libdir/cmake/DDM/Auth*.cmake

%changelog
* Mon Dec 30 2024 Leontiy Volodin <lvol@altlinux.org> 0.1.9-alt1
- Initial build for ALT Sisyphus.
