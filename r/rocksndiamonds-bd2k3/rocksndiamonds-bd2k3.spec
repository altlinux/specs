Name: rocksndiamonds-bd2k3
Version: 1.0.0
Release: alt1

Summary: Extra levels for Rocks'n'Diamonds game
Group: Games/Arcade
License: GPL
URL: http://www.artsoft.org/rocksndiamonds/levels/BD2K3/
BuildArchitectures: noarch
AutoReqProv: no
Requires: rocksndiamonds >= 3.0.8

Source: BD2K3-1.0.0.zip

# Automatically added by buildreq on Wed May 05 2004 (-bi)
BuildRequires: unzip

%description
Rocks'n'Diamonds is a nice little game with color graphics
and sound for your Unix system.

This is a package with "BD2K3" extra levels.

%prep
%setup -qc

%install
mkdir -p $RPM_BUILD_ROOT%_gamesdatadir/rocksndiamonds/levels
cp -a BD2K3 $RPM_BUILD_ROOT%_gamesdatadir/rocksndiamonds/levels

%define _compress_method none
%define _strip_method none

%files
%_gamesdatadir/rocksndiamonds/levels/*

%changelog
* Wed May 05 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- Initial spec.
