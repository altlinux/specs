%define qtdir %_qt3dir
%define kdedir %_K3prefix

Name:		kvkbd
Version:	0.5
Release:	alt4
Summary:	Virtual Keyboard for KDE
Source0:	http://www.kde-apps.org/CONTENT/content-files/56019-%name-%version.tar.bz2
Source1:	hi48-app-%name.png
URL:		http://www.kde-apps.org/content/show.php/Kvkbd?content=56019
Group:		Accessibility
License:	GPLv2
Patch0:		%name-0.5-icon_48.patch
Patch1:		%name-0.5-alt_desktopdir.patch
Patch2:		%name-0.4.7-alt_desktop.patch
Patch3:		%name-0.5-gcc43.patch
Patch4:		%name-0.5-admin-new-autotools.patch
Patch5:		tde-3.5.13-build-defdir-autotool.patch
Patch6:		%name-0.5-shift-togle.patch

# Automatically added by buildreq on Thu Apr 21 2011 (-bi)
# optimized out: elfutils fontconfig kdelibs libICE-devel libSM-devel libX11-devel libXext-devel libXi-devel libXrender-devel libXt-devel libart_lgpl-devel libidn-devel libpng-devel libqt3-devel libqt3-settings libstdc++-devel libtqt-devel libutempter-devel xorg-inputproto-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: gcc-c++ imake kdelibs-devel libXtst-devel xml-utils xorg-cf-files

%description
A nice virtual keyboard for KDE with systray and dock widget
support.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5
%patch6 -p1

cp %SOURCE1 src/

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

%K3configure
%make_build

%install
%K3install

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_K3bindir/%name
%_K3datadir/applications/%name.desktop
%_K3datadir/apps/%name
%_kde3_iconsdir/*/*/apps/%name.png

%changelog
* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.5-alt4
- Build for TDE 3.5.13 release
- Shift toggle fix patch by Roman Savochenko is added.

* Thu Apr 21 2011 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt3.2
- fix build for KDE3 from Sisyphus

* Mon May 25 2009 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt3.1
- fix for automake-1.11

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt3
- delete post/postun scripts (new rpm)

* Mon Oct 27 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt2
- fix fog gcc4.3 (patch from Gentoo)

* Mon Jun 16 2008 Motsyo Gennadi <drool@altlinux.ru> 0.5-alt1
- 0.5

* Thu Apr 03 2008 Motsyo Gennadi <drool@altlinux.ru> 0.4.9-alt1
- 0.4.9
- fix URL
- build for Sisyphus

* Fri Nov 09 2007 Motsyo Gennadi <drool@altlinux.ru> 0.4.7-alt1
- initial build for ALT Linux
