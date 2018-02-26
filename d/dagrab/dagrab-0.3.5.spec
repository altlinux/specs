Summary: Dagrab reads digital audio from CD and puts it on wav files.
Name: dagrab
%define version 0.3.5
Version: %{version}
Release: alt2
License: GPL
Group: Sound
Source: http://web.tiscalinet.it/marcellou/dagrab-%{version}.tar.gz
Patch0: dagrab.Makefile.patch
Patch1: dagrab.localcddb.patch
Packager: Fr. Br. George <george@altlinux.ru>

%description 
DAGRAB is a  program for reading audio tracks from an IDE cdrom drive into wav
sound files.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%make_build PREFIX=/usr

%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_mandir/man1}
%makeinstall PREFIX=/usr INSTROOT=$RPM_BUILD_ROOT

%clean

%files
%_bindir/dagrab
%_bindir/dagmp3cd
%_bindir/dagmp3enc
%_mandir/man?/*

%changelog
* Fri Apr 11 2008 Fr. Br. George <george@altlinux.ru> 0.3.5-alt2
- Shellscript install -s fix

* Mon Feb 16 2004 Fr. Br. George <george@altlinux.ru> 0.3.5-alt1
- ALT Linux port

* Sat Feb 17 2000 Marcello Urbani <murbani@libero.it>
- initial spec file
