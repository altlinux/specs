
Summary: A library for managing OS information for virtualization
Name: libosinfo
Version: 0.1.1
Release: alt1
License: LGPLv2+
Group: System/Libraries

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch2: %name-%version-altlinux.patch

Url: https://fedorahosted.org/libosinfo/
BuildRequires: gnome-common gtk-doc
BuildRequires: glib2-devel libgio-devel
BuildRequires: libsoup-devel libsoup-gnome-devel
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libcheck-devel
BuildRequires: gobject-introspection-devel >= 0.9.0
BuildRequires: perl-podlators
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: gobject-introspection-devel
BuildRequires: pciids usbids

Requires: pciids usbids
Requires: udev

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
%patch -p1
%patch2 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	--enable-introspection \
	--enable-vala \
	--enable-udev \
	--enable-gtk-doc

%make_build

chmod a-x examples/*.js examples/*.py

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.{a,la}

# symlinks to *.ids
ln -sf ../../misc/usb.ids %buildroot%_datadir/%name/db/usb.ids
ln -sf ../../misc/pci.ids %buildroot%_datadir/%name/db/pci.ids

%check
%make check

%files
%doc AUTHORS ChangeLog COPYING.LIB NEWS README
%_bindir/*
%_man1dir/*
%dir %_datadir/%name
%dir %_datadir/%name/db
%dir %_datadir/%name/schemas
%_datadir/%name/db/*
%_datadir/%name/schemas/*
%_libdir/%name-*.so.*
/lib/udev/rules.d/95-osinfo.rules

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
* Mon Apr 23 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- 0.1.1
- add ALTLinux iso's support

* Thu Mar 15 2012 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus
