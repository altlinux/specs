Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/docbook2man /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/xmlto libgio-devel pkgconfig(dbus-1) pkgconfig(gdk-2.0) pkgconfig(gdk-3.0) pkgconfig(gdk-x11-2.0) pkgconfig(gdk-x11-3.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libcanberra-gtk) pkgconfig(libcanberra-gtk3) pkgconfig(unique-3.0) pkgconfig(x11) pkgconfig(xext) pkgconfig(xproto) pkgconfig(xrandr) pkgconfig(xrender)
# END SourceDeps(oneline)
%filter_from_requires /^hal$/d
%define _libexecdir %_prefix/libexec
%define fedora 20
#%%global _internal_version  bc54d96

Name:          mate-power-manager
Version:       1.8.0
#Release:       0.4.git%%{_internal_version}%{?dist}
Release:       alt1_1
Summary:       MATE power management service
License:       GPLv2+
URL:           http://pub.mate-desktop.org

# To generate tarball
# wget http://git.mate-desktop.org/%%{name}/snapshot/%%{name}-{_internal_version}.tar.xz -O %%{name}-%%{version}.git%%{_internal_version}.tar.xz
#Source0: http://raveit65.fedorapeople.org/Mate/git-upstream/%%{name}-%%{version}.git%%{_internal_version}.tar.xz

Source0:       http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz

# upstream patch
# https://github.com/mate-desktop/mate-power-manager/pull/60
# Add DBUS interface to kbdbacklight control
Patch0:        mate-power-manager_dbus_interface_keyboard_backlight_controls.patch

# first work to support upower-1.0
#https://github.com/NiceandGently/mate-power-manager/commits/dev-upower
%if 0%{?fedora} > 20
Patch3:        mate-power-manager_upower.patch
Patch4:        mate-power-manager_upower-remove-recall.patch
Patch5:        mate-power-manager_upower-use-g_signal-notify.patch
Patch6:        mate-power-manager_upower-update-for-libupower-glib-API-changes.patch
Patch7:        mate-power-manager_fix-use-g_signal-notify.patch
%endif


BuildRequires: libcairo-devel
BuildRequires: libdbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: libcanberra-devel
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libnotify-devel
BuildRequires: mate-common
BuildRequires: mate-control-center-devel
BuildRequires: mate-panel-devel
BuildRequires: libGL-devel
BuildRequires: libpangox-compat-devel
BuildRequires: popt-devel
BuildRequires: libunique-devel
BuildRequires: libupower-devel
BuildRequires: xmlto
Source44: import.info
Patch33: 0001-Treat-challenge-as-yes-when-suspend-ability-determen.patch


%description
MATE Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive MATE session.


%prep
%setup -q
#%%setup -q -n %{name}-%{_internal_version}

%patch0 -p1 -b .dbus
%if 0%{?fedora} > 20
%patch3 -p1 -b .upower
%patch4 -p1 -b .remove-recall
%patch5 -p1 -b .use-g_signal-notify
%patch6 -p1 -b .glib-API-changes
%patch7 -p1 -b .fix-use-g_signal-notify
%endif

# nedded to create configure and make files for dbus patch
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1

%build
%configure --disable-static --enable-applets \
     --enable-docbook-docs \
     --enable-unique \
     --with-gtk=2.0 \
     --disable-schemas-compile

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

desktop-file-install                               \
     --delete-original                             \
     --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/*.desktop

# remove needless gsettings convert file
rm -f  %{buildroot}%{_datadir}/MateConf/gsettings/mate-power-manager.convert

%find_lang %{name} --with-gnome --all-name


%files  -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/mate-power-*.*
%{_bindir}/mate-power-bugreport.sh
%{_bindir}/mate-power-manager
%{_bindir}/mate-power-preferences
%{_bindir}/mate-power-statistics
%{_sbindir}/mate-power-backlight-helper
%{_datadir}/applications/mate-*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mate-power-manager/
%{_datadir}/icons/hicolor/*/apps/mate-*.*
%{_datadir}/polkit-1/actions/org.mate.power.policy
%{_datadir}/mate-2.0/ui/brightness-applet-menu.xml
%{_datadir}/mate-2.0/ui/inhibit-applet-menu.xml
%{_datadir}/mate-panel/applets/org.mate.BrightnessApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.InhibitApplet.mate-panel-applet
%{_datadir}/glib-2.0/schemas/org.mate.power-manager.gschema.xml
%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet


%changelog
* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_3
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_2
- new fc release

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1
- new fc release

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt3_2
- new fc release

* Thu Apr 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt3_1
- new fc release

* Tue Apr 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt3
- crash fixed

* Mon Apr 08 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt2
- added suspend/hybernate via logind
- enabled systemdinhibit

* Thu Apr 04 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.0-alt1
- new version
- drop upstreamed patches
- disable systemdinhibit

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_6
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_4
- new fc release

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- get rid of hal dependency

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

