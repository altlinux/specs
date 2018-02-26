Name: x11vnc
Version: 0.9.12
Release: alt3

%def_without avahi

Summary: VNC server for real X displays
License: GPL
Group: Networking/Remote access
Url: http://www.karlrunge.com/x11vnc/
Packager: Maxim Ivanov <redbaron@altlinux.org>

Source: %name-%version.tar
Patch: libvncserver-c656b381fd8158aa73173c157b1492d1014e13f0.patch

BuildRequires: libjpeg-devel zlib-devel libssl-devel libXdamage-devel libXinerama-devel libXrandr-devel libXtst-devel libXt-devel
%if_with avahi
BuildRequires: libavahi-devel
%endif

%description
x11vnc allows one to remotely view and interact with real X displays
(i.e. a display corresponding to a physical monitor, keyboard, and mouse)
with any VNC viewer. In this way it plays the role for Unix/X11 that
WinVNC plays for Windows.

%prep
%setup
%patch -p1

# rfb carries around an ancient keysym.h from year 98. When included together
# with the current keysymdef.h, it generates loads of warnings.
# However, a careful comparison of the headers shows that replacing
# the old one with the new one will only introduce new macros, without
# changing or removing old ones. Therefore it should be safe to do this:
rm rfb/keysym.h
echo '#include <X11/keysym.h>' >rfb/keysym.h

%build
%configure --without-uinput
%make_build

%install
%makeinstall

%files
%_bindir/%name
%_man1dir/%name.*
%_datadir/%name
%_desktopdir/*
%doc README NEWS

%changelog
* Sun Mar 27 2011 Terechkov Evgenii <evg@altlinux.org> 0.9.12-alt3
- Fix build with sisyphus_check 0.8.20-alt1

* Sat Oct  2 2010 Terechkov Evgenii <evg@altlinux.org> 0.9.12-alt2
- Rebuild with libssl10

* Sun Sep 12 2010 Terechkov Evgenii <evg@altlinux.org> 0.9.12-alt1
- 0.9.12

* Wed Apr 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.9-alt2
- fixed starting Xvfb 1.8

* Sat Mar 13 2010 Terechkov Evgenii <evg@altlinux.ru> 0.9.9-alt1
- Patch from upstream git to fix "will always overflow destination" on x86_64
- 0.9.9

* Fri Jun 05 2009 Ivanov Maxim <redbaron@altlinux.org> 0.9.8-alt1
- Bump to 0.9.8 

* Wed Jul 11 2007 Alex V. Myltsev <avm@altlinux.ru> 0.9.2-alt1
- 0.9.1:
- - "-users sslpeer": authentication by unix username in SSL cert id
- - SSL connections in the Java viewer
- - misc bug fixes
- 0.9.2: supports building with external libvncserver (not used yet)

* Fri Apr 20 2007 Alex V. Myltsev <avm@altlinux.ru> 0.9-alt1
- 0.9: avahi advertising, ultravnc extensions, more minor features;
- TightVNC file transfer now off by default

* Mon Feb 19 2007 Alex V. Myltsev <avm@altlinux.ru> 0.8.4-alt1
- 0.8.4: VNC reflector, X session autocreation.

* Sat Nov 25 2006 Alex V. Myltsev <avm@altlinux.ru> 0.8.3-alt1
- 0.8.3: allows unixpw authentication, can rotate screen, etc.

* Thu Jul 20 2006 Alex V. Myltsev <avm@altlinux.ru> 0.8.2-alt1
- New version (display autosearch, kbd/mouse grabbing etc).
- Now built with OpenSSL.

* Tue Mar 28 2006 Alex V. Myltsev <avm@altlinux.ru> 0.8-alt1
- New version (file transfer support, some minor features, bug fixes).

* Mon Aug 29 2005 Alex V. Myltsev <avm@altlinux.ru> 0.7.2-alt1
- First build for ALT Linux.

