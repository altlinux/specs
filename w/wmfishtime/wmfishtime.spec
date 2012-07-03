Name: wmfishtime
Version: 1.24
Release: alt1

Summary: WindowMaker clock dock-app featuring swimming fish
License: GPL
Group: Graphical desktop/Window Maker

Url: http://www.ne.jp/asahi/linux/timecop
Source0: %url/software/%name-%version.tar.gz
Source1: %name.desktop
Patch0: wmfishtime-1.24-gtk.patch
Patch1: wmfishtime-1.24-no_display.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Sep 25 2011 (-bi)
# optimized out: elfutils fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel pkg-config xorg-xproto-devel
BuildRequires: libgtk+2-devel

%description
Welcome to WMFishTime, winner of the "Best Waste Of CPU Power"
award! This is a dockable clock application for WMaker, BlackBox,
E, SawFish etc.

The features include gradient backdrop, anti-aliased hour,
minute, second hands alpha-blended bubbles, real-time sprite
engine, precision accuracy, and shows if you have unread mail
(in the form of swaying weed blocking the day/month numbers).

Well, this is just your standard time dockapp. Top part has the
clock face, bottom part has day of the week, followed by day,
followed by month. Yellow hand counts seconds, green hand counts
minutes, red hand counts hours. Few seconds after startup there
are at least 32 bubbles floating up behind the clock face. There
are 4 fishes randomly swimming back and forth. If you move your
mouse inside the dockapp window, the fish will get scared and run
away. If you compiled in mail checking (default), then whenever
you get new mail in the file pointed to by the $MAIL variable, it
will display green weed partially blocking the day/month counter,
to remind you to read your mail. If $MAIL is not set, nothing
happens.

%prep
%setup
%patch0 -p1
%patch1 -p0
sed -i 's,/usr/X11R6,%prefix,g' Makefile

%build
export CFLAGS="$CFLAGS %optflags \
	-funroll-loops \
	-fexpensive-optimizations \
	-fomit-frame-pointer"
%make_build

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %name.1 %buildroot%_man1dir/%name.1
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%doc ALL_I_GET_IS_A_GRAY_BOX AUTHORS ChangeLog CODING README
%_man1dir/*
%_bindir/*
%_desktopdir/*

# TODO:
# - http://vlad.minisat.ro/~vlad2/dockapps/releases/wmfishtime-1.25.tar.bz2
#   + usleep back to 20ms (or the fish gets too lazy)
#   + tweak too bright clock face bullets down
#   + (ideally) move second hand knob to a runtime option

%changelog
* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.24-alt1
- built for ALT Linux
- gentoo patchset works better for me than debian's one
