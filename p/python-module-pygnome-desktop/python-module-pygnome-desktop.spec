%def_disable gtk_doc
%def_enable evince
%def_disable nautilusburn
%def_disable panel
%def_disable media
%def_disable brasero
%def_disable desktop
%def_enable wnck
%def_enable totem
%def_disable bugbuddy
%def_disable metacity

%define major 2.32
%define oname gnome-python-desktop
%define extras_version 2.19

Name: python-module-pygnome-desktop
Version: %major.0
Release: alt6

Summary: Python modules for some GNOME libraries part of the GNOME Desktop

License: LGPL
Group: Development/Python
Url: http://www.pygtk.org/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://ftp.gnome.org/pub/GNOME/sources/%oname/%major/%oname-%version.tar.bz2

%define bname python-module-pygnome
%define python_gnome_dir %python_sitelibdir/gtk-2.0/gnome

#Requires: %bname-extras >= %extras_version

%{?_enable_evince:BuildRequires: libevince-gtk-devel >= 2.32.0 }
%{?_enable_nautilusburn:BuildRequires: libnautilus-cd-burner-devel}
%{?_enable_panel:BuildRequires: libgnome-panel-devel}
%{?_enable_media:BuildRequires: gnome-media-devel}
%{?_enable_brasero:BuildRequires: libbrasero-devel >= 2.32.0}
%{?_enable_totem:BuildRequires: libtotem-pl-parser-devel}
%{?_enable_desktop:BuildRequires: libgnome-desktop-devel}
%{?_enable_wnck:BuildRequires: libwnck-devel}
%{?_enable_metacity:BuildRequires: libmetacity-devel}
%{?_enable_bugbuddy:BuildRequires: bug-buddy}
BuildRequires: evolution-data-server-devel libgnome-keyring-devel
BuildRequires: libgnomeprintui-devel libgtop-devel
BuildRequires: librsvg-devel python-module-pycairo-devel libgtksourceview-devel
BuildRequires: libgnomeui-devel

BuildRequires: python-module-pygnome-devel >= 2.28.0
BuildRequires: python-module-pygtk-devel >= 2.22.0

%description
GnomePythonDesktop provides python interfacing modules for some
GNOME libraries part of the GNOME Desktop (gnomeapplet, gnomeprint,
gnomeprint.ui, gtksourceview, wnck, totem.plparser, gtop, nautilusburn,
mediaprofiles, metacity).

%package devel
Summary: files needed to build extra wrappers for GNOME libraries
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-devel
Requires: %bname-extras-devel >= %extras_version

%description devel
This package contains files required to build wrappers for GNOME
libraries so that they interoperate with pygnome.

%package devel-doc
Summary: Development documentation for extra wrappers for GNOME libraries
Group: Development/Python
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains development documentation required to develop
wrappers for GNOME libraries so that they interoperate with pygnome.

%package examples
Summary: Example programs that use extra wrappers for GNOME libraries
Group: Development/Python
BuildArch: noarch
Conflicts: %name < %version

%description examples
This package contains example program that use wrappers for GNOME libraries

%package -n %bname-applet
Summary: Python bindings for GNOME Panel applets
Group: System/Libraries
Obsoletes: pygnome-applet
Obsoletes: gnome-python2-applet
Provides: gnome-python2-applet
Requires: %name = %version-%release

%description -n %bname-applet
This module contains a wrapper that allows GNOME Panel applets to be
written in Python.

%package -n %bname-gtkhtml2
Summary: Python bindings for interacting with gtkhtml2
Group: System/Libraries
Requires: %name = %version-%release
Obsoletes: gnome-python2-gtkhtml2
Provides: gnome-python2-gtkhtml2

%description -n %bname-gtkhtml2
This module contains a wrapper that allows the use of gtkhtml2 via Python.

%package -n %bname-gnomeprint
Summary: Python bindings for interacting with libgnomeprint
Group: System/Libraries
Obsoletes: gnome-python2-gnomeprint
Provides: gnome-python2-gnomeprint

