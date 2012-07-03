Name: xwit
Version: 3.4
Release: alt2
Summary: Window interface tool 
Source: ftp://ftp.x.org/contrib/utilities/xwit-%version.tar.gz
License: MIT/X11
Group: System/X11
# thanks Debian for the patch
Patch: xwit_3.4-9.diff

# Automatically added by buildreq on Fri Jun 04 2010
BuildRequires: imake libX11-devel libXext-devel xorg-cf-files

%description
The window interface tool is a utility that can be used from shell scripts
to manipulate windows in the X window system. It can be used to popup, move,
iconify, and resize windows along with a number of other actions.

%prep
%setup
%patch -p1

%build
xmkmf
%make_build

%install
%makeinstall all install.man DESTDIR=%buildroot

%files
%doc README
%_bindir/xwit
%_man1dir/*

%changelog
* Fri Jun 04 2010 Fr. Br. George <george@altlinux.ru> 3.4-alt2
- Freshen build

* Sat Jul 29 2006 Fr. Br. George <george@altlinux.ru> 3.4-alt1
- Initial ALT build from Debian source

