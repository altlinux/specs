# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize libgtk+2-gir-devel libpolkit-gir-devel pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
Group: File tools
%define _libexecdir %_prefix/libexec
Name:		mate-polkit
Version:	1.5.0
Release:	alt1_1
Summary:	Integrates polkit authentication for MATE desktop
License:	LGPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.5/%name-%version.tar.xz

BuildRequires:	gtk2-devel
BuildRequires:	mate-common
BuildRequires:	libpolkit-devel
BuildRequires:	gobject-introspection-devel
# needed for gobject-introspection support somehow,
# https://bugzilla.redhat.com/show_bug.cgi?id=847419#c17 asserts this is a bug (elsewhere)
# but I'm not entirely sure -- rex
BuildRequires: 	libcairo-gobject-devel

Provides:	PolicyKit-authentication-agent
Source44: import.info


%description
Integrates polkit with the MATE Desktop environment

%package devel
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary:	Integrates polkit with the MATE Desktop environment

%description devel
Development libraries for mate-polkit

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh --disable-static


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang %{name}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'


%files -f %{name}.lang
# yes, license really is LGPLv2+, despite included COPYING is about GPL, poke upstreamo
# to include COPYING.LIB here instead  -- rex
%doc AUTHORS COPYING README
%{_sysconfdir}/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%{_libdir}/libpolkit-gtk-mate-1.so.0
%{_libdir}/libpolkit-gtk-mate-1.so.0.0.0
%{_libdir}/girepository-1.0/PolkitGtkMate-1.0.typelib
%{_libexecdir}/polkit-mate-authentication-agent-1

%files devel
%{_libdir}/libpolkit-gtk-mate-1.so
%{_libdir}/pkgconfig/polkit-gtk-mate-1.pc
%{_includedir}/polkit-gtk-mate-1/
%{_datadir}/gir-1.0/PolkitGtkMate-1.0.gir


%changelog
* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Fri Aug 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

