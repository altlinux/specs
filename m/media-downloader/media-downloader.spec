Name: media-downloader
Version: 4.6.0
Release: alt1

Summary: GUI frontend to multiple CLI based downloading programs
License: GPL-2.0-or-later
Group: File tools
Url: https://github.com/mhogomchungu/media-downloader

# Source-url: https://github.com/mhogomchungu/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: desktop-file-utils
Requires: yt-dlp aria2 ffmpeg

%description
This project is a Qt/C++ based GUI frontend to CLI multiple CLI based tools that
deal with downloading online media.
yt-dlp CLI tool is the default supported tool and other tools can be added by
downloading their extension and a list of supported extensions is managed here.

Features offered:-
 1. The GUI can be used to download any media from any website supported by
    installed extensions.
 2. The GUI offers a configurable list of preset options that can be used to
     download media if they are provided in multiple formats.
 3. The GUI offers an ability to do unlimited number of parallel downloads.
    Be careful with this ability because doing too many parallel downloads may
    cause the host to ban you.
 4. The GUI offers an ability to do batch downloads by entering individual link
    in the UI or telling the app to read them from a local file.
 5. The GUI offers an ability to download playlist from websites that supports
    them like youtube.
 6. The GUI offers ability to manage links to playlist to easily monitor their
    activities(subscriptions).
 7. The GUI is offered in multiple languages and as of this writing, the
    supported languages are English, Chinese, Spanish, Polish, Turkish, Russian,
    Japanese, French and Italian.

%prep
%setup

subst 's|"DownloadUrl": "https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest"||' extensions/yt-dlp*.json
subst 's|mainObj.insert( "DownloadUrl","https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest" ) ;||' src/engines/yt-dlp.cpp

%build
%cmake -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop

%files
%doc README.md LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Wed May 15 2024 Ivan Mazhukin <vanomj@altlinux.org> 4.6.0-alt1
- new version 4.6.0 (with rpmrb script)

* Tue Mar 05 2024 Ivan Mazhukin <vanomj@altlinux.org> 4.4.0-alt1
- new version (4.4.0) with rpmgs script
- build with qt6
- added necessary dependencies
- removed automatic downloading of binaries

* Tue Feb 13 2024 Ivan Mazhukin <vanomj@altlinux.org> 4.3.1-alt1
- Initial build for Alt Sisyphus

