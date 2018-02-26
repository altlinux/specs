%define major 0.10
Name: jokosher
Version: %major.1
Release: alt1.1.qa1.1

Summary: Jokosher is a simple yet powerful multi-track studio

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL
Url: http://www.jokosher.org/
Group: Sound
BuildArch: noarch

#Source: http://www.jokosher.org/downloads/source/%name-%version.tar.bz2
Source: http://edge.launchpad.net/jokosher/%major/%version/+download/jokosher-%version.tar.gz

Requires: python%__python_version(libglade)
Requires: gst-plugins-base gst-plugins-good libgnonlin

# Automatically added by buildreq on Sun Jun 22 2008
BuildRequires: librarian python-devel rpm-build-compat
BuildRequires: desktop-file-utils

%description
Jokosher is a simple and poweful multi-track studio. Jokosher
provides a complete application for recording, editing, mixing and
exporting audio, and has been specifically designed with usability
in mind. The developers behind Jokosher have re-thought audio
production at every level, and created something devilishly simple
to use.

%prep
%setup -q

%build
%python_build

%install
%python_install

#DESTDIR=%buildroot mime-info-to-mime
#rm -rf %buildroot%_datadir/mime-info

# icon
install -dm 755 %buildroot%_pixmapsdir
install -m 644 Jokosher/jokosher-logo.png \
	%buildroot%_pixmapsdir/%name.png

# desktop-entry
cat >1%name.desktop << EOF
[Desktop Entry]
Version=%version
Encoding=UTF-8
Name=Jokosher Audio Editor
GenericName=Jokosher audio editor
Comment=Jokosher is a simple yet powerful multi-track studio
Exec=%name
Terminal=false
Type=Application
Icon=%name
StartupNotify=false
MimeType=application/x-jokosher;
EOF

%find_lang %name --with-gnome
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Audio \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/jokosher.desktop

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/%name
%dir %python_sitelibdir/Jokosher/
%python_sitelibdir/Jokosher/*.py*
%dir %python_sitelibdir/Jokosher/elements/
%python_sitelibdir/Jokosher/elements/*.py*
%dir %_datadir/%name/
%_datadir/%name/*.glade
%_datadir/%name/*.png
%dir %_datadir/%name/extensions
%_datadir/%name/extensions/*
%dir %_datadir/%name/pixmaps
%_datadir/%name/pixmaps/*
%dir %_datadir/%name/Instruments
%_datadir/%name/Instruments/*
%_iconsdir/hicolor/*/apps/%{name}*.png
%_pixmapsdir/%{name}*.png
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.1-alt1.1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.10.1-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for jokosher

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.1
- Rebuilt with python 2.6
- Built as noarch

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- new version (0.10.1)

* Sun Jun 22 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus (thanks to SUSE for spec)

* Fri Oct 12 2007 Toni Graffy <toni@links2linux.de> - 0.9-0.pm.2
- rebuild for openSUSE-10.3
* Fri May 25 2007 Toni Graffy <toni@links2linux.de> - 0.9-0.pm.1
- update to 0.9
- repacked as tar.bz2
* Fri Nov 24 2006 Toni Graffy <toni@links2linux.de> - 0.2-0.pm.1
- update to 0.2
* Mon Oct 23 2006 Toni Graffy <toni@links2linux.de> - 0.1-0.pm.1
- build for packman
* Fri Jul 28 2006 oc2pus@arcor.de 0.1-0.oc2pus.1
- Initial build 0.1
