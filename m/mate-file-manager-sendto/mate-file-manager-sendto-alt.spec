# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize pkgconfig(dbus-1) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(mateconf-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
BuildRequires(pre): rpm-macros-mate-conf
%define oldname caja-sendto
Name:           mate-file-manager-sendto
Version:        1.4.0
Release:        alt1_1.1
Summary:        Caja context menu for sending files

Group:          Graphical desktop/Other
License:        GPLv2+
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:  gtk2-devel
BuildRequires:  mate-file-manager-devel >= 1.1.2
BuildRequires:  gettext
BuildRequires:  perl-XML-Parser intltool
BuildRequires:  libdbus-glib-devel >= 0.70
BuildRequires:  libgupnp-devel >= 0.13
BuildRequires: 	mate-common
BuildRequires: 	gtk-doc

Requires(pre): mate-conf
Requires(post): mate-conf
Requires(preun): mate-conf

%description
The caja-sendto package provides a Caja context menu for
sending files via other desktop applications.  These functions are
implemented as plugins, so caja-sendto can be extended with
additional features.

%package devel
Summary:        Development files for %{oldname}
Group:          Development/C
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the libraries amd header files that are needed
for writing plugins for caja-sendto.

%prep
%setup -q -n %{name}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build
%configure
make %{?_smp_mflags}


%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

find $RPM_BUILD_ROOT \( -name '*.a' -o -name '*.la' \) -exec rm -f {} \;

%find_lang %{oldname}

%pre
%mateconf_schema_prepare nst

%preun
%mateconf_schema_remove nst

%files -f %{oldname}.lang
%doc AUTHORS ChangeLog COPYING NEWS
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%{_libdir}/caja-sendto/plugins/*.so
%{_datadir}/caja-sendto
%{_bindir}/caja-sendto
%{_mandir}/man1/caja-sendto.1.*
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/MateConf/gsettings/caja-sendto-convert

%files devel
%{_datadir}/gtk-doc
%{_libdir}/pkgconfig/caja-sendto.pc
%dir %{_includedir}/caja-sendto
%{_includedir}/caja-sendto/caja-sendto-plugin.h

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

