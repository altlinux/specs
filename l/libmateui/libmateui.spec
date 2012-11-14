# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gdk-pixbuf-csource /usr/bin/gtkdocize /usr/bin/mateconftool-2 libSM-devel libpopt-devel pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(ice) pkgconfig(libglade-2.0) pkgconfig(pango) pkgconfig(sm)
# END SourceDeps(oneline)
Group: System/Libraries
BuildRequires: libmatekeyring-devel
%define _libexecdir %_prefix/libexec
Name:		libmateui
Version:	1.4.0
Release:	alt1_2
Summary:	Libraries for MATE Desktop UI
License:	LGPLv2+ 
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires: gtk2-devel glib2-devel libglade2-devel libxml2-devel libmate-devel libmatecanvas-devel libmatecomponentui-devel mate-conf-devel pango-devel mate-vfs-devel mate-keyring-devel mate-common libX11-devel libmatekeyring-devel popt-devel
Source44: import.info
Patch33: libgnomeui-2.23.4-disable-event-sounds.patch

%description
Libraries for MATE Desktop UI

%package devel
Group: Development/C
Summary:	Development files for libmateui
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libmateui

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1


%build
%configure --disable-static --with-gtk=2.0 --with-x
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
%find_lang %{name} --all-name
find %{buildroot} -name '*.la' -exec rm -vf {} ';'
find %{buildroot} -name '*.a' -exec rm -vf {} ';'

%files -f %{name}.lang
%doc AUTHORS COPYING.LIB README
%{_libdir}/libmateui-2.so.0
%{_libdir}/libmateui-2.so.0.396.4
%{_datadir}/pixmaps/mate-about-logo.png

%files devel
%{_datadir}/gtk-doc/html/libmateui/
%{_includedir}/libmateui-2.0/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libglade/2.0/libmate.so
%{_libdir}/libmateui-2.so

%changelog
* Wed Nov 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

