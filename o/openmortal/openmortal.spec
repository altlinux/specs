Name: openmortal
Version: 0.7.1
Release: alt1.1.1.1.1

Summary: Parody of the original fighting game "Mortal Kombat"
Group: Games/Arcade
License: GPLv2

Url: http://openmortal.sourceforge.net/

Source0: %name-0.7-strip.tar.bz2

# from gentoo
Patch0: openmortal-0.7-gcc41.patch

Patch1: openmortal-0.7-alt-freetype2-2.5.1.patch

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: openmortal-data = %version

# Automatically added by buildreq on Sun Dec 08 2013
BuildRequires: gcc-c++ libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libfreetype-devel perl-devel

%description
OpenMortal is a spoof of the original Mortal Kombat fighting game. The
funny thing about OpenMortal is that you can play the game AS YOURSELF.
It takes some work, but if you follow the Character Creation-HOWTO at

http://openmortal.sourceforge.net/Character_HOWTO.html

%prep
%setup -q -n %name-0.7
%patch0 -p0
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog INSTALL PACKAGERS README TODO
%_bindir/openmortal

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1.1
- rebuild with new perl 5.20.1

* Sun Dec 08 2013 Igor Zubkov <icesik@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.7-alt4
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.7-alt3
- rebuilt for perl-5.16

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.7-alt2.2
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7-alt2.1
- rebuilt with perl 5.12

* Thu Jul 13 2006 Igor Zubkov <icesik@altlinux.ru> 0.7-alt2
- fix rebuild with new gcc 4.1 (patch from gentoo) 

* Sat Jan 21 2006 Igor Zubkov <icesik@altlinux.ru> 0.7-alt1
- Initial build for Sisyphus
