%define oname ipod-sharp

Name: lib%oname
Version: 0.8.5
Release: alt1

Summary: Library to control the iPod database
License: LGPLv2
Group: Development/Other
Url: http://banshee-project.org/index.php/Ipod-sharp

Source: http://banshee-project.org/files/ipod-sharp/%oname-%version.tar.bz2
Patch: ipod-sharp-0.8.1-alt-fix-pkgconfig.patch

BuildRequires: libgtk-sharp2
BuildRequires: ndesk-dbus-glib-devel
BuildRequires: podsleuth-devel
BuildRequires: /proc
BuildPreReq: rpm-build-mono mono-devel mono-mcs mono-nunit-devel
Requires: podsleuth

%description
ipod-sharp is a library that allows manipulation of the iTunesDB used
in Apple iPod devices.  Currently it supports adding/removing songs
and manipulating playlists.

%package devel
Summary: Development files %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%package doc
Summary: Development documentation for %name
Group: Documentation
Provides: %name-monodoc = %version-%release
Obsoletes: %name-monodoc
BuildPreReq: monodoc-devel
Requires: monodoc
BuildArch: noarch

%description doc
This package contains the API documentation for the %name in
Monodoc format.

%prep
%setup -q -n %oname-%version
%patch -p1
subst "s|^ipoddir *= \$(prefix)/lib/ipod-sharp|ipoddir = %_monodir/ipod-sharp|" \
	src/Makefile.{am,in} \
	src/Firmware/Makefile.{am,in}
subst "s|^ipodsharpdir *= \$(prefix)/lib/ipod-sharp|ipodsharpdir = %_monodir/ipod-sharp|" \
	ui/Makefile.{am,in}

%build
%configure
%make

%install
%make_install DESTDIR=%buildroot install
rm -f %buildroot%_monodir/ipod-sharp/*

gacutil -i src/ipod-sharp.dll -f -package ipod-sharp -root %buildroot/usr/lib
gacutil -i src/Firmware/ipod-sharp-firmware.dll -f -package ipod-sharp -root %buildroot/usr/lib
gacutil -i ui/ipod-sharp-ui.dll -f -package ipod-sharp -root %buildroot/usr/lib

%files
%doc README AUTHORS NEWS ChangeLog COPYING
%_monodir/ipod-sharp
%_monogacdir/*

%files devel
%_pkgconfigdir/*

%files doc
%_monodocdir/*

%changelog
* Sat Nov 21 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2
- move pkgconfig files from main to devel package

* Thu Nov 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt4
- rebuild with new macros _monodocdir
- remove post scripts
- rename package %name-monodoc to %name-doc

* Thu Nov 13 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt3
- real build for x86_64

* Wed Nov 12 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt2
- rebuild for x86_64 (with fixed podsleuth)

* Sun Oct 26 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- initial build for ALTLinux

