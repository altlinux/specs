%define _unpackaged_files_terminate_build 1
%define sover 23

Name: openvas-scanner
Version: 23.0.1
Release: alt1

Summary: Open Vulnerability Assessment (OpenVAS) Scanner
License: GPL-2.0-only
Group: Security/Networking
Url: http://www.openvas.org
VCS: https://github.com/greenbone/openvas-scanner

ExcludeArch: armh

#Source-url: https://github.com/greenbone/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch0: fix-release-build.patch
Patch1: fix-linking-shared-lib.patch

BuildRequires: cmake
BuildRequires: libbsd-devel
BuildRequires: libgcrypt-devel >= 1.6
BuildRequires: libgvm_boreas-devel >= 22.4
BuildRequires: libjson-glib-devel >= 1.4.4
BuildRequires: libksba-devel >= 1.0.7
BuildRequires: libssh-devel >= 0.6.0
BuildRequires: pkgconfig(libcurl) >= 7.74.0
%ifarch i586
BuildRequires: libgpgme-devel >= 1.1.2
%endif

%description
Scanner module for the Open Vulnerability Assessment System (OpenVAS).

%package -n libopenvas_nasl%sover
Summary: Support library for %name
Group: System/Libraries

%description -n libopenvas_nasl%sover
Support library for %name.

%package -n libopenvas_nasl-devel
Summary: Development files for the openvas nasl library
Group: Development/C

%description -n libopenvas_nasl-devel
Support library for %name.

%package -n libopenvas_misc%sover
Summary: Support library for %name
Group: System/Libraries

%description -n libopenvas_misc%sover
Support library for %name.

%package -n libopenvas_misc-devel
Summary: Development files for the openvas nasl library
Group: Development/C

%description -n libopenvas_misc-devel
Support library for %name.

%prep
%setup
%patch0 -p2
%patch1 -p1

%build
%cmake \
    -DCMAKE_C_FLAGS="%optflags -Wno-error=maybe-uninitialized" \
    -DCMAKE_BUILD_TYPE=Release \
    -DINSTALL_OLD_SYNC_SCRIPT=OFF \
    -DSYSCONFDIR=%_sysconfdir \
    -DLOCALSTATEDIR=%_var \
    -DOPENVAS_FEED_LOCK_PATH=%_sharedstatedir/openvas/feed-update.lock \
    -DOPENVAS_RUN_DIR=%_runtimedir/ospd
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG.md COPYING README.md
%config(noreplace) %_sysconfdir/openvas/openvas_log.conf
%_sbindir/openvas
%_bindir/openvas-nasl*
%_man1dir/*.1.*
%_man8dir/*.8.*

%files -n libopenvas_nasl%sover
%_libdir/*nasl.so.%sover
%_libdir/*nasl.so.%sover.*

%files -n libopenvas_nasl-devel
%_libdir/*nasl.so

%files -n libopenvas_misc%sover
%_libdir/*misc.so.%sover
%_libdir/*misc.so.%sover.*

%files -n libopenvas_misc-devel
%_libdir/*misc.so

%changelog
* Wed Apr 03 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 23.0.1-alt1
- Initial build for ALT Linux
