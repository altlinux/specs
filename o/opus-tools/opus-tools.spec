Name: opus-tools
Version: 0.1.9
Release: alt0.1

Summary: Opus Audio Codec utilities
License: BSD-style
Group: System/Libraries
Url: http://opus-codec.org/
# http://downloads.xiph.org/releases/opus/%name-%version.tar.gz
Source: %name-%version.tar

Buildrequires: libogg-devel libflac-devel libopus-devel

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
* Mon Jun 06 2016 L.A. Kostis <lakostis@altlinux.ru> 0.1.9-alt0.1
- 0.1.9.

* Mon Mar 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.1.6-alt0.M60T.1
- build for t6

* Mon Mar 04 2013 L.A. Kostis <lakostis@altlinux.ru> 0.1.6-alt1
- 0.1.6.

* Sat Aug 25 2012 L.A. Kostis <lakostis@altlinux.ru> 0.1.4-alt1
- 0.1.4.

* Wed Jul 25 2012 L.A. Kostis <lakostis@altlinux.ru> 0.1.3-alt1
- initial build for ALTLinux.

