%define dist SDL
Name: perl-%dist
Version: 2.546
Release: alt3.1.1

Summary: Simple DirectMedia Layer for Perl
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar

Conflicts: frozen-bubble < 2.2.0-alt3.2
Conflicts: perl-SDL_Perl
Conflicts: perl-SDL25 < 2.546-alt2
Obsoletes: perl-SDL25 < 2.546-alt2
Provides: perl-SDL25 = %version

# avoid crazy dependencies
%add_findreq_skiplist */SDL/SMPEG*
%add_findreq_skiplist */SDLx/TTF.pm

BuildRequires: libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel libjpeg-devel libpng-devel libsmpeg-devel perl-Module-Build perl-Alien-SDL perl-Tie-Simple perl-Test-Most libSDL_pango-devel perl-Archive-Zip

%package pods
Summary: POD documentation for Simple DirectMedia Layer for Perl
Group: Development/Perl
Requires: %name = %version-%release

%package -n perl-Module-Build-SDL
Summary: Module::Build subclass for building SDL apps/games
Group: Development/Perl
Requires: %name = %version-%release

%description
SDL Perl is a package of Perl modules that provide both functional and
object oriented interfaces to the Simple DirectMedia Layer for Perl 5.
This package takes some liberties with the SDL API, and attempts to adhere
to the spirit of both the SDL and Perl.

%description pods
SDL Perl is a package of Perl modules that provide both functional and
object oriented interfaces to the Simple DirectMedia Layer for Perl 5.
This package takes some liberties with the SDL API, and attempts to adhere
to the spirit of both the SDL and Perl.
This package contains POD documentation.

%description -n perl-Module-Build-SDL
Module::Build::SDL is a subclass of Module::Build created to make easy
some tasks specific to SDL applications - e.g. packaging SDL
application/game into PAR archive.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGELOG TODO OFL.txt
%perl_vendor_archlib/SDL*
%perl_vendor_autolib/SDL*
%perl_vendor_autolib/share/dist/SDL/GenBasR.ttf

%files pods
%perl_vendor_archlib/pods/SDL*

%files -n perl-Module-Build-SDL
%perl_vendor_archlib/Module/Build/SDL.pm

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.546-alt3.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.546-alt3.1
- rebuild with new perl 5.24.1

* Wed Jun 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.546-alt3
- added conflict with frozen-bubble to help upgrade (closes: #32191)

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.546-alt2
- rename perl-SDL -> perl-SDL_Perl, perl-SDL25 -> perl-SDL

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.546-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.546-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.544-alt1.1
- rebuild with new perl 5.20.1

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.544-alt1
- automated CPAN update

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 2.540-alt2
- built for perl 5.18

* Wed Jun 20 2012 Vladimir Lettiev <crux@altlinux.ru> 2.540-alt1
- 2.2.6 -> 2.540
- new subpackages: %name-pods, perl-Module-Build-SDL
- new builddeps: perl-Alien-SDL, perl-Tie-Simple, perl-Test-Most,
    libSDL_pango-devel, perl-Archive-Zip
- conflict with perl-SDL

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.2.6-alt2.2
- rebuilt for perl-5.14
- rebuilt as plain src.rpm

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2.6-alt2.1
- rebuilt with perl 5.12
- fixed build

* Sun Apr 04 2010 Alexey Tourbin <at@altlinux.ru> 2.2.6-alt2
- Build.PL: eliminated build dependency on YAML

* Wed Feb 17 2010 Alexey Tourbin <at@altlinux.ru> 2.2.6-alt1
- 2.1.3 -> 2.2.6

* Sun Oct 28 2007 Alexey Tourbin <at@altlinux.ru> 2.1.3-alt3
- applied debian/patches/030_opengl_fixes.diff

* Tue Aug 14 2007 Alexey Tourbin <at@altlinux.ru> 2.1.3-alt2
- fixed building with new Module::Build

* Fri Oct 21 2005 Alexey Tourbin <at@altlinux.ru> 2.1.3-alt1
- 2.1.2 -> 2.1.3
- alt-sdl_link.patch merged upstream (cpan #11383)

* Fri Feb 04 2005 Alexey Tourbin <at@altlinux.ru> 2.1.2-alt1
- 1.20.0 -> 2.1.2, major revision
- new subpackage: %name-OpenGL
- alt-sdl_link.patch: fixed linkage (cpan #11383)
- built against new SDL_gfx
- manual pages not packaged (use perldoc)
- updated URL

* Fri Jun 20 2003 Sergey V Turchin <zerg at altlinux dot org> 1.20.0-alt1.1
- rebuild with new SDL_gfx

* Tue Mar 18 2003 Stanislav Ievlev <inger@altlinux.ru> 1.20.0-alt1
- 1.20.0

* Thu Oct 31 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.19.0-alt1
- 1.19.0
- Rebuilt with new perl

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.18-alt1
- 1.18

* Mon May 27 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.18-1mdk
- new stable release

* Sat May 11 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.16-3mdk
- s/SDL::Error/SDL::GetError/ in one pm

* Mon Apr 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.16-2mdk
- fix url
- rebuild for new alsa
- fix buildrequires

* Mon Apr 15 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.16-1mdk
- new version
  - patching Makefile.PL no more needed

* Mon Apr  8 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.11-3mdk
- my mistake, it's LGPL, not GPL

* Tue Mar  5 2002 Grigory Milev <week@altlinux.ru> 1.11-alt1
- ALTLinux adaptation

* Fri Feb 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.11-2mdk
- add dependency on perl

* Mon Jan 28 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.11-1mdk
- new version with another patch sent to author integrated right away

* Wed Jan 23 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.10-1mdk
- new release from author
- my SDL::Music patch integrated upstream

* Tue Jan 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-6mdk
- patch SDL::Music.pm where DESTROY was not calling the right function
  (who's using this library apart me anyway? ;p)

* Mon Oct 15 2001 Stefan van der Eijk <stefan@eijk.nu> 1.08-5mdk
- BuildRequires: libjpeg-devel perl-devel

* Fri Oct 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-4mdk
- rebuild for libpng3
- fix URL

* Thu Jul  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-3mdk
- rebuild

* Mon May 14 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-2mdk
- new SDL

* Tue Jan  2 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-1mdk
- first package in Linux-Mandrake
