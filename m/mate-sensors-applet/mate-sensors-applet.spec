# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/xsltproc libX11-devel libgio-devel libsensors3-devel pkgconfig(cairo) pkgconfig(dbus-glib-1) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libatasmart) pkgconfig(libmatepanelapplet-4.0) pkgconfig(libnotify)
# END SourceDeps(oneline)
# dlopen plugins with plugin_name ?
%set_verify_elf_method unresolved=relaxed
BuildRequires: libXext-devel
%define _libexecdir %_prefix/libexec
Name:           mate-sensors-applet
Version:        1.12.1
Release:        alt1_1
Summary:        MATE panel applet for hardware sensors
Group:          Graphical desktop/MATE
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.11/%{name}-%{version}.tar.xz

BuildRequires:  libdbus-glib-devel
BuildRequires:  libatasmart-devel
BuildRequires:  libnotify-devel
BuildRequires:  libXNVCtrl-devel   
BuildRequires:  lm_sensors3-devel
BuildRequires:  mate-common
BuildRequires:  mate-panel-devel
Source44: import.info

%description
MATE Sensors Applet is an applet for the MATE Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds
and voltage readings under Linux.
Can interface via the Linux kernel i2c modules, or the i8k kernel modules
Includes a simple, yet highly customization display and intuitive 
user-interface.
Alarms can be set for each sensor to notify the user once a certain value
has been reached, and can be configured to execute a given command at given
repeated intervals.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The mate-sensors-applet-devel package contains libraries and header files for
developing applications that use mate-sensors-applet.

%prep
%setup -q

%build
autoreconf -fisv
%configure \
    --disable-static \
    --disable-schemas-compile \
    --enable-libnotify \
    --with-nvidia

make %{?_smp_mflags}


%install
%{makeinstall_std}

find $RPM_BUILD_ROOT -name "*.la" -exec rm -rf {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libexecdir}/mate-sensors-applet
%{_libdir}/libmate-sensors-applet-plugin.so.*
%{_libdir}/mate-sensors-applet/
%{_datadir}/mate-sensors-applet/ui/
%{_datadir}/pixmaps/mate-sensors-applet/
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/dbus-1/services/org.mate.panel.applet.SensorsAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.sensor.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.sensors-applet.mate-panel-applet

%files devel
%{_libdir}/libmate-sensors-applet-plugin.so
%{_includedir}/mate-sensors-applet/


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1_1
- new version

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.4-alt1_1
- update to mate 1.10

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_4
- new fc release

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3
- new fc release

