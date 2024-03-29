%define ver_major 42
%define beta %nil

Name: yelp-xsl
Version: %ver_major.1
Release: alt1%beta

Summary: XSLT stylesheets for the Yelp, GNOME help browser
License: GPL-2.0 and LGPL-2.1 and MIT
Group: Graphical desktop/GNOME
Url: http://yelp.io

Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz

BuildArch: noarch

BuildRequires(pre): rpm-build-gnome
BuildRequires: libxml2-devel libxslt-devel itstool xsltproc xmllint
BuildRequires: python3-module-mallard-ducktype

%description
Yelp is a help browser for the GNOME desktop. Yelp provides a simple
graphical interface for viewing DocBook, HTML, man, and info formatted
documentation.

This package contains XSLT stylesheets that are used by the Yelp.

%prep
%setup -n %name-%version%beta

%build

%configure --enable-doc
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_datadir/%name
%_datadir/pkgconfig/yelp-xsl.pc
%doc AUTHORS README* NEWS COPYING

%changelog
* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sat Dec 04 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Mon Jun 07 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sat Feb 13 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Sat Nov 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sun Oct 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sun Sep 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0
- fixed License tag

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

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

