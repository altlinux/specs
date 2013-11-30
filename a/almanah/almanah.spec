%set_automake_version 1.11
%define ver_major 0.11
%def_enable encryption
%def_enable eds

Name: almanah
Version: %ver_major.0
Release: alt1

Summary: Diary editor for GNOME
License: LGPLv3+
Group: Graphical desktop/GNOME
Url: https://live.gnome.org/Almanah_Diary
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: intltool desktop-file-utils
BuildRequires: libgio-devel libgtkspell3-devel
BuildRequires: libsqlite3-devel libcryptui-devel
%{?_enable_eds:BuildRequires: evolution-data-server-devel >= 3.5.91}
%{?_enable_encryption:BuildRequires: libgpgme-devel libseahorse-devel >= 3.0.0}

%description
Almanah is a small GTK+3 application to allow you to keep a diary of your life.

%prep
%setup -q

%build
%autoreconf
%if_enabled encryption
export CFLAGS="$CFLAGS -D_FILE_OFFSET_BITS=64"
%endif
%configure \
	%{subst_enable encryption} \
	--disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=TextTools \
	%buildroot%_desktopdir/almanah.desktop

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/%name
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/actions/almanah-tags-symbolic.svg
%config %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/GConf/gsettings/%name.convert
%_datadir/appdata/%name.appdata.xml
%doc README AUTHORS NEWS

%changelog
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


