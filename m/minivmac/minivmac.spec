Name:		minivmac
Version:	3.4.1
Release:	alt1
Group:		Emulators
Summary:	MacPlus emulator
License:	GPLv2
# It's tricky thing to get the source:
# http://minivmac.sourceforge.net/doc/build.html
Source:		%name-%version-lx86.tar
Source1:	%name-%version-lx64.tar
# wget -r -np -nH --cut-dirs=1 http://www.gryphel.com/c/minivmac/index.html
Source2:	%name.tar

# Automatically added by buildreq on Tue Nov 22 2016
BuildRequires: libX11-devel

%description
The Mini vMac emulator collection allows modern computers to run
software made for early Macintosh computers, the computers that Apple
sold from 1984 to 1996 based upon Motorola's 680x0 microprocessors. The
first member of this collection emulates the Macintosh Plus.

%prep
%setup -n %name-%version-lx86 -b1 -b2
%ifarch x86_64
cd ../%name-%version-lx64
%endif

%build
%ifarch x86_64
cd ../%name-%version-lx64
%endif
%make_build

%install
%ifarch x86_64
cd ../%name-%version-lx64
%endif
install -sD %name %buildroot/%_bindir/%name

%files
%doc ../%name/*
%_bindir/*

%changelog
* Tue Nov 22 2016 Fr. Br. George <george@altlinux.ru> 3.4.1-alt1
- Version bump
- Introduce x86_64 package

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 3.1.3-alt2
- Accurate arch handling

* Mon Feb 14 2011 Fr. Br. George <george@altlinux.ru> 3.1.3-alt1
- Initial build from scratch

