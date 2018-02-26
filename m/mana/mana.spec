Name: mana
Version: 1.0.0
Release: alt0.beta2.qa1
License: GPLv2+
Url: http://themanaworld.org/
Packager: Egor Glukhov <kaman@altlinux.org>
Obsoletes: tmw
Source0: %name-%version.tar

BuildRequires: gcc-c++ libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel
BuildRequires: libSDL_net-devel libSDL_ttf-devel libcurl-devel libenet-devel
BuildRequires: libguichan-devel libphysfs-devel libpng-devel libxml2-devel

Summary: The Mana World is a free 2D MMORPG
Group: Games/Other
BuildRequires: desktop-file-utils

%description
The Mana World (TMW) is a serious effort to create an innovative
free and open source MMORPG. TMW uses 2D graphics and aims to create
a large and diverse interactive world.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=RolePlaying \
	%buildroot%_desktopdir/mana.desktop

%files -f %name.lang
%doc AUTHORS NEWS README docs
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_datadir/%name
%_man6dir/%name.6.gz

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.0-alt0.beta2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for mana

* Fri Dec 17 2010 Egor Glukhov <kaman@altlinux.org> 1.0.0-alt0.beta2
- 1.0.0 beta2
