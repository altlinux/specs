Name: numlockx
Version: 1.2
Release: alt1
Summary: NumLockX turns on NumLock after starting X

Group: System/X11
License: MIT
Url: http://ktown.kde.org/~seli/%name/
Source0: http://ktown.kde.org/~seli/%name/%name-%version.tar.gz
Source1: %name.sh

Requires: xinitrc
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Wed Sep 19 2007
BuildRequires: imake libXt-devel libXtst-devel libXext-devel

%description
NumLockX turns on NumLock after starting X

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall
install -p -D %SOURCE1 %buildroot%_sysconfdir/X11/xinit.d/%name.sh

%files
%_bindir/%name
%_sysconfdir/X11/xinit.d/%name.sh
%doc AUTHORS README LICENSE

%changelog
* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Autobuild version bump to 1.2

* Tue Dec 02 2008 Fr. Br. George <george@altlinux.ru> 1.0-alt2
- libXext-devel added

* Wed Sep 19 2007 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build for ALT

* Wed Feb 15 2006 John Mahowald <jpmahowald@gmail.com> 1.0-9
- Rebuild for Fedora Extras 5

* Tue Nov 29 2005 John Mahowald <jpmahowald@gmail.com> 1.0-7
- More Buildreqires fixes to satisfy configure

* Tue Nov 29 2005 John Mahowald <jpmahowald@gmail.com> 1.0-6
- Buildrequires fixes

* Mon Nov 28 2005 John Mahowald <jpmahowald@gmail.com> 1.0-5
- Change requires xinitrc to xorg-x11-xinit

* Mon Aug 29 2005 John Mahowald <jpmahowald@gmail.com> 1.0-4
- %%{?dist} in Release

* Sun Aug 28 2005 John Mahowald <jpmahowald@gmail.com> 1.0-3
- Macro changes

* Sat Aug 27 2005 John Mahowald <jpmahowald@gmail.com> 1.0-2
- Script for xinitrc.d
- Use more macros

* Fri Aug 26 2005 John Mahowald <jpmahowald@gmail.com> 1.0-1
- Initial rpm
