%define nam kobodl
Name: KoboDeluxe
Version: 0.5.1
Release: alt4
Summary: 3'rd person scrolling 2D shooter
Group: Games/Arcade
License: GPLv2+
Url: http://olofson.net/kobodl/
Source0: http://olofson.net/kobodl/download/%name-%version.tar.bz2
Source1: %name.png
Source2: %name.desktop
Patch: %name-gcc44.patch

# Automatically added by buildreq on Tue Apr 05 2011
# optimized out: libGL-devel libGLU-devel libSDL-devel libX11-devel libstdc++-devel
BuildRequires: gcc-c++ imake libICE-devel libSDL_image-devel xorg-cf-files

BuildRequires: desktop-file-utils

%description
Kobo Deluxe is a 3'rd person  scrolling 2D shooter with a simple
and responsive control system  - which you'll need to tackle the
tons of enemy ships that shoot at you,  chase you, circle around
you shooting,  or even  launch other ships at you,  while you're
trying to  destroy the  labyrinth  shaped  bases.  There  are 50
action packed  levels with  smoothly increasing  difficulty, and
different combinations of enemies that require different tactics
to be dealt with successfully.

%prep
%setup -q
%patch -p1
#sed -i 's|$(sharedstatedir)/kobo-deluxe/scores|%_var/games/kobo-deluxe|g' \
#  configure
#iconv -f ISO-8859-1 -t UTF8 README > tmp;         mv tmp README
#iconv -f ISO-8859-1 -t UTF8 ChangeLog > tmp;      mv tmp ChangeLog
iconv -f ISO2022JP -t UTF8 README.jp > tmp;       mv tmp README.jp
iconv -f ISO2022JP -t UTF8 README.xkobo.jp > tmp; mv tmp README.xkobo.jp

%build
%configure --disable-dependency-tracking --enable-opengl --sharedstatedir=%_localstatedir
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%_desktopdir
desktop-file-install --vendor "" \
  --dir $RPM_BUILD_ROOT%_desktopdir \
  %SOURCE2
mkdir -p $RPM_BUILD_ROOT%_niconsdir
install -p -m 644 %SOURCE1 \
  $RPM_BUILD_ROOT%_niconsdir

%files
%doc ChangeLog COPYING* README README.jp README.xkobo.jp README.sfont
%doc README.xkobo TODO
%attr(2711,root,games) %_bindir/%nam
%_datadir/kobo-deluxe
%_mandir/man6/%nam.6.gz
%config(noreplace) %attr(0775,root,games) %_localstatedir/kobo-deluxe/scores
%_desktopdir/%name.desktop
%_niconsdir/%name.png

%changelog
* Tue Apr 05 2011 Fr. Br. George <george@altlinux.ru> 0.5.1-alt4
- Forbidden requires eliminated

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.1-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for KoboDeluxe
  * postclean-05-filetriggers for spec file

* Wed May 27 2009 Fr. Br. George <george@altlinux.ru> 0.5.1-alt3
- GCC4.4 build fixup

* Mon Nov 03 2008 Fr. Br. George <george@altlinux.ru> 0.5.1-alt2
- GCC4.3 build fix

* Thu Feb 14 2008 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Version up
- Defults patch removed

* Sat Dec 01 2007 Fr. Br. George <george@altlinux.ru> 0.4.1-alt1
- Initial build for ALT from FC

* Wed Oct 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.1-1
- New upstream release 0.4.1
- Drop integrated patches

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-0.4.pre10
- Update License tag for new Licensing Guidelines compliance

* Mon Feb 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-0.3.pre10
- Some last small specfile improvements from review (bz 228707)

* Mon Feb 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-0.2.pre10
- various specfile improvements from review (bz 228707)
- install (do not remove after make install) kobosfx.h, its not a stray header
  file it actually gets loaded runtime by the game

* Mon Feb 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-0.1.pre10
- Initial Fedora Extras package
