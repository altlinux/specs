
Summary: A library for managing OS information for virtualization
Name: libosinfo
Version: 1.7.1
Release: alt1

License: LGPLv2+
Group: System/Libraries

Source: %name-%version.tar
#Patch2: %name-%version-altlinux.patch

Url: https://libosinfo.org
BuildRequires(pre): meson >= 0.49.0
BuildRequires: gettext >= 0.19.8
BuildRequires: gtk-doc
BuildRequires: pkgconfig(glib-2.0) >= 2.44 pkgconfig(gobject-2.0) pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires: pkgconfig(libxslt) >= 1.0.0
BuildRequires: gobject-introspection-devel >= 0.9.7
BuildRequires: perl-podlators
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: pciids usbids
BuildRequires: osinfo-db

Requires: pciids usbids
Requires: osinfo-db osinfo-db-tools

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
%meson \
    -Denable-gtk-doc=true \
    -Denable-tests=true \
    -Dwith-usb-ids-path=%_datadir/misc/usb.ids \
    -Dwith-pci-ids-path=%_datadir/misc/pci.ids \
    -Denable-introspection=enabled \
    -Denable-vala=enabled

%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
export LD_LIBRARY_PATH=$(pwd)/%{__builddir}/osinfo
%meson_test

%files -f %name.lang
%doc COPYING.LIB NEWS README
%_bindir/*
%_man1dir/*
%_libdir/%name-*.so.*

%files devel
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
* Wed Dec 04 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.1-alt1
- new version 1.7.1

* Fri Aug 23 2019 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- new version 1.6.0

* Wed May 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Sat Mar 02 2019 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Sat Feb 02 2019 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Oct 11 2017 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0

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
