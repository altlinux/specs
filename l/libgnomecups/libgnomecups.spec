%def_disable static
%define ver_major 0.2

Name: libgnomecups
Version: %ver_major.3
Release: alt7

Summary: GNOME CUPS Library
Group: System/Libraries
License: %lgpl2plus
Url: http://www.gnome.org

Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2
# (fc) 0.2.2-4mdv fix cups callback for authentication (SUSE)
Patch1:		libgnomecups-0.2.2-callbackfix.patch
# (fc) 0.2.2-4mdv add dbus support (Fedora)
Patch3:		libgnomecups-0.2.3-dbus.patch
# (fc) 0.2.2-4mdv parse cups loptions (ubuntu)
Patch4:		libgnomecups-0.2.2-parse-dot-cups-loptions.patch
# (fc) 0.2.2-4mdv fix remote printer detection (ubuntu)
Patch5:		libgnomecups-0.2.2-fix-islocal.patch
# (fc) 0.2.2-4mdv don't warn on stderr for IPP_NOT_FOUND (ubuntu)
Patch6:		libgnomecups-0.2.2-ignore-ipp-not-found.patch
# (fc) 0.2.2-4mdv allow to change some cups printer attributes (ubuntu)
Patch7:		libgnomecups-0.2.2-replace-set-printer-attrs.patch
Patch8:		libgnomecups-0.2.3-fix-str-fmt.patch
# (cjw) fix glib includes
Patch9:		libgnomecups-0.2.3-glib.patch
Patch10:	libgnomecups-0.2.3-automake-1.13.patch
Patch11:	libgnomecups-0.2.3-cups-1.6.patch

BuildPreReq: rpm-build-licenses rpm-build-gnome
BuildPreReq: libcups-devel glib2-devel
BuildRequires: libssl-devel intltool zlib-devel

%description
GNOME library for CUPS integration.

%package devel
Summary: Development libraries and header files for GNOME CUPS Library
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the header files and libraries needed to write
or compile programs that use GNOME CUPS Library.

%if_enabled devel-static
%package devel-static
Summary: Static version of GNOME CUPS Library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static libraries needed to compile statically
linked programs that use %name.
%endif

%prep
%setup
%patch1 -p1 -b .callbackfix
%patch3 -p1 -b .dbus
%patch4 -p1 -b .parse-dot-cups-loptions
%patch5 -p1 -b .fix-is-local
%patch6 -p1 -b .ignore-ipp-not-found
%patch7 -p1 -b .replace-set-printer-attrs
%patch8 -p0 -b .str
%patch9 -p1 -b .glib
%patch10 -p1 -b .automake-1_13
%patch11 -p1 -b .cupsfix

%build
%add_optflags -D_IPP_PRIVATE_STRUCTURES
%configure \
    %{subst_enable static}

%make_build

%install
%makeinstall

%find_lang %name

%files -f %name.lang
%_libdir/*.so.*
%doc AUTHORS NEWS
%_datadir/locale/sr@Latn/LC_MESSAGES/libgnomecups.mo

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Sep 01 2021 Leontiy Volodin <lvol@altlinux.org> 0.2.3-alt7
- Returned with libgnomeprint for p9 branch
- Apply patches from PCLinuxOS

* Fri Mar 18 2016 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt6
- Fix build
- Apply patches from Debian

* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt5
- fixed build against glib-2.32

* Wed Jul 06 2011 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt4
- Rebuilt for debuginfo.

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt3
- rebuild for soname set-versions

* Fri Feb 27 2009 Alexey Rusakov <ktirf@altlinux.org> 0.2.3-alt2
- Removed deprecated post/postun scripts.
- Added Packager tag.

* Wed Jan 30 2008 Alexey Rusakov <ktirf@altlinux.org> 0.2.3-alt1
- New version (0.2.3).
- Spec cleanup, removed excess dependencies, use more RPM macros.

* Fri Sep 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.2.2-alt2
- fixed insufficient dependencies.

* Tue Sep 27 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.13-alt1
- 0.1.13

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.12-alt1
- 0.1.12

* Fri Sep 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.11-alt1
- First build for Sisyphus.


