Name:         kdm-themes-12
Summary:      12 eye-candy kdm-themes
Version:      1
Release:      alt1
License:      GPL
Group:        Graphical desktop/KDE
URL:          http://kde-look.org
Packager:     Mikhail Pokidko <pma@altlinux.org>
Source1:      daemonic-smegma_1.0.tar.gz
Source2:      firefighter.tar.gz
Source3:      kdm-beo.tar.gz
Source4:      natur_kdm.tar.gz
Source5:      sidux-highway.tar.gz
Source6:      TheLight_kde.tar.gz
Source7:      AlfaKDM.tar.gz
Source8:      Beach.tar.gz
Source9:      dontyoudare.tar.bz2
Source10:      hardDrive.tar.gz
Source11:      kitty.tar.gz
Source12:      KdmLinux.tar.gz

Requires: kdmtheme, kdebase-kdm

%description
Dozen of very nice themes for KDM

%prep
tar xvfz %SOURCE1
tar xvfz %SOURCE2
tar xvfz %SOURCE3
tar xvfz %SOURCE4
tar xvfz %SOURCE5
tar xvfz %SOURCE6
tar xvfz %SOURCE7
tar xvfz %SOURCE8
bzip2 -cd %SOURCE9 | tar xvf -
tar xvfz %SOURCE10
tar xvfz %SOURCE11
tar xvfz %SOURCE12

#build

%install
mkdir -p %buildroot%_datadir/apps/kdm/themes/KdmLinux \
	%buildroot%_datadir/apps/kdm/themes/natur_kdm \
	%buildroot%_datadir/apps/kdm/themes/firefighter \
	%buildroot%_datadir/apps/kdm/themes/Beach \
	%buildroot%_datadir/apps/kdm/themes/AlfaKDM \
	%buildroot%_datadir/apps/kdm/themes/TheLight_kde \
	%buildroot%_datadir/apps/kdm/themes/daemonic-smegma_1.0 \
	%buildroot%_datadir/apps/kdm/themes/dontyoudare \
	%buildroot%_datadir/apps/kdm/themes/hardDrive \
	%buildroot%_datadir/apps/kdm/themes/kdm-beo \
	%buildroot%_datadir/apps/kdm/themes/kitty \
	%buildroot%_datadir/apps/kdm/themes/sidux-highway
cp -p natur_kdm/* %buildroot%_datadir/apps/kdm/themes/natur_kdm/
cp -p KdmLinux/* %buildroot%_datadir/apps/kdm/themes/KdmLinux/
cp -p firefighter/* %buildroot%_datadir/apps/kdm/themes/firefighter/
cp -p Beach/* %buildroot%_datadir/apps/kdm/themes/Beach/
cp -p AlfaKDM/* %buildroot%_datadir/apps/kdm/themes/AlfaKDM/
cp -p TheLight_kde/* %buildroot%_datadir/apps/kdm/themes/TheLight_kde/
cp -p daemonic-smegma_1.0/* %buildroot%_datadir/apps/kdm/themes/daemonic-smegma_1.0/
cp -p dontyoudare/* %buildroot%_datadir/apps/kdm/themes/dontyoudare/
cp -p hardDrive/* %buildroot%_datadir/apps/kdm/themes/hardDrive/
cp -p kdm-beo/* %buildroot%_datadir/apps/kdm/themes/kdm-beo/
cp -p kitty/* %buildroot%_datadir/apps/kdm/themes/kitty/

cp -p sidux-highway/* %buildroot%_datadir/apps/kdm/themes/sidux-highway/

%files
%_datadir/apps/kdm/themes/*

%changelog
* Fri Sep 14 2007 Pokidko Mikhail <pma@altlinux.org> 1-alt1
- First version


