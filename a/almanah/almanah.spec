%def_enable snapshot

%define ver_major 0.12
%def_enable eds

Name: almanah
Version: %ver_major.3
Release: alt3

Summary: Diary editor for GNOME
License: LGPLv3+
Group: Graphical desktop/GNOME
Url: http://wiki.gnome.org/Apps/Almanah_Diary

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.62

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson desktop-file-utils libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver libgtksourceview3-devel libgtkspell3-devel
BuildRequires: libsqlite3-devel libcryptui-devel gcr-libs-devel libgpgme-devel
%{?_enable_eds:BuildRequires: evolution-data-server-devel >= 3.5.91}

%description
Almanah is a small GTK+3 application to allow you to keep a diary of your life.

%prep
%setup

%build
%meson \
	%{?_disable_eds:-Devolution=false}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=TextTools \
	%buildroot%_desktopdir/almanah.desktop

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/*/%name-*.svg
%config %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/GConf/gsettings/%name.convert
%_datadir/metainfo/%name.appdata.xml
%doc README* AUTHORS NEWS

%changelog
* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt3
- updated to 0.12.3-13-gfe197a0 (fixed build with meson >= 0.61)

* Mon Mar 15 2021 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt2
- rebuild against libedataserver-1.2.so.26

* Fri Mar 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3

* Thu Sep 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- 0.12.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0 (ported to Meson build system)

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt3
- rebuilt with eds-3.16 libraries

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt2
- APPSTREAM_XML used instead of APPDATA_XML

* Thu Sep 25 2014 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1

* Sat Nov 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0
- e-d-s support enabled again
- automake-1.11 used

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt2
- rebuilt for GNOME-3.8
- e-d-s support temporarily disabled

* Mon Mar 11 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Tue Dec 11 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt2
- rebuilt against libgtkspell-3.0

* Sat Sep 22 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt2
- rebuilt against new evolution-data-server (3.2.1)

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for almanah

* Fri Apr 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Mon Oct 11 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt3
- rebuild against new e-d-s-2.32.0 libraries

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt2
- rebuild against libedataserver-1.2.so.13 (e-d-s-2.30.2)

* Sun Apr 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- 0.7.3

* Sun Jan 31 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- first build for Sisyhus


