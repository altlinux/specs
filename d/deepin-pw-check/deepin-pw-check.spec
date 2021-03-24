Name: deepin-pw-check
Version: 5.0.11
Release: alt1
Summary: Verify the validity of the password for DDE
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-pw-check
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: rpm-build-golang
BuildRequires: deepin-gettext-tools
BuildRequires: libpam0-devel
BuildRequires: cracklib-devel
BuildRequires: libiniparser-devel
BuildRequires: golang-github-go-dbus-devel
BuildRequires: golang-github-linuxdeepin-dbus-factory-devel
BuildRequires: golang-deepin-go-lib-devel
BuildRequires: golang-github-fsnotify-devel
BuildRequires: deepin-gir-generator
BuildRequires: golang-golang-x-sys-devel
BuildRequires: glib2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgio-devel

%description
%summary.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name
This packages provides libraries for %name.

%package devel
Summary: Development package for %name
Group: Development/Other

%description devel
This package provides header files and libraries for %name.

%package -n lib%name-static
Summary: Development package for %name
Group: Development/Other

%description -n lib%name-static
This package provides static libraries for %name.

%prep
%setup
sed -i 's|#include <iniparser/iniparser.h>|#include <iniparser.h>|; s|#include <iniparser/dictionary.h>|#include <dictionary.h>|' \
    lib/deepin_pw_check.c \
    tool/pwd_conf_update.c
sed -i 's|/usr/lib|%_libdir|' \
    Makefile \
    misc/pkgconfig/libdeepin_pw_check.pc \
    misc/system-services/com.deepin.daemon.PasswdConf.service
sed -i 's|${PREFIX}/lib|%_libdir|' Makefile
sed -i 's|/usr/local/lib/pkgconfig|%_libdir/pkgconfig|' Makefile

%build
export GOPATH=/usr/share/gocode
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

%files -n lib%name
%dir %_libdir/%name
%_libdir/%name/%name
%_libdir/libdeepin_pw_check.so.*

%files devel
%_includedir/deepin_pw_check.h
%_libdir/libdeepin_pw_check.so
%_libdir/pkgconfig/libdeepin_pw_check.pc

%files -n lib%name-static
%_libdir/libdeepin_pw_check.a

%changelog
* Tue Mar 23 2021 Leontiy Volodin <lvol@altlinux.org> 5.0.11-alt1
- Initial build for ALT Sisyphus.
