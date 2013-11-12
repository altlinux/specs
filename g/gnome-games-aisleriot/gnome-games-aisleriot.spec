%define _unpackaged_files_terminate_build 1

%define _name aisleriot
%define ver_major 3.10
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.2
Release: alt1

Summary: A collection of card games
Group: Games/Cards
License: GPLv3+ and LGPLv3+ and GFDL
Url: http://live.gnome.org/Aisleriot

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Obsoletes: gnome-games-sol
Provides:  gnome-games-sol = %version-%release
Provides:  %_name = %version-%release

Requires(post,preun): GConf
Requires: pysol-cardsets

%define glib_ver 2.32.0
%define gtk_ver 3.0.0

BuildRequires: intltool desktop-file-utils yelp-tools libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver libGConf-devel librsvg-devel libcanberra-gtk3-devel
BuildRequires: libICE-devel libSM-devel gstreamer-devel guile20 libguile20-devel
BuildRequires: /proc

%description
AisleRiot also known as Solitaire or sol is a collection of over 80 card games
which are easy to play with the aid of a mouse.

%prep
%setup -n %_name-%version

%build
%configure \
    --with-pysol-card-theme-path=%_datadir/games/pysol
%make

%install
make DESTDIR=%buildroot install

%find_lang --with-gnome %_name

%post
%gconf2_install %_name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %_name
fi

%files -f %_name.lang
%attr(-,root,games) %_bindir/sol
%_libdir/%_name/
%dir %_libexecdir/%_name
%_libexecdir/%_name/ar-cards-renderer
%_datadir/%_name
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/HighContrast/*/apps/*.svg
%_sysconfdir/gconf/schemas/%_name.schemas
%_datadir/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%_man6dir/sol.*

%exclude %_libdir/valgrind/aisleriot.supp

%changelog
* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.91-alt1
- 3.7.91

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Oct 11 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Nov 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- first build for Sisyphus

