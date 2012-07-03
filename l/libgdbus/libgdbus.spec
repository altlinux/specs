# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize pkgconfig(glib-2.0)
# END SourceDeps(oneline)
Name:           libgdbus
Version:        0.2
Release:        alt3_6
Summary:        Library for simple D-Bus integration with GLib

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.bluez.org/
Source0:        http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.bz2

BuildRequires:  libglib2-devel
BuildRequires:  libdbus-devel
BuildRequires:  gtk-doc
Source44: import.info

%description
libgdbus is a helper library for D-Bus integration with GLib.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

perl -i -npe 's,#include\s*<glib/gmessages.h>,#include <glib.h>,' `pcregrep -rl '#include\s*<glib/gmessages.h>' .`



%build
%configure --disable-static --enable-gtk-doc
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*

%files devel
%doc %{_datadir}/gtk-doc/html/libgdbus/
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt3_6
- fixed build with new glib

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_6
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_6
- initial import by fcimport

