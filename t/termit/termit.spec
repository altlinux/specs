%define _unpackaged_files_terminate_build 1

Name: termit
Version: 2.5.0
Release: alt3.qa1

Summary: Minimalistic terminal emulator with tabs and encoding support
Url: http://code.google.com/p/termit/
License: GPLv2
Group: Terminals
Packager: Maxim Ivanov <redbaron@altlinux.org>

#http://termit.googlecode.com/files/%name-%version.tar.bz2
Source0: %name-%version.tar
Source1: %name-init.lua
Source2: ru.po

Patch0: %name-%version-%release.patch
Patch1: %name.desktop.icon.patch

Provides: xvt, %_bindir/xvt
PreReq: alternatives >= 0:0.2.0-alt0.12
BuildRequires: desktop-file-utils cmake libvte-devel gcc-c++ libtinfo-devel 
BuildRequires: libpixman-devel liblua5-devel libXau-devel

%description
Simple terminal emulator based on vte library. 

Features:
    * multiple tabs
    * switching encodings
    * sessions
    * configurable keybindings
    * embedded Lua
    * xterm-like dynamic window title 

%prep
%setup
%patch0 -p1
%patch1 -p1
cp %SOURCE2 po/ru.po

%build
cmake -DCMAKE_INSTALL_PREFIX=%_prefix .
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt %_bindir/termit 40
EOF

install -m644 -D %SOURCE1 %buildroot%_sysconfdir/xdg/termit/init.lua
sed -ie 's!@docdir@!%_docdir!g' %buildroot%_sysconfdir/xdg/termit/init.lua
sed -ie 's!@name@!%name!g' %buildroot%_sysconfdir/xdg/termit/init.lua
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=System \
	%buildroot%_desktopdir/termit.desktop

%files -f %name.lang
%_bindir/*
%_altdir/%name
%_desktopdir/*.desktop
%_docdir/%name
%_man1dir/*
%_sysconfdir/xdg/*

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.5.0-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for termit

* Sun Dec 12 2010 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt3
- Complete Russian translation (ALT #24672)

* Wed Sep 01 2010 Lenar Shakirov <snejok@altlinux.ru> 2.5.0-alt2
- Icon added to desktop file (ALT #23457)

* Fri Apr 23 2010 Mykola Grechukh <gns@altlinux.ru> 2.5.0-alt1
- new version

* Mon Jun 08 2009 Maxim Ivanov <redbaron at altlinux.org> 2.2.0-alt2
- fix missing buildreq 

* Sun Apr 19 2009 Maxim Ivaniv <redbaron at altlinux.org> 2.2.0-alt1
- 2.2.0

* Sat Sep 20 2008 Maxim Ivanov <redbaron at altlinux.org> 1.3.5-alt1
- Upstream version bump
- [patch] Default encodings hard-coded

* Sun Jun 8 2008 Maxim Ivanov <redbaron at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

