Name: coriander
Version: 2.0.1
Release: alt1.qa1

Summary: Control a 1394 digital camera interactively

License: GPLv2+
Group: Video
Url: http://damien.douxchamps.net/ieee1394/coriander/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/coriander/%name-%version.tar

# Automatically added by buildreq on Sun Oct 17 2010
BuildRequires: libSDL-devel libXext-devel libXv-devel libdc1394-devel libgnomeui-devel
BuildRequires: desktop-file-utils

# FIXME: can use missed ftplib http://nbpfaus.net/~pfau/ftplib/

%description
Coriander is a GUI that let you control your 1394 digital video camera
interactively. It features SDL display, FTP image posting, file saving,
and video streaming. It is for IIDC cameras, not for consumer grade DV
cameras.

%prep
%setup

cat <<EOF >%name.desktop
[Desktop Entry]
Name=Coriander
Comment=Control a 1394 digital video camera
Exec=coriander
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;
Icon=%_pixmapsdir/%name/%name-icon.png
EOF

# used, but missed
cat <<EOF >mkinstalldirs
mkdir -p "\$@"
EOF
chmod 755 mkinstalldirs

%build
%configure
%make_build

%install
%makeinstall_std
install -d -m0755 %buildroot%_desktopdir/
install -m0644 %name.desktop %buildroot%_desktopdir
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Video \
	--add-category=Recorder \
	%buildroot%_desktopdir/coriander.desktop

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/%name
%_pixmapsdir/coriander/coriander-*.png
%_desktopdir/%name.desktop

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for coriander

* Sun Oct 17 2010 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- initial build for ALT Linux Sisyphus

* Sat Jan 19 2008 Tim Niemueller <tim@niemueller.de> - 2.0.0-0.6.rc6
- Long source URL

* Sat Jan 19 2008 Tim Niemueller <tim@niemueller.de> - 2.0.0-0.5.rc6
- Upgrade to 2.0.0-rc6
- Use autotooly only if build is a CVS build
- Do not require libdc1394 >= 2.0.0, automatically handled correctly
- Fixed desktop file glitches
- Add Icon entry for desktop file
- Added ftplib BR to support FTP upload
- Removed Application category to make desktop-file-validate happy

* Wed Jan 16 2008 Tim Niemueller <tim@niemueller.de> - 2.0.0-rc5.4.cvs20080116
- Fixed several rpmlint errors

* Wed Jan 16 2008 Tim Niemueller <tim@niemueller.de> - 2.0.0-rc5.3.cvs20080116
- Updated to release 2.0.0-rc5.cvs20080116

* Mon Nov 26 2007 Tim Niemueller <tim@niemueller.de> - 2.0.0-rc5.2.cvs20071126
- Updated to release 2.0.0-rc5.cvs20071126

* Wed Aug 16 2006 Tim Niemueller <tim@niemueller.de> - 2.0.0-rc1.1
- Updated to release 2.0.0-rc1

* Mon May 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.0-0.pre6
- Updated to release 2.0.0pre6.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.0-0.pre5
- Updated to release 2.0.0pre5.

* Mon Aug 29 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.0-0.pre3
- Initial package.
