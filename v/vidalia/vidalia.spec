Name: vidalia
Version: 0.2.9
Release: alt2
Summary: GUI controller for the Tor Onion Routing Network
Group: Networking/Other
License: GPLv2+
Url: https://www.torproject.org/vidalia/
Packager: Mykola Grechukh <gns@altlinux.ru>

Source: https://www.torproject.org/%name/dist/%name-%version.tar
Source1: %name.desktop

BuildRequires(pre): rpm-macros-qt4

# Automatically added by buildreq on Mon Sep 27 2010 (-bb)
BuildRequires: cmake desktop-file-utils gcc-c++ qt4-designer

Requires: tor
Requires: icon-theme-hicolor

%description
Vidalia is a cross-platform controller GUI for Tor, built using the Qt
framework. Vidalia allows you to start and stop Tor, view the status of
Tor at a glance, and monitor Tor's bandwidth usage. Vidalia also makes
it easy to contribute to the Tor network by helping you setup a Tor
server, if you wish.

%prep
%setup

%build
export PATH=%_qt4dir/bin:$PATH
# fix DSOLinking
%__subst '/torcontrol/a \ \ z' src/vidalia/CMakeLists.txt
%cmake

%make_build -C BUILD

%install
%make_install install INSTALL="install -p" DESTDIR=%buildroot -C BUILD

install -Dpm0644 doc/%name.1 \
	%buildroot%_man1dir/%name.1

desktop-file-install --dir %buildroot%_desktopdir %SOURCE1

chmod -x contrib/*

%files
%doc CHANGELOG CREDITS LICENSE* README
%doc contrib
%_bindir/%name
%_man1dir/%{name}*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Mon Nov 01 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.9-alt2
- build fixed (prereq: rpm-build-qt4=>rpm-macros-qt4)

* Mon Sep 27 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.9-alt1
- first build for ALT Linux

* Wed May 26 2010 Chen Lei <supercyper@163.com> - 0.2.9-1
- New upstream release

* Wed Apr 21 2010 Chen Lei <supercyper@163.com> - 0.2.8-1
- New upstream release
- Remove -doc subpackage

* Sun Jan 31 2010 Chen Lei <supercyper@163.com> - 0.2.7-2
- Add contrib to -doc subpackage

* Sun Jan 31 2010 Chen Lei <supercyper@163.com> - 0.2.7-1
- New upstream release

* Wed Sep 02 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.15-1
- New upstream release

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.1.14-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.14-1
- New upstream release

* Mon Jun 01 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.13-2
- Merge builds for fedora and epel

* Mon Jun 01 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.13-1
- Update to 0.1.13
- Adjust to fedora and epel

* Sun Apr 06 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.12-1
- New upstream release
- Correct typo in URL
- Add R: hicolor for new handling of icons
- Add update-icon-cache sniplet
- Use summary of upstream for Desktopfile and in spec file
- Create doxygen-documentations

* Sun Feb 15 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.10-2
- Correct Qt in Summary
- Correct Qt in desktop-file-source
- Add a german Translation in the desktop-file-source
- Using CMAKE-macro instead of cmake
- Add more files to more documentation

* Tue Feb 10 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.1.10-1
- Initial Package build
