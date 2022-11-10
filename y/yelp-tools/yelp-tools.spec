%define ver_major 42
%define beta %nil

Name: yelp-tools
Version: %ver_major.1
Release: alt1%beta

Summary: Collection of tools for building and converting documentation
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://yelp.io

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz

BuildArch: noarch

Requires: yelp-xsl >= 3.38.0 itstool xmllint xsltproc
# Optional jing dep
#%%filter_from_requires /jing/d

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson python3-module-lxml
BuildRequires: yelp-xsl itstool xml-utils xsltproc

%description
yelp-tools is a collection of scripts and build utilities to help
create, manage, and publish documentation for Yelp and the web. Most of
the heavy lifting is done by packages like yelp-xsl and itstool. This
package just wraps things up in a developer-friendly way.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/yelp-build
%_bindir/yelp-check
%_bindir/yelp-new
%_datadir/yelp-tools/
%_datadir/aclocal/yelp.m4
%doc AUTHORS NEWS

%changelog
* Tue Nov 01 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sun Sep 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Thu Jun 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Tue May 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed Apr 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- first build for Sisyphus

