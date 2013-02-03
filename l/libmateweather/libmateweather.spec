Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize glib2-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(libsoup-gnome-2.4) pkgconfig(libxml-2.0) python-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:          libmateweather
Version:       1.5.1
Release:       alt1_1
Summary:       Libraries to allow MATE Desktop to display weather information
License:       GPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: gtk2-devel
BuildRequires: libsoup-devel
BuildRequires: mate-common
BuildRequires: python-module-pygobject-devel
BuildRequires: python-module-gudev
BuildRequires: python-module-pygtk-devel
Source44: import.info
Patch33: libmateweather-gettext-not-xml.patch

%description
Libraries to allow MATE Desktop to display weather information


%package devel
Group: Development/C
Summary:  Development files for libmateweather
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libmateweather


%prep
%setup -q
%patch33 -p1
NOCONFIGURE=1 ./autogen.sh


%build
%configure --disable-static       \
           --with-gnu-ld          \
           --enable-python        \
           --enable-gtk-doc-html  

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'
find %{buildroot} -name '*.a' -exec rm -fv {} ';'


%find_lang %{name} %{name}-locations
cat libmateweather-locations.lang >> %{name}.lang

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/libmateweather/
%{_datadir}/icons/mate/*/status/*
%{_datadir}/glib-2.0/schemas/org.mate.weather.gschema.xml
%{python_sitelibdir}/mateweather/
%{_libdir}/libmateweather.so.1*

%files devel
%doc %{_datadir}/gtk-doc/html/libmateweather/
%{_libdir}/libmateweather.so
%{_includedir}/libmateweather/
%{_libdir}/pkgconfig/mateweather.pc


%changelog
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

