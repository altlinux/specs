Name: quodlibet
Version: 2.4.1
Release: alt1

Summary: audio library tagger, manager, and player for GTK+
License: GPLv2
Group: Sound

Url: http://code.google.com/p/quodlibet/
Source: %name-%version.tar

PreReq: exfalso = %version-%release
BuildRequires: libgtk+2-devel python-devel python-module-pygtk-devel python-module-mutagen python-module-gst intltool
BuildRequires: desktop-file-utils

%description
Quod Libet is a music management program. It provides several different
ways to view your audio library, as well as support for Internet radio
and audio feeds. It has extremely flexible metadata tag editing and
searching capabilities.

%package -n exfalso
Summary: audio tag editor for GTK+
Group: Sound

%description -n exfalso
exfalso lets you display and edit any tags you want in the file. And it
lets you do this for all the file formats it supports -- Ogg Vorbis,
FLAC, MP3, Musepack, and MOD.

%prep
%setup -q

%build
%python_build

%install
%python_install --install-purelib %python_sitelibdir
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
cp  %buildroot%python_sitelibdir/%name/images/hicolor/scalable/apps/*.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/exfalso.desktop

%files
%_bindir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop
%_man1dir/%name.*
%doc COPYING NEWS HACKING README

%files -n exfalso -f %name.lang
%_bindir/exfalso
%_iconsdir/hicolor/scalable/apps/exfalso.svg
%_desktopdir/exfalso.desktop
%_man1dir/exfalso.*
%python_sitelibdir/%name
%python_sitelibdir/%name-%version-py*

%changelog
* Tue Oct 09 2012 Vladimir Lettiev <crux@altlinux.ru> 2.4.1-alt1
- New version 2.4.1

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.1-alt1.qa1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.1-alt1.qa1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for exfalso

* Sun Mar 28 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2.1-alt1
- New version 2.2.1

* Wed Mar 17 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2-alt1
- initial build

