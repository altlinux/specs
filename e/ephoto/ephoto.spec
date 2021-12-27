%def_enable snapshot
%define _libexecdir %_prefix/libexec
%define beta %nil

Name: ephoto
Version: 1.6.0
Release: alt1

Summary: The Enlightenment Photo Viewer
Group: Graphical desktop/Enlightenment
License: BSD-2-Clause
Url: https://www.smhouston.us/%name/

%if_disabled snapshot
Source: https://www.smhouston.us/stuff/%name-%version%beta.tar.xz
%else
Vcs: https://git.enlightenment.org/apps/ephoto.git
Source: %name-%version%beta.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libelementary-devel >= 1.26.0 libcheck-devel libexif-devel

%description
Photo Viewer for Enlightenment desktop.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/%{name}_thumbnail
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/%name.png
%doc AUTHORS README TODO

%changelog
* Mon Dec 27 2021 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Mon Jun 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt3
- updated to 36b629c (added russian translation)
- fixed License tag

* Thu Feb 11 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt2
- updated to 09873c6 (ported to Meson build system)

* Tue Aug 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- 1.5

* Tue Apr 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0 release

* Thu Mar 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt0.2
- 1.0-beta3

* Tue Aug 30 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt0.1
- 1.0-beta2

* Tue Feb 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt0.2
- updated to f3cff05b
- built for E18

* Mon Jan 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt0.1
- first preview for Sisyphus (2dad9dc6)


