%define definedbackend USEUDISKS
# ACHTUNG!!! Disable udisks for ALT >= 7 and enable for ALT 6
%def_disable udisks
%if_disabled udisks
%define definedbackend USEUDISKS2
%endif

Name:           imagewriter
Summary:        SUSE Imagewriter
Version:        1.10
Release:        alt6
Url:            https://github.com/mbarringer/imagewriter
Group:          Archiving/Other
License:        GPLv2
Source:         imagewriter-%version.tar.gz
Patch1:		imagewriter-add-missing-i18n.patch
Patch2:		imagewriter-add-russian-localization.patch

# https://github.com/openSUSE/imagewriter/pull/28/commits/3164e25267243ef4983f53ef5c1f849d3301c36f
Patch3:     3164e25267243ef4983f53ef5c1f849d3301c36f.patch

BuildRequires: gcc-c++ qt5-tools qt5-base-devel

%if_disabled udisks
Requires: udisks2
%else
Requires: udisks
%endif

%description
SUSE Imagewriter is a graphical utility for writing raw disk images & hybrid isos to USB keys

%prep
%setup
%patch1 -p2
%patch2 -p2
%patch3 -p1
# Generate localization files
lrelease-qt5 imagewriter.pro

%build
qmake-qt5 "QMAKE_CFLAGS+=%optflags -DKIOSKHACK" "QMAKE_CXXFLAGS+=%optflags -DKIOSKHACK" PREFIX=%_prefix DEFINES=%definedbackend imagewriter.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/%name/*
%_man1dir/*

%changelog
* Sun Aug 22 2021 Motsyo Gennadi <drool@altlinux.ru> 1.10-alt6
- rebuild with Qt5

* Thu Apr 15 2021 Grigory Ustinov <grenka@altlinux.org> 1.10-alt5
- Fixed FTBFS.

* Fri Mar 14 2014 Andrey Cherepanov <cas@altlinux.org> 1.10-alt4
- Add Russian localization

* Mon Jan 13 2014 Motsyo Gennadi <drool@altlinux.ru> 1.10-alt3
- fix switching UDISKS/UDISKS2 support and udisks/udisks2 requires

* Mon Jan 13 2014 Motsyo Gennadi <drool@altlinux.ru> 1.10-alt2
- update from git (fix UDISKS2 support)

* Sun Jan 12 2014 Motsyo Gennadi <drool@altlinux.ru> 1.10-alt1
- initial build for ALT Linux from RHEL pakcage
