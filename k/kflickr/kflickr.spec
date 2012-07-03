Name:         kflickr
Version:      0.9.1
Release:      alt2.qa3
Summary:      KFlickr is a standalone KDE application that allows for easy upload of your favourite photos to your Flickr.com account.
License:      GPL
Group:        Graphics
URL:          http://kflickr.sourceforge.net
Packager:     Ilya Mashkin <oddity at altlinux.ru>
Source0:      %name-%version.tar.bz2
Source1:      %name.desktop
Patch0:       %name-0.9.1-alt-DSO.patch

# Automatically added by buildreq on Thu Oct 13 2005
BuildRequires: fontconfig freetype2 gcc-c++ kde-settings kdelibs-devel kdepim-devel kdepim-libs libjpeg-devel libpng-devel libqt3-devel libqt3-settings libstdc++-devel qt3-designer xml-utils zlib-devel libtqt-devel
BuildRequires: desktop-file-utils

%description
KFlickr is a standalone KDE application that allows for easy upload of your favourite photos to your Flickr.com account. KFlickr provides the following features:

* drag and drop from other applications (such as Konqueror and DigiKam)
* easy editing of your photo properties (title, description, privacy, tags)
* access to your Flickr.com list of tags
* support for more than one user
* image preview
* support for the new Flickr.com authentication

			

%prep
%setup
%patch0 -p2
#sed -i "s/\.la\"/\.so\"/g" configure
#sed -i "s/\.la\"/\.so\"/g" admin/acinclude.m4.in 
#sed -i "s/\.la\"/\.so\"/g" aclocal.m4


%build
%configure --disable-rpath --without-arts
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make CXXFLAGS="-I%_includedir/tqtinterface"

%install
%makeinstall
%find_lang %name
rm -rf %buildroot%_datadir/applnk
mkdir -p %buildroot%_datadir/applications
install -m644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Database \
	%buildroot%_desktopdir/kflickr.desktop

%files -f %name.lang 
%doc AUTHORS COPYING ChangeLog README NEWS TODO
%_bindir/%name
%_datadir/applications/*.desktop
%_datadir/applications/kde/*.desktop
%_iconsdir/*/*/*/%name.png
%_datadir/apps/%name
%_datadir/apps/kflickrpart/kflickrpart.rc
%_datadir/apps/konqueror/servicemenus/kflickr_servicemenu.desktop
%_datadir/services/kflickrpart.desktop
%_datadir/doc/HTML/en/%name
%_man1dir/%name.1.gz
%_libdir/kde3/*.so

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2.qa3
- Fixed build

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2.qa2
- Removed bad RPATH

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.1-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for kflickr
  * postclean-03-private-rpm-macros for the spec file

* Sun Apr 17 2011 Ilya Mashkin <oddity at altlinux dot ru> 0.9.1-alt2
- fix build

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.1-alt1.2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for kflickr
  * postclean-05-filetriggers for spec file

* Sat Mar 01 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.1-alt1.2
- rebuild for x86_64

* Fri Feb 29 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.1-alt1.1
- rebuild

* Mon Feb 25 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.1-alt1
- 0.9.1
- add missed files

* Wed Jan 11 2006 Eugene Suchkov <cityhawk@altlinux.ru> 0.5-alt1
- New version build for sisyphus
- Menu bugfix

* Thu Dec 01 2005 Eugene Suchkov <cityhawk@altlinux.ru> 0.4-alt1
New version build for sisyphus

* Thu Oct 13 2005 Eugene Suchkov <cityhawk@altlinux.ru> 0.3-alt1
Inital build for sisyphus

