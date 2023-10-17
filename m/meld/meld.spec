%def_enable snapshot

%define ver_major 3.22
%define xdg_name org.gnome.Meld

%def_enable check

Name: meld
Version: %ver_major.0
Release: alt2

Summary: Meld Diff Viewer
License: GPL-2.0-or-later
Group: Text tools
Url: http://meld.app

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

%define gtk_api_ver 3.0
%define gtksource_api_ver 4

Requires: typelib(Gtk) = %gtk_api_ver
Requires: typelib(GtkSource) = %gtksource_api_ver

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson yelp-tools /usr/bin/appstream-util desktop-file-utils
BuildRequires: python3-devel python3-module-pygobject3-devel python3-module-pycairo-devel
BuildRequires: gir(Gtk) = %gtk_api_ver gir(GtkSource) = %gtksource_api_ver

%description
Meld is a visual diff and merge tool. It lets you compare two or three
files, and updates the comparisons while you edit them in-place. You
can also compare folders, launching comparisons of individual files as
desired. Last but by no means least, Meld lets you work with your
current changes in a wide variety of version control systems,
including Git, Bazaar, Mercurial, Subversion and CVS.

%prep
%setup

%build
%meson -Dbyte-compile=false
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%python3_sitelibdir_noarch/*
%exclude %python3_sitelibdir_noarch/%name/build_helpers.py
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/glib-2.0/schemas/org.gnome.meld.gschema.xml
%_datadir/mime/packages/%xdg_name.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%_man1dir/%name.1.*
%doc NEWS README*

%changelog
* Tue Oct 17 2023 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt2
- updated to 3.22.0-53-geebd1a0e
- excluded useless build_helpers.py

* Sun Sep 04 2022 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Aug 14 2022 Yuri N. Sedunov <aris@altlinux.org> 3.21.3-alt1
- 3.21.3

* Sat Jun 18 2022 Yuri N. Sedunov <aris@altlinux.org> 3.21.2-alt1
- 3.21.2 (ported to Meson build system)

* Fri Aug 13 2021 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Sat Feb 13 2021 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Sun Feb 16 2020 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Sun Mar 31 2019 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sun Jan 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Nov 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.19.1-alt1
- 3.19.1

* Wed Mar 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.19.0-alt1
- 3.19.0

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sun Dec 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt1
- 3.16.4

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Sat Jul 30 2016 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Sun Jun 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu May 05 2016 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Sun Oct 04 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Thu Jul 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Dec 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Mon Nov 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sun Oct 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sat Sep 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sat Jul 19 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.6-alt1
- 1.8.6

* Sun May 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Thu Jan 23 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

* Sun Dec 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Fri Oct 18 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Sun Sep 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Sun Sep 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sun Sep 01 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.5-alt1
- 1.7.5

* Sun Jul 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.4-alt1
- 1.7.4

* Tue Jun 04 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.17.2

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1
- required python(gtksourceview2)

* Sat Oct 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue May 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Tue Apr 03 2012 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Fri Jan 27 2012 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt1.1
- Rebuild with Python-2.7

* Tue Aug 09 2011 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Sun Mar 20 2011 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Thu Mar 10 2011 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0 snapshot, potentially fixed ALT #25213

* Fri Jun 25 2010 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.1
- Rebuilt with python 2.6

* Fri Aug 14 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Sat Apr 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0
- updated requires

* Sun Nov 23 2008 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1
- remove obsolete %%{update,clean}_{scrollkeeper,menus} calls from %%post{,un}

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.1.5.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for meld

* Wed Mar 05 2008 Alexey Rusakov <ktirf@altlinux.org> 1.1.5.1-alt2
- Re-updated Russian translation again.

* Mon Mar 03 2008 Alexey Rusakov <ktirf@altlinux.org> 1.1.5.1-alt1
- New version (1.1.5.1).
- Switching to git-based package building.
- Use license macro, more usage of path macros.
- Removed Russian summary and description from the specfile.
- Added Packager tag to the specfile.
- Updated Russian translation.
- Removed exclusion of Scrollkeeper files in /var, this is no more needed.
- Use %%make_install macro instead of %%makeinstall.

* Sun Jun 10 2007 Alexey Rusakov <ktirf@altlinux.org> 1.1.5-alt1
- new version (1.1.5)
- spec cleanup
- 'tweak patch preview' patch went upstream.
- use %%makeinstall macro for installation, as it is more suitable here than
  %%make_install; added a quickfix for incorrect localstatedir usage inside
  install scripts
- updated Russian translation

* Thu Jun 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.1.4-alt2
- updated from CVS
- 'editable patch preview' patch went upstream.
- minor fix in Russian translation.
- a new patch: 'syntax highlight in patch preview'.

* Sun Jun 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.1.4-alt1
- new version (1.1.4)
- updated Russian translation.

* Tue Jun 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.1.3-alt2
- fixed building on x86_64
- removed Debian menu support.

* Tue Jun 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.1.3-alt1
- new version 1.1.3
- fixed bug #9668.
- patch #3 went upstream.

* Thu Nov 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.1.2-alt2
- Added a patch for cairo drawing and upped PyGtk version requirement due to it.
- Using Russian translation from the tarball (hopefully fixes bug #8428).

* Wed Nov 09 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.1.2-alt1
- new version

* Thu Oct 27 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.1.1-alt1
- new version

* Mon Jul 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.0.0-alt1
- Official release.

* Thu Jun 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.9.6-alt4
- 1.0 pre-release.
- Updated Russian translation.

* Mon Jun 20 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.9.6-alt3
- New CVS snapshot.

* Sat Jun 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.9.6-alt2
- Updated from CVS.
- Added a patch for GNOME Bug #158071.

* Fri May 20 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.9.6-alt1
- New upstream version.

* Sun Apr 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.9.5-alt3
- Sources updated from CVS (minor fixes).
- Additional updates to Russian translation.

* Sat Mar 12 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.9.5-alt2
- Added description to spec.
- Russian translation.

* Tue Feb 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- new version
- add requires for gtksourceview

* Tue Nov 30 2004 Vitaly Lipatov <lav@altlinux.ru> 0.9.4.1-alt2
- add requires for libglade (bug #5583)
- fix source and Url in spec

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 0.9.4.1-alt1
- first build for ALT Linux Sisyphus

