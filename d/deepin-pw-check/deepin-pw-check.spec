%define soname 1
%define llvm_ver 15

%def_disable clang

Name: deepin-pw-check
Version: 5.1.18
Release: alt1
Summary: Verify the validity of the password for DDE
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-pw-check
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-pw-check-5.1.8-alt-exclude-cracklib.patch

%if_enabled clang
#BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: clang%llvm_ver.0-devel
BuildRequires: lld%llvm_ver.0-devel
BuildRequires: llvm%llvm_ver.0-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: rpm-build-golang
BuildRequires: deepin-gettext-tools
BuildRequires: libpam0-devel
# BuildRequires: cracklib-devel
BuildRequires: libiniparser-devel
BuildRequires: glib2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgio-devel
BuildRequires: golang-deepin-api-devel

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
patch -p1 < rpm/0001-fix-for-UonioTech.patch
sed -i 's|/usr/lib|%_libdir|' \
  misc/pkgconfig/libdeepin_pw_check.pc

%build
%if_enabled clang
export CC=clang-%llvm_ver
export CXX=clang++-%llvm_ver
export LDFLAGS="-fuse-ld=lld-%llvm_ver $LDFLAGS"
%endif
export GOPATH="%go_path/src/github.com/linuxdeepin/dde-api/vendor"
export PAM_MODULE_DIR=/%_lib/security
export PKG_FILE_DIR=%_libdir/pkgconfig
export LIBDIR=%_lib
export GO111MODULE=off
%make

%install
export GOPATH=/usr/share/gocode
export PAM_MODULE_DIR=/%_lib/security
export PKG_FILE_DIR=%_libdir/pkgconfig
export LIBDIR=%_lib
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
%dir %_libexecdir/%name/
%_libexecdir/%name/%name

%files -n lib%name%soname
%_libdir/libdeepin_pw_check.so.%{soname}*

%files -n lib%name-devel
%_includedir/deepin_pw_check.h
%_libdir/libdeepin_pw_check.so
%_libdir/pkgconfig/libdeepin_pw_check.pc

%files -n lib%name-devel-static
%_libdir/libdeepin_pw_check.a

%changelog
* Fri Jan 27 2023 Leontiy Volodin <lvol@altlinux.org> 5.1.18-alt1
- New version (5.1.18).

* Tue Nov 29 2022 Leontiy Volodin <lvol@altlinux.org> 5.1.17-alt1
- New version (5.1.17).

* Mon Aug 29 2022 Leontiy Volodin <lvol@altlinux.org> 5.1.16-alt1
- New version (5.1.16).

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
