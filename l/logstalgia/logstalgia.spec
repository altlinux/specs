Name: logstalgia
Version: 1.1.1
Release: alt1

Summary: Web server access log visualizer
License: GPLv3+
Group: Monitoring

Url: http://code.google.com/p/logstalgia/
Source0: http://logstalgia.googlecode.com/files/logstalgia-%version.tar.gz
Source1: logstalgia.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Apr 23 2014
# optimized out: boost-devel-headers gnu-config libGL-devel libGLU-devel libSDL2-devel libX11-devel libcloog-isl4 libstdc++-devel pkg-config xorg-xproto-devel
BuildRequires: boost-devel gcc-c++ libSDL2_image-devel libfreetype-devel libglew-devel libglm-devel libpcre-devel libpng-devel

%description
Logstalgia (aka ApachePong) replays or streams a standard website
access log (eg access.log) as a retro arcade game-like simulation.

%prep
%setup

%build
%configure
%make_build OPTFLAGS="%optflags"

%install
%makeinstall_std

%files
%doc README THANKS
%_bindir/%name
%_datadir/%name
%_man1dir/%name.1*

%changelog
* Tue Feb 13 2018 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1
- new version (watch file uupdate)

* Wed Oct 11 2017 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1
- new version (watch file uupdate)

* Sat Oct 07 2017 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- new version (watch file uupdate)

* Fri Sep 29 2017 Michael Shigorin <mike@altlinux.org> 1.0.8-alt1
- new version (watch file uupdate)

* Thu Oct 22 2015 Michael Shigorin <mike@altlinux.org> 1.0.7-alt1
- new version (watch file uupdate)

* Thu Oct 16 2014 Michael Shigorin <mike@altlinux.org> 1.0.6-alt1
- new version (watch file uupdate)

* Thu Apr 24 2014 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- 1.0.5
- built against libSDL2
- added watch file (github is weird though)

* Fri Mar 21 2014 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- initial build for ALT Linux Sisyphus
  + based on Fedora package by Terje Rosten
- argh, better fix pcre.h location instead
