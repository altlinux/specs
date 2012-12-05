Summary:	is a program for the fast creation of covers for cd/dvd cases and boxes
Name:		koverartist
Version:	0.5
Release:	alt3.3
License:	GPLv2
Packager:       Motsyo Gennadi <drool@altlinux.ru>
Group:		Publishing
Url:		http://kde-apps.org/content/show.php/KoverArtist?content=38195
Source0:	http://members.inode.at/499177/software/koverartist/%name-%version.tar.bz2
Patch0:		%name-0.5-alt_desktopdir.diff 
Patch1:		%name-0.5-alt_freedesktop.diff
Patch2:		%name-0.5-gcc43.patch
Patch3:   %name-0.5-alt-DSO.patch
Patch4:   %name-0.5-alt-glibc-2.16.patch

BuildRequires: gcc-c++ imake kdelibs-devel libXext-devel libXt-devel libjpeg-devel libqt3-devel linux-libc-headers xml-utils xorg-cf-files

%description
KoverArtist is a program for the fast creation of covers for
cd/dvd cases and boxes. The main idea behind it is to be able
to create decent looking covers with some mouseclicks.

With series I usually start with one or two dvds, and add more as
more episodes are available. So the program - KoverArtist - had
to be flexible enough to handle that. This also requires changing
covers on the fly to use cases that can house more discs.

%prep
%setup -n %name
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p2
sed -i 's|/usr/lib/|%_libdir/|' configure

%build
%K3configure
%make_build CXXFLAGS="-I%_includedir/tqtinterface"

%install
%K3install
%K3find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS ChangeLog FAQ FILE_FORMATS NEWS README TODO
%_K3bindir/*
%_desktopdir/%name.desktop
%_K3datadir/apps/%name
%_K3mimelnk/application/*
%_K3datadir/icons/hicolor/*/apps/%name.png

%changelog
* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt3.3
- Fixed build with glibc 2.16

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt3.2
- Fixed build

* Wed Apr 20 2011 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt3.1
- fix build for KDE3 from Sisyphus

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt3
- delete post/postun scripts (new rpm)

* Mon Oct 27 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt2
- fix fog gcc4.3 (patch from FC9)
- cleanup buildrequires

* Sun May 25 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt1
- initial build for ALT Linux
