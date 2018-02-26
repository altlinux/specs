Name: chmsee
Version: 1.3.1.1
Release: alt2

Summary: A GTK+2 based CHM viewer
Group: Office
License: GPLv2+
Url: http://code.google.com/p/%name/

Source: http://chmsee.googlecode.com/files/%name-%version.tar.gz
# http://code.google.com/p/chmsee/issues/detail?id=109
Patch: chmsee-1.3.1.1-webkit.patch

BuildRequires: cmake gcc-c++ intltool libchm-devel libgcrypt-devel
BuildRequires: libxml2-devel libpixman-devel libcairo-devel libglade-devel
BuildRequires: libwebkitgtk2-devel libnspr-devel
BuildRequires: desktop-file-utils

%description
ChmSee is an HTML Help viewer for Unix/Linux. It is based on CHMLIB
and use GTK+2 as frontend toolkit. Because of using gecko as HTML
rendering engine, ChmSee can support rich features of modern HTML
page, such as CSS and JavaScript.

%prep
%setup -q
%patch -p1

%build
%cmake
pushd BUILD
%make_build

%install
pushd BUILD
make DESTDIR=%buildroot install
popd

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=Office \
	--add-category=Viewer \
	%buildroot%_desktopdir/chmsee.desktop

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/%name
%_datadir/mime-info/*
%_datadir/pixmaps/*
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%doc AUTHORS NEWS README

%changelog
* Mon Aug 15 2011 Yuri N. Sedunov <aris@altlinux.org> 1.3.1.1-alt2
- built with webkit (ALT #26064)

* Fri Jun 10 2011 Yuri N. Sedunov <aris@altlinux.org> 1.3.1.1-alt1
- new version (ALT #25745)

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for chmsee

* Thu Apr 21 2011 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Tue Mar 02 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- first build for Sisyphus

