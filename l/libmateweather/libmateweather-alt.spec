# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/mateconftool-2 glib2-devel pkgconfig(gtk+-2.0) pkgconfig(libsoup-gnome-2.4) pkgconfig(pygobject-2.0) python-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           libmateweather
Version:        1.4.0
Release:        alt1_1.1
Summary:        A library for weather information

Group:          System/Libraries
License:        GPLv2+
URL: 			http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

# Patch from Ubuntu...
Patch0: gettext-not-xml.patch

BuildRequires:  mate-conf-devel >= 1.1.0
BuildRequires:  libdbus-devel
BuildRequires:  gtk2-devel >= 2.11.0
BuildRequires:  libsoup-devel >= 2.4
BuildRequires:  libxml2-devel >= 2.6
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk-doc
BuildRequires:  mate-common

# for directories
Requires: mate-icon-theme

%description
libmateweather is a library to access weather information from online
services for numerous locations.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
# libgweather used to be part of mate-applets, and
# mate-applets-devel only had the libmateweather-devel parts in it
Requires:       libmateweather = %{version}-%{release}
Requires:       gtk-doc

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch0 -p1 -b .gettext
gtkdocize
autoreconf -i -f

%build

%configure \
	--disable-static \
	--enable-gtk-doc

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name} libmateweather-locations
cat libmateweather-locations.lang >> %{name}.lang

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 --makefile-install-rule %{_sysconfdir}/mateconf/schemas/mateweather.schemas > /dev/null || :
touch --no-create %{_datadir}/icons/mate &>/dev/null || :

%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/mateweather.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/mateweather.schemas > /dev/null || :
fi

%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/mate &>/dev/null
fi

%files -f %{name}.lang
%doc COPYING
%{_sysconfdir}/mateconf/schemas/mateweather.schemas
%{_libdir}/libmateweather.so.*
%dir %{_datadir}/libmateweather
%{_datadir}/libmateweather/*
%{_datadir}/icons/mate/*/status/*

%files devel
%{_includedir}/libmateweather
%{_libdir}/libmateweather.so
%{_libdir}/pkgconfig/mateweather.pc
%{_datadir}/gtk-doc/html/libmateweather

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

