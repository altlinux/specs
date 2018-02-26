%define ver_major 3.4

Name: yelp-xsl
Version: %ver_major.2
Release: alt1

Summary: XSLT stylesheets for the Yelp, GNOME help browser
License: %gpl2plus
Group: Graphical desktop/GNOME
URL: http://live.gnome.org/yelp
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

BuildPreReq: rpm-build-licenses rpm-build-gnome
BuildRequires: libxml2-devel libxslt-devel intltool itstool xsltproc

%description
Yelp is a help browser for the GNOME desktop. Yelp provides a simple
graphical interface for viewing DocBook, HTML, man, and info formatted
documentation.

This package contains XSLT stylesheets that are used by the Yelp.

%prep
%setup -q

%build

%configure --enable-doc
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_datadir/%name
%_datadir/pkgconfig/yelp-xsl.pc
%doc AUTHORS README NEWS

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Sep 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.5-alt1
- 3.1.5

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.91-alt1
- 2.91.91

* Fri Dec 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.91.8-alt1
- 2.91.8

* Sun Oct 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.5-alt1
- 2.31.5

* Mon Jun 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.3-alt1
- 2.31.3

* Fri May 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.2-alt1
- first build for Sisyphus

