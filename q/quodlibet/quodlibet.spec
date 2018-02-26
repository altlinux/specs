Name: quodlibet
Version: 2.2.1
Release: alt1.qa1.1.1
Summary: music management program

Group: Sound
License: GPLv2
Url: http://code.google.com/p/quodlibet/

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

PreReq: exfalso = %version-%release
BuildRequires: libgtk+2-devel python-devel python-module-pygtk-devel python-module-mutagen python-module-gst intltool ImageMagick
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
mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir}
for n in %name exfalso
do 
  convert %buildroot%python_sitelibdir/%name/images/$n.png -scale 16x16 %buildroot%_miconsdir/$n.png
  convert %buildroot%python_sitelibdir/%name/images/$n.png -scale 32x32 %buildroot%_niconsdir/$n.png
  convert %buildroot%python_sitelibdir/%name/images/$n.png -scale 48x48 %buildroot%_liconsdir/$n.png
done
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/exfalso.desktop

%files
%_bindir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop
%_man1dir/%name.*
%doc COPYING NEWS HACKING README

%files -n exfalso -f %name.lang
%_bindir/exfalso
%_miconsdir/exfalso.png
%_niconsdir/exfalso.png
%_liconsdir/exfalso.png
%_desktopdir/exfalso.desktop
%_man1dir/exfalso.*
%python_sitelibdir/%name
%python_sitelibdir/%name-%version-py*

%changelog
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

