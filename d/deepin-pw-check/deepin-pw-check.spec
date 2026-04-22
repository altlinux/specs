%define soname 1
%define _libexecdir %_prefix/libexec

%def_disable clang
%def_without cracklib

Name: deepin-pw-check
Version: 6.0.8
Release: alt1

Summary: Verify the validity of the password for DDE

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-pw-check

# Source-url: https://github.com/linuxdeepin/deepin-pw-check/archive/%version/%name-%version.tar.gz
Source0: %name-%version.tar
# go mod vendor -o ../vendor
Source1: vendor.tar
Patch0: %name-%version-%release.patch
Patch1: deepin-pw-check-6.0.2-alt-libdir.patch
Patch2: deepin-pw-check-6.0.6-alt-exclude-cracklib.patch

%if_enabled clang
BuildRequires: clang-devel
BuildRequires: lld-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: rpm-build-golang /proc
BuildRequires: deepin-gettext-tools
BuildRequires: libpam0-devel
%if_with cracklib
BuildRequires: cracklib-devel
%endif
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
%setup -a1
%patch0 -p1
%patch1 -p1
%if_without cracklib
%patch2 -p2
%else
patch -p1 < rpm/0001-Mangle-Suit-Cracklib2.9.6.patch
%endif
sed -i 's|os-version|uos-version|g' \
  tool/pwd_conf_update.c
# do not use uadp
sed -i '/\/usr\/share\/uadp/d' \
  misc/systemd-service/deepin-passwd-conf.service

%build
%if_enabled clang
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export GOPATH="$PWD/vendor"
export PAM_MODULE_DIR=%_libdir/security
export PKG_FILE_DIR=%_libdir/pkgconfig
export LIBDIR=%_lib
export GO111MODULE=on
%make

%install
export GOPATH=/usr/share/gocode
export PAM_MODULE_DIR=%_libdir/security
export PKG_FILE_DIR=%_libdir/pkgconfig
export LIBDIR=%_lib
export GO111MODULE=on
%makeinstall_std

%files
%doc README.md LICENSE debian/changelog
%_libdir/security/pam_deepin_pw_check.so
%_bindir/pwd-conf-update
%_unitdir/deepin-passwd-conf.service
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_datadir/dbus-1/system-services/org.deepin.dde.PasswdConf1.service
%_datadir/dbus-1/system.d/org.deepin.dde.PasswdConf1.conf
%_datadir/polkit-1/actions/org.deepin.dde.passwdconf.policy
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
* Wed Apr 22 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.8-alt1
- New version 6.0.8.

* Wed Dec 24 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.7-alt1
- New version 6.0.7.
- Applied usrmerge.

* Fri Aug 08 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.6-alt1
- New version 6.0.6.

* Fri Feb 07 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.4.0.1.9d86-alt1
- New version 6.0.4-1-g9d86d88.

* Mon May 06 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.2-alt2
- Fixed FTBFS.

* Fri Dec 01 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.2-alt1
- New version 6.0.2.
- Used independent vendoring of submodules again.

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
