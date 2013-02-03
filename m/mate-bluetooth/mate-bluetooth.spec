# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtk-update-icon-cache /usr/bin/gtkdocize /usr/bin/update-desktop-database /usr/bin/xmllint libgio-devel libgtk+2-gir-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gmodule-export-2.0) pkgconfig(gtk+-2.0) pkgconfig(x11) pkgconfig(xi)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:		mate-bluetooth
Version:	1.5.0
Release:	alt1_0
Summary:	Bluetooth graphical utilities

Group:		Communications
License:	GPLv2+
URL:		http://pub.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
Source1:	61-mate-bluetooth-rfkill.rules

Patch0:		mate-bluetooth_fix_mate-bluetooth-applet_desktop-file.patch

#BuildRequires:	mate-conf-devel
BuildRequires:	gtk2-devel
BuildRequires:	libunique-devel
BuildRequires:	libdbus-glib-devel
BuildRequires:	libnotify-devel
BuildRequires:	libmx-devel
BuildRequires:	mate-doc-utils rarian-compat
BuildRequires:	mate-file-manager-sendto-devel
BuildRequires:  libmatenotify-devel

BuildRequires:	intltool desktop-file-utils gettext gtk-doc libtool mate-common

BuildRequires:	gobject-introspection-devel

Provides:	dbus-bluez-pin-helper

# Otherwise we might end up with mismatching version
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gvfs-backend-obexftp
Requires:	bluez >= 4.42
Requires:	obexd
Requires:	mate-notification-daemon
#Requires:	pulseaudio-module-bluetooth
Requires:	mate-control-center

Requires(post):		desktop-file-utils
Requires(postun):	desktop-file-utils

%description
The mate-bluetooth package contains graphical utilities to setup,
monitor and use Bluetooth devices.

%package libs
Summary:	GTK+ Bluetooth device selection widgets
Group:		System/Libraries
License:	LGPLv2+
Requires:	gobject-introspection

%description libs
This package contains libraries needed for applications that
want to display a Bluetooth device selection widget.

%package libs-devel
Summary:	Development files for %{name}-libs
Group:		Development/C
License:	LGPLv2+
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk-doc
Provides:	mate-bluetooth-devel = %{version}

%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a Bluetooth device selection widget.

%prep
%setup -q
%patch0 -p1 -b .mate-bluetooth_fix_mate-bluetooth-applet_desktop-file

NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--disable-desktop-update \
	--disable-icon-update \
	--enable-caja-sendto=yes \
	--disable-schemas-compile \
	--enable-gtk-doc

make %{?_smp_mflags}

%install
export MATEGCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libmate-bluetooth.la \
	   $RPM_BUILD_ROOT/%{_libdir}/mate-bluetooth/plugins/*.la \
	   $RPM_BUILD_ROOT/%{_libdir}/caja-sendto/plugins/*.la \
	   $RPM_BUILD_ROOT/%{_libdir}/control-center-1/panels/libbluetooth.la

desktop-file-install --vendor=""				\
	--delete-original					\
	--remove-category MATE  \
	--add-category X-MATE   \
	--remove-only-show-in XFCE \
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications		\
	$RPM_BUILD_ROOT%{_datadir}/applications/mate-bluetooth-properties.desktop

desktop-file-install --vendor=""				\
	--delete-original					\
	--remove-category MATE  \
	--add-category X-MATE   \
	--remove-only-show-in XFCE \
	--dir=$RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/	\
	$RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/mate-bluetooth-applet.desktop

install -m0644 -D %{SOURCE1} $RPM_BUILD_ROOT/lib/udev/rules.d/61-mate-bluetooth-rfkill.rules

# mate-bluetooth2 is the name for the gettext domain,
# mate-bluetooth is the name in the docs
%find_lang mate-bluetooth
%find_lang %{name} --all-name
cat %{name}.lang >> mate-bluetooth2.lang

# save space by linking identical images in translated docs
helpdir=$RPM_BUILD_ROOT%{_datadir}/mate/help/%{name}
for f in $helpdir/C/figures/*.png; do
  b="$(basename $f)"
  for d in $helpdir/*; do
    if [ -d "$d" -a "$d" != "$helpdir/C" ]; then
      g="$d/figures/$b"
      if [ -f "$g" ]; then
        if cmp -s $f $g; then
          rm "$g"; ln -s "../../C/figures/$b" "$g"
        fi
      fi
    fi
  done
done

%files
%doc README NEWS COPYING
%{_sysconfdir}/xdg/autostart/mate-bluetooth-applet.desktop
%{_bindir}/mate-bluetooth-applet
%{_bindir}/mate-bluetooth-sendto
%{_bindir}/mate-bluetooth-wizard
%{_bindir}/mate-bluetooth-properties
%{_libdir}/mate-bluetooth/
%{_datadir}/applications/*.desktop
%{_datadir}/mate-bluetooth/
%{_mandir}/man1/*
%{_libdir}/caja-sendto/plugins/*.so
/lib/udev/rules.d/61-mate-bluetooth-rfkill.rules
%{_datadir}/MateConf/gsettings/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/mate/help/mate-bluetooth/
%{_datadir}/omf/mate-bluetooth/

%files -f mate-bluetooth2.lang libs
%doc COPYING.LIB
%{_libdir}/libmate-bluetooth.so.*
%{_libdir}/girepository-1.0/MateBluetooth-1.0.typelib
%{_datadir}/icons/mate/*/apps/*
%{_datadir}/icons/mate/*/status/*

%files libs-devel
%{_includedir}/mate-bluetooth/
%{_libdir}/libmate-bluetooth.so
%{_libdir}/pkgconfig/mate-bluetooth-1.0.pc
%{_datadir}/gir-1.0/MateBluetooth-1.0.gir
%{_datadir}/gtk-doc/html/mate-bluetooth/

%changelog
* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- mate 1.5

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

