# TODO: build with unity

Name: pantheon-files
Version: 0.1.5
Release: alt2

Summary: The file manager of the Pantheon desktop
License: GPLv3
Group: File tools
Url: https://launchpad.net/pantheon-files

Source0: %name-%version.tgz

Patch0: pantheon-files-0.1.4-alt-fix-pkgconfig-file.patch

Packager: Igor Zubkov <icesik@altlinux.org>

#Depends: tumbler
#Recommends: contractor
#Suggests: tumbler-plugins-extra

BuildRequires: cmake vala libsqlite3-devel libgtk+3-devel
BuildRequires: libgee-devel libpixman-devel libgranite-devel
BuildRequires: libgail3-devel libdbus-glib-devel libnotify-devel
BuildRequires: libXdmcp-devel libGConf-devel libXdamage-devel
BuildRequires: libXxf86vm-devel libharfbuzz-devel libpng-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel
BuildRequires: libXcursor-devel libXcomposite-devel
BuildRequires: libxkbcommon-devel libwayland-cursor-devel
BuildRequires: at-spi2-atk-devel gcc-c++ libgranite-vala

%description
Files is well-designed with a focus on speed, simplicity and ease of use.

%package devel
Summary: Development files for pantheon-files
Group: Development/C

Requires: %name = %version-%release

%description devel
Development files for pantheon-files.

%package vala
Summary: Vala language bindings for the pantheon-files
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides Vala language bindings for the pantheon-files.

%prep
%setup -q
%patch0 -p1

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%ifarch x86_64
mkdir -p %buildroot%_libdir/
mv %buildroot/usr/lib/* %buildroot%_libdir/
%endif

%find_lang %name

%files -f %name.lang
%doc AUTHORS HACKING INSTALL README
%_bindir/*
%_libdir/*.so.*
%dir %_libdir/pantheon-files
%_libdir/pantheon-files/
%_datadir/applications/pantheon-files.desktop
%_datadir/dbus-1/services/marlin.service
%_datadir/glib-2.0/schemas/org.pantheon.files.gschema.xml
%dir %_datadir/pantheon-files
%_datadir/pantheon-files/
%_datadir/pixmaps/pantheon-files/thumbnail_frame.png

%files devel
%_libdir/*.so
%dir %_includedir/marlincore
%_includedir/marlincore/*.h
%_pkgconfigdir/marlincore.pc

%files vala
%_datadir/vala/vapi/marlincore-C.vapi
%_datadir/vala/vapi/marlincore.deps
%_datadir/vala/vapi/marlincore.vapi

%changelog
* Mon Nov 11 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt2
- Make build more verbose

* Sat Oct 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt1
- 0.1.4 -> 0.1.5

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt2
- Fix pkgconfig file

* Mon Sep 09 2013 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt1
- 0.1.3 -> 0.1.4

* Sat Aug 24 2013 Igor Zubkov <icesik@altlinux.org> 0.1.3-alt1
- build for Sisyphus