%description -n %bname-gnomeprint
This module contains a wrapper that allows the use of libgnomeprint via Python.

%package -n %bname-wnck
Summary: Python bindings for interacting with libwnck
Group: System/Libraries

%description -n %bname-wnck
This module contains a wrapper that allows the use of libwnck via Python.

%package -n %bname-nautilusburn
Summary: Python bindings for interacting with nautilus burn
Group: System/Libraries
Requires: %name = %version-%release

%description -n %bname-nautilusburn
This module contains a wrapper that allows the use of nautilusburn via Python

%package -n %bname-brasero
Summary: Python bindings for interacting with Brasero
Group: System/Libraries
Requires: %name = %version-%release

%description -n %bname-brasero
This module contains a wrapper that allows the use of Brasero via Python

%package -n %bname-totem
Summary: Python bindings for interacting with totem
Group: System/Libraries

%description -n %bname-totem
This module contains a wrapper that allows the use of totem via Python

%package -n %bname-metacity
Summary: Python bindings for interacting with metacity
Group: System/Libraries
Requires: %name = %version-%release

%description -n %bname-metacity
This module contains a wrapper that allows the use of metacity via Python

%package -n %bname-evolution
Summary: Python bindings for interacting with evolution
Group: System/Libraries
Requires: %name = %version-%release

%description -n %bname-evolution
This module contains a wrapper that allows the use of evolution via Python

%package -n %bname-gnome-keyring
Summary: Python bindings for interacting with gnome-keyring
Group: System/Libraries

%description -n %bname-gnome-keyring
This module contains a wrapper that allows the use of gnome-keyring via Python

%package -n %bname-evince
Summary: Python bindings for interacting with Evince
Group: System/Libraries
Obsoletes: python-module-evince
Provides: python-module-evince = %version-%release

%description -n %bname-evince
This module contains a wrapper that allows the use of Evince document
viewer via Python

%prep
%setup -q -n %oname-%version

%build
export CFLAGS="$CFLAGS `pkg-config --cflags gtk+-2.0`"
%configure --enable-metacity \
	--disable-dependency-tracking \
	--enable-evolution \
	--enable-evolution-ecal \
	%{subst_enable bugbuddy} \
	%{subst_enable metacity} \
	%{subst_enable nautilusburn} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall

mkdir -p %buildroot%_docdir/%name
cp -R examples %buildroot%_docdir/%name/

%files
%python_sitelibdir/gtk-2.0/gtop.so
%python_sitelibdir/gtk-2.0/rsvg.so
%{?_enable_media:%python_sitelibdir/gtk-2.0/mediaprofiles.so}
%{?_enable_bugbuddy:%python_sitelibdir/gtk-2.0/bugbuddy.*}
%{?_enable_desktop:%python_sitelibdir/gtk-2.0/gnomedesktop/}
%dir %_docdir/%name
%doc AUTHORS ChangeLog README NEWS

