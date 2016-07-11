%define pkgname flacon

Name: %pkgname-qt5
Version: 2.0.1
Release: alt1

Summary: Audio File Encoder
Summary(ru_RU.UTF-8): Конвертер аудиофайлов
Summary(uk_UA.UTF-8): Кодувальник аудіофайлів
License: LGPLv2.1
Group: Sound

Url: http://%pkgname.github.io/
Packager: Nazarov Denis <nenderus@altlinux.org>

#https://github.com/%pkgname/%pkgname/archive/v%version.tar.gz
Source0: %pkgname-%version.tar.gz

Conflicts: %pkgname

Requires: shntool

BuildRequires: cmake
BuildRequires: libuchardet-devel
BuildRequires: qt5-tools-devel

%description
Extracts audio tracks from audio CD image to separate tracks.

%description -l ru_RU.UTF-8
Извлекает аудио треки из CD образа WAV, FLAC, APE в отдельные файлы.

%description -l uk_UA.UTF-8
Витягує доріжки з образу аудіо-CD.

%prep
%setup -n %pkgname-%version

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DUSE_QT5=Yes

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform

%files
%doc LICENSE README.md
%_bindir/%pkgname
%_desktopdir/%pkgname.desktop
%_miconsdir/%pkgname.png
%_liconsdir/%pkgname.png
%_niconsdir/%pkgname.png
%_datadir/%pkgname
%_man1dir/%pkgname.1.*

%changelog
* Mon Jul 11 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux
