%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize libICE-devel libSM-devel libX11-devel
# END SourceDeps(oneline)
%def_disable gtkdoc
Summary: utility functions for the Xsettings protocol (GPE)
Name: libxsettings-client0
Version: 0.17
Release: alt4
Packager: Igor Vlasenko <viy@altlinux.ru>
License: BSD-like, LGPL
Group: System/Libraries
URL: http://standards.freedesktop.org/xsettings-spec/0.5/

Source0: libxsettings-client-0.17.tar.gz
Source1: libxsettings-client_0.17-10.debian.tar
Source2: libxsettings-client.watch
Patch: cflags.patch

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
%patch -p1

%build
%configure \
%if_enabled gtkdoc
	--enable-gtk-doc
%endif
%make LIBS=-lX11

%install
make install DESTDIR=%buildroot
#ln -s -T /usr/share/gtk-doc/html/libXsettings-client/ %buildroot/usr/share/doc/libxsettings-client-doc/html

%files 
%_libdir/lib*.so.*

%files -n libxsettings-client-devel
%_libdir/*.so
%exclude %_libdir/*.a
%_includedir/xsettings-client.h
%_includedir/xsettings-common.h
%_libdir/pkgconfig/*.pc

%if 0
%files -n libxsettings-client-devel-static
%_libdir/*.a
%endif

%files -n libxsettings-client-doc
%_datadir/gtk-doc/html/libXsettings-client

%changelog
* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 0.17-alt4
- fixed build with LTO

* Fri Apr 16 2021 Igor Vlasenko <viy@altlinux.org> 0.17-alt3
- exclude static lib

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2
- sync with debian
- fixed build (disabled gtk-doc; /usr/bin/gtkdoc-mktmpl no more)

* Fri Nov 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- initial import from debian.
- powered by debian2spec ;)
