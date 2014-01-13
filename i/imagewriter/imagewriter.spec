%define definedbackend USEUDISKS
# ACHTUNG!!! Disable udisks for ALT >= 7 and enable for ALT 6
%def_disable udisks
%if_disabled udisks
%define definedbackend USEUDISKS2
%endif

Name:           imagewriter
Summary:        SUSE Imagewriter
Version:        1.10
Release:        alt3
Url:            https://github.com/mbarringer/imagewriter
Group:          Archiving/Other
License:        GPLv2
Source:         imagewriter-%version.tar.gz

BuildRequires: gcc-c++ libqt4-devel

%if_disabled udisks
Requires: udisks2
%else
Requires: udisks
%endif

%description
SUSE Imagewriter is a graphical utility for writing raw disk images & hybrid isos to USB keys

%prep
%setup

%build
qmake-qt4 "QMAKE_CFLAGS+=%optflags -DKIOSKHACK" "QMAKE_CXXFLAGS+=%optflags -DKIOSKHACK" PREFIX=%_prefix DEFINES=%definedbackend imagewriter.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Mon Jan 13 2014 Motsyo Gennadi <drool@altlinux.ru> 1.10-alt3
- fix switching UDISKS/UDISKS2 support and udisks/udisks2 requires

* Mon Jan 13 2014 Motsyo Gennadi <drool@altlinux.ru> 1.10-alt2
- update from git (fix UDISKS2 support)

* Sun Jan 12 2014 Motsyo Gennadi <drool@altlinux.ru> 1.10-alt1
- initial build for ALT Linux from RHEL pakcage
