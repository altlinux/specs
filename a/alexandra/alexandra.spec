Name:		alexandra
Version:	1.5.1
Release:	alt1
Summary:	A small and user friendly opensource video library with great potential
License:	GPLv2
Group:		Video
Url:		http://alexandra-qt.sourceforge.net/
Source0:	%name-%version.tar.gz

BuildRequires: gcc-c++ libmediainfo-devel qt5-base-devel qt5-tools qt5-translations

%description
Alexandra Video Library - a simple and convenient program for the organization
and management of the home video library. You can completely customize the
catalog movies in a list, add a description and detailed information about the
movie in a lot of fields available, attach posters and much more. Directly from
the program, you can start playing the film, with the available choice of any
video player on your computer if you wish.

A small and user friendly opensource video library with great potential,
written in C++ using Qt5 framework.

%prep
%setup

%build
%qmake_qt5 %name.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%doc LICENSE README.md CHANGELOG
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Fri Jan 26 2018 Motsyo Gennadi <drool@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Thu Apr 14 2016 Motsyo Gennadi <drool@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Sun Oct 18 2015 Motsyo Gennadi <drool@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Sat Aug 29 2015 Motsyo Gennadi <drool@altlinux.ru> 1.3.0-alt1.1
- fix BuildRequires (tnx to Gleb Fotengauer-Malinovskiy for note)

* Fri Aug 28 2015 Motsyo Gennadi <drool@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Tue Aug 25 2015 Motsyo Gennadi <drool@altlinux.ru> 1.2.3-alt2.1
- rebuild with libmediainfo-0.7.76

* Sun Aug 23 2015 Motsyo Gennadi <drool@altlinux.ru> 1.2.3-alt2
- fix build for Sisyphus (build with gcc4.7, tnx to Michael Shigorin)

* Fri Aug 14 2015 Motsyo Gennadi <drool@altlinux.ru> 1.2.3-alt1
- initial build for ALT Linux
