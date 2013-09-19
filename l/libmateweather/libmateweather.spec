Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize glib2-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(libsoup-gnome-2.4) pkgconfig(libxml-2.0) python-devel
# END SourceDeps(oneline)
# for --enable-python
BuildRequires: python-module-pygobject-devel
BuildRequires: python-module-gudev
BuildRequires: python-module-pygtk-devel

%define _libexecdir %_prefix/libexec
Name:          libmateweather
Version:       1.6.2
Release:       alt1_3
Summary:       Libraries to allow MATE Desktop to display weather information
License:       GPLv2+ and LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz

BuildRequires: gtk2-devel
BuildRequires: libsoup-devel
BuildRequires: mate-common

Requires:      %{name}-data = %{version}-%{release}
Source44: import.info
Patch33: libmateweather-gettext-not-xml.patch

%description
Libraries to allow MATE Desktop to display weather information

%package data
Group: System/Libraries
Summary: Data files for the libmateweather
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description data
This package contains shared data needed for libmateweather.

%package devel
Group: Development/C
Summary:  Development files for libmateweather
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libmateweather


%prep
%setup -q
%patch33 -p1


%build
autoreconf -fisv
%configure --enable-python --disable-static       \
           --disable-schemas-compile \
           --with-gnu-ld          \
           --enable-gtk-doc-html

# fix unused-direct-shlib-dependency
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool 

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'
find %{buildroot} -name '*.a' -exec rm -fv {} ';'

%find_lang %{name} %{name}-locations
cat libmateweather-locations.lang >> %{name}.lang


%files
%doc AUTHORS COPYING README
%{_datadir}/glib-2.0/schemas/org.mate.weather.gschema.xml
%{_libdir}/libmateweather.so.1*

%files data -f %{name}.lang
%{_datadir}/icons/mate/*/status/*
%{_datadir}/libmateweather/

%files devel
%doc %{_datadir}/gtk-doc/html/libmateweather/
%{_libdir}/libmateweather.so
%{_includedir}/libmateweather/
%{_libdir}/pkgconfig/mateweather.pc


%changelog
* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_3
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

