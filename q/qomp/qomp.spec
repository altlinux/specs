%define _unpackaged_files_terminate_build 1

Name: qomp
Version: 1.4
Release: alt1

Summary: Quick(Qt) Online Music Player 
License: GPLv2
Group: Sound

URL: http://qomp.sourceforge.net
Source: %name-%version.tar
Source1: %name-%version-ga.tar
Source2: %name-%version-themes.tar
Source3: %name-%version-translations.tar
Source4: %name-%version-singleapp.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: qt5-multimedia-devel 
BuildRequires: qt5-x11extras-devel 
BuildRequires: qt5-tools-devel 
BuildRequires: qt5-base-devel
BuildRequires: libcue-devel
BuildRequires: libtag-devel 
BuildRequires: cmake

Requires: gstreamer

%description
Qomp's main features:
- Search and play music from several online music hostings (Yandex.Music, myzuka.ru, pleer.com)
- Play music from local filesystem
- Last.fm scrobbling
- MPRIS support(Linux only)
- CUE SHEET support(*.cue files)
- System tray integration
- Proxy-server support
- Playlists support
- Themes support
- Crossplatform (Windows, OS X, Linux, Android)


%prep
%setup -a 1 -a 2 -a 3 -a 4

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name
%_libdir/%name
%_libdir/*.so*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/%name.png

%changelog
* Fri Nov 16 2018 Alexander Makeenkov <amakeenk@altlinux.org> 1.4-alt1
- Initial build for ALT

