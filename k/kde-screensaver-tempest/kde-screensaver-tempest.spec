%define		srcname tempest
Name:		kde-screensaver-%srcname
Version:	20070726
Release:	alt1.1
Summary:	Tempest Screensaver for KDE
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.personal.utulsa.edu/~dan-guernsey/
Source0:	http://www.personal.utulsa.edu/~dan-guernsey/dist/%srcname.tar.gz
Patch0:		%srcname-alt_categories.diff
Packager:	Motsyo Gennadi <drool@altlinux.ru>

Requires:	kdebase-wm

# Automatically added by buildreq on Mon Dec 01 2008 (-bi)
BuildRequires: libGL-devel libX11-devel

%description
Tempest is an xscreensaver hack based on a
physical model where particles are attracted
to their 8 neightbors. With some tweaking,
it can produce some very neat effects.

%prep
%setup -q -c -n %srcname
%patch0 -p1

%build
gcc %optflags -o tempest tempest.c -lGL -lm

%install
%__install -Dp -m 0755 %srcname %buildroot%_bindir/%srcname.kss
%__install -Dp -m 0644 %srcname.desktop %buildroot/%_datadir/applnk/System/ScreenSavers/%srcname.desktop

%files
%doc README
%_bindir/%srcname.kss
%_datadir/applnk/System/ScreenSavers/%srcname.desktop

%changelog
* Mon Dec 01 2008 Motsyo Gennadi <drool@altlinux.ru> 20070726-alt1.1
- fix BuildRequires (new libX*-devel)

* Sat Sep 08 2007 Motsyo Gennadi <drool@altlinux.ru> 20070726-alt1
- initial build for ALT Linux
