Name: gimagereader
Version: 2.93
Release: alt1

Summary: A graphical GTK frontend to tesseract-ocr

License: GPLv3+
Group: Office
Url: http://sourceforge.net/projects/gimagereader/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://sourceforge.net/projects/gimagereader/files/%version/%name-%version.tar

# Workaround for rbhz#1065695
Patch: gimagereader_no-sane-exit.patch

# manually removed:  python3 ruby ruby-stdlibs 
# Automatically added by buildreq on Fri Oct 10 2014
# optimized out: at-spi2-atk fontconfig fontconfig-devel glib2-devel gnu-config libX11-devel libat-spi2-core libatk-devel libatkmm-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcairomm-devel libcloog-isl4 libenchant-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglibmm-devel libgtk+3-devel libgtkmm3-devel libgtkspell3-devel libpango-devel libpangomm-devel libpoppler8-glib libsigc++2-devel libstdc++-devel libwayland-client libwayland-cursor libwayland-server perl-XML-Parser pkg-config python3-base tesseract xorg-xproto-devel
BuildRequires: gcc-c++ glibc-devel intltool libdb4-devel libgtkspellmm3-devel libpoppler-glib-devel libsane-devel tesseract-devel

%description
gImageReader is a simple Gtk front-end to tesseract. Features include:
 - Automatic page layout detection
 - User can manually define and adjust recognition regions
 - Import images from disk, scanning devices, clipboard and screenshots
 - Supports multipage PDF documents
 - Recognized text displayed directly next to the image
 - Editing of output text, including search/replace and removing line breaks
 - Spellchecking for output text (if corresponding dictionary installed)

%prep
%setup
%patch0 -p1

%build
%configure --disable-versioncheck
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/%name
%_datadir/%name/
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/256x256/apps/%name.png
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml

%changelog
* Fri Oct 10 2014 Vitaly Lipatov <lav@altlinux.ru> 2.93-alt1
- initial build for ALT Linux Sisyphus

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Sandro Mani <manisandro@gmail.com> - 2.93-4
- Rebuild (tesseract)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 Sandro Mani <manisandro@gmail.com> - 2.93-2
- Workaround rhbz #1065695

* Wed Apr 30 2014 Sandro Mani <manisandro@gmail.com> - 2.93-1
- Update to 2.93

* Wed Mar 19 2014 Sandro Mani <manisandro@gmail.com> - 2.92-1
- Update to 2.92

* Thu Feb 20 2014 Sandro Mani <manisandro@gmail.com> - 2.91-1
- Update to 2.91

* Sat Feb 15 2014 Sandro Mani <manisandro@gmail.com> - 2.91-0.2git20140216
- Update to newer 2.91 pre, work around crash at exit

* Thu Feb 13 2014 Sandro Mani <manisandro@gmail.com> - 2.91-0.1
- Update to 2.91 pre

* Thu Feb 13 2014 Sandro Mani <manisandro@gmail.com> - 2.90-3
- Require hicolor-icon-theme
- Add missing icon theme scriptlets

* Wed Feb 12 2014 Sandro Mani <manisandro@gmail.com> - 2.90-2
- Add appdata file

* Tue Feb 11 2014 Sandro Mani <manisandro@gmail.com> - 2.90-1
- Initial package.
