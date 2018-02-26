Summary:	is a program for the fast creation of covers for cd/dvd cases and boxes
Name:		koverartist
Version:	0.5
Release:	alt3.1
License:	GPLv2
Packager:       Motsyo Gennadi <drool@altlinux.ru>
Group:		Publishing
Url:		http://kde-apps.org/content/show.php/KoverArtist?content=38195
Source0:	http://members.inode.at/499177/software/koverartist/%name-%version.tar.bz2
Patch0:		%name-0.5-alt_desktopdir.diff 
Patch1:		%name-0.5-alt_freedesktop.diff
Patch2:		%name-0.5-gcc43.patch

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
* Wed Apr 20 2011 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt3.1
- fix build for KDE3 from Sisyphus

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt3
- delete post/postun scripts (new rpm)

* Mon Oct 27 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt2
- fix fog gcc4.3 (patch from FC9)
- cleanup buildrequires

* Sun May 25 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt1
- initial build for ALT Linux
