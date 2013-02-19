# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/docbook2man /usr/bin/glib-gettextize /usr/bin/gtkdocize gcc-c++ libcups-devel libexif-devel libgio-devel libsane-devel pkgconfig(exiv2) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(lcms) pkgconfig(libcanberra-gtk) pkgconfig(libexif) pkgconfig(sane-backends) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary:   Color management tools for MATE
Name:      mate-color-manager
Version:   1.5.0
Release:   alt1_0
License:   GPLv2+
Group:     File tools
URL:       https://github.com/NiceandGently/mate-color-manager
Source0:   https://github.com/downloads/NiceandGently/mate-color-manager/%{name}-%{version}.tar.xz

Requires:  color-filesystem rpm-macros-color >= 1-7
Requires:  mate-icon-theme
Requires:  shared-mime-info
Requires:  shared-color-profiles
Requires:  yelp
Requires:  mate-conf

BuildRequires: gtk2-devel >= 2.16.0
BuildRequires: scrollkeeper
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: libvte-devel
BuildRequires: mate-doc-utils
BuildRequires: libunique-devel >= 1.0.0
BuildRequires: intltool
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
BuildRequires: gtk-doc
BuildRequires: libmatenotify-devel
Source44: import.info

%description
mate-color-manager is a session framework that makes it easy to manage, install
and generate color profiles in the MATE desktop.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-scrollkeeper --disable-schemas-install
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

for i in mcm-prefs mcm-import ; do
  desktop-file-install --delete-original                                \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications/                      \
    $RPM_BUILD_ROOT%{_datadir}/applications/$i.desktop
done

mkdir -p %buildroot%{_var}/lib/color

%find_lang %name --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
/lib/udev/rules.d/*.rules
%{_bindir}/mcm-*
%dir %{_datadir}/mate-color-manager
%{_datadir}/mate-color-manager/mcm-*.ui
%dir %{_datadir}/mate-color-manager/targets
%dir %{_datadir}/mate-color-manager/icons
%{_datadir}/mate-color-manager/targets/*.png
%{_datadir}/mate-color-manager/icons/*.svg
%{_datadir}/man/man1/*.1.*
%{_datadir}/mate/help/mate-color-manager
%{_datadir}/omf/mate-color-manager
%{_datadir}/icons/mate/*/*/*.png
%{_datadir}/icons/mate/scalable/*/*.svg*
%{_datadir}/applications/mcm-prefs.desktop
%{_datadir}/applications/mcm-import.desktop
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/dbus-1/services/org.mate.ColorManager.service
%{_sbindir}/mcm-install-system-wide
%{_datadir}/polkit-1/actions/org.mate.color.policy
/usr/libexec/mcm-helper-exiv
%{_datadir}/MateConf/gsettings/org.mate.color-manager.gschema.migrate
%{_datadir}/applications/mcm-picker.desktop
%{_datadir}/dbus-1/interfaces/org.mate.ColorManager.xml
%{_datadir}/glib-2.0/schemas/org.mate.color-manager.gschema.xml


# this is probably better in a shared package
%dir %{_var}/lib/color

%changelog
* Tue Feb 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- updated to 1.5

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3
- added mate-desktop-1.5.0-alt-settings.patch - font settings

