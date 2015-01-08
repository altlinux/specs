%define ver_major 1.0
%def_with recording

Name: girl
Version: %ver_major.0
Release: alt1

Summary: GNOME Internet Radio Locator
License: LGPLv2+
Group: Sound

URL: http://people.gnome.org/~paobac/goobox/
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: totem
%{?_with_recording:Requires: streamripper}

%define gtk_ver 3.6.0

BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: gnome-common intltool libgnomeui-devel libxml2-devel

%description
GIRL is a GNOME Internet Radio Locator program that allows the user
to easily find and record live radio programs on radio broadcasters
on the Internet.

%prep
%setup
echo "girl_LDADD=\$(GIRL_LIBS)" >> src/Makefile.am

%build
%autoreconf
export ac_cv_path_GIRL_HELPER_PLAYER=%_bindir/totem
export ac_cv_path_GIRL_HELPER_RECORD=%_bindir/streamripper
%configure \
	%{subst_with recording}
%make_build V=1

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/appdata/%name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS NEWS README TODO LETTER HACKING


%changelog
* Thu Jan 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Dec 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- first build for Sisyphus

