Name: xfractint
Version: 20.04p12
Release: alt1
License: Freeware
Group: Sciences/Mathematics
Summary: The oldest fractal generator program ever
Source: %name-%version.tar.gz
Patch1: %name-20.04p10-patch
Patch2: %name-20-fake_lut_palette.patch
Url: http://www.fractint.org/

# Automatically added by buildreq on Tue Jun 21 2011
# optimized out: fontconfig fontconfig-devel libX11-devel libXrender-devel libfreetype-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libXft-devel

%description
Fractint is a freeware fractal generator created for IBMPC's and
compatible computers to run under DOS and ported to Linux.

%prep
%setup
%patch1 -p1
%patch2 -p1
sed -n '/Copyright Information:/,/as the source of the code/p' fractsrc.txt > LICENSE

%build
%make_build

%install
%makeinstall DESTDIR=%buildroot%prefix

%files
%doc LICENSE
%_bindir/*
%_datadir/%name
%_man1dir/*

%changelog
* Wed Feb 22 2012 Fr. Br. George <george@altlinux.ru> 20.04p12-alt1
- Autobuild version bump to 20.04p12

* Tue Jun 21 2011 Fr. Br. George <george@altlinux.ru> 20.04p11-alt1
- Autobuild version bump to 20.04p11

* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 20.04p10-alt1
- Autobuild version bump to 20.04p10

* Wed Jun 23 2010 Fr. Br. George <george@altlinux.ru> 20.04p09-alt1
- Initial build from scratch

