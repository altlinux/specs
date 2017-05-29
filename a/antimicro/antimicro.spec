Name: antimicro
Version: 2.23
Release: alt1

Summary: Graphical program used to map keyboard buttons and mouse controls to a gamepad
License: GPLv3+
Group: System/Configuration/Hardware

Url: https://github.com/Ryochan7/%name
Source: %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
# qt5: base, tools
BuildRequires: libqt4-devel
BuildRequires: libSDL2-devel
# for appdata
BuildRequires: libappstream-glib
BuildRequires: itstool
BuildRequires: gettext

%description
AntiMicro is a graphical program used to map keyboard keys and
mouse controls to a gamepad. This program is useful for playing
PC games using a gamepad that do not have any form of built-in
gamepad support. AntiMicro was inspired by QJoyPad but has
additional features.

%prep
%setup

%build
%cmake_insource \
	-DAPPDATA=ON \
	-DWITH_X11=ON \
	-DWITH_XTEST=ON \
	-DWITH_UINPUT=ON \
	#
%make_build appdata

%install
%makeinstall_std

# install and verify desktop file
%_bindir/desktop-file-install other/%name.desktop

# validate appdata file
appstream-util validate-relax --nonet \
	%buildroot%_datadir/appdata/%name.appdata.xml

%find_lang %name --with-qt

%files -f %name.lang
%doc Changelog gpl.txt README.md
%_bindir/%name
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%_datadir/mime/packages/%name.xml
%_datadir/appdata/%name.appdata.xml
%_man1dir/%name.1*

# TODO:
# - consider qt5 build?

%changelog
* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 2.23-alt1
- 2.23

* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 2.20.2-alt1
- 2.20.2

* Thu May 07 2015 Michael Shigorin <mike@altlinux.org> 2.14-alt1
- 2.14

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 2.11.1-alt1
- 2.11.1
- added appdata file

* Sun Dec 28 2014 Michael Shigorin <mike@altlinux.org> 2.10-alt1
- built for ALT Linux (as per user request)
  + based on fedora and opensuse spec files
