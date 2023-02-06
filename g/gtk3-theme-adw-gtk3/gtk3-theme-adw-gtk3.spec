%def_disable snapshot
%define themename adw-gtk3

Name: gtk3-theme-%themename
Version: 4.3
Release: alt1

Summary: The theme from libadwaita ported to GTK+3
License: LGPL-2.1
Group: Graphical desktop/GNOME
Url: https://github.com/lassekongo83/adw-gtk3

%if_disabled snapshot
Source: https://github.com/lassekongo83/adw-gtk3/archive/v%version/%themename-%version.tar.gz
%else
Vcs: https://github.com/lassekongo83/adw-gtk3.git
Source: %themename-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson sassc

%description
%summary

%prep
%setup -n %themename-%version

%build
%meson
%meson_build

%install
%meson_install

%files
%_datadir/themes/%themename
%_datadir/themes/%themename-dark
%doc README*

%changelog
* Mon Feb 06 2023 Yuri N. Sedunov <aris@altlinux.org> 4.3-alt1
- 4.3

* Mon Jan 02 2023 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2

* Tue Nov 15 2022 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- 4.1

* Wed Oct 05 2022 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0

* Tue Oct 04 2022 Yuri N. Sedunov <aris@altlinux.org> 3.7-alt1
- first build for Sisyphus


