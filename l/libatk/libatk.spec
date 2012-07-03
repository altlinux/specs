%define _name atk
%define ver_major 2.4
%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: libatk
Version: %ver_major.0
Release: alt1

Summary: Accessibility features for Gtk+
License: %lgpl2plus
Group: System/Libraries
Url: http://developer.gnome.org/projects/gap

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
Source1: atk-compat.map
Source2: atk-compat.lds
Patch: atk-1.33.6-alt-compat-version-script.patch

Requires: %name-locales = %version

Provides: atk = %version
Obsoletes: atk < %version

%define glib_ver 2.5.7
%define gtk_doc_ver 1.0

BuildPreReq: rpm-build-gnome rpm-build-licenses
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: gtk-doc >= %gtk_doc_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.6.7}

%description
Accessibility means providing system infrastructure that allows add-on
assistive software to transparently provide specalized input and ouput
capabilities. For example, screen readers allow blind users to navigate
through applications, determine the state of controls, and read text via
text to speech conversion. On-screen keyboards replace physical
keyboards, and head-mounted pointers replace mice.

ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

%package locales
Summary: Internationalization for ATK
Group: System/Internationalization
Conflicts: %name < %version-%release
BuildArch: noarch

%description locales
This package provides internationalization support for ATK,
the Accessibility Toolkit.

%package devel
Summary: Development environment for atk
Group: Development/C
Requires: %name = %version-%release
Provides: atk-devel = %version
Obsoletes: atk-devel < %version

%description devel
This package contains the necessary components to develop for ATK,
the Accessibility Toolkit.

%package devel-doc
Summary: Development documentation for ATK
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

This package contains development documentation for ATK.

%package devel-static
Summary: Stuff for developing with atk
Group: Development/C
Requires: %name-devel = %version-%release
Provides: atk-devel-static = %version
Obsoletes: atk-devel-static < %version

%description devel-static
This package contains the necessary components to develop statically
linked software for atk, the Accessibility Toolkit.

%package gir
Summary: GObject introspection data for the Atk library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Atk library

%package gir-devel
Summary: GObject introspection devel data for the Atk library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Atk library

%prep
%setup -q -n %_name-%version
%patch -p1
install -p -m644 %_sourcedir/atk-compat.map atk/compat.map
install -p -m644 %_sourcedir/atk-compat.lds atk/compat.lds

%build
%autoreconf
%configure %{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %{_name}10

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files locales -f %{_name}10.lang

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 1.91.92-alt1
- 1.91.92

* Thu Feb 10 2011 Alexey Tourbin <at@altlinux.ru> 1.33.6-alt2
- rebuilt for debuginfo
- disabled symbol versioning
- split libatk-locales noarch subpackage

* Tue Feb 01 2011 Yuri N. Sedunov <aris@altlinux.org> 1.33.6-alt1
- 1.33.6

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 1.32.0-alt1
- 1.32.0

* Wed Jun 30 2010 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt2
- rebuild with gobject-introspection-0.9.0

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt1
- 1.30.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 1.29.92-alt1
- 1.29.92

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 1.29.4-alt2
- rebuild using rpm-build-gir

* Thu Dec 24 2009 Yuri N. Sedunov <aris@altlinux.org> 1.29.4-alt1
- 1.29.4
- new gir{,-devel} subpackages
- updated version script for ATK_1.29.4

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 1.28.0-alt1
- 1.28.0

* Mon Aug 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.27.90-alt1
- 1.27.90

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt1
- 1.26

* Wed Jan 21 2009 Yuri N. Sedunov <aris@altlinux.org> 1.25.2-alt1
- 1.25.2
- updated version script
- removed obsolete *_ldconfig
- don't rebuild documentation
- built devel-doc package as noarch

* Fri Sep 26 2008 Alexey Shabalin <shaba@altlinux.ru> 1.24.0-alt1
- New version (1.24.0).

* Wed Mar 12 2008 Alexey Rusakov <ktirf@altlinux.org> 1.22.0-alt1
- New version (1.22.0).

* Wed Mar 05 2008 Alexey Rusakov <ktirf@altlinux.org> 1.21.92-alt1
- New version (1.21.92).

* Thu Oct 11 2007 Igor Zubkov <icesik@altlinux.org> 1.20.0-alt2
- update version script
- add packager tag

* Wed Oct 10 2007 Alexey Rusakov <ktirf@altlinux.org> 1.20.0-alt1
- new version (1.20.0)
- use a macro from rpm-build-licenses

* Fri Jun 29 2007 Alexey Rusakov <ktirf@altlinux.org> 1.18.0-alt1
- new version (1.18.0)
- added exported symbols versioning.

* Thu Oct 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.12.3-alt1
- new version 1.12.3 (with rpmrb script)

* Wed Aug 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.12.1-alt1
- new version 1.12.1 (with rpmrb script)

* Wed Mar 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.11.3-alt1
- new version 1.11.3 (with rpmrb script)

* Sat Feb 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.11.2-alt1
- new version

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Thu Jan 27 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Wed Sep 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.8.0-alt1
- 1.8.0
- documentation moved to devel-doc subpackage.

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Mon Apr 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.5-alt1
- 1.5.5

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Wed Dec 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.4.1-alt2
- do not package .la files.
- devel-static subpackage is optional now.

* Sun Oct 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Aug 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Thu Jun 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Fri May 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Sat May 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Sat Mar 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Mon Jan 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sat Jan 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Dec 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Sat Dec 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sat Nov 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Sun Nov 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Thu Oct 31 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Mon Oct 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Sep 03 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt1
- 1.0.3
- Description that actually describe

* Tue May 28 2002 Igor Androsov <blake@altlinux.ru> 1.0.2-alt1
- New releasa

* Thu May 23 2002 Igor Androsov <blake@altlinux.ru> 1.0.1-alt2
- clean spec
- enabled gtk-doc

* Sun Mar 31 2002 AEN <aen@logic.ru> 1.0.1-alt1
- new version

* Wed Mar 27 2002 AEN <aen@logic.ru> 1.0.0-alt1
- release

* Wed Jan 09 2002 AEN <aen@logic.ru> 0.8.90-alt1
- new version

* Wed Oct 17 2001 AEN <aen@logic.ru> 0.5-alt1
- new version

* Tue Sep 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.3-alt2
- Specfile cleanup.
- Corrected requires.

* Tue Sep 25 2001 AEN <aen@logic.ru> 0.3-alt1
- new version
- RH patch

* Wed Jun 27 2001 AEN <aen@logic.ru> 0.1-alt1
- first build for Siysphus
- static package

* Sat Jun 16 2001 Stefan van der Eijk <stefan@eijk.nu> 0.1-6mdk
- remove BuildRequires: glib-devel
- BuildRequires: libglib2-devel

* Sat Jun 16 2001 Stefan van der Eijk <stefan@eijk.nu> 0.1-5mdk
- BuildRequires: glib-devel

* Sat Jun 16 2001 Stefan van der Eijk <stefan@eijk.nu> 0.1-4mdk
- BuildRequires: pango-devel

* Tue Jun 05 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.1-3mdk
- Rebuild so that it is built for the i586 architecture (Peter Polman).

* Fri May 11 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 0.1-2mdk
- rebuild to link agaisnt new libglib2

* Sun May 06 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.1-1mdk
- First attempt for Gtk+.
