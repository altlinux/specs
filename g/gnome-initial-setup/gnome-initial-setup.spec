%define ver_major 41
%define beta %nil
%define gst_api_ver 1.0
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%def_disable software_sources
%def_enable cheese
%def_enable systemd
%def_enable malcontent

Name: gnome-initial-setup
Version: %ver_major.4
Release: alt1%beta

Summary: GNOME Initial Setup
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://gitlab.gnome.org/GNOME/gnome-initial-setup

Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version%beta.tar.xz

%define nm_ver 1.2
%define nma_ver 1.0
%define glib_ver 2.64.0
%define gtk_ver 3.12.0
%define secret_ver 0.18.8
%define geoclue_ver 2.4.3
%define packagekit_ver 1.1.4
%define gsds_ver 3.37.1
%define cheese_ver 3.28
%define ibus_ver 1.4.99
%define malcontent_ver 0.6.0

Requires: gnome-shell >= 3.37.92 gdm dconf geoclue2 >= %geoclue_ver
Requires: gsettings-desktop-schemas >= %gsds_ver
Requires: ibus gnome-keyring
Requires: gnome-getting-started-docs
%{?_enable malcontent:Requires: malcontent}
#Requires: gnome-tour

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: libnm-devel >= %nm_ver libnma-devel >= %nma_ver
BuildRequires: libkrb5-devel libpwquality-devel
BuildRequires: libxkbfile-devel libibus-devel >= %ibus_ver librest-devel
BuildRequires: libaccountsservice-devel libgnome-desktop3-devel
BuildRequires: gstreamer%gst_api_ver-devel libclutter-gst3.0-devel
BuildRequires: libgweather-devel libgnome-online-accounts-devel
BuildRequires: gdm-libs-devel iso-codes-devel libpolkit-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libsecret-devel >= %secret_ver
BuildRequires: libgeoclue2-devel >= %geoclue_ver libgeocode-glib-devel
BuildRequires: libwebkit2gtk-devel
%{?_enable_cheese:BuildRequires: libcheese-devel >= %cheese_ver}
%{?_enable_software_sources:BuildRequires: pkgconfig(packagekit-glib2) >= %packagekit_ver}
%{?_enable_malcontent:BuildRequires: pkgconfig(malcontent-ui-0) >= %malcontent_ver}

%description
GNOME Initial Setup is an alternative to firstboot, providing
a good setup experience to welcome you to your system, and walks
you through configuring it. It is integrated with gdm.

%prep
%setup -n %name-%version%beta

%build
%meson \
	%{?_enable_software_sources:-Dsoftware-sources=enabled} \
	%{?_disable_systemd:-Dsystemd=false} \
	%{?_disable malcontent:-Dparental_controls=false}
%nil
%meson_build

%install
%meson_install

mkdir -p %buildroot%_localstatedir/lib/%name
mkdir -p %buildroot%_localstatedir/run/%name

%find_lang %name

%pre
useradd -rM -d %_localstatedir/lib/%name -s /sbin/nologin %name &>/dev/null || :

%files -f %name.lang
%_libexecdir/%name
%_libexecdir/%name-copy-worker
#%_libexecdir/gnome-welcome-tour
#%_sysconfdir/xdg/autostart/gnome-welcome-tour.desktop
%_sysconfdir/xdg/autostart/%name-copy-worker.desktop
%_sysconfdir/xdg/autostart/%name-first-login.desktop
#%_datadir/gdm/greeter/applications/%name.desktop
%_desktopdir/%name.desktop
%_datadir/gnome-session/sessions/%name.session
%_datadir/gnome-shell/modes/initial-setup.json
%_datadir/polkit-1/rules.d/20-gnome-initial-setup.rules
%_userunitdir/*
%attr(1770, %name, %name) %dir %_localstatedir/lib/%name
%attr(1777, root, %name) %dir %_localstatedir/run/%name
%doc README* NEWS

%changelog
* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 41.4-alt1
- 41.4

* Thu Dec 02 2021 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Fri Sep 17 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Sat Aug 14 2021 Yuri N. Sedunov <aris@altlinux.org> 40.4-alt1
- 40.4

* Tue Jul 13 2021 Yuri N. Sedunov <aris@altlinux.org> 40.3-alt1
- 40.3

* Thu Jun 03 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Thu Apr 29 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Mon Feb 15 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.4-alt1
- 3.38.4

* Fri Jan 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Sat Nov 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Fri Oct 02 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Thu Sep 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sun Jul 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Sun May 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Sun Apr 26 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Sat Mar 28 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Fri Mar 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Sun Jan 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Sun Oct 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Fri Apr 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Sep 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Aug 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.29.92-alt1
- 3.29.92

* Wed Jun 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt2
- fixed buildreqs

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Sep 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.92-alt1
- 3.21.92

* Tue Apr 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Feb 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Fri Nov 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2.1-alt1
- 3.14.2.1

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Fri Oct 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1.1-alt1
- 3.10.1.1

* Thu Sep 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Jul 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt1
- 0.10

* Wed Apr 17 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.8-alt1
- 0.8

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- first build for people/gnome

