%define _name adwaita-icon-theme
%define ver_major 44
%define beta %nil

Name: icon-theme-adwaita
Version: %ver_major.0
Release: alt1%beta

Summary: Adwaita icon theme
License: CC-BY-SA-3.0 and LGPL-3.0
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz

Provides: %_name = %version-%release
Conflicts: gnome-theme-standard < 3.13.0

Requires: icon-naming-utils
BuildRequires: intltool icon-naming-utils gtk-update-icon-cache %_bindir/gtk-encode-symbolic-svg

%description
Adwaita icon theme for GTK

%prep
%setup -n %_name-%version%beta

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
%doc AUTHORS NEWS COPYING

%changelog
* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 43-alt1
- 43

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sat Sep 11 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Tue May 04 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1.1-alt1
- 40.1.1

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Fri Apr 16 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Wed Mar 17 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.8.rc
- 40.rc

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Apr 17 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Fri Nov 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Mon Nov 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Thu Sep 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Mar 18 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Feb 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.31.91-alt1
- 3.31.91

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

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

