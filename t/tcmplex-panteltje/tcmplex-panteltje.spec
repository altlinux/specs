%define name	tcmplex-panteltje
%define version	0.4.7
%define release	alt1

Summary: Audio/Video multiplexer
Name: %name
Version: %version
Release: %release
License: GPL
Group: Video
Url: http://panteltje.com/panteltje/dvd/
Source0: http://panteltje.com/panteltje/dvd/tcmplex-panteltje-%version.tar.bz2

%description
tcmplex-pantelje is an audio/video multiplexer from the transcode
distribution which has been re-written to support up to 8 audio
channels.

%prep
%setup -q
%__subst 's/-O2/%optflags/' Makefile

%build
%make CC="%__cc"

%install
%__mkdir_p %buildroot%_bindir
%__install -p -m 755 %name %buildroot%_bindir/%name
%__ln_s %name %buildroot%_bindir/tcmplex

%clean
%__rm -rf %buildroot

%files
%doc CHANGES COPYRIGHT LICENSE README %name-%version.lsm
%_bindir/%name
%_bindir/tcmplex

%changelog
* Sun Apr 16 2006 LAKostis <lakostis at altlinux.ru> 0.4.7-alt1
- rebuild for ALTLinux distribution.

* Fri Feb 24 2006 David Walluck <walluck@mandriva.org> 0:0.4.7-1mdk
- release
