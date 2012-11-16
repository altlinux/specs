# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize gcc-c++ libICE-devel libSM-devel pkgconfig(dbus-1) pkgconfig(fontconfig) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gstreamer-0.10) pkgconfig(gstreamer-plugins-base-0.10) pkgconfig(gthread-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libmatekbdui) pkgconfig(libpulse) pkgconfig(libpulse-mainloop-glib) pkgconfig(polkit-gobject-1)
# END SourceDeps(oneline)
Group: System/Servers
BuildRequires: libXext-devel
%define _libexecdir %_prefix/libexec

Name:           mate-settings-daemon
Version:        1.5.3
Release:        alt1_1
Summary:        MATE Desktop settings daemon
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(clutter-gst-1.0)
BuildRequires:  icon-naming-utils
BuildRequires:  mate-common
BuildRequires:  pkgconfig(MateCORBA-2.0)
BuildRequires:  pkgconfig(mate-desktop-2.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(libmatekbd)
BuildRequires:  pkgconfig(libmatenotify)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gtk-mate-1)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)

Requires: gsettings-desktop-schemas
Requires: mate-icon-theme
Source44: import.info
Patch33: mate-settings-daemon-keyboard-icon.patch

%description
MATE Desktop settings daemon

%package devel
Group: Development/C
Summary:        Development files for mate-settings-daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for mate-panel

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1


%build
%configure --disable-static \
           --enable-polkit \
           --enable-profiling \
           --with-x \
           --with-nssdb
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.a" -exec rm -f {} ';'

%find_lang %{name}



%files -f %{name}.lang
%doc AUTHORS COPYING README
%config %{_sysconfdir}/dbus-1/system.d/org.mate.SettingsDaemon.DateTimeMechanism.conf
%config %{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%{_libdir}/mate-settings-daemon-1.5.3/
%{_libexecdir}/mate-settings-daemon
%{_libexecdir}/msd-datetime-mechanism
%{_libexecdir}/msd-locate-pointer
%{_datadir}/dbus-1/services/org.mate.SettingsDaemon.service
%{_datadir}/dbus-1/system-services/org.mate.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/icons/mate/*/*/*
%{_datadir}/mate-settings-daemon/
%{_datadir}/glib-2.0/schemas/org.mate.*.xml
%{_datadir}/polkit-1/actions/org.mate.settingsdaemon.datetimemechanism.policy

%files devel
%{_includedir}/mate-settings-daemon/
%{_libdir}/pkgconfig/mate-settings-daemon.pc


%changelog
* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_1
- use F19 import base

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

