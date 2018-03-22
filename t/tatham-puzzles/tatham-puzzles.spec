Name: tatham-puzzles
Version: 20180227
Release: alt1
License: MIT
Group: Games/Puzzles
Url: http://www.chiark.greenend.org.uk/~sgtatham/puzzles/
Source: puzzles-r%version.tar.gz
Source1: %name.patchmakefile.sed
# See Makefile for obtaining wget command
Source2: www.chiark.greenend.org.uk.tar
Source3: %name.sh
Source4: CHANGELOG.txt

Summary: A collection of small one-player puzzle games
Summary(ru_RU.UTF-8): Коллекция небольших логических головоломок

# Automatically added by buildreq on Sun Oct 11 2009
BuildRequires: ImageMagick-tools fonts-type1-urw libgtk+2-devel xvfb-run xauth halibut
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
A collection of little puzzle games you can pop up in a window and play for two or three minutes while you take a break from whatever else you were doing.
Their names: Black Box, Bridges, Cube, Dominosa, Fifteen, Filling, Flip, Flood, Galaxies, Guess, Inertia, Keen, Light Up, Loopy, Magnets, Map, Mines, Net, Netslide, Palisade, Pattern, Pearl, Pegs, Range, Rectangles, Same Game, Signpost, Singles, Sixteen, Slant, Solo, Tents, Towers, Tracks, Twiddle, Undead, Unequal, Unruly, Untangle. Rules, descriptions and tips can be found in documentation.

%description -l ru_RU.UTF-8
Коллекция из небольших логических головоломок класса "открой в окошке, потыкай пять минут -- отдохни"; сложность можно настроить.
Названия головоломок: Black Box, Bridges, Cube, Dominosa, Fifteen, Filling, Flip, Flood, Galaxies, Guess, Inertia, Keen, Light Up, Loopy, Magnets, Map, Mines, Net, Netslide, Palisade, Pattern, Pearl, Pegs, Range, Rectangles, Same Game, Signpost, Singles, Sixteen, Slant, Solo, Tents, Towers, Tracks, Twiddle, Undead, Unequal, Unruly, Untangle. Rules, descriptions and tips can be found in documentation.
Описания, правила и подсказки -- в докуметации.
%package -n %name-solvers
Summary: Stand-alone solvers for some of the %name puzzles
Summary(ru_RU.UTF-8): Набор "решалок" к некоторым головоломкам из %name
Group: Games/Puzzles

%description -n %name-solvers
Stand-alone solvers for some of the %name puzzles.

%description -l ru_RU.UTF-8 -n %name-solvers
Набор "решалок" к некоторым головоломкам из %name.

# TODO separate puzzles/js into another package
# TODO separate docs
# TODO add help links and/or text into launcher
# TODO separate all the desktop files into mandatory package in the sake of launcher

%prep
%setup -n puzzles-r%version -a2
./mkfiles.pl

sed '/^IN=/s@.*@IN="%_defaultdocdir/%name-%version/index.html"@
/^GBD=/s@.*@GBD="%_gamesbindir"@' < %SOURCE3 > %name

cat > mkicons <<@@@
( cd icons
make
%make_build web pngicons
for S in 16 32 48; do
  mkdir \$S
  for N in *\${S}d24.png; do
    ln \$N \$S/\${N%%-*}.png
  done
done
)
@@@
chmod +x mkicons

cp %SOURCE4 .

%build
%autoreconf
%configure --bindir=%_gamesbindir
%make_build

xvfb-run ./mkicons
sh %SOURCE3 desktop

# hack a little
##sed -i 's/Icon=rectangles/Icon=rect/' rectangles.desktop

halibut --info=%name.info puzzles.but
sed -i '/^$/a\
INFO-DIR-SECTION Games\
START-INFO-DIR-ENTRY\
* %name: (%name).	A collection of small one-player puzzle games\
END-INFO-DIR-ENTRY\
' %name.info

