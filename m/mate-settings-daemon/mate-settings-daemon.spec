Group: System/Servers
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize gcc-c++ libICE-devel libSM-devel libgio-devel pkgconfig(dbus-1) pkgconfig(fontconfig) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(libcanberra-gtk) pkgconfig(libmatekbdui) pkgconfig(libpulse) pkgconfig(libpulse-mainloop-glib) pkgconfig(polkit-gobject-1)
# END SourceDeps(oneline)
BuildRequires: libXext-devel
%define _libexecdir %_prefix/libexec
Name:           mate-settings-daemon
Version:        1.5.4
Release:        alt1_3
Summary:        MATE Desktop settings daemon
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
Requires:       gsettings-desktop-schemas
Requires:       mate-icon-theme

BuildRequires:  icon-naming-utils
BuildRequires:  mate-common
BuildRequires:  pkgconfig(clutter-gst-1.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:  pkgconfig(libmatekbd)
BuildRequires:  pkgconfig(libmatenotify)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(mate-desktop-2.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gtk-mate-1)
BuildRequires:  pkgconfig(sm)
Source44: import.info
Patch33: mate-settings-daemon-keyboard-icon.patch
Requires: dconf

%description
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%package devel
Group: Development/C
Summary:        Development files for mate-settings-daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the daemon which is responsible for setting the
various parameters of a MATE session and the applications that run
under it.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1


%build
%configure                             \
   --disable-pulse                     \
   --disable-static                    \
   --disable-schemas-compile           \
   --enable-polkit                     \
   --enable-gstreamer                  \
   --with-x                            \
   --with-gnu-ld                       \
   --with-nssdb
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%config %{_sysconfdir}/dbus-1/system.d/org.mate.SettingsDaemon.DateTimeMechanism.conf
%config %{_sysconfdir}/xdg/autostart/mate-settings-daemon.desktop
%{_libdir}/mate-settings-daemon
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
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_3
- new fc release

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_2
- new fc release

* Tue Dec 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_1
- new fc release

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_5
- new fc release

* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_4
- added dconf dependency (closes: 28110)

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

