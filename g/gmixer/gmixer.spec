Name: gmixer
Version: 1.3
Release: alt3.1.1
License: GPLv3
Summary: Simple Gtk/GStreamer volume control applet
Packager: Egor Glukhov <kaman@altlinux.org>
Group: Sound
Url: https://launchpad.net/gmixer
Source0: %name-%version.tar
BuildRequires: libgtk+2-devel python-module-pygtk-devel python-module-pygtk-libglade
Requires: python-module-pygtk-libglade

%description
GMixer is a simple gtk/gstreamer audio mixer, armed to work with light desktop manager.

Features:
 - supports all mixer plugins of gstreamer (alsa/oss/pulseaudio/...)
 - tray icon support
 - supports special keys of multimedia keyboard

%prep
%setup

%build
%python_build

%install
%python_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%python_sitelibdir/*

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt3.1
- Rebuild with Python-2.7

* Wed Nov 10 2010 Egor Glukhov <kaman@altlinux.org> 1.3-alt3
- Fixed crash on startup when no controllable channels are available

* Sat Nov 06 2010 Egor Glukhov <kaman@altlinux.org> 1.3-alt2
- Added dependency on python-module-pygtk-libglade (Closes: 24320)

* Thu Jun 4 2010 Egor Glukhov <kaman@altlinux.org> 1.3-alt1
- initial build for Sisyphus
