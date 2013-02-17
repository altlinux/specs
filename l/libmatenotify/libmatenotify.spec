Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/xmlto pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           libmatenotify
Version:        1.5.0
Release:        alt1_2
Summary:        Libraries for mate notify
License:        LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  libdbus-glib-devel
BuildRequires:  gtk2-devel
BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  mate-desktop-devel
Source44: import.info

%description
Libraries for mate notify.

%package devel
Group: Development/C
Summary:  Development libraries for libmatenotify
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for libmatenotify


%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh


%build
%configure                 \
   --enable-gtk-doc-html   \
   --with-gnu-ld           \
   --disable-static

make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS COPYING README
%{_bindir}/mate-notify-send
%{_libdir}/libmatenotify.so.1*
%{_datadir}/gtk-doc/html/libmatenotify

%files devel
%{_libdir}/libmatenotify.so
%{_libdir}/pkgconfig/libmatenotify.pc
%{_includedir}/libmatenotify


%changelog
* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Tue Nov 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