%install
mkdir -p %buildroot/%_gamesbindir %buildroot%_desktopdir %buildroot%_miconsdir %buildroot%_liconsdir %buildroot%_niconsdir %buildroot%_pixmapsdir/%name %buildroot%_infodir
%makeinstall bindir=%buildroot/%_gamesbindir
#-f Makefile.linux
install -m755 *solver %buildroot/%_gamesbindir/
install -m 755 %name %buildroot/%_gamesbindir/
install *.desktop %buildroot%_desktopdir/
install icons/16/*.png %buildroot%_miconsdir/
install icons/32/*.png %buildroot%_niconsdir/
install icons/48/*.png %buildroot%_liconsdir/
install icons/*-*se*.png %buildroot%_pixmapsdir/%name/
install *.info* %buildroot%_infodir/

%files -n %name-solvers
%_gamesbindir/*solver

%files
%doc README *.txt www.chiark.greenend.org.uk/~sgtatham/puzzles/* 
#icons/*-web.png
%exclude %_gamesbindir/*solver
%_gamesbindir/*
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%dir %_pixmapsdir/%name
%_pixmapsdir/%name/*
%_infodir/*%{name}*

%changelog
* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 20180227-alt1
- Manual update

* Mon Sep 25 2017 Fr. Br. George <george@altlinux.ru> 20170925-alt1
- Manual update

* Thu Nov 17 2016 Fr. Br. George <george@altlinux.ru> 20161031-alt1
- Upstream switch to GH

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 10286-alt1.1
- NMU: added BR: texinfo

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 10286-alt1
- Autobuild version bump to 10286

* Mon Sep 29 2014 Fr. Br. George <george@altlinux.ru> 10274-alt1
- Autobuild version bump to 10274

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 10196-alt1
- Autobuild version bump to 10196

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 10180-alt1
- Autobuild version bump to 10180

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 10167-alt1
- Autobuild version bump to 10167

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 10116-alt1
- Autobuild version bump to 10116

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 10108-alt1
- Autobuild version bump to 10108

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 10051-alt1
- Autobuild version bump to 10051

* Fri Aug 23 2013 Fr. Br. George <george@altlinux.ru> 9976-alt1
- Autobuild version bump to 9976
- Fix build

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 9861-alt1
- Autobuild version bump to 9861

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 9840-alt1
- Autobuild version bump to 9840

* Mon Apr 29 2013 Fr. Br. George <george@altlinux.ru> 9835-alt1
- Autobuild version bump to 9835
- Drop ImageMagick pipe hack

* Tue Apr 23 2013 Fr. Br. George <george@altlinux.ru> 9794-alt2
- Avoid ImageMagick pipe i/o bug

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 9794-alt1
- Autobuild version bump to 9794

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 9751-alt1
- Autobuild version bump to 9751
- Convert russian descriptions to UTF

* Wed Jan 16 2013 Fr. Br. George <george@altlinux.ru> 9737-alt1
- Autobuild version bump to 9737

* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 9712-alt1
- Autobuild version bump to 9712

* Wed Nov 14 2012 Fr. Br. George <george@altlinux.ru> 9694-alt1
- Autobuild version bump to 9694
- New puzzle: Undead

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 9682-alt1
- Autobuild version bump to 9682

* Tue Aug 21 2012 Fr. Br. George <george@altlinux.ru> 9606-alt1
- Autobuild version bump to 9606

* Sun Jul 29 2012 Fr. Br. George <george@altlinux.ru> 9561-alt1
- Autobuild version bump to 9561

* Wed Jul 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9558-alt1.1
- Avoid strip

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 9558-alt1
- Autobuild version bump to 9558

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 9455-alt1
- Autobuild version bump to 9455

* Wed Feb 22 2012 Fr. Br. George <george@altlinux.ru> 9411-alt1
- Autobuild version bump to 9411

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 9405-alt1
- Autobuild version bump to 9405

* Sun Jan 22 2012 Fr. Br. George <george@altlinux.ru> 9381-alt1
- Autobuild version bump to 9381

* Wed Jan 11 2012 Fr. Br. George <george@altlinux.ru> 9375-alt1
- Autobuild version bump to 9375

* Tue Sep 20 2011 Fr. Br. George <george@altlinux.ru> 9306-alt1
- Autobuild version bump to 9306

* Sat Jul 23 2011 Fr. Br. George <george@altlinux.ru> 9179-alt1
- Autobuild version bump to 9179
- Autoupdate scheme is used

* Wed May 11 2011 Fr. Br. George <george@altlinux.ru> 9172-alt1
- Base script improved

* Thu Sep 16 2010 Fr. Br. George <george@altlinux.ru> 8999-alt3
- Version up (new puzzle: Range)

* Mon Aug 23 2010 Fr. Br. George <george@altlinux.ru> 8981-alt3
- Version up
- Generate info file

* Mon Apr 12 2010 Fr. Br. George <george@altlinux.ru> 8896-alt3
- Use xvfb instead on vnc server to generate icons

* Fri Mar 12 2010 Fr. Br. George <george@altlinux.ru> 8896-alt2
- New puzzle: signpost

* Wed Jan 20 2010 Fr. Br. George <george@altlinux.ru> 8845-alt2
- Fix icon names

* Sun Jan 17 2010 Fr. Br. George <george@altlinux.ru> 8845-alt1
- Version up
- Two puzzles added (Magnets and Singles)

* Sun Jan 10 2010 Fr. Br. George <george@altlinux.ru> 8824-alt1
- Version up
- New puzzle (Towers)

* Mon Dec 28 2009 Fr. Br. George <george@altlinux.ru> 8798-alt1
- Version up
- New puzzle (keen, the magic square)

* Mon Oct 12 2009 Fr. Br. George <george@altlinux.ru> 8690-alt1
- Version up
+ Desktop files

* Sun Oct 11 2009 Fr. Br. George <george@altlinux.ru> 8686-alt2
- Documentation added
- Simple start script provided

* Fri Oct 09 2009 Fr. Br. George <george@altlinux.ru> 8686-alt1
- Version up

* Sat Nov 18 2006 Fr. Br. George <george@altlinux.ru> 6907-alt1
- Initial ALT build

