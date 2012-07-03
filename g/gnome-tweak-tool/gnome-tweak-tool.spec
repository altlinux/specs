%define ver_major 3.4

Name: gnome-tweak-tool
Version: %ver_major.0.1
Release: alt1

Summary: A tool to customize advanced GNOME 3 options
Group: Graphical desktop/GNOME
License: GPLv3
Url: http://live.gnome.org/GnomeTweakTool
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar.xz

BuildArch: noarch
Requires: gnome-shell >= %ver_major

BuildRequires: GConf gnome-common intltool libgio-devel
BuildRequires: gsettings-desktop-schemas-devel >= 3.3.2
BuildRequires: python-module-pygobject-devel >= 2.28.0
BuildRequires: python-module-pygobject3-devel >= 3.0.0

%description
GNOME Tweak Tool is an application for changing the advanced settings
of GNOME 3.

Features:
* Install and switch gnome-shell themes
* Switch GTK+ themes
* Switch icon themes
* Change
  - The user-interface and title bar fonts
  - Icons in menus and buttons
  - Behavior on laptop lid close
  - Shell font size
  - File manager desktop icons
  - Title bar click action
  - Shell clock to show date
  - Font hinting
  - Font anti-aliasing

%prep
%setup

%build
# NOCONFIGURE=1 ./autogen.sh
%configure --disable-schemas-compile
%make_build

%install
%make_install install DESTDIR=%buildroot

%find_lang %name

%files -f %name.lang
%_bindir/%name
%python_sitelibdir/gtweak
%_datadir/applications/%name.desktop
%_datadir/%name
%doc AUTHORS NEWS README

%changelog
* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Thu Mar 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.5-alt1
- 3.3.5 snapshot

* Sat Nov 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.0-alt1.1
- Rebuild with Python-2.7

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Sun May 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Thu Apr 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Wed Apr 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Thu Apr 07 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- Initial package
