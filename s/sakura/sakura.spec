Name: sakura
Version: 2.4.2
Release: alt1

Summary: Terminal emulator application
License: GPL
Group: Terminals
Url: http://www.pleyades.net/david/sakura.php

Source: http://www.pleyades.net/david/projects/sakura/sakura-%version.tar.bz2
Source1: sakura.conf

Patch0: sakura-2.3.0-no-tab-titles.patch
Patch1: sakura-system-config-file.patch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: cmake gcc-c++ libvte-devel perl-podlators rpm-build-xdg
BuildRequires: desktop-file-utils

%description
Sakura is a lightweight and easy to use terminal emulator for X windowing 
system with some new ideas and features that makes it unique among X terminal 
emulators.

%prep
%setup -q
#patch0 -p2
%patch1 -p2

sed '/POD2MAN/ s,-u ,,' -i CMakeLists.txt

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix
%make_build

%install
%makeinstall DESTDIR=%buildroot
install -m644 -D %SOURCE1 %buildroot%_xdgconfigdir/%name/%name.conf
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=System \
	%buildroot%_desktopdir/sakura.desktop

%files -f %name.lang
%doc AUTHORS
%_bindir/%name
%_xdgconfigdir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/*
%_man1dir/*

%changelog
* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 2.4.2-alt1
- new version.

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.4.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for sakura

* Mon Feb 14 2011 Mykola Grechukh <gns@altlinux.ru> 2.4.0-alt1
- new version. Manpage fixed

* Wed Jun 09 2010 Mykola Grechukh <gns@altlinux.ru> 2.3.8-alt1
- new version. Default configfile added

* Tue Apr 13 2010 Mykola Grechukh <gns@altlinux.ru> 2.3.7-alt2
- build fixed

* Tue Apr 13 2010 Mykola Grechukh <gns@altlinux.ru> 2.3.7-alt1
- new version

* Tue May 26 2009 Nick S. Grechukh <gns@altlinux.org> 2.3.3-alt1
- new version

* Thu Oct 09 2008 Nick S. Grechukh <gns@altlinux.org> 2.3.0-alt2
- new version

* Mon Aug 04 2008 Nick S. Grechukh <gns@altlinux.org> 2.2.0-alt1
- first build
