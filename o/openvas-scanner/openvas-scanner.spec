%define _unpackaged_files_terminate_build 1
%define sover 23

%def_enable docs

Name: openvas-scanner
Version: 23.45.0
Release: alt1

Summary: Open Vulnerability Assessment (OpenVAS) Scanner
License: GPL-2.0-or-later
Group: Security/Networking
Url: http://www.openvas.org
VCS: https://github.com/greenbone/openvas-scanner

ExcludeArch: armh

#Source-url: https://github.com/greenbone/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch0: fix-release-build.patch
Patch1: fix-linking-shared-lib.patch
Patch2: alt-fix-specifier-char-type.patch

BuildRequires: cmake
BuildRequires: libbsd-devel
BuildRequires: libcurl-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgvm_boreas-devel
BuildRequires: libjson-glib-devel
BuildRequires: libkrb5-devel
BuildRequires: libksba-devel
BuildRequires: libssh-devel
BuildRequires: libmagic-devel
%if_enabled docs
BuildRequires: doxygen
%endif
%ifarch %ix86
BuildRequires: libgpgme-devel
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

%if_enabled docs
%package devel-doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
%summary
%endif

%prep
%setup
%patch0 -p2
%patch1 -p1
%ifarch %ix86
%patch2 -p1
%endif

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

%if_enabled docs
%cmake_build -t doxygen-full
%endif

%install
%cmake_install

%if_enabled docs
%__mkdir_p %buildroot%_defaultdocdir/%name/html
%__mv %_cmake__builddir/doc/generated/html %buildroot%_defaultdocdir/%name/
%endif

%files
%doc CHANGELOG.md COPYING README.md
%config(noreplace) %_sysconfdir/openvas/openvas_log.conf
%_sbindir/openvas
%_bindir/openvas-nasl*
%_man1dir/*.1.*
%_man8dir/*.8.*
%dir %_sysconfdir/openvas

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

%if_enabled docs
%files devel-doc
%dir %_defaultdocdir/%name
%doc %_defaultdocdir/%name/html
%endif

%changelog
* Fri Apr 24 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 23.45.0-alt1
- new version

* Tue Apr 07 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 23.43.1-alt1
- new version

* Fri Mar 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 23.41.7-alt1
- new version

* Wed Mar 04 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 23.40.3-alt1
- new version

* Mon Dec 01 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 23.32.3-alt1
- new version

* Tue Nov 25 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 23.31.5-alt2
- update

* Fri Nov 21 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 23.31.5-alt1
- new version

* Tue Jun 17 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 23.20.1-alt1
- new version

* Mon Feb 17 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 23.15.3-alt1
- new version

* Wed Apr 03 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 23.0.1-alt1
- Initial build for ALT Linux
