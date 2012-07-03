%define ver_major 3.2

Name: simple-scan
Version: %ver_major.1
Release: alt1

Summary: Simple scanning utility
License: GPLv3+
Group: Graphics

Url: http://launchpad.net/simple-scan
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%version/+download/simple-scan-%version.tar.xz

BuildRequires: gnome-doc-utils intltool
BuildRequires: libgtk+3-devel libgudev-devel libcolord-devel
BuildRequires: libjpeg-devel libsane-devel zlib-devel

# For gconf_schemasdir and gnome_helpdir definitions:
BuildRequires: rpm-build-gnome

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%gnome_helpdir/%name
%_desktopdir/*
%_datadir/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%_man1dir/*

%changelog
* Wed Nov 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Apr 25 2011 Victor Forsiuk <force@altlinux.org> 2.32.0.2-alt1
- 2.32.0.2

* Tue Mar 08 2011 Victor Forsiuk <force@altlinux.org> 2.32.0.1-alt2
- Refresh BuildRequires.

* Mon Dec 06 2010 Victor Forsiuk <force@altlinux.org> 2.32.0.1-alt1
- 2.32.0.1

* Wed Oct 20 2010 Victor Forsiuk <force@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 28 2010 Victor Forsiuk <force@altlinux.org> 2.31.91-alt1
- 2.31.91
- Patch to remove zlib detection by pkgconfig (no zlib.pc in our zlib-devel).

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 2.31.1-alt1
- 2.31.1

* Tue Mar 16 2010 Victor Forsiuk <force@altlinux.org> 0.9.9-alt1
- 0.9.9

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 0.9.7-alt1
- 0.9.7

* Mon Mar 01 2010 Victor Forsiuk <force@altlinux.org> 0.9.5-alt1
- Initial build.
