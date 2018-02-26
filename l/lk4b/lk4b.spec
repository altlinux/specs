Name: lk4b
Version: 20080706
Release: alt2

Summary: Lock Keyboard For Baby
License: %gpl2plus
Group: Accessibility
Url: http://csincock.customer.netspace.net.au/lock-keyboard-for-baby.htm
Packager: Timur Batyrshin <erthad@altlinux.org>

BuildArch:noarch

Source0: %name.pl
Source1: %name.desktop
Source2: %name.png

BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sat Oct 10 2009 (-bi)
BuildRequires: ImageMagick-tools perl-Gtk2

%description
Lock-keyboard-for-Baby (lk4b) is a small program which locks your keyboard
but leaves your mouse free. I wrote it because my niece likes to bash away
at my keyboard whenever she sees me sit down at it.

When started, lock-keyboard-for-baby opens a small window which grabs the
keyboard and echos keys which are typed. By default, it tells you what to
type to quit ("Quit Now"). Unlike a screensaver, your screen is not blocked
and the mouse still partially works, so you can still see what is on your
screen - keep watching tv / video and/or read a document using the mouse to
scroll.

%build
convert %SOURCE2 -resize "48x48" %name-48x48.png

%install
install -Dpm0755 %SOURCE0 %buildroot%_bindir/%name
install -Dpm0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -Dpm0644 %SOURCE2 %buildroot%_iconsdir/hicolor/96x96/apps/%name.png
install -Dpm0644 %name-48x48.png %buildroot%_liconsdir/%name.png

%files
%_bindir/*
%_desktopdir/*
%_liconsdir/*
%_iconsdir/hicolor/96x96/apps/*

%changelog
* Sun Oct 11 2009 Timur Batyrshin <erthad@altlinux.org> 20080706-alt2
- arch fixed

* Sat Oct 10 2009 Timur Batyrshin <erthad@altlinux.org> 20080706-alt1
- Initial build

