Name: giggle
Version: 0.6.1
Release: alt2

Summary: Giggle is a Gtk frontend to git.
Group: Development/Other
License: GPL
URL: http://live.gnome.org/giggle
Packager: Vladimir Lettiev <crux@altlinux.ru>

Source: %name-%version.tar
Patch: giggle-0.6.1-up-link.patch

Requires: git-core

# Automatically added by buildreq on Mon Apr 30 2007
BuildRequires: git-core libgtksourceview3-devel yelp-tools itstool
BuildRequires: intltool evolution-data-server-devel cvs gnome-common libvte3-devel

%description
Giggle is a Gtk frontend to git.

With Giggle you will be able to visualize and browse easily the revision tree,
view changed files and differences between revisions, visualize summarized info
for the project, commit changes and other useful tasks for any git managed
projects contributor.

See http://live.gnome.org/giggle for more information.

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %version-%release
%description devel
%summary

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static \
	--enable-evolution-data-server

%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name
%_libdir/lib%name.so.*
%_libdir/lib%name-git.so.*
%_iconsdir/*/*/*/*
%_desktopdir/%name.desktop
%dir %_datadir/%name
%_datadir/%name/*

%files devel
%_libdir/*.so
%_includedir/%name

%changelog
* Thu Mar 29 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt2
- rebuild against libebook-1.2.so.13

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Fri Oct 21 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6
- updated buildreqs

* Mon Oct 11 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5-alt2
- rebuild

* Sat Apr 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.5-alt1
- New version 0.5

* Sun Mar 14 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.97-alt1
- New version 0.4.97

* Wed Mar 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.96-alt1
- New version 0.4.96
- 001-Replace_deprecated_GtkSourceView_function.patch merged upstream

* Mon Jan 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.91-alt2
- fix build

* Mon Apr 13 2009 Vladimir Lettiev <crux@altlinux.ru> 0.4.91-alt1
- new version
- build devel subpackage

* Wed Jan 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4-alt2
- add missed library to package
- fix #13940

* Tue Dec 25 2007 Eugene Ostapets <eostapets@altlinux.org> 0.4-alt1
- 0.4

* Sun Jun 17 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3-alt1
- new version
- fix 11803

* Mon Apr 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2-alt0.1
- first build
