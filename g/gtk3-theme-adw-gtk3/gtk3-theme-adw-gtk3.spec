%def_disable snapshot
%define themename adw-gtk3

%def_disable precompiled_dart_sass

Name: gtk3-theme-%themename
Version: 6.5
Release: alt1

Summary: The theme from libadwaita ported to GTK+3
License: LGPL-2.1
Group: Graphical desktop/GNOME
Url: https://github.com/lassekongo83/adw-gtk3

Vcs: https://github.com/lassekongo83/adw-gtk3.git

%if_disabled snapshot
Source: https://github.com/lassekongo83/adw-gtk3/archive/v%version/%themename-%version.tar.gz
%else
Source: %themename-%version.tar
%endif
Source1: https://github.com/sass/dart-sass/releases/download/1.87.0/dart-sass-1.87.0-linux-x64.tar.gz

ExclusiveArch: x86_64
BuildArch: noarch
Provides: %themename = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
%{?_disable_precompiled_dart_sass:BuildRequires: dart-sass}

%description
%summary

%prep
%setup -n %themename-%version %{?_enable_precompiled_dart_sass:-a1}

%build
%{?_enable_precompiled_dart_sass:export PATH=$PATH:$PWD/dart-sass}
%meson
%meson_build

%install
%meson_install

%files
%_datadir/themes/%themename
%_datadir/themes/%themename-dark
%doc README*

%changelog
* Tue Apr 14 2026 Yuri N. Sedunov <aris@altlinux.org> 6.5-alt1
- 6.5

* Sat Sep 27 2025 Yuri N. Sedunov <aris@altlinux.org> 6.4-alt1
- 6.4

* Sat Sep 06 2025 Yuri N. Sedunov <aris@altlinux.org> 6.3-alt1
- 6.3

* Fri Jun 13 2025 Yuri N. Sedunov <aris@altlinux.org> 6.2-alt1.1
- rebuilt with our dart-sass

* Sat May 10 2025 Yuri N. Sedunov <aris@altlinux.org> 6.2-alt1
- 6.2

* Fri May 02 2025 Yuri N. Sedunov <aris@altlinux.org> 6.1-alt1
- 6.1

* Fri Apr 18 2025 Yuri N. Sedunov <aris@altlinux.org> 5.10-alt1
- 5.10

* Tue Apr 15 2025 Yuri N. Sedunov <aris@altlinux.org> 5.9-alt1
- 5.9

* Tue Apr 08 2025 Yuri N. Sedunov <aris@altlinux.org> 5.8-alt1
- 5.8

* Tue Mar 18 2025 Yuri N. Sedunov <aris@altlinux.org> 5.7-alt1
- 5.7

* Sun Dec 01 2024 Yuri N. Sedunov <aris@altlinux.org> 5.6-alt1
- 5.6

* Sun Oct 13 2024 Yuri N. Sedunov <aris@altlinux.org> 5.5-alt1
- 5.5

* Mon Sep 23 2024 Yuri N. Sedunov <aris@altlinux.org> 5.4-alt1
- 5.4

* Mon Mar 18 2024 Yuri N. Sedunov <aris@altlinux.org> 5.3-alt1
- 5.3

* Sun Dec 10 2023 Yuri N. Sedunov <aris@altlinux.org> 5.2-alt1
- 5.2

* Thu Oct 19 2023 Yuri N. Sedunov <aris@altlinux.org> 5.1-alt1
- 5.1

* Fri Oct 13 2023 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1
- 5.0

* Fri Sep 01 2023 Yuri N. Sedunov <aris@altlinux.org> 4.9-alt1
- 4.9

* Thu Jun 15 2023 Yuri N. Sedunov <aris@altlinux.org> 4.8-alt1
- 4.8

* Fri May 19 2023 Yuri N. Sedunov <aris@altlinux.org> 4.7-alt1
- 4.7

* Wed May 03 2023 Yuri N. Sedunov <aris@altlinux.org> 4.6-alt1
- 4.6

* Tue Apr 04 2023 Yuri N. Sedunov <aris@altlinux.org> 4.5-alt1
- 4.5

* Fri Mar 24 2023 Yuri N. Sedunov <aris@altlinux.org> 4.4-alt1
- 4.4

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


