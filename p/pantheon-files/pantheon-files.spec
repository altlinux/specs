%def_disable snapshot
%def_enable check

%define _libexecdir %_prefix/libexec

%define ver_major 7.0
%define _name files
%define xdg_name org.pantheon.%_name
%define rdn_name io.elementary.%_name

Name: pantheon-files
Version: %ver_major.0
Release: alt1

Summary: The file manager of the Pantheon desktop
License: GPL-3.0
Group: File tools
Url: https://github.com/elementary/%_name

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/elementary/files.git
Source: %_name-%version.tar
%endif

Provides: %rdn_name = %EVR

#Depends: tumbler
#Recommends: contractor
#Suggests: tumbler-plugins-extra
Requires: polkit zeitgeist tumbler elementary-icon-theme

%define vala_ver 0.48.2
%define glib_ver 2.64.6
%define gtk_ver 3.22.25
%define granite_ver 6.1.0

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson vala-tools > %vala_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libappstream-glib-devel desktop-file-utils
BuildRequires: libsqlite3-devel libgtk+3-devel >= %gtk_ver
BuildRequires: libgee0.8-devel libgranite-devel
BuildRequires: libdbus-glib-devel libnotify-devel
BuildRequires: libxkbcommon-devel libgranite-vala >= %granite_ver
BuildRequires: libzeitgeist2.0-devel libplank-devel libplank-vala
BuildRequires: libpolkit-devel
BuildRequires: libcanberra-devel libcanberra-vala
BuildRequires: libcloudproviders-devel
BuildRequires: libgit2-glib-devel
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk3)
%{?_enable_check:BuildRequires: elementary-icon-theme}

%description
The simple, powerful, and sexy file manager from elementary.

%package devel
Summary: Development files for pantheon-files
Group: Development/C
Requires: %name = %EVR

%description devel
Development files for pantheon-files.

%package vala
Summary: Vala language bindings for the pantheon-files
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %EVR

%description vala
This package provides Vala language bindings for the pantheon-files.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%check
%__meson_test

%files -f %rdn_name.lang
%doc AUTHORS README*
%_bindir/*
%_libdir/*.so.*
%_libdir/%rdn_name/
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/dbus-1/services/%rdn_name.Filemanager1.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/polkit-1/actions/%rdn_name.policy
%_datadir/metainfo/%rdn_name.metainfo.xml

%_libexecdir/%rdn_name.xdg-desktop-portal
%_prefix/lib/systemd/user/%rdn_name.xdg-desktop-portal.service
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.elementary.files.service
%_datadir/xdg-desktop-portal/portals/%rdn_name.portal

%files devel
%_includedir/%name-core/
%_libdir/*.so
%_pkgconfigdir/%name-core.pc

%if 0
%files vala
%_vapidir/%name-core.vapi
%endif

%changelog
* Sun Aug 04 2024 Yuri N. Sedunov <aris@altlinux.org> 7.0.0-alt1
- 7.0.0

* Mon Dec 18 2023 Yuri N. Sedunov <aris@altlinux.org> 6.5.3-alt1
- updated to 6.5.3-7-g56202aa10

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 6.5.2-alt1
- updated to 6.5.2-5-gbda7d69d2

* Mon Sep 25 2023 Yuri N. Sedunov <aris@altlinux.org> 6.5.1-alt1
- 6.5.1

* Fri Aug 25 2023 Yuri N. Sedunov <aris@altlinux.org> 6.5.0-alt1
- updated to 6.5.0-19-gd3e70e095

* Tue Jul 05 2022 Yuri N. Sedunov <aris@altlinux.org> 6.1.4-alt1
- updated to 6.1.4-9-gac6487cb1

* Mon Jun 20 2022 Yuri N. Sedunov <aris@altlinux.org> 6.1.3-alt1
- updated to 6.1.3-5-g660492c9d

* Wed Jan 26 2022 Yuri N. Sedunov <aris@altlinux.org> 6.1.2-alt1
- updated to 6.1.2-6-g9f7866d32

* Sat Dec 11 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.1-alt1
- updated to 6.1.1-22-g5207a47cd

* Thu Dec 02 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.0-alt1
- updated to 6.1.0-37-g1e03757fb

* Mon Nov 01 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.4-alt1
- updated to 6.0.4-5-g4f6823d72

* Thu Sep 30 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.3-alt1
- updated to 6.0.3-5-g8260a5b83

* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.2-alt1
- updated to 6.0.2-36-g6d824249f

* Wed Aug 04 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt1
- updated to 6.0.1-1-g2cdf65659

* Mon Jul 19 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1
- updated to 6.0.0-14-g01589044d

* Thu May 27 2021 Yuri N. Sedunov <aris@altlinux.org> 4.5.0-alt3
- updated to 4.5.0-425-g447d98bfc
- updated BR

* Fri Dec 04 2020 Yuri N. Sedunov <aris@altlinux.org> 4.5.0-alt1
- updated to 4.5.0-133-g96fe89cfd

* Sun Jul 05 2020 Yuri N. Sedunov <aris@altlinux.org> 4.4.4-alt1
- 4.4.4

* Tue Jun 02 2020 Yuri N. Sedunov <aris@altlinux.org> 4.4.3-alt1
- 4.4.3

* Sun Apr 05 2020 Yuri N. Sedunov <aris@altlinux.org> 4.4.2-alt1
- 4.4.2

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 4.4.1-alt1
- updated to 4.4.1-29-g25cfc857

* Sat Jan 11 2020 Yuri N. Sedunov <aris@altlinux.org> 4.3.0-alt1
- updated to 4.3.0-3-gac90956e

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Fri Aug 09 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.9-alt1
- 4.1.9

* Sun May 12 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.8-alt1
- 4.1.8

* Thu Apr 25 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.7-alt1
- updated to 4.1.7-7-g732d80c3

* Wed Apr 03 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.6-alt1
- updated to 4.1.6-11-g7629b75d

* Fri Feb 15 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.5-alt1
- 4.1.5

* Fri Jan 25 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.3-alt1
- updated to 4.1.3-30-gedee9887

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 4.1.2-alt1
- updated to 4.1.2-4-g08e2084f

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt3
- updated to d5c2444 (no tags in git)
- built against libgranite.so.5

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt2
- rebuilt against libgranite.so.4

* Sun Jun 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- 0.3.5

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Tue Apr 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Sat Mar 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.1.1-alt1
- 0.3.1.1

* Sat Jan 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Sun Jan 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.0.5-alt1
- 0.3.0.5

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.0.3.1-alt1
- 0.3.0.3.1

* Thu Sep 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.0.2-alt1
- 0.3.0.2

* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5.1-alt1
- 0.1.5.1

* Mon Nov 11 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt2
- Make build more verbose

* Sat Oct 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt1
- 0.1.4 -> 0.1.5

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt2
- Fix pkgconfig file

* Mon Sep 09 2013 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt1
- 0.1.3 -> 0.1.4

* Sat Aug 24 2013 Igor Zubkov <icesik@altlinux.org> 0.1.3-alt1
- build for Sisyphus

