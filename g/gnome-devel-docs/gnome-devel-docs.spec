%define ver_major 3.4

Name: gnome-devel-docs
Version: %ver_major.1
Release: alt1

Summary: General GNOME Developper Documentation
License: %fdl
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

Obsoletes: gnome-users-guide
Provides: gnome-users-guide
Obsoletes: gnome2-user-docs
Provides: gnome2-user-docs

PreReq: librarian

BuildPreReq: rpm-build >= 4.0.4-alt100.39
BuildPreReq: rpm-build-gnome rpm-build-licenses rpm-build-gir
BuildPreReq: rpm >= 4.0.4-alt14
BuildPreReq: gnome-doc-utils >= 0.5.6

BuildRequires: intltool xml-utils xsltproc

%description
This package contains documents which are targeted for GNOME developers.
It provides the Platform Overview, Human Interface Guidelines, the
Integration Guide, the Documentation Style Guide, the Accessibility
Guide and the Handbook of Writing Software Documentation.

%package -n gnome-devel-demos
Summary: GNOME Developer Platform demos
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description -n gnome-devel-demos
This package is a part of %name and provides demos for GNOME developpers

%prep
%setup -q

%build
%configure

%make_build

%install

%make_install DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang hig-book integration-guide platform-overview optimization-guide accessibility-devel-guide

%files -f %name.lang
%doc AUTHORS README NEWS

%files -n gnome-devel-demos
%_datadir/gnome/help/gnome-devel-demos/

%changelog
* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.1-alt1.1
- Rebuild with Python-2.7

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sat Apr 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Fri Nov 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Dec 15 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- first build for Sisyphus.

