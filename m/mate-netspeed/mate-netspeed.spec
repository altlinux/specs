Group: Networking/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize libgio-devel pkgconfig(gio-2.0) pkgconfig(libgtop-2.0) pkgconfig(libmatepanelapplet-4.0) pkgconfig(mate-desktop-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-netspeed
Version:        1.12.0
Release:        alt1_1
Summary:        MATE netspeed
License:        GPLv2+
URL:            http://www.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.12/%{name}-%{version}.tar.xz

BuildRequires:  mate-common
BuildRequires:  libgtop2-devel
BuildRequires:  mate-panel-devel
BuildRequires:  gtk2-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  wireless-tools-devel
Source44: import.info


%description
MATE netspeed is an applet that shows how much 
traffic occurs on a specified network device. 

%prep
%setup -q

%build
%configure                    \
   --disable-static           \
   --disable-schemas-compile  

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libexecdir}/mate-netspeed-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.NetspeedAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.netspeed.gschema.xml
%{_datadir}/icons/hicolor/*x*/apps/*.png
%{_datadir}/icons/hicolor/*x*/devices/*.png
%{_datadir}/help/*/mate-netspeed-applet
%{_datadir}/icons/hicolor/*x*/status/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-netspeed-applet.svg
%{_datadir}/mate-panel/applets/org.mate.panel.NetspeedApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/netspeed-menu.xml


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_1
- new version

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_1
- rebuild with libgtop

* Thu Mar 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_2
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- new fc release

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

