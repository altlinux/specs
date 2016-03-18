%def_disable static
%define ver_major 0.2

Name: libgnomecups
Version: %ver_major.3
Release: alt6

Summary: GNOME CUPS Library
Group: System/Libraries
License: %lgpl2plus
Url: http://www.gnome.org

Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2
Patch: %name-0.2.3-alt-glib_fixes.patch
Patch1: libgnomecups-20_parse-dot-cups-lpoptions.patch
Patch2: libgnomecups-21_fix-islocal.patch
Patch3: libgnomecups-22_ignore-ipp-not-found.patch
Patch4: libgnomecups-23_replace-set-printer-attrs.patch
Patch5: libgnomecups-25_browsed_ppds.patch
Patch6: libgnomecups-26_format-security.patch

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
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

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

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
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


