# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/mateconftool-2 libICE-devel libSM-devel pkgconfig(gdk-2.0) pkgconfig(gdk-3.0) pkgconfig(gdk-x11-2.0) pkgconfig(gdk-x11-3.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           libmatekbd
Version:        1.4.0
Release:        alt2_1.1.1
Summary:        A keyboard configuration library

Group:          System/Libraries
License:        LGPLv2+
URL: 			http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:  libcairo-devel
BuildRequires:  libxklavier-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  mate-conf-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk2-devel
BuildRequires:  mate-common

Requires(post): mate-conf
Requires: iso-codes

%description
The libmatekbd package contains a MATE library which manages
keyboard configuration and offers various widgets related to
keyboard configuration.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libmatekbd = %{version}-%{release}


%description    devel
The libgnomekbd-devel package contains libraries and header files for
developing applications that use libmatekbd.


%package        capplet
Summary:        A configuration applet to select libmatekbd plugins
Group:          Graphical desktop/Other
Requires:       libmatekbd = %{version}-%{release}

%description    capplet
The libmatekbd-capplet package contains a configuration applet to
select libmatekbd plugins. These plugins can modify the appearance
of the keyboard indicator applet.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static 

make %{?_smp_mflags}


%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%find_lang %{name}

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_keyboard_xkb.schemas \
	> /dev/null || :


%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_keyboard_xkb.schemas \
	> /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_keyboard_xkb.schemas \
	> /dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS COPYING.LIB
%{_libdir}/*.so.*
%{_datadir}/libmatekbd
%{_sysconfdir}/mateconf/schemas/desktop_mate_peripherals_keyboard_xkb.schemas


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files capplet
%{_bindir}/matekbd-indicator-plugins-capplet
%{_datadir}/applications/matekbd-indicator-plugins-capplet.desktop

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- added Requires: iso-codes

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

