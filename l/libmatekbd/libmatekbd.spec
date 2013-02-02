Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize libICE-devel libSM-devel libgio-devel pkgconfig(gdk-2.0) pkgconfig(gdk-3.0) pkgconfig(gdk-x11-2.0) pkgconfig(gdk-x11-3.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           libmatekbd
Version:        1.5.0
Release:        alt1_2
Summary:        Libraries for mate kbd
License:        LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  mate-common
BuildRequires:  pkgconfig(gsettings-desktop-schemas)

Requires:       gsettings-desktop-schemas
Source44: import.info
Requires: iso-codes


%description
Libraries for matekbd

%package devel
Group: Development/C
Summary:  Development libraries for libmatekbd
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for libmatekbd

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh


%build
%configure --disable-static
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'


#desktop-file-install									\
#	--remove-category="MATE"							\
#	--add-category="X-Mate"								\
#	--delete-original								\
#	--dir=%{buildroot}%{_datadir}/applications					\
#%{buildroot}%{_datadir}/applications/matekbd-indicator-plugins-capplet.desktop


%find_lang %{name} --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING.LIB README
%{_datadir}/libmatekbd/
%{_datadir}/glib-2.0/schemas/org.mate.peripherals-keyboard-xkb.gschema.xml
%{_libdir}/libmatekbd.so.4*
%{_libdir}/libmatekbdui.so.4*

%files devel
%{_includedir}/libmatekbd/
%{_libdir}/pkgconfig/libmatekbd.pc
%{_libdir}/pkgconfig/libmatekbdui.pc
%{_libdir}/libmatekbdui.so
%{_libdir}/libmatekbd.so

%changelog
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Tue Nov 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

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

