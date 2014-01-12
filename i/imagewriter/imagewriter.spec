# For ALT >= 7
    %define definedbackend USEUDISKS2
# for ALT 6
# #    %define definedbackend USEUDISKS

Name:           imagewriter
Summary:        SUSE Imagewriter
Version:        1.10
Release:        alt1
Url:            https://github.com/mbarringer/imagewriter
Group:          Archiving/Other
License:        GPLv2
Source:         imagewriter-%version.tar.gz

BuildRequires: gcc-c++ libqt4-devel

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
* Sun Jan 12 2014 Motsyo Gennadi <drool@altlinux.ru> 1.10-alt1
- initial build for ALT Linux from RHEL pakcage
