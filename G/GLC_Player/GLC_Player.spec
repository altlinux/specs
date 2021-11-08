Name: GLC_Player
Version: 2.3.0
Release: alt3.20200519
Summary: GLC_Player is an Open Source software used to view 3d models (OBJ Format)

Group: Graphics
License: GPLv2+
Url: https://github.com/alon/GLC_Player

Source: %name-%version.tar
Source1: glc_player.desktop
Patch: GLC_Player_src_2.3.0-cache.patch
Patch1: GLC_Player_src_2.3.0-prefix.patch

BuildRequires: GLC_lib-devel >= 3.0.1
BuildRequires: desktop-file-utils

# GLC_Lib not available for %arm
ExcludeArch: %arm

%description
GLC_Player is an Open Source software used to view 3d models (OBJ Format).
With the session concept and navigation possibilities GLC_Player is the
accurate tools to review a lot of 3D models. GLC_Player is a
cross-platform, Qt 5 and GLC_lib application.

%prep
%setup
%patch0 -p1 -b .cache
#patch1 -p1 -b .prefix

%build
%qmake_qt5 glc_player.pro
%make_build

%install
mkdir -p %buildroot%_bindir
install -pm 0755 glc_player %buildroot%_bindir

mkdir -p %buildroot%_datadir/{applications,pixmaps}

install -pm 0644 ressources/images/GLC_logo_blanc.png \
%buildroot%_pixmapsdir/glc_player.png

desktop-file-install \
  --dir %buildroot%_desktopdir \
  --mode 644 \
%SOURCE1

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %buildroot%_datadir/appdata
cat > %buildroot%_datadir/appdata/glc_player.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: laumaya@users.sourceforge.net
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">glc_player.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>View 3D models</summary>
  <description>
  <p>
    GLC Player is an application for viewing 3D models.
    It supports a wide range of formats, including:  COLLADA, 3DXML, OBJ,
    3DS, STL, OFF and COFF.
    It can also be used to export still images of your models, and even
    export a library of models to a gallery HTML page.
  </p>
  </description>
  <url type="homepage">http://www.glc-player.net/</url>
  <screenshots>
    <screenshot type="default">http://www.glc-player.net/images/Lin_corsair_full.jpg</screenshot>
  </screenshots>
</application>
EOF

%files
%doc
%_bindir/glc_player
%_pixmapsdir/glc_player.png
%_datadir/appdata/*.appdata.xml
%_desktopdir/*.desktop

%changelog
* Mon Nov 08 2021 Anton Midyukov <antohami@altlinux.org> 2.3.0-alt3.20200519
- new snapshot from commit c513c3d15f6395121e156ef47efa0bfe9cd71f40
- build with qt5 and GLC_lib 3.0.1
- Update Url Tag
- ExcludeArch: %arm

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_14
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_11
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_7
- update to new release by fcimport

* Thu May 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2_6
- moved to Sisyphus by request of dd@

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_6
- update to new release by fcimport

* Sat Apr 13 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_5
- update to new release by fcimport

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_4
- update to new release by fcimport

* Wed Jan 16 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_3
- initial fc import

