Name: kaptain
Summary: An universal graphical front-end for command line programs
Version: 0.72
Release: alt1
Epoch: 1
Source0: %name-%version.tar.gz
Source1: %name.info
Url: http://kaptain.sourceforge.net
Group: Shells
License: GPLv2
Patch2: kaptain-0.72-fix.patch

# Automatically added by buildreq on Thu Jul 08 2021
# optimized out: fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXext-devel libstdc++-devel python3 python3-base sh4
BuildRequires: flex gcc-c++ libqt3-devel

%description
Kaptain is a universal graphical front-end for command line programs.
It works on linux/UNIX platforms whereever Qt3 and Qt4 is available.

%prep
%setup
cp %SOURCE1 doc
%patch2 -p1

%build
%configure
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot # /usr/lib64/qt3/src
mkdir -p %buildroot%_libexecdir
mv %buildroot%_datadir/%name %buildroot%_libexecdir/%name
chmod +x %buildroot%_libexecdir/%name/*.kaptn

%files
%doc README COPYING AUTHORS INSTALL ChangeLog
%_bindir/%name
%_libexecdir/%name
%_man1dir/*
%_infodir/%{name}*

%changelog
* Fri Jul 09 2021 Fr. Br. George <george@altlinux.ru> 1:0.72-alt1
- Build with Qt3

* Sun Apr 18 2021 Fr. Br. George <george@altlinux.ru> 0.73-alt2
- Fix build with bison3.7
- Fix parallel build race

* Thu Sep 05 2013 Fr. Br. George <george@altlinux.ru> 0.73-alt1
- Initial build from Mageia

* Sun Jan 13 2013 luigiwalser <luigiwalser> 0.73-3.mga3
+ Revision: 361454
- do not own man1 directory

  + umeabot <umeabot>
    - Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

  + matteo <matteo>
    - spec file reviewed

* Tue Jul 12 2011 matteo <matteo> 0.73-1.mga2
+ Revision: 123183
- imported package kaptain

* Sun May 29 2011 Matteo Pasotti <pasotti.matteo@gmail.com> 0.8-1
- create spec

