# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/pkg-config /usr/sbin/httpd /usr/sbin/httpd2 libICE-devel libSM-devel libX11-devel libgio-devel pkgconfig(dbus-1) pkgconfig(gdk-x11-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary: Mate user file sharing
Name:    mate-user-share
Version: 1.6.0
Release: alt2_4
License: GPLv2+
Group:   System/Libraries
URL:     http://mate-desktop.org
Source0: http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz

BuildRequires: gtk2-devel
BuildRequires: httpd apache2-mod_dnssd
BuildRequires: mate-bluetooth-devel
BuildRequires: libcanberra-devel
BuildRequires: desktop-file-utils
BuildRequires: mate-doc-utils
BuildRequires: libselinux-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libnotify-devel
BuildRequires: mate-file-manager-devel
BuildRequires: libunique-devel
BuildRequires: perl(XML/Parser.pm)
BuildRequires: mate-common

Requires: httpd
Requires: obex-data-server
Requires: apache2-mod_dnssd
Requires: icon-theme-hicolor
Source44: import.info

%description
mate-user-share is a small package that binds together various free
software projects to bring easy to use user-level file sharing to the
masses.

The program is meant to run in the background when the user is logged
in, and when file sharing is enabled a webdav server is started that
shares the $HOME/Public folder. The share is then published to all
computers on the local network using mDNS/rendezvous, so that it shows
up in the Network location in MATE.

The program also allows to share files using ObexFTP over Bluetooth.

%prep
%setup -q
# nedded to create missing configure and make files
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
    --disable-scrollkeeper \
    --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm -f $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

# no need to provide a convert file for mateconf user settings,
# because Mate started with gsettings in f17/18
rm -f $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/mate-user-share.convert

%find_lang %{name}

desktop-file-validate ${RPM_BUILD_ROOT}/%{_datadir}/applications/mate-user-share-properties.desktop
desktop-file-validate ${RPM_BUILD_ROOT}/%{_sysconfdir}/xdg/autostart/mate-user-share.desktop

%files -f %{name}.lang
%doc README COPYING NEWS
%{_bindir}/mate-file-share-properties
%{_libexecdir}/mate-user-share
%{_datadir}/mate-user-share/
%{_datadir}/applications/mate-user-share-properties.desktop
%{_sysconfdir}/xdg/autostart/mate-user-share.desktop
%{_datadir}/icons/hicolor/*/apps/mate-obex-server.png
%{_libdir}/caja/extensions-2.0/*.so
%{_datadir}/glib-2.0/schemas/org.mate.FileSharing.gschema.xml


%changelog
* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2_4
- new fc release

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2_3
- new fc release

* Thu Apr 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt2
- use mate-desktop instead libmatenotify

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_0
- new version

* Sat Mar 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt4_0
- fixed build

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt3_0
- cleaned up obsolete mate-conf BR:

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0
- cleaned up dependencies

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_1
- added mate-desktop-1.5.0-alt-settings.patch - font settings