%files devel
%_pkgconfigdir/*
%_datadir/pygtk/2.0/defs/*.defs

%files examples
%_docdir/%name/examples

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled wnck
%files -n %bname-wnck
%python_sitelibdir/gtk-2.0/wnck.so
%endif

%files -n %bname-gnome-keyring
%python_sitelibdir/gtk-2.0/gnomekeyring.so

%if_enabled panel
%files -n %bname-applet
%python_gnome_dir/applet.*
%python_sitelibdir/gtk-2.0/gnomeapplet.so
%endif

%files -n %bname-gnomeprint
%python_sitelibdir/gtk-2.0/gnomeprint/

%if_enabled totem
%files -n %bname-totem
%python_sitelibdir/gtk-2.0/totem/
%endif

%if_enabled nautilusburn
%files -n %bname-nautilusburn
%python_sitelibdir/gtk-2.0/nautilusburn.so
%endif

%if_enabled brasero
%files -n %bname-brasero
%python_sitelibdir/gtk-2.0/braseroburn.so
%python_sitelibdir/gtk-2.0/braseromedia.so
%endif

%if_enabled metacity
%files -n %bname-metacity
%python_sitelibdir/gtk-2.0/metacity.so
%endif

%files -n %bname-evolution
%python_sitelibdir/gtk-2.0/evolution/

%if_enabled evince
%files -n %bname-evince
%python_sitelibdir/gtk-2.0/evince.so
%endif

%exclude %python_sitelibdir/gtk-2.0/*.la

%changelog
* Wed Jun 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt6
- moved wnck module to separate subpackage
- removed baseless dependence on python-module-pygnome-extras

* Thu Mar 29 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt5
- rebuilt against new e-d-s
- disabled bug-buddy and metacity modules

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.32.0-alt4.1
- Rebuild with Python-2.7

* Fri Oct 28 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt4
- rebuild against new gnome-3.2 libraries

* Sat Sep 17 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt3
- restored wnck module

* Fri Apr 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- built in GNOME3 environment, a few modules disabled

* Thu Oct 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt2
- rebuild against libedataserver-1.2.so.13 (e-d-s-2.30.2)

* Mon Jun 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Sun Mar 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt3
- updated for evince-2.29

* Thu Mar 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Tue Jan 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.1-alt1
- 2.29.1
- updated buildreqs

* Thu Sep 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0
- don't build nautilus-cd-burning bindings
- new brasero package

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- built evince bindings

* Mon Feb 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.90-alt1
- 2.25.90
- prepared to build new evince bindings, evince-devel required now

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.1-alt1
- 2.25.1
- updated buildreqs

* Fri Dec 19 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- new version

* Wed Dec 10 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt3
- rebuilt to link totem module with libtotem-plparser.so.12
- documentation moved to new devel-doc noarch subpackage
- examples moved to new examples noarch subpackage

* Sat Oct 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt2
- rebuild against libgnome-desktop-2.so.7

* Tue Sep 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Thu Sep 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.0-alt2
- enable build evolution module (fix bug #16648)
- update buildreq

* Wed Apr 30 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.0-alt1
- new version 2.22.0 (with rpmrb script)

* Fri Mar 21 2008 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- new version 2.20.0 (with rpmrb script)

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt2
- rebuild with new libtotem (fix bug #13890)
- add metacity subpackage
- update buildreq (remove libgtksourceview-devel from one)

* Fri Nov 30 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- update buildreq
- remove gtksourceview subpackage

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt0
- new version 2.20.0 (with rpmrb script)

* Mon Sep 03 2007 Vitaly Lipatov <lav@altlinux.ru> 2.18.0-alt3
- rebuild stable version 2.18.0, update buildreq

* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.19.2-alt1
- new version 2.19.2 (with rpmrb script)
- build without libwnck (wait for #12490)

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.18.0-alt2
- add libSM-devel to buildreq

* Fri Apr 06 2007 Vitaly Lipatov <lav@altlinux.ru> 2.18.0-alt1
- new version (2.18.0)
- add nautilus-burn, totem packages

* Sun Nov 19 2006 Vitaly Lipatov <lav@altlinux.ru> 2.17.1-alt0.3
- fix extras requires again

* Thu Nov 16 2006 Vitaly Lipatov <lav@altlinux.ru> 2.17.1-alt0.2
- fix extras requires

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.17.1-alt0.1
- new version 2.17.1 (with rpmrb script)
- The following modules will NOT be built:
  - totem.plparser
  - nautilusburn
  - metacity (too old -devel, needed 2.17.0)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.15.90-alt0.1
- new version (2.15.90)
- fix version in spec
- missed wnck

* Sun May 28 2006 Vitaly Lipatov <lav@altlinux.ru> 2.15.2-alt0.1
- new version 2.15.2 (with rpmrb script)

* Tue Mar 28 2006 Vitaly Lipatov <lav@altlinux.ru> 2.13.3-alt0.2
- update buildreqs

* Tue Mar 07 2006 Vitaly Lipatov <lav@altlinux.ru> 2.13.3-alt0.1
- initial build for ALT Linux Sisyphus
- split from -gnome-extras
- disable media
