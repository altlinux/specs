Name: xbelld
Version: 0.3.3
Release: alt5
Summary: X11 virtual PC speaker

Group: Graphical desktop/Other

License: GPLv3+
Url: http://code.google.com/p/xbelld/
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sun Oct 24 2010 (-bb)
BuildRequires: libX11-devel libalsa-devel

%description
xbelld is a tiny utility to aid people who either don't like the default PC
speaker beep, or (like me) use an ALSA driver that doesn't yet have support for
the PC speaker (e.g. the AD1981 chipset in the snd_hda_intel driver, as of
2008-04-06).

xbelld performs a given action every time the X bell is rung. The actions
xbelld can currently perform include running a specified program, emulating the
PC speaker beep using your sound card (default), or playing a PCM encoded WAVE
file.

%prep
%setup -q
%patch -p1

%build
%make_build

%install
install -D -m755 xbelld %buildroot%_bindir/xbelld
install -D -m644 xbelld.1 %buildroot%_man1dir/xbelld.1
%files
%_bindir/xbelld
%_man1dir/xbelld.*

%changelog
* Mon Jun 18 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.3-alt5
- fix build

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3.3-alt4
- fix build

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3.3-alt3
- fix build

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3.3-alt2
- rebuild

* Mon Jun 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3.3-alt1
- first build for Sisyphus
