Name: sakura
Version: 3.5.0
Release: alt2

Summary: Terminal emulator application
License: GPL
Group: Terminals
Url: https://launchpad.net/sakura

Source: https://launchpad.net/sakura/trunk/%version/+download/%name-%version.tar.bz2
Source1: sakura.conf

Patch0: sakura-2.3.0-no-tab-titles.patch
Patch1: sakura-system-config-file.patch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: cmake gcc-c++ libvte3-devel perl-podlators rpm-build-xdg
BuildRequires: desktop-file-utils libpixman-devel libharfbuzz-devel 

Requires: fonts-bitmap-terminus
Conflicts: libfreetype < 2.4.10-alt2

%description
Sakura is a lightweight and easy to use terminal emulator for X windowing 
system with some new ideas and features that makes it unique among X terminal 
emulators.

%prep
%setup -q
#patch0 -p2
#patch1 -p2

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

#Strange, that command doesn't work in %%clean section
rm -f %buildroot/%_docdir/%name/INSTALL

%files -f %name.lang
%doc AUTHORS INSTALL
%_bindir/%name
%_xdgconfigdir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/*
%_man1dir/*

%changelog
* Mon Dec 04 2017 Konstantin Artyushkin <akv@altlinux.org> 3.5.0-alt2
- new version

* Fri Sep 08 2017 Konstantin Artyushkin <akv@altlinux.org> 3.4.0-alt2
- new version

* Sat Apr 30 2016 Konstantin Artyushkin <akv@altlinux.org> 3.3.4-alt2
- new version

* Sat Apr 30 2016 Konstantin Artyushkin <akv@altlinux.org> 3.2.0-alt5
- fix of unpacked INSTALL file

* Sat May 16 2015 Konstantin Artyushkin <akv@altlinux.org> 3.2.0-alt4
- Remove patches

* Sat Apr 11 2015 Konstantin Artyushkin <akv@altlinux.org> 3.2.0-alt3
-  3.2.0 build 

* Tue Feb 26 2013 Mykola Grechukh <gns@altlinux.ru> 2.4.2-alt3
- REALLY fixed (closes: #28607)

* Tue Feb 19 2013 Mykola Grechukh <gns@altlinux.ru> 2.4.2-alt2
- default font fixed

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
