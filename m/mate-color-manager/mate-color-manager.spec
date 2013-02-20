# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/docbook2man /usr/bin/glib-gettextize /usr/bin/gtkdocize gcc-c++ libcups-devel libgio-devel libsane-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(lcms) pkgconfig(libcanberra-gtk) pkgconfig(sane-backends) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary:   Color management tools for MATE
Name:      mate-color-manager
Version:   1.5.3
Release:   alt1_0101
License:   GPLv2+
Group:     File tools
URL:       https://github.com/NiceandGently/mate-color-manager
Source0:   https://github.com/NiceandGently/mate-color-manager/archive/%{name}-%{version}.tar.gz

Requires: color-filesystem rpm-macros-color
Requires:  mate-icon-theme
Requires:  shared-mime-info
Requires:  shared-color-profiles
Requires:  yelp
Requires:  dconf

BuildRequires: gtk2-devel >= 2.16.0
BuildRequires: librarian
BuildRequires: desktop-file-utils
BuildRequires: libvte-devel
BuildRequires: mate-doc-utils
BuildRequires: libunique-devel >= 1.0.0
BuildRequires: libgudev-devel
BuildRequires: libdbus-glib-devel >= 0.73
BuildRequires: libXxf86vm-devel
BuildRequires: libXrandr-devel
BuildRequires: mate-desktop-devel
BuildRequires: lcms-devel
BuildRequires: cups-devel
BuildRequires: sane-devel
BuildRequires: libtiffxx-devel libtiff-devel
BuildRequires: libcanberra-devel
BuildRequires: mate-common
BuildRequires: libmatenotify-devel
BuildRequires: libexiv2-devel
BuildRequires: libexif-devel
Source44: import.info


%description
mate-color-manager is a session framework that makes it easy to manage, install
and generate color profiles in the MATE desktop.

%prep
%setup -q

NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-scrollkeeper
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/mcm-prefs.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/mcm-import.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/mcm-picker.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/mcm-apply.desktop


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
/lib/udev/rules.d/*.rules
%{_bindir}/mcm-*
%dir %{_datadir}/mate-color-manager/
%{_datadir}/mate-color-manager/mcm-*.ui
%dir %{_datadir}/mate-color-manager/targets/
%dir %{_datadir}/mate-color-manager/icons/
%{_datadir}/mate-color-manager/targets/*.png
%{_datadir}/mate-color-manager/icons/*.svg
%{_datadir}/man/man1/*.1.*
%{_datadir}/mate/help/mate-color-manager/
%{_datadir}/omf/mate-color-manager/
%{_datadir}/icons/mate/*/*/*.png
%{_datadir}/icons/mate/scalable/*/*.svg*
%{_datadir}/applications/mcm-prefs.desktop
%{_datadir}/applications/mcm-import.desktop
%{_datadir}/applications/mcm-picker.desktop
%{_sysconfdir}/xdg/autostart/mcm-apply.desktop
%{_datadir}/dbus-1/services/org.mate.ColorManager.service
%{_datadir}/dbus-1/interfaces/org.mate.ColorManager.xml
%{_sbindir}/mcm-install-system-wide
%{_datadir}/polkit-1/actions/org.mate.color.policy
%{_datadir}/MateConf/gsettings/org.mate.color-manager.gschema.migrate
%{_datadir}/glib-2.0/schemas/org.mate.color-manager.gschema.xml
%{_libexecdir}/mcm-helper-exiv


%changelog
* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_0101
- new version

* Tue Feb 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0
- dropped obsolete mateconf dependencies

* Tue Feb 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- updated to 1.5

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3
- added mate-desktop-1.5.0-alt-settings.patch - font settings

