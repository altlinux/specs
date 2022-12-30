%define        _unpackaged_files_terminate_build 1

Name:          termit
Version:       3.1
Release:       alt2
Summary:       Minimalistic terminal emulator with tabs and encoding support
Url:           https://github.com/nonstop/termit/wiki
Vcs:           https://github.com/nonstop/termit.git
License:       GPLv3
Group:         Terminals
Packager:      Maxim Ivanov <redbaron@altlinux.org>

Source0:       %name-%version.tar
Source1:       %name-init.lua
Patch:         ru.po.patch
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: desktop-file-utils
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgtk+3-devel
BuildRequires: libvte3-devel
BuildRequires: libtinfo-devel
BuildRequires: libpixman-devel
BuildRequires: libXau-devel
BuildRequires: liblua5.3-devel

Requires(pre): alternatives >= 0:0.2.0-alt0.12
Requires:      fonts-ttf-paratype-pt-mono

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
%patch

%build
cmake -DCMAKE_INSTALL_PREFIX=%_prefix .
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt %_bindir/termit 100
EOF

install -m644 -D %SOURCE1 %buildroot%_sysconfdir/xdg/termit/rc.lua
sed -ie 's!@docdir@!%_docdir!g' %buildroot%_sysconfdir/xdg/termit/rc.lua
sed -ie 's!@name@!%name!g' %buildroot%_sysconfdir/xdg/termit/rc.lua
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
%_metainfodir/%name.metainfo.xml

%changelog
* Fri Dec 30 2022 Pavel Skrylev <majioa@altlinux.org> 3.1-alt2
- ! termit init lua-script

* Thu Nov 26 2020 Pavel Skrylev <majioa@altlinux.org> 3.1-alt1.2
- ! alternatives files for termit to proper format

* Mon Nov 23 2020 Pavel Skrylev <majioa@altlinux.org> 3.1-alt1.1
- - invalid provides
- ! invalid alternatives files for termit (closes #39338)

* Thu Apr 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.1-alt1
- ^ 2.5.0 -> 3.1
- * configuration lua-file

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt3.qa2
- NMU: rebuild with new lua 5.1

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

