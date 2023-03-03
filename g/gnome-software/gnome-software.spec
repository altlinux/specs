%def_disable snapshot

%define ver_major 43
%define beta %nil
%define plugins_ver 19
%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.Software

%def_disable soup2
%def_enable gudev
%def_enable gnome_desktop
%def_enable polkit
%ifarch armh mipsel %e2k
%def_disable fwupd
%else
%def_enable fwupd
%endif
%def_enable flatpak
%def_disable limba
%def_enable packagekit
%def_enable webapps
%def_enable odrs
# dropped since 3.27.90
%def_disable rpm
%def_disable rpm_ostree
%def_disable external_appstream
%def_enable malcontent
%ifarch %e2k
%def_disable sysprof
%else
%def_enable sysprof
%endif
%def_enable tests
%def_disable check

Name: gnome-software
Version: %ver_major.5
Release: alt1%beta

Summary: Software manager for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Software

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

%define glib_ver 2.66
%define gtk4_ver 4.0.0
%define appstream_ver 0.14
%define json_glib_ver 1.1.1
%define soup_ver 2.52
%define soup3_ver 3.0
%define packagekit_ver 1.1.9
%define gsds_ver 3.18
%define fwupd_ver 1.0.3
%define flatpak_ver 0.99.3
%define ostree_ver 2018.4
%define xmlb_ver 0.1.4
%define adwaita_ver 1.0.1
%define malcontent_ver 0.11

%{?_enable_fwupd:Requires: fwupd >= %fwupd_ver}
%{?_enable_packagekit:Requires: appstream-data gnome-packagekit}
%{?_enable_malcontent:Requires: malcontent} >= %malcontent_ver

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
BuildRequires: meson libgio-devel >= %glib_ver
BuildRequires: libgtk4-devel >= %gtk4_ver pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(appstream) >= %appstream_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver
%if_enabled soup2
BuildRequires: libsoup-devel >= %soup_ver
%else
BuildRequires: libsoup3.0-devel >= %soup3_ver
%endif
BuildRequires: yelp-tools gtk-doc xsltproc docbook-style-xsl desktop-file-utils
BuildRequires: libsqlite3-devel libsecret-devel gsettings-desktop-schemas-devel liboauth-devel
BuildRequires: libgnome-online-accounts-devel
BuildRequires: libxmlb-devel >= %xmlb_ver
BuildRequires: libglib-testing-devel
%{?_enable sysprof:BuildRequires: pkgconfig(sysprof-capture-4)}
%{?_enable_gudev:BuildRequires: libgudev-devel}
%{?_enable_gnome_desktop:BuildRequires: gsettings-desktop-schemas >= %gsds_ver}
%{?_enable_polkit:BuildRequires: libpolkit-devel}
%{?_enable_fwupd:BuildRequires: fwupd-devel >= %fwupd_ver}
%{?_enable_flatpak:BuildRequires: libflatpak-devel >= %flatpak_ver}
%{?_enable_packagekit:BuildRequires: libpackagekit-glib-devel >= %packagekit_ver}
%{?_enable_rpm_ostree:BuildRequires: libostree-devel >= %ostree_ver}
%{?_enable_rpm:BuildRequires: librpm-devel}
%{?_enable_malcontent:BuildRequires: pkgconfig(malcontent-0) >= %malcontent_ver}
%{?_enable_check:BuildRequires: gcab}

%description
GNOME Software is a software center for GNOME.

%package devel
Summary: Development files for GNOME Software
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains files necessary to develop plugins for GNOME
Software.

%package devel-doc
Summary: Development documentation for GNOME Software
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains documentation necessary to develop plugins for
GNOME Software.


%prep
%setup -n %name-%version%beta

%build
%meson \
	%{?_enable_soup2:-Dsoup2=true} \
	%{?_enable_gudev:-Dgudev=true} \
	%{?_disable_gnome_desktop:-Dgsettings_desktop_schemas=disabled} \
	%{?_enable_polkit:-Dpolkit=true} \
	%{?_disable_fwupd:-Dfwupd=false} \
	%{?_enable_flatpak:-Dflatpak=true} \
	%{?_enable_ostree:-Dostree=true} \
	%{?_enable_rpm_ostree:-Drpm_ostree=true} \
	%{?_disable_packagekit:-Dpackagekit=false} \
	%{?_disable_tests:-Dtests=false} \
	%{?_disable_external_appstream:-Dexternal_appstream=false} \
	%{?_disable_sysprof:-Dsysprof=disabled} \
	%{?_disable_malcontent:-Dmalcontent=false}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

ln -sf %name/libgnomesoftware.so.%plugins_ver \
%buildroot%_libdir/libgnomesoftware.so.%plugins_ver

%check
%__meson_test

