Name: feh
Version: 2.1
Release: alt1
Summary: Image viewer using Imlib 2
Group: Graphics
License: BSD
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://derf.homelinux.org/projects/feh/
Source: http://derf.homelinux.org/projects/feh/%name-%version.tar.bz2

# Automatically added by buildreq on Thu Sep 08 2011
# optimized out: imlib2 imlib2-devel libX11-devel xorg-xproto-devel zlib-devel
BuildRequires: libXinerama-devel libXt-devel libcurl-devel libgiblib-devel libpng-devel

%description
feh is a versatile and fast image viewer using imlib2, the
premier image file handling library. feh has many features,
from simple single file viewing, to multiple file modes using
a slideshow or multiple windows. feh supports the creation of
montages as index prints with many user-configurable options.

%prep
%setup -q
sed -in 's/\/usr\/local/\/usr\//' config.mk

%build
%make_build PREFIX="%_prefix" 
#CFLAGS="optflags" 

%install
#makeinstall
mkdir -p %buildroot{%_bindir,%_datadir,%_man1dir}
install -pm755 %_builddir/%name-%version/src/%name %buildroot%_bindir/%name
install -pm755 %_builddir/%name-%version/cam/%name-cam %buildroot%_bindir/%name-cam
install -pm755 %_builddir/%name-%version/cam/gen-cam-menu %buildroot%_bindir/gen-cam-menu
mv %_builddir/%name-%version/share/ %buildroot%_datadir/%name
cp %_builddir/%name-%version/man/*.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*
%_datadir/%name

%doc AUTHORS ChangeLog README TODO

%changelog
* Sun Nov 13 2011 Andrew Clark <andyc@altlinux.org> 2.1-alt1
- version update to 2.1-alt1

* Thu Sep 8 2011 Andrew Clark <andyc@altlinux.org> 1.16-alt1
- version update to 1.16-alt1

* Sat Jun 4 2011 Andrew Clark <andyc@altlinux.org> 1.14.1-alt1
- version update to 1.14.1-alt1

* Sun Feb 13 2011 Andrew Clark <andyc@altlinux.org> 1.11.2-alt1
- version update to 1.11.2-alt1

* Fri Jan 7 2011 Andrew Clark <andyc@altlinux.org> 1.10.1-alt1
- version update to 1.10.1-alt1

* Sun Oct 10 2010 Andrew Clark <andyc@altlinux.org> 1.10-alt1
- version update to 1.10-alt1

* Sun Sep 5 2010 Andrew Clark <andyc@altlinux.org> 1.9-alt1
- version update to 1.9-alt1

* Sat Jul 31 2010 Andrew Clark <andyc@altlinux.org> 1.8-alt1
- version update to 1.8-alt1

* Fri Jan 27 2006 Alex Murygin <murygin@altlinux.ru> 1.3.4-alt1
- new version

* Mon Jul 18 2005 Alex Murygin <murygin@altlinux.ru> 1.3.3-alt1
- new version
- changed url

* Wed Feb 09 2005 Alex Murygin <murygin@altlinux.ru> 1.3.0-alt1
- new version

* Thu Dec 16 2004 Alex Murygin <murygin@altlinux.ru> 1.2.9-alt1
- new version

* Sat Dec 06 2003 Alex Murygin <murygin@altlinux.ru> 1.2.6-alt1
- First build for AltLinux

