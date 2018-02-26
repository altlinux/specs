Name: splitvt
Version: 1.6.6_6
Release: alt1

Summary: Splitvt splits console or shell screen to sections in which you can start different shells

License: GPL
Group: Terminals
Url: http://www.devolution.com/~slouken/projects/splitvt/
Packager: Denis Medvedev <nbr@altlinux.ru>

Source: splitvt-%version.tar.bz2

BuildPreReq: gcc ncurses-devel

%description
   This program takes any VT100 terminal window and splits it into two shell windows, one on top and one on bottom. It allows you to watch two terminal sessions at once, which can be very useful whenever you want more screen real-estate without messing with windows.

%prep
%setup -q
%build
./configure 
make
%install
mkdir -p %buildroot/usr/share/man/man1
mkdir -p %buildroot/usr/bin

%make_install install DESTDIR=%buildroot

%files
/usr/bin/splitvt
/usr/bin/xsplitvt
/usr/share/man/man1/*

%changelog
* Thu Jul 17 2008 Denis Medvedev <nbr@altlinux.ru> 1.6.6_6-alt1
- Initial ALT release, with debian patches


