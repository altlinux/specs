%define shortname qalculate

Name: qalculate-gtk
Version: 0.9.7
Release: alt3.qa2

Summary: A very versatile desktop calculator - GTK+ version.
Group: Office
License: GPL
Url: http://qalculate.sourceforge.net
Packager: Alexey Morsov <swi@altlinux.ru>
Requires: %shortname-common

Source: %name-%version.tar

BuildRequires: gcc-c++ libcln-devel libdbus-glib libglade-devel libgmp-devel libgnome-devel 
BuildRequires: libqalculate-devel = %version
BuildRequires: perl-XML-Parser scrollkeeper yelp intltool
BuildRequires: desktop-file-utils

%description
A GTK+ graphical interface for Qalculate!

%prep
%setup

%build 
%autoreconf
%configure --disable-rpath --enable-static=no
%make_build

%install
%make_install DESTDIR=%buildroot install

rm -f %buildroot%_bindir/qalculate
rm -rf %buildroot%_datadir/locale

%find_lang --with-gnome %shortname
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Calculator \
	%buildroot%_desktopdir/qalculate-gtk.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Calculator \
	--add-category=GTK \
	%buildroot%_desktopdir/qalculate-gtk.desktop

%files -f %shortname.lang
%_bindir/%name
%_datadir/applications/*
%_datadir/gnome/help/
%_datadir/%name/glade/
%_pixmapsdir/%shortname.png


%changelog
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


