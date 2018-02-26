%define ver_major 3.4

Name: yelp-tools
Version: %ver_major.1
Release: alt1

Summary: Collection of tools for building and converting documentation
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://projects.gnome.org/yelp/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch
Requires: yelp-xsl

BuildRequires: yelp-xsl itstool xml-utils xsltproc

%description
yelp-tools is a collection of scripts and build utilities to help
create, manage, and publish documentation for Yelp and the web. Most of
the heavy lifting is done by packages like yelp-xsl and itstool. This
package just wraps things up in a developer-friendly way.

%prep
%setup

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/yelp-build
%_bindir/yelp-check
%_bindir/yelp-new
%_datadir/yelp-tools/
%_datadir/aclocal/yelp.m4
%doc AUTHORS README

%changelog
* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- first build for Sisyphus

