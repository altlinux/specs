Name: opus-tools
Version: 0.1.3
Release: alt1

Summary: Opus Audio Codec utilities
License: BSD-style
Group: System/Libraries
Url: http://opus-codec.org/
# http://downloads.xiph.org/releases/opus/%name-%version.tar.gz
Source: %name-%version.tar

Buildrequires: libogg-devel libopus-devel

%description
The Opus codec is designed for interactive speech and audio transmission
over the Internet. It is designed by the IETF Codec Working Group and
incorporates technology from Skype's SILK codec and Xiph.Org's CELT
codec.

Opus-tools provides command-line utilities to encode, inspect, and
decode .opus files.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS COPYING ChangeLog

%changelog
* Wed Jul 25 2012 L.A. Kostis <lakostis@altlinux.ru> 0.1.3-alt1
- initial build for ALTLinux.

