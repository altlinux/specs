Name: kaptain
Summary: An universal graphical front-end for command line programs
Version: 0.73
Release: alt1
Source0: http://sourceforge.net/projects/kaptain/files/kaptain/0.73/kaptain-0.73.tgz
Url: http://kaptain.sourceforge.net
Group: Shells
License: GPLv2

# Automatically added by buildreq on Thu Sep 05 2013
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-xml libstdc++-devel
BuildRequires: flex gcc-c++ phonon-devel

%description
Kaptain is a universal graphical front-end for command line programs.
It works on linux/UNIX platforms whereever Qt3 and Qt4 is available.

%prep
%setup

%build
%qmake_qt4 PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
mkdir -p %buildroot%_libexecdir
mv %buildroot%_datadir/%name %buildroot%_libexecdir/%name

%files
%doc README COPYING AUTHORS INSTALL ChangeLog
%doc %_defaultdocdir/%name
%_bindir/%name
%attr(0755,root,root) %_libexecdir/%name/*.kaptn
%_libexecdir/%name/*.tgz
%_man1dir/*

%changelog
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

