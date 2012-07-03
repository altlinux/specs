Name: openmortal
Version: 0.7
Release: alt2.2

Summary: Parody of the original fighting game "Mortal Kombat"
Group: Games/Arcade
License: GPL

Url: http://openmortal.sourceforge.net/

Source0: %name-%version-strip.tar.bz2

# from gentoo
Patch0: openmortal-0.7-gcc41.patch

Packager: Igor Zubkov <icesik@altlinux.ru>

Requires: openmortal-data

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libfreetype-devel perl-devel zlib-devel

%description
OpenMortal is a spoof of the original Mortal Kombat fighting game. The
funny thing about OpenMortal is that you can play the game AS YOURSELF.
It takes some work, but if you follow the Character Creation-HOWTO at

http://openmortal.sourceforge.net/Character_HOWTO.html

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/openmortal

%changelog
* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.7-alt2.2
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7-alt2.1
- rebuilt with perl 5.12

* Thu Jul 13 2006 Igor Zubkov <icesik@altlinux.ru> 0.7-alt2
- fix rebuild with new gcc 4.1 (patch from gentoo) 

* Sat Jan 21 2006 Igor Zubkov <icesik@altlinux.ru> 0.7-alt1
- Initial build for Sisyphus
