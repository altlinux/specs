# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize libICE-devel libSM-devel libX11-devel
# END SourceDeps(oneline)
Summary: utility functions for the Xsettings protocol (GPE)
Name: libxsettings-client0
Version: 0.17
Release: alt1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: BSD-like, LGPL
Group: System/Libraries
URL: http://standards.freedesktop.org/xsettings-spec/0.5/

Source0: libxsettings-client-0.17.tar.gz
Source1: libxsettings-client_0.17-6.debian.tar.gz
Source2: libxsettings-client.watch

%description
This library is used for applications making use of the Xsettings
 configuration setting propagation protocol. Controls setting of
 double click timeout, drag-and-drop threshold, and default foreground and
 background colors for all applications running within a desktop.
 .
 Used by the GPE Palmtop Environment.

%package -n libxsettings-client-devel
Summary: utility functions for the Xsettings protocol (Development files)
Group: Development/C
Requires: %name = %version-%release

%description -n libxsettings-client-devel
This package contains headers and other files required to compile
 software using the GPE scheduling library to use the Xsettings 
 configuration setting propagation protocol. Controls setting of
 double click timeout, drag-and-drop threshold, and default foreground and
 background colors for all applications running within a desktop.
 .
 Used by the GPE Palmtop Environment.

%package -n libxsettings-client-doc
Summary: utility functions for the Xsettings protocol (Documentation)
Group: Development/Documentation

%description -n libxsettings-client-doc
Documentation for the Xsettings protocol that controls setting of
 double click timeout, drag-and-drop threshold, and default foreground and
 background colors for all applications running within a desktop.

%prep
%setup -q -n libxsettings-client-%version

%build
%configure \
	--enable-gtk-doc
%make LIBS=-lX11

%install
make install DESTDIR=%buildroot
#ln -s -T /usr/share/gtk-doc/html/libXsettings-client/ %buildroot/usr/share/doc/libxsettings-client-doc/html

%files 
%_libdir/lib*.so.*

%files -n libxsettings-client-devel
%_libdir/*.so
%_libdir/*.a
%_includedir/xsettings-client.h
%_includedir/xsettings-common.h
%_libdir/pkgconfig/*.pc

%files -n libxsettings-client-doc
%_datadir/gtk-doc/html/libXsettings-client

%changelog
* Fri Nov 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- initial import from debian.
- powered by debian2spec ;)
