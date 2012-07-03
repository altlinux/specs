Name: ksubtile
Version: 1.3
Release: alt3

Summary: KDE application for subtitles editing
License: GPL
Group: Video

Url: http://ksubtile.sourceforge.net

BuildRequires: kdelibs-devel libjpeg-devel
BuildRequires: gcc4.5-c++
Source: %name-%version.tar.bz2
Patch0: ksubtile-1.3_curposLength_Line3Conn.patch
Patch1: amarok-alt-DSO.patch
Patch2: ksubtile-fix-automake-detection.patch

Packager: Roman Savochenko <rom_as@altlinux.ru>

%description
This is an editor for the KDE environment to edit, make and save subtitles in the SRT subtitle format.
It is made by Tom Deblauwe.

%prep
%setup
%patch0 -p1
%patch1
%patch2

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
%make -f admin/Makefile.common svn

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure
%make_build

%install
%K3install
%K3find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_K3bindir/%name
%_K3datadir/applnk/Editors/%name.desktop
%_K3datadir/apps/%name
/usr/share/kde/icons/hicolor/16x16/apps/%name.png
/usr/share/kde/icons/hicolor/32x32/apps/%name.png
%_K3datadir/mimelnk/application/srt.desktop
/usr/share/kde/doc/HTML/en/ksubtile

%changelog
* Fri May 25 2012 Roman Savochenko <rom_as@altlinux.ru> 1.3-alt3
- Build for TDE 3.5.13 release.
- Curpos length activate and set realised.
- Line3 connection is fixed.

* Thu Mar 03 2011 Timur Aitov <timonbl4@altlinux.org> 1.3-alt2
- move to alternate place

* Mon Sep 15 2008 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt1
- Initial build for ALT Linux
