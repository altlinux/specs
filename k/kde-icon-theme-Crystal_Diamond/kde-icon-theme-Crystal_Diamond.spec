%define theme Crystal_Diamond
%define srcname KDE_Crystal_Diamond_2.8_Oxygen_Mod

Name: kde-icon-theme-%theme
Version: 2.8
Release: alt1

Summary: Crystal Diamond Icons 2.8: Wonderful, Realistic and complete Theme for your KDE
License: GPL
Group: Graphical desktop/KDE
Url: http://www.paolocampitelli.com/kde-icons/

Packager: Konstantin Baev <kipruss@altlinux.org>

Source: %srcname.tar

BuildArch: noarch

%description
Crystal Diamond is a wonderful and realistic theme for Kde.
I take the best icons from Crystal Project, Realistik, Vista Ispirate,
Nuove XT, Crystal Clear, OSX, Debian Icons and many other and I made
this Icon Theme. The icons are not mine! I simply take the best icons
(for me) and made these packs!

There are different mod such classical, shining, gentoo, arch,
debian and kubuntu. The only difference between "Mods" is Kmenu except
for Debian Mod and Oxygen Mod (also Kcontrol, Trash and Folder Icon).

There are more icons for one application. For example there are 6 different
icons for Firefox! If you like, change into your favorite icon!
(Left click, change icon). In the second image for example,
I change firefox icon.

There are many Mod for your distro:

* Classical
* Shining
* Gentoo
* Debian
* Kubuntu
* Arch (New Logo!)
* FreeBsd/PcBsd
* Red Hat
* MacOsX
* MacOsX Finder
* Mandriva
* Slackware
* Suse Classic
* Suse Alternative
* Ubuntu
* OpenBsd
* Fedora
* Oxygen (NEW!!!) - this mod is in the current rpm

%prep
%setup -q -n %srcname

find -type f -exec chmod a-x {} \;

%install
mkdir -p %buildroot/%_iconsdir/%theme/
cp -ar [^R]* %buildroot/%_iconsdir/%theme/

%files
%doc README
%_iconsdir/%theme

%changelog
* Wed Aug 13 2008 Konstantin Baev <kipruss@altlinux.org> 2.8-alt1
- initial build for Sisyphus
