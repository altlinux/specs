
Summary: A library for managing OS information for virtualization
Name: libosinfo
Version: 0.3.0
Release: alt1

License: LGPLv2+
Group: System/Libraries

Source: %name-%version.tar
#Patch2: %name-%version-altlinux.patch

Url: https://fedorahosted.org/libosinfo/
BuildRequires: intltool >= 0.40.0
BuildRequires: gnome-common gtk-doc
BuildRequires: glib2-devel libgio-devel
BuildRequires: libsoup-devel >= 2.42
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.0.0
BuildRequires: libcheck-devel
BuildRequires: gobject-introspection-devel >= 0.9.0
BuildRequires: perl-podlators
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: gobject-introspection-devel
BuildRequires: pciids usbids

Requires: pciids usbids

%description
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package devel
Summary: Libraries, includes, etc. to compile with the libosinfo library
Group: Development/Other
Requires: %name = %version-%release

%description devel
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

Libraries, includes, etc. to compile with the libosinfo library

%package gir
Summary: GObject introspection data for the libosinfo library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the libosinfo library

%package gir-devel
Summary: GObject introspection devel data for the libosinfo library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the libosinfo library

%package devel-doc
Summary: Development package for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Contains developer documentation for %name.


%prep
%setup
#%%patch2 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	--enable-introspection \
	--with-usb-ids-path=%_datadir/misc/usb.ids \
	--with-pci-ids-path=%_datadir/misc/pci.ids \
	--enable-vala \
	--enable-gtk-doc

%make_build

chmod a-x examples/*.js examples/*.py

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.{a,la}

%find_lang --with-gnome %name

%check
%make check

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING.LIB NEWS README
%_bindir/*
%_man1dir/*
%dir %_datadir/%name
%dir %_datadir/%name/db
%dir %_datadir/%name/schemas
%_datadir/%name/db/*
%_datadir/%name/schemas/*
%_libdir/%name-*.so.*

%files devel
%doc examples/demo.js
%doc examples/demo.py
%_libdir/%name-*.so
%dir %_includedir/%name-1.0
%dir %_includedir/%name-1.0/osinfo
%_includedir/%name-1.0/osinfo/*.h
%_pkgconfigdir/%name-*.pc
%_datadir/vala/vapi/*

%files gir
%_libdir/girepository-1.0/*.typelib

%files gir-devel
%_datadir/gir-1.0/*.gir

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Tue Jun 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.12-alt1
- 0.2.12

* Tue Sep 30 2014 Alexey Shabalin <shaba@altlinux.ru> 0.2.11-alt2
- update altlinux support

* Fri Sep 12 2014 Alexey Shabalin <shaba@altlinux.ru> 0.2.11-alt1
- 0.2.11

* Tue Mar 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.2.10-alt1
- 0.2.10

* Tue Feb 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.2.9-alt0.git.68e147
- upstream snapshot 68e147f8f51c0cb76f4c6e4948350741e324dac0

* Thu Sep 19 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.8-alt1
- 0.2.8

* Fri Aug 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.7-alt1
- 0.2.7

* Thu Mar 21 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Tue Nov 13 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Wed Sep 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- 0.2.0
- add "ALT Linux 7.0.0 Centaurus" support

* Mon Apr 23 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1
- add ALTLinux iso's support

* Thu Mar 15 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus
