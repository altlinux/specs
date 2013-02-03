Group: Networking/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize libgio-devel pkgconfig(gio-2.0) pkgconfig(libgtop-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-netspeed
Version:        1.5.0
Release:        alt1_1
Summary:        MATE netspeed
License:        GPLv2+
URL:            http://www.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  libgtop2-devel
BuildRequires:  mate-panel-devel
BuildRequires:  gtk2-devel
Requires:       mate-panel
Source44: import.info

%description
MATE netspeed is an applet that shows how much 
traffic occurs on a specified network device. 

%prep
%setup -q
%build
NOCONFIGURE=1 ./autogen.sh
export LDFLAGS="$LDFLAGS -lm"
%configure                                 \
                --disable-static           \
                --disable-scrollkeeper     \
                --disable-schemas-compile  \
                --with-gnu-ld

make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libexecdir}/mate-netspeed-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.NetspeedAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.netspeed.gschema.xml
%{_datadir}/icons/hicolor/*x*/apps/*.png
%{_datadir}/icons/hicolor/*x*/devices/*.png
%{_datadir}/mate/help/mate_netspeed_applet
%{_datadir}/omf/mate_netspeed_applet
%{_datadir}/icons/hicolor/*x*/status/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-netspeed-applet.svg
%{_datadir}/mate-panel/applets/org.mate.panel.NetspeedApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/netspeed-menu.xml


%changelog
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- new fc release

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

