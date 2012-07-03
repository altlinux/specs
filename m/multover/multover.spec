BuildRequires: desktop-file-utils
Name: multover
Version: 0.02
Release: alt1
Summary: An Xdialog/kdialog3 script for easy animation assebmly
Group: Graphics
License: Public domain

Source: %name-%version.tar
URL: http://git.altlinux.org/people/george/packages/?p=%name.git

BuildREquires: ImageMagick ImageMagick-doc

Requires: nish-functions >= 1.0

BuildArch: noarch

# Automatically added by buildreq on Mon Jun 13 2011
# optimized out: ImageMagick-tools fontconfig
BuildRequires: ImageMagick-doc

%description
Multover is an Xdialog-based shell script used for converting a set of
images into an AVI animation file. It performs not more than unification
of images' size, FPS selection and preview-recreate workflow.

%prep
%setup

%build
# XXX buggy 128x128 generation skipped
convert /usr/share/doc/ImageMagick-*/images/wand.ico %name-%%d.png || :
sed '
	s@^Comment=$@Comment=%summary@g
	s/^Exec=$/Exec=%name/g
	s/^Icon=$/Icon=%name/g

' %name.desktop.in > %name.desktop

%install
install -D %name %buildroot/%_bindir/%name
install -D create_example %buildroot/%_bindir/%{name}_create_example
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -D %name-0.png %buildroot%_iconsdir/hicolor/16x16/%name.png
install -D %name-1.png %buildroot%_iconsdir/hicolor/32x32/%name.png
install -D %name-2.png %buildroot%_iconsdir/hicolor/64x64/%name.png
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
# install -D %name-3.png %buildroot%_iconsdir/hicolor/128x128/%name.png

%files
%_bindir/*
%_iconsdir/hicolor/*/*.png
%_desktopdir/*

%changelog
* Tue Jun 14 2011 Fr. Br. George <george@altlinux.ru> 0.02-alt1
- KDialog support removed
- Optionally create an example from gui

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.01-alt7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for multover

* Wed Apr 28 2010 Fr. Br. George <george@altlinux.ru> 0.01-alt7
- Desktop file fixes

* Mon Apr 26 2010 Fr. Br. George <george@altlinux.ru> 0.01-alt6
- Convert bug workaround
- Switch $LANG to UTF

* Sat Mar 21 2009 Fr. Br. George <george@altlinux.ru> 0.01-alt5
- Typo (#19177) fixed

* Fri Dec 19 2008 Fr. Br. George <george@altlinux.ru> 0.01-alt4
- Idiotic .desktop bug fix

* Fri Dec 19 2008 Fr. Br. George <george@altlinux.ru> 0.01-alt3
- Both Xdialog and kdialog are implemented
- Remode Xdialog and kdialog dependency

* Thu Dec 18 2008 Fr. Br. George <george@altlinux.ru> 0.01-alt1
- Swtching to ALT packaging
