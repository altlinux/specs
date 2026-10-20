Name: pardus-pen
Version: 4.3.0
Release: alt1

Summary: Fast tool for drawing with a pen over the screen
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/pardus/pardus-pen

# Source-url: https://github.com/pardus/pardus-pen.git/tree/debian/%version
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson qt6-base-devel qt6-svg-devel
BuildRequires: libpoppler-qt6-devel libdbus-devel libarchive-devel

%description
Pardus Pen is a fast and simple tool for drawing on the screen and on a
whiteboard with a pen, designed for interactive boards and touch panels.
It supports pens of different sizes and colors, selection, backgrounds,
screenshots, PDF import and saving of drawings.

%prep
%setup

%build
export PATH=%_libdir/qt6/libexec:$PATH
%meson \
	-Dsave=true \
	-Detap19=false \
	-Dresources=true \
	-Dscreenshot=true \
	-Dqt=6
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/pardus/
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/mime/packages/*.xml
%_datadir/metainfo/*.xml

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 4.3.0-alt1
- initial build for Sisyphus
