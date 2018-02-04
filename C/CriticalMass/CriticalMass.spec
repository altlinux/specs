# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libGL-devel libSDL-devel zlib-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           CriticalMass
Version:        1.5
Release:        alt2_20
Summary:        SDL/OpenGL space shoot'em up game also known as critter
Group:          Games/Other
License:        GPLv2+
URL:            http://criticalmass.sourceforge.net/critter.php
Source0:        http://downloads.sourceforge.net/criticalmass/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         CriticalMass-1.0.2-res-change-rh566533.patch
Patch1:         CriticalMass-1.5-libpng15.patch
Patch2:         CriticalMass-1.5-gcc47.patch
Patch3:         CriticalMass-1.5-cflags.patch
Patch4:         CriticalMass-1.5-gcc6.patch
BuildRequires:  libSDL_image-devel libSDL_mixer-devel libpng-devel curl-devel
BuildRequires:  tinyxml-devel desktop-file-utils libtool
Requires:       icon-theme-hicolor opengl-games-utils
# Also known as critter, so make "yum install critter" work
Provides:       critter = %{version}-%{release}
Source44: import.info

%description
Critical Mass (aka Critter) is an SDL/OpenGL space shoot'em up game. Your
world has been infested by an aggressive army of space critters. Overrun and
unprepared, your government was unable to defend its precious resources. As
a last effort to recapture some of the "goodies", you have been placed into
a tiny spacecraft and sent after them.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
sed -i 's/curl-gnutls/curl/g' configure.in
touch NEWS README AUTHORS ChangeLog
autoreconf -ivf


%build
%configure
%make_build


%install
%makeinstall_std
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/critter-wrapper

# remove unwanted utility
rm $RPM_BUILD_ROOT%{_bindir}/Packer

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
install -p -m 644 critter.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: crittermail2005@telus.net
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">CriticalMass.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A top-down space shoot-em-up game</summary>
  <description>
    <p>
      Critical Mass (also known as Critter) is a top-down shoot-em-up game where your home world
      has been infested by an aggressive army of space critters and
      you are required to pilot a small spacecraft to destroy them all.
    </p>
  </description>
  <url type="homepage">http://criticalmass.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://criticalmass.sourceforge.net/images-critter/pics.v100/snap09.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap17.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap13.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap04.jpeg</screenshot>
    <screenshot>http://criticalmass.sourceforge.net/images-critter/pics.v100/snap00.jpeg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files
%doc Readme.html TODO
%doc --no-dereference COPYING
%{_bindir}/critter*
%{_datadir}/Critical_Mass
%{_mandir}/man6/critter.6*
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/critter.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_20
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_19
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_17
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_15
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_10
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_9
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_8
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_6
- update to new release by fcimport

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2_5.1
- Rebuilt with libpng15

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_5
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_4
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_3
- rebuild with fixed sourcedep analyser (#27020)

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3
- update to new release by fcimport

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- update to new release by fcimport

* Thu Feb 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_9
- converted from Fedora by srpmconvert script

