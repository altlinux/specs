Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize libgio-devel pkgconfig(dbus-1) pkgconfig(dbus-glib-1) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-file-manager-sendto
Version:        1.5.0
Release:        alt1_2
Summary:        MATE file manager send to
License:        GPLv2+
URL:            http://www.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  mate-panel-devel
BuildRequires:  mate-file-manager-devel
BuildRequires:  mate-file-manager-extensions
BuildRequires:  libgupnp-devel
BuildRequires:  pidgin-devel
BuildRequires:  gajim
Source44: import.info

%description
s package provides 'send to' functionality to the MATE Desktop file
manager, Caja.

%package devel
Group: Development/C
Summary:   Development libraries and headers for mate-file-manager-send-to
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for mate-file-manager-sendto

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure   \
          --disable-static             \
          --disable-schemas-compile    \
          --with-gnu-ld                \
          --with-gajim

make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
%find_lang %{name} --all-name
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/caja-sendto.1*
%{_bindir}/caja-sendto
%{_datadir}/MateConf/gsettings/caja-sendto-convert
%{_datadir}/caja-sendto/ui/caja-sendto.ui
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/gtk-doc/html/caja-sendto
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_libdir}/caja-sendto/plugins/libnstgajim.so
%{_libdir}/caja-sendto/plugins/libnstpidgin.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_libdir}/caja-sendto/plugins/libnstupnp.so
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so

%files devel
%{_includedir}/caja-sendto/caja-sendto-plugin.h
%{_libdir}/pkgconfig/caja-sendto.pc

%changelog
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

