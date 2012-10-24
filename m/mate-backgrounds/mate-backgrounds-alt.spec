%define _libexecdir %_prefix/libexec
#different version fc17
Summary: 		Desktop backgrounds packaged with the MATE desktop
Name: 			mate-backgrounds
Version: 		1.4.0
Release: 		alt1_1.1.1
License: 		GPLv2
Group: 			Graphics
URL: 			http://pub.mate-desktop.org
Source0: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Patch0: 		mate-backgrounds_change_backgrounds_path.patch
BuildArch: 		noarch
BuildRequires: 	intltool
BuildRequires: 	gettext
BuildRequires:  mate-common
BuildRequires:  glib2-devel
Requires: 		design-graphics
#fc17
#Requires: 		beefy-miracle-backgrounds-single
#Requires: 		beefy-miracle-backgrounds-gnome

%description
The mate-backgrounds package contains images and tiles
to use for your desktop background which are packaged
with the MATE desktop.

%prep
%setup -q
#patch0 -p1 -b .mate-backgrounds_change
sed -i -e s,/pixmaps/backgrounds/,/backgrounds/,g `grep -rl /pixmaps/backgrounds/ .`
NOCONFIGURE=1 ./autogen.sh

%build

%configure


make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING NEWS README AUTHORS
%{_datadir}/mate-background-properties
%{_datadir}/backgrounds/mate/*
%_datadir/locale/*/*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Tue Oct 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- adapted alt patches

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

