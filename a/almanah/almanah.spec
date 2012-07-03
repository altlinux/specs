BuildRequires: desktop-file-utils
%define ver_major 0.9
%def_enable encryption

Name: almanah
Version: %ver_major.0
Release: alt1

Summary: Diary editor for GNOME
License: LGPLv3+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/Almanah_Diary
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: intltool
BuildRequires: libgio-devel libgtkspell3-devel evolution-data-server-devel >= 3.0.0
BuildRequires: libsqlite3-devel libcryptui-devel
%{?_enable_encryption:BuildRequires: libgpgme-devel libseahorse-devel >= 3.0.0}

%description
Almanah is a small GTK+3 application to allow you to keep a diary of your life.

%prep
%setup -q

%build
%if_enabled encryption
export CFLAGS="$CFLAGS -D_FILE_OFFSET_BITS=64"
%endif

%configure \
	%{subst_enable encryption} \
	--disable-schemas-compile
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=TextTools \
	%buildroot%_desktopdir/almanah.desktop

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/%name
%_iconsdir/hicolor/*x*/apps/%name.png
%config %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/GConf/gsettings/%name.convert
%doc README AUTHORS NEWS

%changelog
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


