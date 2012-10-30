# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/mateconftool-2 gcc-c++ libICE-devel libSM-devel pkgconfig(dbus-1) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gstreamer-0.10) pkgconfig(gstreamer-plugins-base-0.10) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libxklavier) pkgconfig(nss) pkgconfig(polkit-gobject-1)
# END SourceDeps(oneline)
BuildRequires: libXext-devel
%define _libexecdir %_prefix/libexec
BuildRequires(pre): rpm-macros-mate-conf
Name:           mate-settings-daemon
Version:        1.4.0
Release:        alt3_1.1
Summary:        The daemon sharing settings from MATE to GTK+/KDE applications

Group:          System/Servers
License:        GPLv2+
URL:            http://pub.mate-desktop.org
Source:         http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

Requires(pre): 	mate-conf >= 1.1.0
Requires(preun): mate-conf >= 1.1.0
Requires(post): mate-conf >= 1.1.0
#Requires: 		mate-control-center-filesystem

BuildRequires:  libdbus-glib-devel
BuildRequires:  mate-conf-devel
BuildRequires:  gtk2-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  libglade2-devel
BuildRequires:  libmateui-devel
BuildRequires:  libmate-devel
BuildRequires:  xorg-x11-proto-devel
#BuildRequires:  gstreamer-devel
#BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  libpulseaudio-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  libmatenotify-devel
BuildRequires:  gettext intltool
BuildRequires:  fontconfig-devel
BuildRequires:  libcanberra-devel
BuildRequires:  mate-polkit-devel
BuildRequires:  mate-common
BuildRequires:  nss-devel

# change font rendering
Patch3: slight-hinting.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=610319
Patch4: keyboard-icon.patch

Patch6: mate-settings-daemon_remove_mate-bg-crossfade.patch
Patch33: gnome-settings-daemon-2.30.0-enable_font_plugin.patch

%description
A daemon to share settings from MATE to other applications. It also
handles global keybindings, as well as a number of desktop-wide settings.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch3 -p1 -b .slight-hinting
%patch4 -p1 -b .keyboard-icon
%patch6 -p1 -b .mate-settings-demeon_mate-bg-crossfade

NOCONFIGURE=1 ./autogen.sh
%patch33 -p0

%build

%configure \
    --disable-static \
	--with-nssdb \
	--enable-polkit \
	--enable-profiling \
	--enable-pulse \
	--disable-gstreamer

make %{?_smp_mflags}


%install

make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

%post
%mateconf_schema_upgrade apps_mate_settings_daemon_housekeeping apps_mate_settings_daemon_keybindings apps_mate_settings_daemon_xrandr desktop_mate_font_rendering desktop_mate_keybindings desktop_mate_peripherals_smartcard desktop_mate_peripherals_touchpad mate-settings-daemon

touch --no-create %{_datadir}/icons/mate >&/dev/null || :

%pre
%mateconf_schema_prepare apps_mate_settings_daemon_housekeeping apps_mate_settings_daemon_keybindings apps_mate_settings_daemon_xrandr desktop_mate_font_rendering desktop_mate_keybindings desktop_mate_peripherals_smartcard desktop_mate_peripherals_touchpad mate-settings-daemon

%preun
%mateconf_schema_remove apps_mate_settings_daemon_housekeeping apps_mate_settings_daemon_keybindings apps_mate_settings_daemon_xrandr desktop_mate_font_rendering desktop_mate_keybindings desktop_mate_peripherals_smartcard desktop_mate_peripherals_touchpad mate-settings-daemon

%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/mate >&/dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS
%{_sysconfdir}/mateconf/schemas/*
%dir %{_sysconfdir}/mate-settings-daemon
%dir %{_sysconfdir}/mate-settings-daemon/xrandr
%{_libdir}/mate-settings-daemon-%{version}
%{_libexecdir}/mate-settings-daemon
%{_libexecdir}/msd-locate-pointer
%{_libexecdir}/msd-datetime-mechanism
%{_datadir}/mate-settings-daemon/
%{_datadir}/mate-control-center/keybindings/50-accessibility.xml
%{_datadir}/dbus-1/services/org.mate.SettingsDaemon.service
%{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%{_datadir}/icons/mate/*/apps/*
%{_datadir}/icons/mate/*/actions/*
%{_sysconfdir}/dbus-1/system.d/org.mate.SettingsDaemon.DateTimeMechanism.conf
%{_datadir}/dbus-1/system-services/org.mate.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/polkit-1/actions/org.mate.settingsdaemon.datetimemechanism.policy

%files devel
%{_libdir}/pkgconfig/mate-settings-daemon.pc
%{_includedir}/mate-settings-daemon/*.h


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt3_1.1
- Build for Sisyphus
- dep on mate-control-center-filesystem temporary disabled

* Tue Oct 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_1
- adapted alt patches

* Sun Oct 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- fixed localstatedir in macros

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

