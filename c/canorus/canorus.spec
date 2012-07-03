BuildRequires: desktop-file-utils
Name: canorus
Version: 0.6svn
%define svnver 877
Release: alt1.qa2

Summary: Free cross-platform music score editor
Group: Sound
License: GPL
Url: http://www.canorus.org/
#Url: http://developer.berlios.de/projects/%name

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://193.95.242.3/canorusNightly/source/%{name}_%version.R%{svnver}_source.tar
#Source: http://download.berlios.de/%name/%{name}_%{version}_source.tar
#.bz2
Source1: %name.desktop

# Patch1: %name-...patch
Patch2: %name-0.6svn-alt-DSO.patch

# Automatically added by buildreq on Thu Jan 03 2008
BuildRequires: ImageMagick cmake gcc-c++ libalsa-devel libqt4-devel libqt4-svg

# Century Schoolbook L
PreReq: urw-fonts
# FreeSans
PreReq: fonts-ttf-freefont

%description
Canorus is a free next generation cross-platform music score editor
 written in Qt4. It is a sequel of the well-known music score editor
 for Linux, NoteEdit.

 Canorus supports Python and Ruby scripting languages for plugins, a
 fast and straight-forward user interface, source view of the score,
 a number of import and export filters for LilyPond, MusicXML,
 NoteEdit and others.

%prep
%setup -q -n %name-%version.R%svnver
#%%patch1 -p1
%patch2 -p2

%build
cmake -D CMAKE_INSTALL_PREFIX=/usr \
	-D NO_RUBY:BOOL=TRUE \
	-D NO_PYTHON:BOOL=TRUE \
	-D CMAKE_SKIP_RPATH:BOOL=TRUE .
%make VERBOSE=1

%install
find -name cmake_install.cmake | xargs -i \
	subst 's|DESTINATION \"/usr/|DESTINATION \"%buildroot/usr/|' {}
%make install
rm -f %buildroot%_datadir/%name/*.so
rm -f %buildroot%_libdir/*.py
rm -rf %buildroot%_datadir/fonts/truetype/
mkdir -p %buildroot%_datadir/fonts/ttf/%name/
install -m644 src/fonts/Emmentaler-14.ttf %buildroot%_datadir/fonts/ttf/%name/

mkdir -p %buildroot%_desktopdir
install -m644 %SOURCE1 %buildroot%_desktopdir

mkdir -p %buildroot%_iconsdir/hicolor/{48x48,32x32,16x16}/apps/
convert %buildroot%_datadir/%name/images/clogosm.png -resize 48x48 %buildroot%_liconsdir/clogosm.png
convert %buildroot%_datadir/%name/images/clogosm.png -resize 32x32 %buildroot%_niconsdir/clogosm.png
convert %buildroot%_datadir/%name/images/clogosm.png -resize 16x16 %buildroot%_miconsdir/clogosm.png

# TODO
#	py and ruby
#	%%find_lang --with-kde %name

%add_findreq_skiplist %_datadir/%name/scripts/*
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=AudioVideo \
	%buildroot%_desktopdir/canorus.desktop

%post
fc-cache %_datadir/fonts/ttf/%name ||:

%files
%_bindir/%name
#%%_libdir/*.so
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/fonts/ttf/%name
%_iconsdir/hicolor/*/apps/*.png
%doc AUTHORS DEVELOPERS NEWS README TODO

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6svn-alt1.qa2
- Fixed build

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.6svn-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for canorus

* Fri Nov 07 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.6svn-alt1
- snapshot SVN version 877
- desktop file fixes
- native icon

* Mon Apr 14 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.5-alt1
- new version
- desktop file categories fix

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for canorus

* Thu Jan 03 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.4-alt1
- 1st Sisyphus release

