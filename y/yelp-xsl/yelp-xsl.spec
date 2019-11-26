%define ver_major 3.34

Name: yelp-xsl
Version: %ver_major.2
Release: alt1

Summary: XSLT stylesheets for the Yelp, GNOME help browser
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://yelp.io

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

BuildPreReq: rpm-build-licenses rpm-build-gnome
BuildRequires: libxml2-devel libxslt-devel itstool xsltproc xmllint
BuildRequires: python3-module-mallard-ducktype

%description
Yelp is a help browser for the GNOME desktop. Yelp provides a simple
graphical interface for viewing DocBook, HTML, man, and info formatted
documentation.

This package contains XSLT stylesheets that are used by the Yelp.

%prep
%setup

%build

%configure --enable-doc
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_datadir/%name
%_datadir/pkgconfig/yelp-xsl.pc
%doc AUTHORS README NEWS

%changelog
* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Oct 06 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Mar 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.92-alt1
- 3.15.92

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

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

