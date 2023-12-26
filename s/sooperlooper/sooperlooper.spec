Name: sooperlooper
Version: 1.7.9
Release: alt1

Summary: Live Looping Sampler
License: GPLv2
Group: Sound

Requires: sooperlooper-headless = %version-%release

Url: https://github.com/essej/sooperlooper
Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libalsa-devel ncurses-devel libwxBase3.2-devel
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: pkgconfig(sndfile)

%package headless
Summary: Live Looping Sampler Engine
Group: Sound

%define desc \
SooperLooper is a live looping sampler capable of immediate loop \
recording, overdubbing, multiplying, reversing and more.  It allows \
for multiple simultaneous multi-channel loops limited only by your \
computer's available memory.  The feature-set and operation was \
inspired by the impressive Gibson Echoplex Digital Pro (EDP). When used \
with a low-latency audio configuration it is capable of truly realtime \
live performance looping.

%description %desc

%description headless %desc
This package contais SooperLooper Engine.

%prep
%setup

%build
sh autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files
%doc doc/html
%_bindir/slgui

%files headless
%doc CHANGES COPYING OSC README.md
%_bindir/slconsole
%_bindir/slregister
%_bindir/sooperlooper
%_datadir/sooperlooper

%changelog
* Tue Dec 26 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.9-alt1
- initial
