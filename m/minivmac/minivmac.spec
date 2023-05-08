Name: minivmac
Version: 36.04
Release: alt1.1
Group: Emulators
Summary: MacPlus emulator
ExclusiveArch: %ix86 x86_64 %e2k
License: GPLv2
Source: %name-%version.src.tgz
# wget -r -np -nH --cut-dirs=1 http://www.gryphel.com/c/minivmac/index.html
# wget -e robots=off -A "*.jpg" -A "*.gif" -A "*.png" -A "*.html" -k -r -p -np https://www.gryphel.com/c/minivmac/index.html
Source1: %name.tar

# Automatically added by buildreq on Tue Nov 22 2016
BuildRequires: libX11-devel

%description
The Mini vMac emulator collection allows modern computers to run
software made for early Macintosh computers, the computers that Apple
sold from 1984 to 1996 based upon Motorola's 680x0 microprocessors. The
first member of this collection emulates the Macintosh Plus.

%prep
%setup -n %name -a1

%build
%ifarch x86_64
%define March lx64
%else
%define March lx86
%endif
cc setup/tool.c -o setup_t
./setup_t -t %March | grep -v strip > setupI.sh
./setup_t -t %March -m II -hres 800 -vres 600 -depth 5 | grep -v strip > setupII.sh

sh setupII.sh
%make_build
mv minivmac minivmacII
rm -rf Makefile bld
sh setupI.sh
%make_build

%install
mkdir -p %buildroot/%_bindir
install minivmac minivmacII %buildroot/%_bindir/

%files
%doc www.gryphel.com/*
%_bindir/*

%changelog
* Mon May 8 2023 Artyom Bystrov <arbars@altlinux.org> 36.04-alt1.1
- add e2k macros in ExclusiveArch

* Thu Feb 20 2020 Fr. Br. George <george@altlinux.ru> 36.04-alt1
- Autobuild version bump to 36.04

* Thu Feb 20 2020 Fr. Br. George <george@altlinux.ru> 36.02-alt1
- Live upstream is found, versioning changed

* Tue Nov 22 2016 Fr. Br. George <george@altlinux.ru> 3.4.1-alt1
- Version bump
- Introduce x86_64 package

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 3.1.3-alt2
- Accurate arch handling

* Mon Feb 14 2011 Fr. Br. George <george@altlinux.ru> 3.1.3-alt1
- Initial build from scratch

