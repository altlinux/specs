%define _name elementaryicons
%define ver_major 7.0
%define rdn_name io.elementary.icons
%def_disable palettes

Name: elementary-icon-theme
Version: %ver_major.0
Release: alt1

Summary: simple and appealing Tango-styled icon theme
Group: Graphical desktop/Other
License: GPL-3.0
Url: https://github.com/elementary/icons

# VCS:https://github.com/elementary/icons.git
Source: %url/archive/%version/icons-%version.tar.gz

BuildArch: noarch

Requires: icon-theme-hicolor

BuildRequires(pre): meson
BuildRequires: inkscape xcursorgen /usr/bin/rsvg-convert

%description
The official elementary icons are designed to be simple and appealing.

These icons are the inspiration behind Ubuntu's default Humanity icon
theme.

%prep
%setup -n icons-%version

%build
%meson %{?_disable_palettes:-Dpalettes=false}
%meson_build

%install
%meson_install

%files
%_iconsdir/elementary
%if_enabled palettes
%_datadir/gimp/2.0/palettes/elementary.gpl
%_datadir/inkscape/palettes/elementary.gpl
%endif
%_datadir/metainfo/%rdn_name.appdata.xml
%doc README*

%changelog
* Wed May 04 2022 Yuri N. Sedunov <aris@altlinux.org> 7.0.0-alt1
- 7.0.0

* Thu Nov 25 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.0-alt1
- 6.1.0

* Mon Jul 19 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1
- 6.0.0

* Sat May 30 2020 Yuri N. Sedunov <aris@altlinux.org> 5.3.1-alt1
- 5.3.1

* Sun May 10 2020 Yuri N. Sedunov <aris@altlinux.org> 5.3.0-alt1
- 5.3.0

* Mon Jan 27 2020 Yuri N. Sedunov <aris@altlinux.org> 5.2.0-alt1
- 5.2.0
- updated BR

* Fri Nov 08 2019 Yuri N. Sedunov <aris@altlinux.org> 5.1.0-alt1
- 5.1.0

* Mon Jul 22 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.4-alt1
- 5.0.4

* Fri Feb 15 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.3-alt1
- 5.0.3

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.2-alt1
- 5.0.2

* Fri Oct 26 2018 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1
- 5.0

* Thu Apr 05 2018 Yuri N. Sedunov <aris@altlinux.org> 4.3.1-alt1
- 4.3.1

* Thu Sep 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Sep 13 2013 Igor Zubkov <icesik@altlinux.org> 3.2-alt1
- 3.1 -> 3.2 (bzr -r1136)

* Mon Sep 09 2013 Igor Zubkov <icesik@altlinux.org> 3.1-alt1
- build for Sisyphus


