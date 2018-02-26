%set_automake_version 1.7
Name: divxcalc
Version: 0.5.1
Release: alt2
Summary: DivX bitrate calculator
License: GPL
Group: Graphical desktop/KDE
URL: http://axljab.homelinux.org/
Source: %name-%version.tar.bz2
Patch0: divxcalc-autotoolscheck.patch

# Automatically added by buildreq on Tue Apr 12 2005
BuildRequires: fontconfig freetype2 gcc-c++ hostinfo kdelibs-devel libjpeg-devel libpng-devel libqt3-devel libqt3-settings libstdc++-devel samba-common zlib-devel

%description
DivX Calculator was created simply for the purpose to give an average for the DivX 4 (and upwards) bitrates, incl. OpenDivX, but NOT DivX 3 bitrates used to encode avi videos.

%prep
%setup -q -n %name-%version
%patch0 -p1

%build
make -f Makefile.dist
%__subst "s/\.la/.so/g" configure
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*

%changelog
* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt2
- fix build

* Mon Dec 31 2007 Nick S. Grechukh <gns@altlinux.ru> 0.5.1-alt1.1
- fix build with new autotools

* Sun Apr 10 2005 Nick S. Grechukh <gns@altlinux.ru> 0.5.1-alt1
- initial build