%files -f %name.lang
%_xdgconfigdir/autostart/%xdg_name.desktop
%_bindir/%name
%_libexecdir/%name-cmd
%_libexecdir/%name-restarter
%{?_enable_external_appstream:%_libexecdir/%name-install-appstream}
%dir %_libdir/%name
%_libdir/%name/libgnomesoftware.so*
#symlink
%_libdir/libgnomesoftware.so.%plugins_ver
%_libdir/%name/plugins-%plugins_ver/
%_desktopdir/%xdg_name.desktop
%_desktopdir/%name-local-file-flatpak.desktop
%{?_enable_fwupd:%_desktopdir/%name-local-file-fwupd.desktop}
%_desktopdir/%name-local-file-packagekit.desktop
%_datadir/swcatalog/xml/%xdg_name.Featured.xml
%_datadir/swcatalog/xml/gnome-pwa-list-foss.xml
%_datadir/swcatalog/xml/gnome-pwa-list-proprietary.xml
%_datadir/swcatalog/xml/%xdg_name.Curated.xml
%_datadir/dbus-1/services/%xdg_name.service
%{?_enable_packagekit:%_datadir/dbus-1/services/org.freedesktop.PackageKit.service}
%{?_enable_external_appstream:%_datadir/polkit-1/actions/org.gnome.software.external-appstream.policy}
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
%_iconsdir/hicolor/*/*/*.svg
%_datadir/glib-2.0/schemas/org.gnome.software.gschema.xml
%_datadir/metainfo/%xdg_name.metainfo.xml
%_datadir/metainfo/%xdg_name.Plugin.Epiphany.metainfo.xml
%{?_enable_flatpak:%_datadir/metainfo/%xdg_name.Plugin.Flatpak.metainfo.xml}
%{?_enable_fwupd:%_datadir/metainfo/%xdg_name.Plugin.Fwupd.metainfo.xml}
%_man1dir/%name.1.*
%doc AUTHORS README* NEWS

%files devel
%_includedir/%name/
%_pkgconfigdir/%name.pc

%files devel-doc
%_datadir/gtk-doc/html/%name/

%changelog
* Fri Mar 03 2023 Yuri N. Sedunov <aris@altlinux.org> 43.5-alt1
- 43.5

* Fri Feb 10 2023 Yuri N. Sedunov <aris@altlinux.org> 43.4-alt1
- 43.4

* Sun Jan 08 2023 Yuri N. Sedunov <aris@altlinux.org> 43.3-alt1
- 43.3

* Sat Dec 03 2022 Yuri N. Sedunov <aris@altlinux.org> 43.2-alt1
- 43.2

* Thu Dec 01 2022 Ivan A. Melnikov <iv@altlinux.org> 43.1-alt2
- Drop valgrind option and dependency, just like
  upstream did (see upstream commit 788e37f0).

* Fri Oct 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Fri Aug 05 2022 Yuri N. Sedunov <aris@altlinux.org> 42.4-alt1
- 42.4

* Thu Jun 30 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Mon May 30 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Wed Apr 27 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 41.5-alt1
- 41.5

* Mon Feb 28 2022 Yuri N. Sedunov <aris@altlinux.org> 41.4-alt1
- 41.4

* Fri Jan 07 2022 Yuri N. Sedunov <aris@altlinux.org> 41.3-alt1
- 41.3

* Fri Dec 03 2021 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Thu Oct 28 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Tue Sep 07 2021 Yuri N. Sedunov <aris@altlinux.org> 41-alt1.rc
- 41

* Fri Aug 13 2021 Yuri N. Sedunov <aris@altlinux.org> 40.4-alt1
- 40.4

* Sat Jul 10 2021 Yuri N. Sedunov <aris@altlinux.org> 40.3-alt1
- 40.3

* Fri Jun 04 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Sat May 01 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0 (ported to upstream instead of libappstream-glib)

* Thu Mar 11 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Mon Feb 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sun Jan 10 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1.1
- e2k: disabled fwupd and sysprof

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Wed Sep 02 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt2
- updated to 3.36.1-9-gf044085f
- disabled fwupd support on armh only

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0
- disabled shell extensions plugin

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Thu Jul 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.4-alt1
- 3.32.4

* Thu Jul 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.3-alt2
- local-file.desktop.in: removed unsupported mime types (ALT #37014)

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.3-alt1
- 3.32.3

* Tue May 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Tue Apr 16 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt2
- updated to 3.32.0-19-g6740a695

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Dec 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.6-alt2
- enabled PackageKit support (ALT #35817)

* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.6-alt1
- 3.30.6

* Wed Oct 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.5-alt1
- 3.30.5

* Thu Oct 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Fri Jun 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt2
- enabled fwupd support

* Wed May 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Fri Mar 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.7-alt1
- 3.26.7

* Thu Feb 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.6-alt1
- 3.26.6

* Tue Jan 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.5-alt1
- 3.26.5

* Tue Dec 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.4-alt1
- 3.26.4

* Tue Nov 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Thu Nov 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt2
- new -devel, -devel-doc subpackages

* Mon May 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt0.2
- 3.24.1

* Sun Mar 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt0.2
- 3.24.0

* Sat Mar 18 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.7-alt0.2
- 3.22.7
- enabled ostree/flatpak support

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.6-alt0.1
- 3.22.6

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt0.1
- 3.22.5

* Fri Dec 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt0.1
- first preview for Sisyphus


