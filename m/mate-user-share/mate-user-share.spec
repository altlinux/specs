# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/docbook2man /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/gtkdocize /usr/bin/mateconftool-2 /usr/bin/pkg-config /usr/sbin/httpd /usr/sbin/httpd2 libICE-devel libSM-devel libX11-devel libcups-devel libsane-devel libtiff-devel pkgconfig(dbus-1) pkgconfig(gdk-x11-2.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(lcms) pkgconfig(libcanberra-gtk) pkgconfig(sane-backends) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
BuildRequires(pre): rpm-macros-mate-conf
Summary: Mate user file sharing
Name: mate-user-share
Version: 1.4.1
Release: alt1_1
License: GPLv2+
Group: System/Libraries
URL: http://pub.mate-desktop.org
Source0: http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires: mate-conf-devel
BuildRequires: gtk2-devel
BuildRequires: httpd apache2-mod_dnssd
BuildRequires: mate-bluetooth-libs-devel
BuildRequires: libcanberra-devel
BuildRequires: desktop-file-utils
BuildRequires: mate-doc-utils
BuildRequires: libselinux-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libmatenotify-devel
BuildRequires: mate-file-manager-devel
BuildRequires: libunique-devel
BuildRequires: gettext
BuildRequires: perl(XML/Parser.pm) intltool
BuildRequires: scrollkeeper
BuildRequires: mate-common

Requires: httpd
Requires: obex-data-server
Requires: apache2-mod_dnssd

Requires(post): mate-conf
Requires(pre): mate-conf
Requires(preun): mate-conf
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
NOCONFIGURE=1 ./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

rm -f $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

#desktop-file-install --vendor gnome --delete-original                   \
#  --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
#  --add-only-show-in GNOME                                              \
#  --add-category X-Red-Hat-Base                                         \
#  $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%find_lang %{name} --all-name

%post
%mateconf_schema_upgrade desktop_mate_file_sharing 

%pre
%mateconf_schema_prepare desktop_mate_file_sharing

%preun
%mateconf_schema_remove desktop_mate_file_sharing

%files -f %{name}.lang
%doc README COPYING NEWS
%{_bindir}/*
%{_libexecdir}/*
# wildcard _libexecdir/*
%exclude %_prefix/lib/debug
%{_datadir}/mate-user-share
%{_datadir}/applications/*
%{_sysconfdir}/xdg/autostart/mate-user-share.desktop
%{_sysconfdir}/mateconf/schemas/*
%{_datadir}/icons/hicolor/*/apps/mate-obex-server.png
%{_libdir}/caja/extensions-2.0/*.so

%changelog
* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_1
- added mate-desktop-1.5.0-alt-settings.patch - font settings

