Name: castle-combat
Version: 0.8.1
Release: alt2.1
License: GPL
Group: Games/Strategy
Summary: castle-combat - enclose land and destroy your opponent's castle
Packager: Fr. Br. George <george@altlinux.ru>
Source: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Source1: %name.desktop
Url: http://user.cs.tu-berlin.de/~karlb/castle-combat/
BuildArch: noarch

# Automatically added by buildreq on Sun Jan 04 2009
BuildRequires: python-devel ImageMagick

%add_python_req_skip AppKit PyObjCTools

%description
Castle-Combat is a clone of the old arcade game Rampart. Up to four players (or more in future versions) build castle walls, place cannons inside these walls, and shoot at the walls of their enemy(s). If a player cannot build a complete wall around one of his castles, he loses. The last surviving player wins.

%prep
%setup -q

%build
python setup.py build
echo "#!/bin/sh
cd %_gamesdatadir/%name
python %name.py" > %name.sh
convert -bordercolor transparent -border 4 data/gfx/cannon0001.png 48.png
convert -bordercolor transparent -border 2 data/gfx/bigcannon0001.png 64.png

%install
install -D %name.py %buildroot/%_gamesdatadir/%name/%name.py
install -D -m755 %name.sh %buildroot/%_gamesbindir/%name
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D 48.png %buildroot%_liconsdir/%name.png
install -D 64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
cp -a build/lib/src %buildroot/%_gamesdatadir/%name/
cp -a data %buildroot/%_gamesdatadir/%name/

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%files
%doc README TODO
%attr(755,root,root) %_gamesbindir/*
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2
- Changed using from Numeric to numpy.oldnumeric

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.qa1.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * macos-resource-fork-file-in-package for castle-combat
  * postclean-05-filetriggers for spec file

* Sun Jan 04 2009 Fr. Br. George <george@altlinux.ru> 0.8.1-alt1
- Initial build from scratch

