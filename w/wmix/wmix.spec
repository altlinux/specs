Name: wmix
Version: 3.1
Release: alt3

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Nice mixer dockapp for WindowMaker
License: GPLv2+
Group: Graphical desktop/Window Maker

URL: http://www.ne.jp/asahi/linux/timecop
Source: %url/software/wmix-%version.tar.gz
Source1: wmix.1
Source2: wmix.menu
Source3: sample.wmixrc-ALT

# Automatically added by buildreq on Wed Dec 17 2008
BuildRequires: libXext-devel libXpm-devel

%description
WMix is a dockapp mixer (OSS API) with OSD and mouse wheel
support, among other features. Look and feel can be customized;
volume can be regulated by sending signals to wmix.

You might want to wrap it with aoss(1) if using ALSA.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
install -pDm0755 wmix %buildroot%_bindir/wmix
install -pDm0644 %SOURCE1 %buildroot%_man1dir/wmix.1
install -pDm0644 %SOURCE2 %buildroot%_menudir/wmix.menu
install -pm0644  %SOURCE3 .

%files
%doc NEWS README sample.wmixrc sample.wmixrc-ALT
%_bindir/*
%_man1dir/*
%_menudir/*

%changelog
* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 3.1-alt3
- fixed menu file not to reference obsolete binary location
  (closes: #23565)
  + thanks NotHAM

* Wed Dec 17 2008 Victor Forsyuk <force@altlinux.org> 3.1-alt2
- Remove obsolete install time scripts.

* Fri May 13 2005 Victor Forsyuk <force@altlinux.ru> 3.1-alt1
- New version, update buildreqs.

* Mon Oct 07 2002 Michael Shigorin <mike@altlinux.ru> 3.0-alt2
- menu entry added
- second sample .wmixrc added to docdir

* Tue May 07 2002 Michael Shigorin <mike@altlinux.ru> 3.0-alt1
- built for ALT Linux
