%define _name adwaita-icon-theme
%define ver_major 3.26

Name: icon-theme-adwaita
Version: %ver_major.1
Release: alt1

Summary: Adwaita icon theme
License: Creative Commons Attribution-Share Alike 3.0
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Provides: %_name = %version-%release
Conflicts: gnome-theme-standard < 3.13.0

Requires: icon-naming-utils
BuildRequires: intltool icon-naming-utils gtk-update-icon-cache

%description
Adwaita icon theme for GTK+.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %_name

%files -f %_name.lang
%_iconsdir/Adwaita/
%_datadir/pkgconfig/%_name.pc
%doc AUTHORS README NEWS COPYING

%changelog
* Mon Nov 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Thu Sep 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20-alt1
- 3.20

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2.1-alt1
- 3.16.2.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed Jul 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.13.4-alt1
- first build for Sisyphus

