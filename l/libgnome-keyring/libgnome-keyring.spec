%define ver_major 3.4
%def_disable static
%def_disable gtk_doc
%def_disable debug
%def_enable introspection

Name: libgnome-keyring
Version: %ver_major.1
Release: alt1

Summary: Compatibility library for accessing secrets
License: LGPL
Group: System/Libraries
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Source1: %name.map

%define glib_ver 2.16.0
%define dbus_ver 1.0
%define gcrypt_ver 1.2.2

# From configure.in
BuildPreReq: intltool >= 0.35.0
BuildPreReq: glib2-devel >= %glib_ver libgio-devel
BuildPreReq: libdbus-devel >= %dbus_ver
BuildPreReq: libgcrypt-devel >= %gcrypt_ver
BuildRequires: gtk-doc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}

# for check
#BuildRequires: gnome-keyring dbus-tools-gui /proc

%description
The %name library is used by applications to integrate with the
gnome-keyring system.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains headers and development libraries for %name.

%package devel-static
Summary: Static version of %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package provides libraries for develop programs statically linked
against %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
This package contains development documentation for %name

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for %name

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for %name

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -q

install -p -m644 %SOURCE1 library/%name-altlinux.ver

%build
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable static} \
	%{subst_enable debug}

%make_build

# X11 required for tests
#%check
#%make check

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_libdir/*.so.*
%doc README AUTHORS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files devel-doc
%_gtk_docdir/*

%if_enabled introspection
%files gir
%_typelibdir/GnomeKeyring-1.0.typelib

%files gir-devel
%_girdir/GnomeKeyring-1.0.gir
%endif

%changelog
* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sun Sep 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Aug 30 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90

* Fri May 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Thu May 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- fixed crash (https://bugzilla.gnome.org/show_bug.cgi?id=650840)

* Sun May 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- rebuild for debuginfo

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Mon Dec 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- updated buildreqs

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sun Apr 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Sat Apr 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- fix for gnomebug #575247 from svn

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- added libtasn1-utils and valgrind to buildreqs if debug enabled

* Mon Mar 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Sun Feb 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.90-alt1
- 2.25.90

* Wed Jan 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- drop upstreamed patches

* Thu Dec 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.25.2-alt1
- 2.25.2
- updated symver.map

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- removed obsolete post{,un}_ldconfig
- use pkgconfig for tasn1-1.7 without libtasn1.m4

* Mon Oct 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.1-alt1
- 2.24.1
- don't rebuild development documentation

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0
- add versioning for old versions
- add devel-doc package(noarch)

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- 2.22.3

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1
- changed libexec dir to %_prefix/libexec/%name

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Wed Mar 05 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- 2.21.92
- build --with-root-certs=/usr/share/ca-certificates
- add gconf_install/gconf_uninstall in %%post and %%preun
- updated BuildPreReq

* Mon Jan 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.3-alt1
- 2.20.3

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt1
- 2.20.2

* Tue Oct 16 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- 2.20.1
- remove backported patches:
  + gnome-keyring-2.20-add_new_keyrings.patch (fixed upstream)
  + gnome-keyring-2.20-no_match.patch (fixed upstream)
  + gnome-keyring-2.20-selinux-pam.patch (not actual for ALTLinux)
  + gnome-keyring-2.20-link-against-pam.patch (fixed upstream)
- fixed section install (upstream removed install-pam)
- disabled gnome-keyring-2.20-no-unset-default.patch (need this patch?)

* Sat Oct 13 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- new version 2.20.0
- add packager
- add package pam
- backport patches from svn

* Mon Apr 09 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Thu Mar 15 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8-alt1
- new version 0.8 (with rpmrb script)

* Thu Mar 15 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8.0-alt1
- new version 0.8 (with rpmrb script)

* Sun Feb 25 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.92-alt1
- new version 0.7.92 (with rpmrb script)

* Wed Feb 14 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.91-alt1
- new version 0.7.91 (with rpmrb script)

* Fri Jan 05 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.3-alt1
- new version 0.7.3 (with rpmrb script)

* Mon Sep 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.6.0-alt1
- new version (0.6.0)

* Sat Aug 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.5.1-alt1
- new version 0.5.1 (with rpmrb script)

* Sat Mar 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.4.7-alt1
- new version 0.4.7 (with rpmrb script)

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.4.6-alt1
- new version

* Thu Sep 22 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.4.5-alt1
- 0.4.5

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.4.4-alt1
- 0.4.4
- Removed more excess buildreqs.

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.4.3-alt1
- 0.4.3
- Removed excess buildreqs.

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.1-alt1
- 0.4.1.

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Apr 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.90-alt1
- 0.1.90

* Wed Feb 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Sat Jan 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Thu Jan 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.2-alt1
- First build for Sisyphus.

