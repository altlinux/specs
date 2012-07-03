Packager: Alex Negulescu <alecs@altlinux.org>
Summary: Full-screen task-switcher
Name: skippy
Version: 0.5.0
Release: alt2
License: GPL
Group: Graphical desktop/KDE
Url: http://thegraveyard.org/skippy.php
Source: skippy-0.5.0.tar.bz2
Patch: skippy.patch
Source1: skippy.png
BuildRequires: imlib2-devel libXext-devel libXft-devel libXinerama-devel libXmu-devel pango-devel

%description
Skippy is a full screen pager for X11, not entirely unlike expocity and
Apple's Expose. It arranges snapshots of all windows on the current
desktop, allowing you to easily switch between applications. It doesn't
require a specific window manager, but requires NetWM or GNOME WM specs
compliance to work. The default hotkey is F11.

%prep
%setup
%patch -p1

%__cat <<EOF >skippy.desktop
[Desktop Entry]
Name=Skippy Screen Pager
Comment=Switch between applications visually
Encoding=UTF-8
Exec=skippy
Terminal=false
Type=Application
Icon=skippy.png
Categories=Application;System;
EOF

%build
%__make %{?_smp_mflags}

%install
%__rm -rf %buildroot
%__install -D -m0755 skippy %buildroot%_bindir/skippy
%__install -D -m0644 skippyrc-default %buildroot%_sysconfdir/skippyrc
%__install -D -m0644 %SOURCE1 %buildroot%_datadir/pixmaps/skippy.png
%__install -D -m0644 skippy.desktop %buildroot%_datadir/applnk/Utilities/skippy.desktop

%clean
%__rm -rf %buildroot

%files
%doc CHANGELOG COPYING skippyrc*
%config(noreplace) %_sysconfdir/skippyrc
%_bindir/skippy
%_datadir/applnk/Utilities/skippy.desktop
%_datadir/pixmaps/skippy.png

%changelog
* Wed Jan 12 2011 Alex Negulescu <alecs@altlinux.org> 0.5.0-alt2
- patched for x86_64
* Sun May 17 2009 Alex Negulescu <alecs@altlinux.org> 0.5.0-alt1
- Initial package
