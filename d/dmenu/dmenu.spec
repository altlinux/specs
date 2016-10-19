Name: dmenu
Version: 4.6
Release: alt1

Summary: Dynamic menu
License: MIT
Group: Graphical desktop/Other

Url: http://tools.suckless.org/
Source: %name-%version.tar.gz

Patch1: dmenu-4.6-alt-make.patch

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: libX11-devel xorg-xproto-devel
BuildRequires: libXinerama-devel libXft-devel

%description
dynamic menu for dwm

%prep
%setup
%patch1 -p1

%build
%make_build OPTFLAGS="%optflags"

%install
%makeinstall_std PREFIX="%prefix"

%files
%doc LICENSE README
%_bindir/*
%_man1dir/*

%changelog
* Wed Oct 19 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.6-alt1
- Updated to 4.6.

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 4.5-alt1
- Autobuild version bump to 4.5

* Tue Sep 20 2011 Fr. Br. George <george@altlinux.ru> 4.4.1-alt1
- Autobuild version bump to 4.4.1

* Sat Jul 23 2011 Fr. Br. George <george@altlinux.ru> 4.4-alt1
- Autobuild version bump to 4.4

* Mon Jun 27 2011 Fr. Br. George <george@altlinux.ru> 4.3.1-alt1
- Autobuild version bump to 4.3.1

* Fri Apr 15 2011 Fr. Br. George <george@altlinux.ru> 4.2.1-alt1
- Autobuild version bump to 4.2.1

* Mon Jun 18 2007 Alexey Tourbin <at@altlinux.ru> 3.2-alt1
- updated to 3.2

* Mon Apr 02 2007 Alexey Tourbin <at@altlinux.ru> 2.9-alt0.1
- updated to 2.8+
- imported sources from mercurial into git

* Sun Nov 05 2006 Lunar Child <luch@altlinux.ru> 1.4-alt1
- First build for ALT Linux Sisyphus
