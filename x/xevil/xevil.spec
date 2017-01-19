# $Revision: 1.23 $, $Date: 2004/08/01 22:28:32 $
Summary: A fast-action violent game for the X Window System
Name: xevil
Version: 2.02r2
Release: alt2
License: GPL
Group: Games/Arcade
Source0: http://www.xevil.com/download/stable/%{name}src%version.zip
# Source0-md5:	09a9ef720b7204b0be68c4f462def370
Source1: %name.desktop
Source2: %name.png
Patch: xevil_2.02r2.patch
Url: http://www.xevil.com/

# Automatically added by buildreq on Sat Oct 05 2013
# optimized out: libX11-devel libstdc++-devel xorg-xproto-devel
BuildRequires: gcc-c++ libXpm-devel unzip

%description
XEvil is an X Window System based game with a side view display
reminiscent of LodeRunner. The object of the game is to run around
killing everything in sight and exploring the different levels. XEvil
can be played against the computer or against other people.

%prep
%setup -c
find . -type f \! -iname \*.bmp \! -iname \*.wav \! -iname \*.mid \! -iname \*.cur \! -iname \*.ico -exec sed -i 's/\r//' {} \;
%patch -p1

%build
%make_build HOSTTYPE=i686

%install
install -d $RPM_BUILD_ROOT{%_bindir,%_desktopdir,%_pixmapsdir}

install x11/REDHAT_LINUX/xevil $RPM_BUILD_ROOT%_bindir
install x11/REDHAT_LINUX/serverping $RPM_BUILD_ROOT%_bindir/%name-serverping

install %SOURCE1 $RPM_BUILD_ROOT%_desktopdir
install %SOURCE2 $RPM_BUILD_ROOT%_pixmapsdir

%files
%doc readme.txt instructions
%_bindir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png

%changelog
* Thu Jan 19 2017 Fr. Br. George <george@altlinux.ru> 2.02r2-alt2
- GCC6 fix

* Sat Oct 05 2013 Fr. Br. George <george@altlinux.ru> 2.02r2-alt1
- Initial (?) build from PLD
