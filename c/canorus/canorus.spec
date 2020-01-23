Name:          canorus
Version:       0.7.3.git3a25392
Release:       alt1
Summary:       Free cross-platform music score editor
Group:         Sound
License:       GPLv3+
Url:           http://www.canorus.org/
Vcs:           https://github.com/canorusmusic/canorus.git
Packager:      Ildar Mulyukov <ildar@altlinux.ru>

Source:        %name-%version.tar
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: convert
BuildRequires: libalsa-devel
BuildRequires: qt5-webkit-devel
BuildRequires: qt5-tools-devel
BuildRequires: zlib-devel
BuildRequires: qt5-svg-devel

%add_findreq_skiplist %_datadir/%name/*

%description
Canorus is a free next generation cross-platform music score editor
written in Qt4. It is a sequel of the well-known music score editor
for Linux, NoteEdit.

Canorus supports Python and Ruby scripting languages for plugins, a
fast and straight-forward user interface, source view of the score,
a number of import and export filters for LilyPond, MusicXML,
NoteEdit and others.


%prep
%setup

%build
%cmake_insource
%make_build VERBOSE=1

%install
find -name cmake_install.cmake | xargs -i \
	subst 's|/usr/share/canorus/doc|%buildroot/usr/share/canorus/doc|' {}
%makeinstall_std
%find_lang %name
rm -f %buildroot%_datadir/%name/*.so
rm -f %buildroot%_libdir/*.py
rm -rf %buildroot%_datadir/fonts/truetype/
mkdir -p %buildroot%_datadir/fonts/ttf/%name/
install -m644 src/fonts/Emmentaler-14.ttf %buildroot%_datadir/fonts/ttf/%name/

mkdir -p %buildroot%_desktopdir
install -m644 %name.desktop %buildroot%_desktopdir

mkdir -p %buildroot%_iconsdir/hicolor/{48x48,32x32,16x16}/apps/
convert %buildroot%_datadir/%name/images/clogosm.png -resize 48x48 %buildroot%_liconsdir/clogosm.png
convert %buildroot%_datadir/%name/images/clogosm.png -resize 32x32 %buildroot%_niconsdir/clogosm.png
convert %buildroot%_datadir/%name/images/clogosm.png -resize 16x16 %buildroot%_miconsdir/clogosm.png

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=AudioVideo \
	%buildroot%_desktopdir/canorus.desktop

%post
fc-cache %_datadir/fonts/ttf/%name ||:

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/fonts/ttf/%name
%_iconsdir/hicolor/*/apps/*.png
%doc AUTHORS DEVELOPERS NEWS README TODO

%changelog
* Wed Jan 22 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.3.git3a25392-alt1
- updated (^) 0.6svn -> 0.7.3.git3a25392

* Tue Feb 12 2019 Pavel Moseev <mars@altlinux.org> 0.6svn-alt2
- no return statement in the non-void function fixed (according g++8)

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

