Name: lxdream
Version: 0.9.1
Release: alt2.qa3

Summary: Lxdream is an emulator for the Sega Dreamcast system
License: GPL

Group: Emulators

Url: http://www.lxdream.org

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: %name-%version.tar.gz
#Source1: %name.png
Patch0: %name-0.9.1-alt-glib2-2.32.0.patch
Patch1: %name-0.9.1-alt-DSO.patch

# Automatically added by buildreq on Tue Oct 28 2008 (-bi)
BuildRequires: esound-devel libalsa-devel libgtk+2-devel libGL-devel subversion fontconfig-devel glib2-devel
BuildRequires: libatk-devel libaudiofile-devel libcairo-devel libfreetype-devel libgtk+2-common libgtk+2-common-devel
BuildRequires: libpango-devel libpng-devel pkg-config xorg-x11-proto-devel zlib-devel libX11-devel perl-podlators
BuildRequires: liblirc-devel
BuildRequires: libSDL-devel

%description
Lxdream is an emulator for the Sega Dreamcast system, running on Linux and OS X. While it is still in heavy development (and many features are buggy or unimplemented), it is capable of running most demos and some games.

%prep
%setup -q
%patch0 -p2
%patch1 -p2

%build
%configure
%make

%install
%makeinstall

#debian menu remnant
echo "Comment=Lxdream is an emulator for the Sega Dreamcast" >> %buildroot%_desktopdir/%name.desktop

%find_lang %name


%files -f %name.lang
%doc README ChangeLog
%_bindir/*
%_datadir/pixmaps/%name
%_datadir/pixmaps/%name.png
%_desktopdir/%name.desktop
%_libdir/%name/*.so
%_sysconfdir/lxdreamrc
%_man1dir/*
#_docdir/%name
#_iconsdir/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2.qa3
- Fixed build

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2.qa2
- Fixed build with new glib2

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2.qa1
- NMU: dropped debian menu; fixed build; added BR: lirc and SDL

* Thu Dec 23 2010 Ilya Mashkin <oddity@altlinux.ru> 0.9.1-alt2
- fix build

* Sat Sep 19 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Tue Oct 28 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9-alt1
- Initial Build

