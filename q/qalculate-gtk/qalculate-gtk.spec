%define _unpackaged_files_terminate_build 1

%define shortname qalculate

Name: qalculate-gtk
Version: 2.8.2
Release: alt1

Summary: A very versatile desktop calculator - GTK+ version.
Group: Office
License: GPL
Url: https://qalculate.github.io/

# https://github.com/Qalculate/qalculate-gtk.git
Source: %name-%version.tar

BuildRequires: gcc-c++ libcln-devel libdbus-glib libglade-devel libgmp-devel libgnome-devel
BuildRequires: libqalculate-devel = %version
BuildRequires: perl-XML-Parser scrollkeeper yelp intltool
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(libxml-2.0) pkgconfig(gtk+-3.0)

%description
A GTK+ graphical interface for Qalculate!

%prep
%setup

%build
%autoreconf
%configure --disable-rpath --enable-static=no
%make_build

%install
%makeinstall_std

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Calculator \
	--add-category=GTK \
	%buildroot%_desktopdir/qalculate-gtk.desktop

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/appdata/%name.appdata.xml
%_defaultdocdir/%name
%_desktopdir/*
%_pixmapsdir/%shortname.png

%changelog
* Tue Jan 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.2-alt1
- Updated to upstream version 2.8.2.

* Fri Jul 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.1-alt1
- Updated to upstream version 2.6.1.

* Fri May 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1
- Updated to upstream version 2.5.0.

* Mon Sep 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.7-alt3.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qalculate-gtk

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.7-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qalculate-gtk

* Mon Feb 14 2011 Nick S. Grechukh <gns@altlinux.ru> 0.9.7-alt3
- rebuilt

* Thu Apr 22 2010 Nick S. Grechukh <gns@altlinux.ru> 0.9.7-alt2
- build fixed (intltool)

* Thu Apr 22 2010 Alexey Morsov <swi@altlinux.ru> 0.9.7-alt1
- new version

* Thu Nov 27 2008 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt1.1
- build with cln 1.2.2

* Mon Jun 18 2007 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt1
- version 0.9.6
- clean spec for git

* Wed Dec 20 2006 Alexey Morsov <swi@altlinux.ru> 0.9.5-alt1
- initial build for sisyphus


