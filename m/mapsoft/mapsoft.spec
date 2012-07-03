Name: mapsoft
Version: 20120625
Release: alt1
License: GPL
Summary: mapsoft - programs for working with maps and geodata
Group: Sciences/Geosciences
Url: http://github.org/ushakov/mapsoft
Packager: Vladislav Zavjalov <slazav@altlinux.org>

Source: %name-%version.tar

BuildRequires: boost-devel gcc-c++ libcurl-devel libzip-devel zlib-devel
BuildRequires: libcairomm-devel libpixman-devel libgtkmm2-devel
BuildRequires: libpng-devel libjpeg-devel libtiff-devel
BuildRequires: libusb-devel libyaml-devel libxml2-devel proj-devel
BuildRequires: python-devel scons swig m4
BuildRequires: /usr/bin/gs netpbm transfig ImageMagick-tools /usr/bin/pod2man

%package tools
Summary: mapsoft-tools - rarely-used tools from mapsoft package
Group: Sciences/Geosciences
Requires: %name = %version-%release

%package vmap
Summary: mapsoft-vmap - programs for working with vector maps
Group: Sciences/Geosciences
Requires: %name = %version-%release

%description
mapsoft - programs for working with maps and geodata

%description tools
mapsoft-tools - rarely-used tools from mapsoft package

%description vmap
mapsoft-vmap - programs for working with vector maps

%prep
%setup -q

%build
scons -Q minimal=1

%install
scons -Q minimal=1 -Q prefix=%buildroot install

%files
%_bindir/mapsoft_convert
%_bindir/mapsoft_mapview
%_mandir/man1/mapsoft_convert.1.gz
%_mandir/man1/mapsoft_mapview.1.gz

%files tools
%_bindir/catfig
%_bindir/catmp
%_bindir/convs_*
%_bindir/mapsoft_toxyz
%_bindir/mapsoft_geofig
%_bindir/mapsoft_mkmap
%_mandir/man1/mapsoft_geofig.1.gz
%_libdir/gimp/2.0/plug-ins/map-helper.py

%files vmap
%_bindir/mapsoft_vmap
%_bindir/vmap_copy
%_bindir/vmap_render
%dir %_datadir/mapsoft
%_datadir/mapsoft/*
%_datadir/xfig/Libraries/*
%_mandir/man1/mapsoft_vmap.1.gz

%changelog
* Mon Jun 25 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120625-alt1
- current snapshot
 - simple navigation mode
 - support for tiled maps, some examples
 - faster map rescaling
 - support for finnish KKJ maps
 - add map-helper and mapsoft_mkmap to mapsoft-tools package
 - increase thickness of viewer marks

* Wed Jun 20 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120620-alt1
- current snapshot (more bugs fixed)

* Wed Jun 20 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120619-alt1
- build current snapshot (some bugs fixed)

* Sun Jun 17 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120617-alt1
- build current snapshot

* Sun May 06 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120506-alt1
- build current snapshot

* Mon Mar 05 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120304-alt1
- build current snapshot

* Thu Feb 16 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120222-alt1
- build current snapshot (16-02-2012)

* Sun Feb 12 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120221-alt1
- build current snapshot (12-02-2012)

* Wed Feb 08 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120220-alt1
- build current snapshot (08-02-2012)

* Tue Jan 10 2012 Vladislav Zavjalov <slazav@altlinux.org> 20120110-alt1
- build current snapshot

* Tue Nov 22 2011 Vladislav Zavjalov <slazav@altlinux.org> 20111122-alt1
- build current snapshot

* Thu Nov 19 2009 Vladislav Zavjalov <slazav@altlinux.org> 20091119-alt1
- first build for altlinux

