Name:          canorus
Version:       0.7.3.git45e82ec
Release:       alt1
Summary:       Free cross-platform music score editor
Group:         Sound
License:       GPLv3+
Url:           http://www.canorus.org/
Vcs:           https://github.com/canorusmusic/canorus.git
Packager:      Ildar Mulyukov <ildar@altlinux.ru>

Source:        %name-%version.tar
Patch:         config.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: swig
BuildRequires: desktop-file-utils
BuildRequires: convert
BuildRequires: libruby-devel
BuildRequires: libalsa-devel
BuildRequires: qt5-webkit-devel
BuildRequires: qt5-tools-devel
BuildRequires: zlib-devel
BuildRequires: qt5-svg-devel
%add_optflags -Wno-error=deprecated-declarations -Wno-error=return-type -Wno-error

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
%patch

%build
%cmake -DTTF_INSTALL_DIR:PATH=%_datadir/fonts/ttf/%name \
       -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmakeinstall_std

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
%doc AUTHORS DEVELOPERS NEWS README TODO
%_bindir/%name
%_datadir/%name
%_datadir/fonts/ttf/%name
%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/%name.desktop


%changelog
* Tue Oct 12 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.3.git45e82ec-alt1
- ^ 0.7.3.git3a25392 -> 0.7.3.git45e82ec

* Thu Aug 27 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.3.git3a25392-alt2
- ! build

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

