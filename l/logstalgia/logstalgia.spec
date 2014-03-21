Name: logstalgia
Version: 1.0.3
Release: alt1

Summary: Web server access log visualizer
License: GPLv3+
Group: Monitoring

Url: http://code.google.com/p/logstalgia/
Source0: http://logstalgia.googlecode.com/files/logstalgia-%version.tar.gz
Source1: %name.watch
Patch: logstalgia-1.0.3-alt-configure.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libpcre-devel
BuildRequires: libftgl-devel libjpeg-devel libpng-devel

%description
Logstalgia (aka ApachePong) replays or streams a standard website
access log (eg access.log) as a retro arcade game-like simulation.

%prep
%setup
%patch -p1

%build
%autoreconf
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
* Fri Mar 21 2014 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- initial build for ALT Linux Sisyphus
  + based on Fedora package by Terje Rosten
- argh, better fix pcre.h location instead
