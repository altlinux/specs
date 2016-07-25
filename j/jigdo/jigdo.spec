Name: jigdo
Version: 0.7.3
Release: alt5
Summary: Jigsaw Download
Group: Networking/WWW
License: GPL

Url: http://atterer.org/jigdo
Source: http://atterer.net/jigdo/%name-%version.tar.bz2
Patch1: jigdo-0.7.3-string_h.patch
Patch2: jigdo-0.7.3-curl_h.patch
Requires: wget

# Automatically added by buildreq on Thu May 30 2013
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel libwayland-client libwayland-server pkg-config zlib-devel
BuildRequires: ImageMagick-tools bzlib-devel gcc-c++ libcurl-devel libdb4-devel libgtk+2-devel wget

%description
Jigsaw Download, or short jigdo, is an intelligent tool that can be used on the
pieces of any chopped-up big file to create a special "template" file which
makes reassembly of the file very easy for users who only have the pieces.

What makes jigdo special is that there are no restrictions on what
offsets/sizes the individual pieces have in the original big image. This makes
the program very well suited for distributing CD/DVD images (or large zip/tar
archives) because you can put the files of the CD on an FTP server - when jigdo
is presented the files along with the template you generated, it is able to
recreate the CD image.

%prep
%setup
%patch1 -p1
%patch2 -p1

cat > %name.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Exec=%name
Icon=%name
Terminal=0
Name=Jigdo
Comment=Jigsaw Download
Categories=Application;Network
EOF

%build
%configure
%make_build

%define slist 16 32 48 64 72 96 128
for N in %slist; do
	convert gfx/jigdo-icon.png -geometry $N $N.png
done

%install
%makeinstall #_std
mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
for N in %slist; do
	install -D $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang
%doc README doc/TechDetails.txt doc/*.html
%_man1dir/*
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Mon Jul 25 2016 Fr. Br. George <george@altlinux.ru> 0.7.3-alt5
- Introduce curl.h patch

* Thu Sep 11 2014 Fr. Br. George <george@altlinux.ru> 0.7.3-alt5
- Rebuild with new libdb

* Thu May 30 2013 Fr. Br. George <george@altlinux.ru> 0.7.3-alt4
- Resurrected from orphaned using upstream spec

* Tue Sep 02 2008 Vladimir V Kamarzin <vvk@altlinux.org> 0.7.3-alt3
- Fixed directories packaging
- Updated desktop-file

* Tue Mar 27 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 0.7.3-alt2
- Rebuild with libcurl.so.4

* Tue Jun 06 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.7.3-alt1
- 0.7.3
- Added .desktop file

* Wed Feb 01 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.7.2-alt4
- Corrected buildrequires (libdb4.3-devel->libdb4-devel)

* Mon Oct 10 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.7.2-alt3
- rebuild with libdb4.3

* Tue Sep 13 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.7.2-alt2
- fixed package ownership of %_datadir/%name
- minor spec cleanup
- added Packager tag

* Tue Aug 30 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.7.2-alt1
- Initial build for Sisyphus.

