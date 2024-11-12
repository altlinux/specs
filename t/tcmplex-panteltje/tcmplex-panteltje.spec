%define name	tcmplex-panteltje
%define version	0.4.7
%define release	alt1

Summary: Audio/Video multiplexer
Name: %name
Version: %version
Release: alt2
License: GPLv2+
Group: Video
Url: http://panteltje.com/panteltje/dvd/
Source0: http://panteltje.com/panteltje/dvd/tcmplex-panteltje-%version.tar.bz2
Patch: %name-alt-gcc14-fix.patch

%description
tcmplex-pantelje is an audio/video multiplexer from the transcode
distribution which has been re-written to support up to 8 audio
channels.

%prep
%setup
%patch -p2
subst 's/-O2/%optflags/' Makefile

%build
%make CC="%__cc"

%install
mkdir -p %buildroot%_bindir
install -p -m 755 %name %buildroot%_bindir/%name
ln -s %name %buildroot%_bindir/tcmplex

%clean
rm -rf %buildroot

%files
%doc CHANGES COPYRIGHT LICENSE README %name-%version.lsm
%_bindir/%name
%_bindir/tcmplex

%changelog
* Tue Nov 12 2024 L.A. Kostis <lakostis@altlinux.ru> 0.4.7-alt2
- Fix FTBFS with gcc14.
- cleanup .spec.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.7-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Apr 16 2006 LAKostis <lakostis at altlinux.ru> 0.4.7-alt1
- rebuild for ALTLinux distribution.

* Fri Feb 24 2006 David Walluck <walluck@mandriva.org> 0:0.4.7-1mdk
- release
