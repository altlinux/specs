# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/pkg-config /usr/sbin/httpd /usr/sbin/httpd2 libX11-devel libgio-devel pkgconfig(dbus-1) pkgconfig(gdk-x11-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(libcanberra-gtk)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define fedora 21
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.12

Summary:         Mate user file sharing
Name:            mate-user-share
Version:         %{branch}.0
Release:         alt2_0
License:         GPLv2+
Group:           System/Libraries
URL:             http://mate-desktop.org

# Settings used for build from snapshots.
%{!?rel_build:%global commit c0f0c63c670d799dee4fa7577083d0cbace56db4}
%{!?rel_build:%global commit_date 20140210}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

# for downloading the tarball use 'spectool -g -R mate-user-share.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  mate-file-manager-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  yelp-tools
BuildRequires:  libgtk+2-devel
BuildRequires:  libgtk+3-devel
BuildRequires:  httpd
BuildRequires:  libcanberra-devel
BuildRequires:  libICE-devel
BuildRequires:  libnotify-devel
BuildRequires:  libselinux-devel
BuildRequires:  libSM-devel
BuildRequires:  mate-common
BuildRequires:  mate-file-manager-devel
BuildRequires:  apache2-mod_dnssd
BuildRequires:  perl(XML/Parser.pm)
BuildRequires:  libunique-devel

# disable bluetooth support for bluez5
#BuildRequires: mate-bluetooth-devel
BuildRequires: mate-file-manager-devel


Requires: httpd
# obsolete with bluez5
%if 0%{?fedora} > 19
#Requires: obex-data-server
%else
Requires: obex-data-server
%endif
Requires: apache2-mod_dnssd
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
%setup -q%{!?rel_build:n %{name}-%{commit}}

# nedded to create missing configure and make files
# for git snapshot builds, comment out for release builds
#NOCONFIGURE=1 ./autogen.sh

%build
# disable bluetooth support for bluez5
%configure \
    --with-httpd=/usr/sbin/httpd2 \
    --disable-static \
    --disable-bluetooth \
    --disable-schemas-compile

make %{?_smp_mflags}

%install
%{makeinstall_std}

rm -f $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

# no need to provide a convert file for mateconf user settings,
# because Mate started with gsettings in f17/18
rm -f $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/mate-user-share.convert

%find_lang %{name} --with-gnome --all-name

# disable bluetooth support for bluez5
%if 0%{?fedora} > 19
rm -f ${RPM_BUILD_ROOT}/%{_sysconfdir}/xdg/autostart/mate-user-share-obexftp.desktop
rm -f desktop-file-validate ${RPM_BUILD_ROOT}/%{_sysconfdir}/xdg/autostart/mate-user-share-obexpush.desktop
%else
desktop-file-validate ${RPM_BUILD_ROOT}/%{_sysconfdir}/xdg/autostart/mate-user-share-obexftp.desktop
desktop-file-validate ${RPM_BUILD_ROOT}/%{_sysconfdir}/xdg/autostart/mate-user-share-obexpush.desktop
%endif
desktop-file-validate ${RPM_BUILD_ROOT}/%{_datadir}/applications/mate-user-share-properties.desktop
desktop-file-validate ${RPM_BUILD_ROOT}/%{_sysconfdir}/xdg/autostart/mate-user-share-webdav.desktop

%files -f %{name}.lang
%doc README COPYING NEWS
%{_bindir}/mate-file-share-properties
%{_libexecdir}/mate-user-share
%{_datadir}/mate-user-share/
%{_datadir}/applications/mate-user-share-properties.desktop
# disable bluetooth support for bluez5
%if 0%{?fedora} > 19
%{_sysconfdir}/xdg/autostart/mate-user-share-webdav.desktop
%else
%{_sysconfdir}/xdg/autostart/mate-user-share-obexftp.desktop
%{_sysconfdir}/xdg/autostart/mate-user-share-obexpush.desktop
%{_sysconfdir}/xdg/autostart/mate-user-share-webdav.desktop
%endif
%{_datadir}/icons/hicolor/*/apps/mate-obex-server.png
%{_libdir}/caja/extensions-2.0/*.so
%{_datadir}/caja/extensions/libcaja-user-share.caja-extension
%{_datadir}/glib-2.0/schemas/org.mate.FileSharing.gschema.xml
%{_mandir}/man1/mate-file-share-properties.1.*


%changelog
* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt2_0
- added --with-httpd=/usr/sbin/httpd2 (closes: #31965)

* Mon Apr 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_0
- new version

* Thu Oct 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_0
- new version

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_1
- new fc release

* Sun Mar 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_0
- no bluetooth for now

* Fri Mar 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_0
- new fc release

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

