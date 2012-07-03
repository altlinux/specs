Name:		minivmac
Version:	3.1.3
Release:	alt2
Group:		Emulators
Summary:	MacPlus emulator
License:	GPLv2
# segfaults on x86_64
ExclusiveArch:	%ix86
# It's tricky thing to get the source:
# http://minivmac.sourceforge.net/doc/build.html
Source:		%name-%version-lx86.tar
#wget -r -l1 -p http://minivmac.sourceforge.net/
Source1:	%name.sourceforge.net.tar
Patch:		minivmac-as-needed.patch

# Automatically added by buildreq on Sun Feb 13 2011
BuildRequires: libgtk+2-devel

%description
The Mini vMac emulator collection allows modern computers to run
software made for early Macintosh computers, the computers that Apple
sold from 1984 to 1996 based upon Motorola's 680x0 microprocessors. The
first member of this collection emulates the Macintosh Plus.

%prep
%setup -n %name-%version-lx86
%patch -p1
tar xf %SOURCE1

%build
%make_build

%install
install -sD %name %buildroot/%_bindir/%name

%files
%doc README* %name.sourceforge.net/*
%_bindir/*

%changelog
* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 3.1.3-alt2
- Accurate arch handling

* Mon Feb 14 2011 Fr. Br. George <george@altlinux.ru> 3.1.3-alt1
- Initial build from scratch

