Name: deja-dup
Version: 44.1
Release: alt1

Summary: Simple backup tool and frontend for duplicity

License: GPLv3+
Group: Archiving/Other
Url: https://gitlab.gnome.org/World/deja-dup

# Source-url: https://gitlab.gnome.org/World/deja-dup/-/archive/%version/deja-dup-%version.tar.bz2
Source: %name-%version.tar

BuildRequires: meson
BuildRequires: gettext gettext-tools desktop-file-utils intltool
BuildRequires: yelp-tools libpango-devel libpango-gir-devel libcairo-devel
BuildRequires: libvala-devel >= 0.36 vala vala-tools valadoc-devel
BuildRequires: libtool glib2-devel libgio libgio-devel libnotify-devel libnotify-gir-devel
BuildRequires: libpeas-devel libpeas-gir-devel
BuildRequires: libsecret-devel libsecret-gir-devel
BuildRequires: gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel itstool
BuildRequires: libappstream-glib libappstream-glib-gir
BuildRequires: libgnome-online-accounts-devel libgnome-online-accounts-gir-devel
BuildRequires: libgpg-error-devel
BuildRequires: dbus libdbus-devel
BuildRequires: libjson-glib libjson-glib-devel libjson-glib-gir-devel libsoup-devel libsoup-gir-devel libsoup-gnome-devel libsoup-gnome-gir-devel
BuildRequires: libhandy1-devel libadwaita-devel

BuildRequires: %_bindir/desktop-file-validate

Requires: duplicity >= 0.6.23

Requires: python3-module-pygobject3 python3-module-pygobject3-pygtkcompat

# ignore dep for now
#Requires:       python3-module-PyDrive2
Requires: fuse-gvfs

%description
DA.jA. Dup is a simple backup tool. It hides the complexity of doing backups the
'right way' (encrypted, off-site, and regular) and uses duplicity as the
backend.

Features:
 a.. Support for local, remote, or consumer cloud backup locations (Google Drive, etc)
 a.. Securely encrypts and compresses your data
 a.. Incrementally backs up, letting you restore from any particular backup
 a.. Schedules regular backups
 a.. Integrates well into your GNOME desktop

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
rm -f %buildroot/%_libdir/deja-dup/*.la

desktop-file-validate %buildroot/%_desktopdir/org.gnome.DejaDup.desktop
desktop-file-validate %buildroot/%_sysconfdir/xdg/autostart/org.gnome.DejaDup.Monitor.desktop

#appstream-util validate-relax --nonet %buildroot/%_datadir/metainfo/*.appdata.xml

%find_lang %name --with-gnome

%files -f %name.lang
%doc --no-dereference LICENSES/
%doc NEWS.md README.md
%_bindir/deja-dup
%_man1dir/deja-dup.1*
%_datadir/glib-2.0/schemas/org.gnome.DejaDup.gschema.xml
%_sysconfdir/xdg/autostart/org.gnome.DejaDup.Monitor.desktop
%_libdir/deja-dup/
%_libexecdir/deja-dup/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/org.gnome.DejaDup*
%_datadir/dbus-1/services/org.gnome.DejaDup.service
%_datadir/metainfo/org.gnome.DejaDup.metainfo.xml
#_datadir/help/*

%changelog
* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 44.1-alt1
- new version 44.1 (with rpmrb script)

* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 42.8-alt2
- human build for ALT Sisyphus

* Wed Dec 29 2021 Igor Vlasenko <viy@altlinux.org> 42.8-alt1_2
- fixed build

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 42.2-alt1_1
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 42.0-alt1_1
- update to new release by fcimport

* Sat Jun 13 2020 Igor Vlasenko <viy@altlinux.ru> 41.1-alt1_1
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 40.6-alt1_2
- update to new release by fcimport

* Thu Dec 26 2019 Igor Vlasenko <viy@altlinux.ru> 40.6-alt1_1
- update to new release by fcimport

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 40.4-alt1_1
- update to new release by fcimport

* Tue Oct 29 2019 Igor Vlasenko <viy@altlinux.ru> 40.2-alt1_1
- update to new release by fcimport

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 40.1-alt1_4
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 40.1-alt1_3
- update to new release by fcimport

* Sun Apr 21 2019 Igor Vlasenko <viy@altlinux.ru> 40.1-alt1_1
- update to new release by fcimport

* Thu Apr 11 2019 Igor Vlasenko <viy@altlinux.ru> 39.1-alt1_1
- update to new release by fcimport

* Fri Mar 08 2019 Igor Vlasenko <viy@altlinux.ru> 38.4-alt1_1
- update to new release by fcimport

* Fri Jan 25 2019 Igor Vlasenko <viy@altlinux.ru> 38.1-alt1_1
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 27.3.1-alt1_2
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 27.3.1-alt1_1
- update to new release by fcimport

* Tue Dec 18 2012 Igor Vlasenko <viy@altlinux.ru> 24.0-alt1_1
- initial fc import

