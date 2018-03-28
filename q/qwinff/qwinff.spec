Name: 	  qwinff
Version:  0.2.1
Release:  alt1

Summary:  A Qt5 GUI Frontend for FFmpeg
License:  GPL-3.0
Group:    Video
Url: 	  https://github.com/qwinff/qwinff

Packager: Andrey Solodovnikov <hepoh@altlinux.org>

Source:   %name-%version.tar

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
Requires: ffmpeg
Requires: sox

%description
%summary

%prep
%setup

%build
%make_build QMAKE=qmake-qt5 LRELEASE=lrelease-qt5

%install
%makeinstall_std

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_man1dir/%name.1.xz
%_pixmapsdir/%name.png
%_datadir/%name

%changelog
* Wed Mar 28 2018 Andrey Solodovnikov <hepoh@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus (Closes: 32412)
