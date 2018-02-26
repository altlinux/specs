Name: autocutsel
Version: 0.9.0
Release: alt1.1

Summary: Autocutsel synchronizes the two copy/paste buffers mainly used by X applications. It also unifies "clipboards" between VNC servers and Windows.
License: GPL
Group: System/X11
Url: http://www.nongnu.org/autocutsel

Source: %name-%version.tar.gz
Source1: %name.sh

BuildRequires: libX11-devel libXaw-devel libXt-devel libXmu-devel

%description
Autocutsel tracks changes in the server's cutbuffer and CLIPBOARD selection.
When the CLIPBOARD is changed, it updates the cutbuffer. When the cutbuffer 
is changed, it owns the CLIPBOARD selection. The cutbuffer and CLIPBOARD 
selection are always synchronized. Since the VNC client synchronizes the 
Windows' clipboard and the server's cutbuffer, all three "clipboards" are 
always kept synchronized. When you copy some text in Windows, the cutbuffer
and the CLIPBOARD selection are updated. When you copy text on the server
using either the cutbuffer or the CLIPBOARD selection, the Windows's clipboard
is always updated.

You can also use autocutsel to track the PRIMARY selection to copy text when
it's selected. To do this, simply run autocutsel with the arguments "-s PRIMARY"

Some softwares (like Open Office Writer) have trouble when the PRIMARY selection
is requested before the mouse button is released. As a workaround, you can run
autocutsel with the "-buttonup" option and it will only get the selection when
the first mouse button is not pressed.

%package autostart
Summary: This package autostarts the %name utility in the user's X session.
Group: System/X11
Requires: %name = %version

%description autostart
%summary

%prep
%setup

%build
%configure
%make_build

%install
mkdir -p %buildroot%_x11sysconfdir/xinit.d/
%make_install DESTDIR=%buildroot install
cp %SOURCE1 %buildroot%_x11sysconfdir/xinit.d/
chmod 755 %buildroot%_x11sysconfdir/xinit.d/%name.sh

%files
%doc README TODO AUTHORS COPYING INSTALL ChangeLog NEWS
%_bindir/*

%files autostart
%_x11sysconfdir/xinit.d/*

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Wed Jun 04 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.9.0-alt1
- First build for Sisyphus
