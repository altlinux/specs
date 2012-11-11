# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-mkenums /usr/bin/gtkdocize /usr/bin/pkg-config libICE-devel libSM-devel libpopt-devel pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) pkgconfig(libglade-2.0) pkgconfig(libxml-2.0)
# END SourceDeps(oneline)
Group: System/Libraries
%define _libexecdir %_prefix/libexec
Name:	libmatecomponentui	
Version:	1.4.0
Release:	alt1_2
Summary:	Libraries for MATE Desktop ui
License:	GPLv2+
URL:	http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils mate-common mate-conf-devel libmatecanvas-devel libmatecomponent-devel libmate-devel mate-doc-utils libglade2-devel popt-devel
Source44: import.info

%description
Libraries for MATE Desktop ui

%package devel
Group: Development/C
Summary: Includes for libmatecomponentui
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libmatecomponentui

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh


%build
%configure --disable-static --enable-gtk-doc-html
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'
desktop-file-install									\
	--remove-category="MATE"							\
	--add-category="X-Mate"								\
	--remove-only-show-in="MATE"							\
	--add-only-show-in="X-Mate"							\
	--delete-original								\
	--dir=%{buildroot}%{_datadir}/applications					\
%{buildroot}/%{_datadir}/applications/matecomponent-browser.desktop


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mate-test-moniker
%{_bindir}/matecomponent-browser
%{_libdir}/libmatecomponentui-2.so.*
%{_datadir}/gtk-doc/html/libmatecomponentui/
%{_datadir}/mate-2.0/ui/
%{_datadir}/applications/matecomponent-browser.desktop
%{_libdir}/matecomponent-2.0/samples/matecomponent-sample-controls-2
%{_libdir}/matecomponent/servers/CanvDemo.server
%{_libdir}/matecomponent/servers/MateComponent_Sample_Controls.server

%files devel
%{_includedir}/libmatecomponentui-2.0/
%{_libdir}/libglade/2.0/libmatecomponent.so
%{_libdir}/pkgconfig/libmatecomponentui-2.0.pc
%{_libdir}/libmatecomponentui-2.so

%changelog
* Sun Nov 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

