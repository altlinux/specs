%define rname mirall
Name: owncloud-client
Version: 1.0.2
Release: alt2

Group: Networking/File transfer
Summary: Applet for owncloud files syncronization
License: GPLv2

Conflicts: mirall

Source: %rname-%version.tar
Source1: owncloud-client.desktop
Patch1: mirall-1.0.2-alt-notwarn-notconfigured.patch
Patch2: mirall-1.0.3-alt-dont-check-updates.patch
Patch3: mirall-1.0.3-alt-owncloud-client.patch

BuildRequires: rpm-macros-cmake cmake libqt4-devel gcc-c++ libcsync-devel kde-common-devel desktop-file-utils

%description
Applet for file syncronization via owncloud.

%prep
%setup -qn %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%Kbuild

%install
%Kinstall
mkdir -p %buildroot/%_desktopdir
desktop-file-install \
    --dir=%buildroot/%_desktopdir \
    %{SOURCE1}

%find_lang %name

%files -f %name.lang
%_bindir/owncloud
%config(noreplace) %_sysconfdir/exclude.lst
%_desktopdir/%name.desktop
%_datadir/mirall
%_iconsdir/hicolor/*/apps/owncloud.*

%changelog
* Thu Aug 23 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt2
- fix menu item

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt0.M60P.1
- built for M60P

* Wed Aug 22 2012 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- initial build
