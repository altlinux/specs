# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/php glib2-devel
# END SourceDeps(oneline)
### Abstract ###

Name: libsoup22
Version: 2.2.105
Release: alt3_9
License: LGPLv2+
Group: Development/C
Summary: Soup, an HTTP library implementation
URL: ftp://ftp.gnome.org/pub/gnome/sources/libsoup/
Source: ftp://ftp.gnome.org/pub/gnome/sources/libsoup/2.2/libsoup-%{version}.tar.bz2

### Patches ###

# RH bug #511673
Patch1: libsoup-2.2.105-dprintf-conflict.patch

### Dependencies ###

Requires: glib2 >= 2.12

### Build Dependencies ###

BuildRequires: libglib2-devel
BuildRequires: libgnutls-devel
BuildRequires: libxml2-devel
Source44: import.info

%description
Libsoup is an HTTP library implementation in C. It was originally part
of a SOAP (Simple Object Access Protocol) implementation called Soup, but
the SOAP and non-SOAP parts have now been split into separate packages.
 
libsoup uses the Glib main loop and is designed to work well with GTK
applications. This enables GNOME applications to access HTTP servers
on the network in a completely asynchronous fashion, very similar to
the Gtk+ programming model (a synchronous operation mode is also
supported for those who want it).

%package devel
Summary: Header files for the Soup library
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
Libsoup is an HTTP library implementation in C. This package allows 
you to develop applications that use the libsoup library.

%prep
%setup -q -n libsoup-%{version}
%patch1 -p1 -b .dprintf-conflict

perl -i -npe 's,#include\s*<(?:glib/gmessages|glib/gversionmacros|glib/gmacros|glib/gtypes|glib/gthread|glibconfig)\.h>,#include <glib.h>,' `pcregrep -rl '#include\s*<\(glib/gmessages\|glib/gversionmacros\|glib/gmacros\|glib/gtypes\|glib/gthread\|glibconfig\)\.h>' .`


%build
%configure
make %{?_smp_mflags}

#%check
#make check

%install
make DESTDIR=${RPM_BUILD_ROOT} install

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a

%files
%doc README COPYING NEWS AUTHORS
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libsoup-2.2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/libsoup-2.2

%changelog
* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.105-alt3_9
- fixed build with new glib

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.105-alt2_9
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.105-alt1_9
- initial import by fcimport

