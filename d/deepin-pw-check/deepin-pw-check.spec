%define soname 1

Name: deepin-pw-check
Version: 5.1.8
Release: alt1
Summary: Verify the validity of the password for DDE
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-pw-check
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-pw-check-5.1.8-alt-exclude-cracklib.patch

BuildRequires: gcc-c++
BuildRequires: rpm-build-golang
BuildRequires: deepin-gettext-tools
BuildRequires: libpam0-devel
# BuildRequires: cracklib-devel
BuildRequires: libiniparser-devel
BuildRequires: glib2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgio-devel

%description
%summary.

%package -n lib%name%soname
Summary: Libraries for %name
Group: System/Libraries
Provides: lib%name = %version
Obsoletes: lib%name < %version

%description -n lib%name%soname
This packages provides libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/Other
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%name-devel
This package provides header files and libraries for %name.

%package -n lib%name-devel-static
Summary: Development package for %name
Group: Development/Other
Provides: %name-static = %version
Obsoletes: %name-static < %version

%description -n lib%name-devel-static
This package provides static libraries for %name.

%prep
%setup
%patch -p1
sed -i 's|/usr/lib|%_libdir|' \
    Makefile \
    misc/pkgconfig/libdeepin_pw_check.pc \
    misc/system-services/com.deepin.daemon.PasswdConf.service
sed -i 's|${PREFIX}/lib|%_libdir|' Makefile
sed -i 's|/usr/local/lib/pkgconfig|%_libdir/pkgconfig|' Makefile

%build
export GOPATH="$(pwd)/vendor:%go_path"
export PAM_MODULE_DIR=/%_lib/security
# export PKG_FILE_DIR=%%_libdir/pkgconfig
export GO111MODULE=off
%make

%install
export GOPATH=/usr/share/gocode
export PAM_MODULE_DIR=/%_lib/security
export GO111MODULE=off
%makeinstall_std

%files
%doc README.md LICENSE
/%_lib/security/pam_deepin_pw_check.so
%_bindir/pwd-conf-update
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_datadir/dbus-1/system-services/com.deepin.daemon.PasswdConf.service
%_datadir/dbus-1/system.d/com.deepin.daemon.PasswdConf.conf
%_datadir/polkit-1/actions/com.deepin.daemon.passwdconf.policy

%files -n lib%name%soname
%dir %_libdir/%name
%_libdir/%name/%name
%_libdir/libdeepin_pw_check.so.%{soname}*

%files -n lib%name-devel
%_includedir/deepin_pw_check.h
%_libdir/libdeepin_pw_check.so
%_libdir/pkgconfig/libdeepin_pw_check.pc

%files -n lib%name-devel-static
%_libdir/libdeepin_pw_check.a

%changelog
* Thu Apr 28 2022 Leontiy Volodin <lvol@altlinux.org> 5.1.8-alt1
- New version (5.1.8).
- Excluded cracklib.
- Returned as require for deepin-control-center.

* Thu Jul 01 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.17-alt1
- New version (5.0.17).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.13-alt1
- New version (5.0.13) with rpmgs script.

* Tue Mar 23 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.11-alt1
- Initial build for ALT Sisyphus.
