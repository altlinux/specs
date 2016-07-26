# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ unzip
# END SourceDeps(oneline)
Name:           GLC_Player
Version:        2.3.0
Release:        alt2_13
Summary:        GLC_Player is an Open Source software used to view 3d models (OBJ Format)

Group:          Graphics
License:        GPLv2+
URL:            http://www.glc-player.net/
Source0:        http://downloads.sourceforge.net/glc-player/GLC_Player_src_%{version}.zip
Source1:        glc_player.desktop
Patch0:         GLC_Player_src_2.3.0-cache.patch
Patch1:         GLC_Player_src_2.3.0-prefix.patch

BuildRequires:  GLC_lib-devel >= 2.0.0
BuildRequires:  desktop-file-utils
Source44: import.info

%description
GLC_Player is an Open Source software used to view 3d models (OBJ Format).
With the session concept and navigation possibilities GLC_Player is the
accurate tools to review a lot of 3D models. GLC_Player is a 
cross-platform, Qt 4 and GLC_lib application.


%prep
%setup -q -c
%patch0 -p1 -b .cache
%patch1 -p1 -b .prefix


%build
%{qmake_qt4} glc_player.pro
make %{?_smp_mflags}


%install

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -pm 0755 glc_player $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}

install -pm 0644 ressources/images/GLC_logo_blanc.png \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/glc_player.png

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  %{SOURCE1}	

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/glc_player.appdata.xml <<EOF
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
%{_bindir}/glc_player
%{_datadir}/pixmaps/glc_player.png
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop


%changelog
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

